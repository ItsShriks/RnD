import pcl
import numpy as np
import os
import open3d as o3d  # Open3D for file handling and visualization

# Load the point cloud data (PLY format) using Open3D, then convert it to PCL format
def load_ply_file(file_path):
    pcd = o3d.io.read_point_cloud(file_path)
    points = np.asarray(pcd.points)
    
    # Create a PCL PointCloud from the numpy array
    cloud = pcl.PointCloud()
    cloud.from_array(points.astype(np.float32))  # Ensure proper dtype
    return cloud

# Define the path to your PLY file
file_path = "/home/shrikar/RnD/dataset/filtered_point_cloud.ply"

# Load the point cloud data
cloud = load_ply_file(file_path)

# Apply Voxel Grid filtering for downsampling
def voxel_grid_filter(cloud, leaf_size=0.1):
    voxel = cloud.make_voxel_grid_filter()
    voxel.set_leaf_size(leaf_size, leaf_size, leaf_size)  # Set the leaf size (resolution of downsampling)
    return voxel.filter()

cloud_filtered = voxel_grid_filter(cloud)

# Perform RANSAC-based Ground Segmentation
def ransac_ground_segmentation(cloud, max_distance=0.1):
    seg = cloud.make_segmenter()
    seg.set_method_type(pcl.SAC_RANSAC)  # Use RANSAC algorithm
    seg.set_distance_threshold(max_distance)  # Maximum distance for a point to be considered fitting the model
    
    # Segment the cloud into inliers (ground) and outliers (non-ground)
    seg.set_axis([0, 0, 1])  # Set the axis for vertical plane (Z-axis in this case)
    seg.set_input_cloud(cloud)
    
    # Call segment function to obtain set of inlier indices and model coefficients
    inliers, coefficients = seg.segment()

    # Extract inliers (ground points)
    ground_cloud = cloud.extract(inliers, negative=False)
    non_ground_cloud = cloud.extract(inliers, negative=True)

    return ground_cloud, non_ground_cloud

# Segment the cloud using RANSAC
ground_cloud, non_ground_cloud = ransac_ground_segmentation(cloud_filtered)

# Save the segmented point clouds
output_dir = "/home/shrikar/RnD/Trials/terrain"

# Ensure the output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Save ground and non-ground point clouds as PLY files
ground_pcd_path = os.path.join(output_dir, "ground_points.ply")
non_ground_pcd_path = os.path.join(output_dir, "non_ground_points.ply")

ground_cloud.to_file(ground_pcd_path)
non_ground_cloud.to_file(non_ground_pcd_path)

print(f"Ground points saved to {ground_pcd_path}")
print(f"Non-ground points saved to {non_ground_pcd_path}")

# Visualization of the point clouds using Open3D
ground_points = np.asarray(ground_cloud)
non_ground_points = np.asarray(non_ground_cloud)

# Create Open3D point clouds
ground_pcd_o3d = o3d.geometry.PointCloud()
ground_pcd_o3d.points = o3d.utility.Vector3dVector(ground_points)
non_ground_pcd_o3d = o3d.geometry.PointCloud()
non_ground_pcd_o3d.points = o3d.utility.Vector3dVector(non_ground_points)

# Visualize ground points in green and non-ground points in red
ground_pcd_o3d.paint_uniform_color([0, 1, 0])  # Green
non_ground_pcd_o3d.paint_uniform_color([1, 0, 0])  # Red

# Save visualization image
def save_visualization_image(ground_pcd_o3d, non_ground_pcd_o3d, save_path):
    o3d.visualization.draw_geometries([ground_pcd_o3d, non_ground_pcd_o3d])
    # Open3D does not support direct screenshot saving from its visualization window.
    # You can manually take a screenshot from the visualization window or use other methods like 'OpenCV' to capture.

# Save the visualization image manually or programmatically
save_visualization_image(ground_pcd_o3d, non_ground_pcd_o3d, "/home/shrikar/RnD/Trials/terrain/ground_non_ground_visualization_open3d.jpg")
