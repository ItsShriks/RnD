import open3d as o3d
import numpy as np
from pyransac3d import Cylinder

# Load the point cloud file
pcd = o3d.io.read_point_cloud("/Users/shrikar/Library/Mobile Documents/com~apple~CloudDocs/Sem III/R&D/RnD/dataset/Separated.ply")

# Convert point cloud to NumPy array (N, 3)
points = np.asarray(pcd.points)

# Create a Cylinder object
cylinder = Cylinder()

# Fit the cylinder to the point cloud
center, axis, radius, inliers = cylinder.fit(points, thresh=0.05, maxIteration=1000)

# Extract the inlier points (points belonging to the detected cylinder)
cylinder_points = points[inliers]

print(f"Cylinder center: {center}")
print(f"Cylinder axis: {axis}")
print(f"Cylinder radius: {radius}")
print(f"Number of inlier points: {len(inliers)}")

# Create a new point cloud for the detected cylinder
cylinder_pcd = o3d.geometry.PointCloud()
cylinder_pcd.points = o3d.utility.Vector3dVector(cylinder_points)

# Assign color to highlight cylinder (e.g., red)
cylinder_pcd.paint_uniform_color([1, 0, 0])  # Red color for visualization

# Save the detected cylinder points to a new .ply file
#o3d.io.write_point_cloud("detected_cylinder.ply", cylinder_pcd)

# Visualize the original and detected cylinder
o3d.visualization.draw_geometries([pcd, cylinder_pcd], window_name="Detected Cylinder")