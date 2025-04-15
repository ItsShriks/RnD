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

        # Ensure at least 3 unique neighbors
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
    """
    Assign labels to points based on their z-values.
    The labels are determined by thresholds defined in z_thresholds.
    """
    # Extract the z-values from the point cloud
    z_values = np.asarray(pcd.points)[:, 2]  # Get z-values (third column)

    # Initialize an array to store labels
    labels = np.zeros_like(z_values, dtype=int)

    # Assign labels based on z-value thresholds
    for i, z in enumerate(z_values):
        if z < z_thresholds[0]:
            labels[i] = 0  # Label for low z-values
        elif z < z_thresholds[1]:
            labels[i] = 1  # Label for mid-range z-values
        elif z < z_thresholds[2]:
            labels[i] = 2  # Label for high z-values
        else:
            labels[i] = 3  # Label for very high z-values

    return labels

def extract_labels_with_plyfile(ply_path):
    try:
        ply = PlyData.read(ply_path)
        vertex_data = ply['vertex']

        # Print all available properties in the vertex data for debugging
        print(f"Available properties in {ply_path}: {vertex_data.properties}")

        # Look for labels under different possible names
        for label_name in ['label', 'class', 'segmentation']:
            if label_name in vertex_data.properties:
                print(f"Found {label_name} in {ply_path}")
                return np.array(vertex_data[label_name])

    except Exception as e:
        print(f"Error reading label from {ply_path}: {e}")

    return None

def process_ply_to_csv(ply_path, output_csv_path, z_thresholds=[0.0, 1.0, 2.0]):
    # Open3D for geometry
    pcd = o3d.io.read_point_cloud(ply_path)

    # Estimate normals, curvature, density
    curvature = estimate_normals_and_curvature(pcd)
    if curvature is None:
        curvature = np.zeros(len(np.asarray(pcd.points)))  # Fallback to zero curvature if None
    density = compute_density(pcd)

    xyz = np.asarray(pcd.points)
    normals = np.asarray(pcd.normals)

    # Assign labels based on z-values
    labels = assign_labels_based_on_z(pcd, z_thresholds)

    # Combine data
    data = np.hstack((xyz, normals, curvature.reshape(-1, 1), density.reshape(-1, 1)))

    columns = ['x', 'y', 'z', 'nx', 'ny', 'nz', 'curvature', 'density']
    df = pd.DataFrame(data, columns=columns)

    # Add labels to dataframe
    df["label"] = labels

    # Save to CSV
    df.to_csv(output_csv_path, index=False)
    print(f"✅ Saved: {output_csv_path}")

# Example usage on a directory
def process_all_plys(input_dir, output_dir, z_thresholds=[0.0, 1.0, 2.0]):
    os.makedirs(output_dir, exist_ok=True)
    files = [f for f in os.listdir(input_dir) if f.endswith('.ply')]

    for file in tqdm(files):
        in_path = os.path.join(input_dir, file)
        out_path = os.path.join(output_dir, file.replace('.ply', '.csv'))
        process_ply_to_csv(in_path, out_path, z_thresholds)

# Example paths and z-thresholds
input_ply_dir = '/Users/shrikar/Library/Mobile Documents/com~apple~CloudDocs/Sem IV/R&D/RnD/dataset/grids_2.5/grids_2.5_ply'
output_csv_dir = '/Users/shrikar/Library/Mobile Documents/com~apple~CloudDocs/Sem IV/R&D/RnD/dataset/grids_2.5/grids_2.5_csv'
z_thresholds = [0.0, 1.0, 2.0]  # Adjust these thresholds as needed
process_all_plys(input_ply_dir, output_csv_dir, z_thresholds)
