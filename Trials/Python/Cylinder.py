import open3d as o3d
import numpy as np
from pyransac3d import Cylinder

# Load the point cloud file
pcd = o3d.io.read_point_cloud("/home/shrikar/RnD/dataset/Separated.ply")

# Convert point cloud to NumPy array (N, 3)
points = np.asarray(pcd.points)

# Create a mask to track inlier points (initially all False)
inlier_mask = np.zeros(points.shape[0], dtype=bool)

# Create a Cylinder object
cylinder = Cylinder()

# Parameters
max_iterations = 1000  # Max iterations for RANSAC
min_inliers = 500  # Minimum points required to consider a valid cylinder

# List to store all detected cylinders
cylinder_points_list = []

while True:
    # Fit a cylinder to the remaining points
    try:
        center, axis, radius, inliers = cylinder.fit(points[~inlier_mask], thresh=thresh, maxIteration=max_iterations)
        if len(inliers) < min_inliers:
            break  # Stop if no significant cylinder is found
        
        # Update inlier mask
        inlier_indices = np.where(~inlier_mask)[0][inliers]
        inlier_mask[inlier_indices] = True
        
        # Store inlier points for coloring
        cylinder_points_list.append(inlier_indices)
    except:
        break  # Stop if no more cylinders can be found

# Print number of detected cylinders
print(f"Number of detected cylinders: {len(cylinder_points_list)}")

# Assign colors: Green for cylinder points, Black for everything else
colors = np.zeros_like(points)  # Default black
for inlier_indices in cylinder_points_list:
    colors[inlier_indices] = [0, 1, 0]  # Green for cylinder points

# Apply colors to point cloud
pcd.colors = o3d.utility.Vector3dVector(colors)

# Save the colored point cloud
# o3d.io.write_point_cloud("colored_cylinders.ply", pcd)

# Visualize the results

vis = o3d.visualization.Visualizer()
vis.create_window()
vis.add_geometry(pcd)
vis.run()
vis.destroy_window()
