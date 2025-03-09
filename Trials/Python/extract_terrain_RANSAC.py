import open3d as o3d
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
from sklearn.pipeline import make_pipeline
import os

# Load the point cloud data (PLY format)
def load_ply_file(file_path):
    pcd = o3d.io.read_point_cloud(file_path)
    points = np.asarray(pcd.points)
    return points

# Define the path to your PLY file
file_path = "/home/shrikar/RnD/dataset/filtered_point_cloud.ply"

# Load the point cloud data
points = load_ply_file(file_path)

# Extract features (x, y, z) and additional features
x = points[:, 0]
y = points[:, 1]
z = points[:, 2]

# Calculate additional features: Curvature and Slope
def compute_curvature(points):
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)
    radius = 0.1  # Define search radius for computing normal curvature
    pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=radius, max_nn=30))
    normals = np.asarray(pcd.normals)
    
    # Curvature = Normal dot Product with Surface Normal (for rough estimation)
    curvature = np.linalg.norm(normals, axis=1)
    return curvature

curvature = compute_curvature(points)

# Calculate slope as the angle between the normal vector and the z-axis
def compute_slope(normals):
    slope = np.arccos(normals[:, 2]) * 180 / np.pi  # in degrees
    return slope

# Feature Engineering: Stack features like x, y, z, curvature, and slope
features = np.vstack([x, y, z, curvature]).T
scaler = StandardScaler()
features = scaler.fit_transform(features)  # Normalize the features

# Generate labels manually or based on a heuristic (e.g., height threshold for initial guess)
height_threshold = np.percentile(z, 25)  # Ground points are typically lower
labels = np.array([0 if z_val < height_threshold else 1 for z_val in z])  # 0: ground, 1: non-ground

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2)

# Machine learning classifier (Random Forest or SVM)
clf = make_pipeline(StandardScaler(), RandomForestClassifier(n_estimators=100, max_depth=10))
clf.fit(X_train, y_train)

# Predict labels for the entire point cloud
predicted_labels = clf.predict(features)

# Extract ground and non-ground points based on predictions
ground_points = points[predicted_labels == 0]
non_ground_points = points[predicted_labels == 1]

# Visualize the results using Open3D
ground_pcd = o3d.geometry.PointCloud()
non_ground_pcd = o3d.geometry.PointCloud()

# Set the points for the point clouds
ground_pcd.points = o3d.utility.Vector3dVector(ground_points)
non_ground_pcd.points = o3d.utility.Vector3dVector(non_ground_points)

# Set colors for visualization
ground_pcd.paint_uniform_color([0, 1, 0])  # Green for ground points
non_ground_pcd.paint_uniform_color([1, 0, 0])  # Red for non-ground points

# Save the point clouds to files
output_dir = "/home/shrikar/RnD/Trials/terrain"

# Ensure the output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Save the ground and non-ground point clouds as PLY files
ground_pcd_path = os.path.join(output_dir, "ground_points.ply")
non_ground_pcd_path = os.path.join(output_dir, "non_ground_points.ply")

o3d.io.write_point_cloud(ground_pcd_path, ground_pcd)
o3d.io.write_point_cloud(non_ground_pcd_path, non_ground_pcd)

print(f"Ground points saved to {ground_pcd_path}")
print(f"Non-ground points saved to {non_ground_pcd_path}")

# Classification Report for performance evaluation
print(classification_report(y_test, clf.predict(X_test)))

# RANSAC-based Ground Segmentation (optional, better precision)
from sklearn.linear_model import RANSACRegressor

def ransac_ground_segmentation(points, max_distance=0.1):
    # Use RANSAC to fit the ground plane
    ransac = RANSACRegressor(residual_threshold=max_distance, random_state=42)
    X = points[:, :2]  # Only x, y for plane fitting
    y = points[:, 2]  # z-coordinate is the target value
    ransac.fit(X, y)
    inliers = ransac.inlier_mask_

    return points[inliers], points[~inliers]

# Perform RANSAC segmentation on the original points
ransac_ground, ransac_non_ground = ransac_ground_segmentation(points)

# Visualize RANSAC-based segmentation results
ransac_ground_pcd = o3d.geometry.PointCloud()
ransac_non_ground_pcd = o3d.geometry.PointCloud()

ransac_ground_pcd.points = o3d.utility.Vector3dVector(ransac_ground)
ransac_non_ground_pcd.points = o3d.utility.Vector3dVector(ransac_non_ground)

ransac_ground_pcd.paint_uniform_color([0, 1, 0])  # Green for ground points
ransac_non_ground_pcd.paint_uniform_color([1, 0, 0])  # Red for non-ground points

# Save RANSAC results
ransac_ground_pcd_path = os.path.join(output_dir, "ransac_ground_points.ply")
ransac_non_ground_pcd_path = os.path.join(output_dir, "ransac_non_ground_points.ply")

o3d.io.write_point_cloud(ransac_ground_pcd_path, ransac_ground_pcd)
o3d.io.write_point_cloud(ransac_non_ground_pcd_path, ransac_non_ground_pcd)

print(f"RANSAC Ground points saved to {ransac_ground_pcd_path}")
print(f"RANSAC Non-ground points saved to {ransac_non_ground_pcd_path}")

# Function to save a screenshot of the Open3D visualizer
def save_visualization_image(pcds, save_path):
    vis = o3d.visualization.Visualizer()
    vis.create_window(visible=False)
    for pcd in pcds:
        vis.add_geometry(pcd)
    vis.poll_events()
    vis.update_renderer()
    vis.capture_screen_image(save_path)
    vis.destroy_window()

o3d.visualization.draw_geometries([ransac_ground_pcd, ransac_non_ground_pcd])


# Save images for both ground/non-ground and RANSAC visualizations
save_visualization_image([ground_pcd, non_ground_pcd], "/home/shrikar/RnD/Trials/terrain/ground_non_ground_visualization.jpg")
save_visualization_image([ransac_ground_pcd, ransac_non_ground_pcd], "/home/shrikar/RnD/Trials/terrain/ransac_visualization.jpg")

print("Visualization images saved.")
