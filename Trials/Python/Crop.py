import open3d as o3d
import numpy as np

# Define your 5 points as a numpy array
five_points = np.array([
    [-2.294216, 36.315838, -4.84553],
    [16.956844, -44.380180, -4.84553],
    [65.558228, 32.719646, -4.84553],
    [65.664795, 26.725346, -4.84553],
    [50.484165, -21.520457, -4.84553],
    [-2.294216, 36.315838, 13.5509],
    [16.956844, -44.380180, 13.5509],
    [65.558228, 32.719646, 13.5509],
    [65.664795, 26.725346, 13.5509],
    [50.484165, -21.520457, 13.5509],
])

# Load your full point cloud
pcd = o3d.io.read_point_cloud("Final.ply")  # Replace with your file path

# Calculate the bounding box limits based on the five points
min_bound = np.min(five_points, axis=0)
max_bound = np.max(five_points, axis=0)

# Crop the point cloud using the bounding box limits
cropped_pcd = pcd.crop(o3d.geometry.AxisAlignedBoundingBox(min_bound, max_bound))

# Save or display the cropped point cloud
o3d.io.write_point_cloud("cropped_point_cloud.ply", cropped_pcd)
o3d.visualization.draw_geometries([cropped_pcd], window_name="Cropped Point Cloud")