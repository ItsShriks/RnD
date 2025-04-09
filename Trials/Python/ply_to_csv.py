import open3d as o3d
import numpy as np
import os
import pandas as pd
from tqdm import tqdm
from scipy.spatial import KDTree

def estimate_normals_and_curvature(pcd, radius=0.05, max_nn=30):
    pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=radius, max_nn=max_nn))
    pcd.orient_normals_consistent_tangent_plane(30)

    kdtree = o3d.geometry.KDTreeFlann(pcd)
    curvatures = []

    for i in range(len(pcd.points)):
        _, idx, _ = kdtree.search_knn_vector_3d(pcd.points[i], 30)
        neighbors = np.asarray(pcd.points)[idx, :]
        cov = np.cov(neighbors.T)
        eigvals, _ = np.linalg.eigh(cov)
        eigvals = np.sort(eigvals)
        curvature = eigvals[0] / (eigvals.sum() + 1e-8)
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

def process_ply_files_to_csv(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    files = [f for f in os.listdir(input_dir) if f.endswith(".ply")]

    for file in tqdm(files):
        path = os.path.join(input_dir, file)
        pcd = o3d.io.read_point_cloud(path)

        # Estimate normals and curvature
        curvature = estimate_normals_and_curvature(pcd)
        density = compute_density(pcd)

        xyz = np.asarray(pcd.points)
        normals = np.asarray(pcd.normals)

        # Stack all into one array
        data = np.hstack((xyz, normals, curvature.reshape(-1, 1), density.reshape(-1, 1)))

        # Create a DataFrame and save as CSV
        df = pd.DataFrame(data, columns=["x", "y", "z", "nx", "ny", "nz", "curvature", "density"])
        csv_path = os.path.join(output_dir, file.replace(".ply", ".csv"))
        df.to_csv(csv_path, index=False)

        print(f"Saved {csv_path}")

# Example usage
input_dir = "/Users/shrikar/Library/Mobile Documents/com~apple~CloudDocs/Sem IV/R&D/RnD/Trials/Python/grids_2.5"
output_dir = "/Users/shrikar/Library/Mobile Documents/com~apple~CloudDocs/Sem IV/R&D/RnD/Trials/Python/grids_2.5/csv"
process_ply_files_to_csv(input_dir, output_dir)
