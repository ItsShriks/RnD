import open3d as o3d
import numpy as np
import pandas as pd
from plyfile import PlyData
from scipy.spatial import KDTree
import os
from tqdm import tqdm

def estimate_normals_and_curvature(pcd, radius=0.05, max_nn=30):
    pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=radius, max_nn=max_nn))
    if len(pcd.points) >= 4:
        pcd.orient_normals_consistent_tangent_plane(30)
    else:
        print("⚠️ Skipping normal orientation (not enough points).")
    points = np.asarray(pcd.points)

    kdtree = o3d.geometry.KDTreeFlann(pcd)
    curvatures = []

    for i in range(len(points)):
        _, idx, _ = kdtree.search_knn_vector_3d(points[i], 30)
        neighbors = points[idx, :]

        if len(neighbors) < 3 or np.linalg.matrix_rank(neighbors - neighbors.mean(axis=0)) < 3:
            curvatures.append(0.0)
            continue

        try:
            cov = np.cov(neighbors.T)
            eigvals, _ = np.linalg.eigh(cov)
            eigvals = np.sort(eigvals)
            curvature = eigvals[0] / (eigvals.sum() + 1e-8)
        except np.linalg.LinAlgError:
            curvature = 0.0

        curvatures.append(curvature)

    return np.array(curvatures)

def compute_density(pcd, radius=0.05):
    points = np.asarray(pcd.points)
    tree = KDTree(points)
    densities = []

    for point in points:
        indices = tree.query_ball_point(point, r=radius)
        densities.append(len(indices))
    return np.array(densities)

def assign_labels_based_on_z(pcd, z_thresholds=[0.0, 1.0, 2.0]):
    z_values = np.asarray(pcd.points)[:, 2]
    labels = np.zeros_like(z_values, dtype=int)

    for i, z in enumerate(z_values):
        if z < z_thresholds[0]:
            labels[i] = 1
        elif z < z_thresholds[1]:
            labels[i] = 2
        elif z < z_thresholds[2]:
            labels[i] = 2
        else:
            labels[i] = 3

    return labels

def assign_labels_by_percentage(pcd, percentages={1: 0.8, 2: 0.1, 3: 0.1}, seed=None):
    if seed is not None:
        np.random.seed(seed)

    num_points = len(pcd.points)
    labels = np.zeros(num_points, dtype=int)

    label_counts = {label: int(p * num_points) for label, p in percentages.items()}

    # Adjust for rounding errors
    assigned_total = sum(label_counts.values())
    if assigned_total < num_points:
        max_label = max(percentages, key=percentages.get)
        label_counts[max_label] += num_points - assigned_total

    all_indices = np.arange(num_points)
    np.random.shuffle(all_indices)
    idx = 0

    for label, count in label_counts.items():
        labels[all_indices[idx:idx + count]] = label
        idx += count

    return labels

def extract_labels_with_plyfile(ply_path):
    try:
        ply = PlyData.read(ply_path)
        vertex_data = ply['vertex']
        print(f"Available properties in {ply_path}: {vertex_data.properties}")
        for label_name in ['label', 'class', 'segmentation']:
            if label_name in vertex_data.properties:
                print(f"Found {label_name} in {ply_path}")
                return np.array(vertex_data[label_name])
    except Exception as e:
        print(f"Error reading label from {ply_path}: {e}")
    return None

def process_ply_to_csv(ply_path, output_csv_path, use_percentage=True,
                       z_thresholds=[0.0, 1.0, 2.0],
                       percentages={1: 0.1, 2: 0.1, 3: 0.8}):
    pcd = o3d.io.read_point_cloud(ply_path)

    curvature = estimate_normals_and_curvature(pcd)
    if curvature is None:
        curvature = np.zeros(len(np.asarray(pcd.points)))
    density = compute_density(pcd)

    xyz = np.asarray(pcd.points)
    normals = np.asarray(pcd.normals)

    if use_percentage:
        labels = assign_labels_by_percentage(pcd, percentages)
    else:
        labels = assign_labels_based_on_z(pcd, z_thresholds)

    data = np.hstack((xyz, normals, curvature.reshape(-1, 1), density.reshape(-1, 1)))
    columns = ['x', 'y', 'z', 'nx', 'ny', 'nz', 'curvature', 'density']
    df = pd.DataFrame(data, columns=columns)
    df["label"] = labels

    df.to_csv(output_csv_path, index=False)
    print(f"✅ Saved: {output_csv_path}")

def process_all_plys(input_dir, output_dir, use_percentage=True,
                     z_thresholds=[0.0, 1.0, 2.0],
                     percentages={1: 0.1, 2: 0.1, 3: 0.8}):
    os.makedirs(output_dir, exist_ok=True)
    files = [f for f in os.listdir(input_dir) if f.endswith('.ply')]

    for file in tqdm(files):
        in_path = os.path.join(input_dir, file)
        out_path = os.path.join(output_dir, file.replace('.ply', '.csv'))
        process_ply_to_csv(in_path, out_path, use_percentage, z_thresholds, percentages)

# Example usage
input_ply_dir = '/Users/shrikar/Library/Mobile Documents/com~apple~CloudDocs/Sem IV/R&D/RnD/dataset/grids_5.0/grids_5.0_ply'
output_csv_dir = '/Users/shrikar/Library/Mobile Documents/com~apple~CloudDocs/Sem IV/R&D/RnD/dataset/grids_5.0/grids_5.0_csv'

# ✅ Use this to switch between the two methods
use_percentage = True  # Set to False to use z-thresholds instead
z_thresholds = [0.0, 1.0, 2.0]  # Used only if use_percentage=False
percentages = {1: 0.1, 2: 0.1, 3: 0.8}  # Used only if use_percentage=True

# Run it
process_all_plys(input_ply_dir, output_csv_dir, use_percentage, percentages)
