import open3d as o3d
import numpy as np
import os

def load_ply(file_path):
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return None

    pcd = o3d.io.read_point_cloud(file_path)
    points = np.asarray(pcd.points)

    if points.shape[0] == 0:
        print(f"⚠️ No points found in: {file_path}")
        return None

    print(f"✅ Loaded {points.shape[0]} points from: {file_path}")
    return points

def check_overlap(pcd1, pcd2, distance_threshold=0.01):
    from scipy.spatial import cKDTree
    tree = cKDTree(pcd2)
    distances, _ = tree.query(pcd1, k=1)

    overlap_indices = np.where(distances < distance_threshold)[0]
    overlap_points = pcd1[overlap_indices]
    return overlap_points

def main(ply_file1, ply_file2, distance_threshold=0.01):
    pcd1 = load_ply(ply_file1)
    pcd2 = load_ply(ply_file2)

    if pcd1 is None or pcd2 is None:
        print("❗ Exiting due to file loading issue.")
        return

    overlap_points = check_overlap(pcd1, pcd2, distance_threshold)

    if len(overlap_points) > 0:
        print(f"🔁 Found {len(overlap_points)} overlapping points.")
    else:
        print("✅ No overlapping points found.")

# ----------- Replace with your file paths ------------
ply_file1 = "path_to_first.ply"
ply_file2 = "path_to_second.ply"
# -----------------------------------------------------
main(ply_file1, ply_file2, distance_threshold=0.01)
