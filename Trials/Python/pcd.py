import open3d as o3d
import numpy as np
if __name__ == "__main__":
    pcd = o3d.io.read_point_cloud("GlobalMapply.ply")
    o3d.visualization.draw_geometries([pcd])

min_bound = np.array([-1000, -1000, -1000])  # lower bound of the square (cube)
max_bound = np.array([1000, 1000, 1000])     # upper bound of the square (cube)

# Create the axis-aligned bounding box
aabb = o3d.geometry.AxisAlignedBoundingBox(min_bound, max_bound)

# Step 3: Crop the point cloud using the bounding box
cropped_point_cloud = pcd.crop(aabb)

# Step 4: Visualize the cropped point cloud
o3d.visualization.draw_geometries([cropped_point_cloud])
print(cropped_point_cloud)
