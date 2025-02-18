import open3d as o3d
import numpy as np

def augment_point_cloud(point_cloud):
    """Apply random rotation, translation, and scaling to a point cloud."""
    # Random rotation (around the Z-axis)
    rotation = np.random.uniform(0, 2 * np.pi)
    rotation_matrix = np.array([
        [np.cos(rotation), -np.sin(rotation), 0],
        [np.sin(rotation), np.cos(rotation), 0],
        [0, 0, 1]
    ])
    point_cloud = np.dot(point_cloud, rotation_matrix.T)  # Apply rotation
    
    # Random translation
    translation = np.random.uniform(-0.1, 0.1, size=3)
    point_cloud += translation  # Apply translation
    
    # Random scaling
    scale = np.random.uniform(0.8, 1.2)
    point_cloud *= scale  # Apply scaling
    
    return point_cloud

# Load a point cloud file
pcd = o3d.io.read_point_cloud("/Users/shrikar/Library/Mobile Documents/com~apple~CloudDocs/Sem III/R&D/RnD/dataset/Separated.ply")  # Change to your filename

# Convert to NumPy array
points = np.asarray(pcd.points)

# Apply augmentation
augmented_points = augment_point_cloud(points)

# Convert back to Open3D point cloud
augmented_pcd = o3d.geometry.PointCloud()
augmented_pcd.points = o3d.utility.Vector3dVector(augmented_points)

# Save the augmented point cloud
o3d.io.write_point_cloud("augmented_point_cloud.ply", augmented_pcd)

# Visualize the original and augmented point cloud
o3d.visualization.draw_geometries([pcd], window_name="Original Point Cloud")
o3d.visualization.draw_geometries([augmented_pcd], window_name="Augmented Point Cloud")