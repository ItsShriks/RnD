import laspy
import numpy as np
import pandas as pd
import open3d as o3d
from tqdm import tqdm

def read_las_file(las_path):
    try:
        print(f"Reading LAS file from: {las_path}")
        las = laspy.read(las_path)
        points = np.vstack((las.x, las.y, las.z)).T
        print(f"Loaded {points.shape[0]} points.")
        return points
    except Exception as e:
        print(f"❌ Error reading LAS file: {e}")
        raise

def estimate_normals(points, k=30):
    try:
        print("Estimating normals...")
        pcd = o3d.geometry.PointCloud()
        pcd.points = o3d.utility.Vector3dVector(points)
        pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamKNN(knn=k))
        return pcd, np.asarray(pcd.normals)
    except Exception as e:
        print(f"❌ Error estimating normals: {e}")
        raise

def estimate_curvature(pcd, k=30):
    try:
        print("Estimating curvature...")
        curvatures = []
        pcd_tree = o3d.geometry.KDTreeFlann(pcd)
        for i in tqdm(range(len(pcd.points)), desc="Curvature"):
            _, idx, _ = pcd_tree.search_knn_vector_3d(pcd.points[i], k)
            neighbors = np.asarray(pcd.points)[idx, :]
            cov = np.cov(neighbors.T)
            eigvals, _ = np.linalg.eigh(cov)
            curvature = eigvals[0] / np.sum(eigvals)
            curvatures.append(curvature)
        return np.array(curvatures)
    except Exception as e:
        print(f"❌ Error estimating curvature: {e}")
        raise

def estimate_density(pcd, radius=1.0):
    try:
        print("Estimating density...")
        densities = []
        pcd_tree = o3d.geometry.KDTreeFlann(pcd)
        for i in tqdm(range(len(pcd.points)), desc="Density"):
            _, idx, _ = pcd_tree.search_radius_vector_3d(pcd.points[i], radius)
            densities.append(len(idx))
        return np.array(densities)
    except Exception as e:
        print(f"❌ Error estimating density: {e}")
        raise

def create_dataframe(points, normals, curvatures, densities):
    print("Creating DataFrame...")
    df = pd.DataFrame({
        'x': points[:, 0],
        'y': points[:, 1],
        'z': points[:, 2],
        'nx': normals[:, 0],
        'ny': normals[:, 1],
        'nz': normals[:, 2],
        'curvature': curvatures,
        'density': densities
    })
    rows, cols = df.shape
    print(f"✅ DataFrame created with {rows} rows and {cols} columns.")
    print(f"📋 Columns: {list(df.columns)}")
    return df
def save_dataframe_to_csv(df, csv_path):
    try:
        print(f"Saving DataFrame to CSV at: {csv_path}")
        df.to_csv(csv_path, index=False)
        print("✅ CSV file saved successfully.")
    except Exception as e:
        print(f"❌ Error saving CSV file: {e}")
        raise

def process_las_to_csv(las_path, csv_path):
    try:
        points = read_las_file(las_path)
        pcd, normals = estimate_normals(points)
        curvatures = estimate_curvature(pcd)
        densities = estimate_density(pcd)
        df = create_dataframe(points, normals, curvatures, densities)
        save_dataframe_to_csv(df, csv_path)
    except Exception as e:
        print(f"❌ Processing failed: {e}")

# Example usage:
if __name__ == "__main__":
    las_file = "your_file.las"
    csv_file = "output.csv"
    process_las_to_csv(las_file, csv_file)
