

import open3d as o3d
import numpy as np

# Load non-ground points
pcd = o3d.io.read_point_cloud("/Users/shrikar/Library/Mobile Documents/com~apple~CloudDocs/Sem III/R&D/RnD/dataset/Separated.ply")
points = np.asarray(pcd.points)

# Height-based filtering (removing canopy)
min_height = 1.0  # Minimum height to consider as a trunk
max_height = 10.0  # Max height (avoid canopy)
trunk_points = points[(points[:, 2] > min_height) & (points[:, 2] < max_height)]

# Convert back to Open3D PointCloud
trunk_pcd = o3d.geometry.PointCloud()
trunk_pcd.points = o3d.utility.Vector3dVector(trunk_points)

# Save trunks
o3d.io.write_point_cloud("tree_trunks.ply", trunk_pcd)

# Visualize trunks
o3d.visualization.draw_geometries([trunk_pcd], window_name="Extracted Tree Trunks")