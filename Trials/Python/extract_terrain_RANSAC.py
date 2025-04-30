import open3d as o3d
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
from sklearn.pipeline import make_pipeline
import os
import matplotlib.pyplot as plt

def plot_with_legend_and_scale(ground_points, non_ground_points, save_path):
    fig, ax = plt.subplots(figsize=(10, 8))

    # Project to 2D (e.g., x, y)
    ax.scatter(non_ground_points[:, 0], non_ground_points[:, 1], c='red', s=1, label='Non-Ground')
    ax.scatter(ground_points[:, 0], ground_points[:, 1], c='green', s=1, label='Ground')

    # Add legend and scale
    ax.legend(loc='upper left')
    ax.set_title("Ground vs Non-Ground Segmentation")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")

    # Add a simple scale bar (e.g., 1 meter)
    scale_length = 1  # meters
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    ax.plot([xlim[0] + 0.05*(xlim[1]-xlim[0]), xlim[0] + 0.05*(xlim[1]-xlim[0]) + scale_length],
            [ylim[0] + 0.05*(ylim[1]-ylim[0])]*2, 'k-', lw=2)
    ax.text(xlim[0] + 0.05*(xlim[1]-xlim[0]), ylim[0] + 0.07*(ylim[1]-ylim[0]), f"{scale_length} m")

    plt.axis('equal')
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.close()

def load_ply_file(file_path):
    pcd = o3d.io.read_point_cloud(file_path)
    points = np.asarray(pcd.points)
    return points

file_path = '/Users/shrikar/RnD/dataset/filtered_point_cloud.ply'
points = load_ply_file(file_path)

x = points[:, 0]
y = points[:, 1]
z = points[:, 2]

def compute_curvature(points):
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)
    radius = 0.1
    pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=radius, max_nn=30))
    normals = np.asarray(pcd.normals)
    curvature = np.linalg.norm(normals, axis=1)
    return curvature

curvature = compute_curvature(points)

def compute_slope(normals):
    slope = np.arccos(normals[:, 2]) * 180 / np.pi
    return slope

features = np.vstack([x, y, z, curvature]).T
scaler = StandardScaler()
features = scaler.fit_transform(features)

height_threshold = np.percentile(z, 25)
labels = np.array([0 if z_val < height_threshold else 1 for z_val in z])

X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2)

clf = make_pipeline(StandardScaler(), RandomForestClassifier(n_estimators=100, max_depth=10))
clf.fit(X_train, y_train)

predicted_labels = clf.predict(features)

ground_points = points[predicted_labels == 0]
non_ground_points = points[predicted_labels == 1]

ground_pcd = o3d.geometry.PointCloud()
non_ground_pcd = o3d.geometry.PointCloud()

ground_pcd.points = o3d.utility.Vector3dVector(ground_points)
non_ground_pcd.points = o3d.utility.Vector3dVector(non_ground_points)

ground_pcd.paint_uniform_color([0, 1, 0])
non_ground_pcd.paint_uniform_color([1, 0, 0])

output_dir = "/Users/shrikar/RnD/Snaps"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

ground_pcd_path = os.path.join(output_dir, "ground_points.ply")
non_ground_pcd_path = os.path.join(output_dir, "non_ground_points.ply")

o3d.io.write_point_cloud(ground_pcd_path, ground_pcd)
o3d.io.write_point_cloud(non_ground_pcd_path, non_ground_pcd)

print(f"Ground points saved to {ground_pcd_path}")
print(f"Non-ground points saved to {non_ground_pcd_path}")

print(classification_report(y_test, clf.predict(X_test)))

from sklearn.linear_model import RANSACRegressor

def ransac_ground_segmentation(points, max_distance=0.1):
    ransac = RANSACRegressor(residual_threshold=max_distance, random_state=42)
    X = points[:, :2]
    y = points[:, 2]
    ransac.fit(X, y)
    inliers = ransac.inlier_mask_
    return points[inliers], points[~inliers]

ransac_ground, ransac_non_ground = ransac_ground_segmentation(points)

ransac_ground_pcd = o3d.geometry.PointCloud()
ransac_non_ground_pcd = o3d.geometry.PointCloud()

ransac_ground_pcd.points = o3d.utility.Vector3dVector(ransac_ground)
ransac_non_ground_pcd.points = o3d.utility.Vector3dVector(ransac_non_ground)

ransac_ground_pcd.paint_uniform_color([0, 1, 0])
ransac_non_ground_pcd.paint_uniform_color([1, 0, 0])

ransac_ground_pcd_path = os.path.join(output_dir, "ransac_ground_points.ply")
ransac_non_ground_pcd_path = os.path.join(output_dir, "ransac_non_ground_points.ply")

o3d.io.write_point_cloud(ransac_ground_pcd_path, ransac_ground_pcd)
o3d.io.write_point_cloud(ransac_non_ground_pcd_path, ransac_non_ground_pcd)

print(f"RANSAC Ground points saved to {ransac_ground_pcd_path}")
print(f"RANSAC Non-ground points saved to {ransac_non_ground_pcd_path}")

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

save_visualization_image([ground_pcd, non_ground_pcd], "/Users/shrikar/RnD/Snaps/ground_non_ground_visualization.jpg")
save_visualization_image([ransac_ground_pcd, ransac_non_ground_pcd], "/Users/shrikar/RnD/Snaps/ransac_visualization.jpg")
plot_with_legend_and_scale(ground_points, non_ground_points, "/Users/shrikar/RnD/Snaps/ground_non_ground_with_legend.jpg")
print("Visualization images saved.")
