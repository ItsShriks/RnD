import open3d as o3d
import numpy as np

# Load the .ply file
ply_file = "filtered_point_cloud.ply"  # Replace with the actual file path
pcd = o3d.io.read_point_cloud(ply_file)

# Convert point cloud to numpy array
points = np.asarray(pcd.points)

# Identify NaN and Inf points
nan_mask = np.isnan(points).any(axis=1)  # Check for NaN in any coordinate
inf_mask = np.isinf(points).any(axis=1)  # Check for Inf or -Inf in any coordinate

# Count NaN and Inf points
num_nan_points = np.sum(nan_mask)
num_inf_points = np.sum(inf_mask)

# Print results
print(f"Number of NaN points: {num_nan_points}")
print(f"Number of Inf points: {num_inf_points}")

# Optional: Get the indices or coordinates of invalid points
nan_points = points[nan_mask]
inf_points = points[inf_mask]

print(f"NaN points: {nan_points}")
print(f"Inf points: {inf_points}")
