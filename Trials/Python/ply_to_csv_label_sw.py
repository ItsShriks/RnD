import open3d as o3d
import numpy as np

ply_file = "/Users/shrikar/RnD/Trials/terrain/ransac_non_ground_points.ply"
pcd = o3d.io.read_point_cloud(ply_file)
points = np.asarray(pcd.points)

# Manually assign labels as either 0 or 1 for each point
labels = np.zeros(len(points), dtype=int)  # Start with label 0 for all points

# Example: Assign label 1 to some points based on some condition
# Here, all points with x > 0 will be labeled as 1
labels[points[:, 0] > 0] = 1  # Replace this with your custom logic

# Create data with x, y, z, label, 0, 0
data = np.column_stack((points, labels, np.zeros((len(points), 2))))  # np.zeros creates two additional columns of zeros
data = data.astype(np.float64)

# Save the data as .npy file
npy_file = "non_ground_points_ransac.npy"
np.save(npy_file, data)

print(f"Data saved as {npy_file}")
