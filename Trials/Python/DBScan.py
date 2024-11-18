import open3d as o3d
import numpy as np
from sklearn.cluster import DBSCAN
import matplotlib as plt

# Load point cloud from file
pcd = o3d.io.read_point_cloud("/home/shrikar/RnD/filtered_point_cloud.ply")  # Replace with your file path
# Convert Open3D point cloud to NumPy array for DBSCAN processing
points = np.asarray(pcd.points)

# Apply DBSCAN clustering
db = DBSCAN(eps=0.05, min_samples=10).fit(points)  # Adjust eps and min_samples based on your data

# Get cluster labels for each point
labels = db.labels_

# Get the unique cluster labels (excluding -1 for noise)
unique_labels = set(labels)
num_clusters = len(unique_labels) - (1 if -1 in unique_labels else 0)

# Print the number of clusters
print(f"Number of clusters (excluding noise): {num_clusters}")

# Visualize the point cloud with clusters color-coded
colors = plt.cm.jet(np.linspace(0, 1, len(unique_labels)))

# Initialize an array for colors (size of points array, RGB format)
pcd_colors = np.zeros((points.shape[0], 3))  # Initialize as black (0,0,0)

# Assign colors to each point based on its label
for i, label in enumerate(labels):
    if label == -1:  # Noise points
        pcd_colors[i] = [0, 0, 0]  # Black for noise
    else:
        # Get the RGB values from the colormap (ignore alpha channel)
        pcd_colors[i] = colors[label][:3]  # Extract RGB from RGBA

# Apply the color array to the point cloud
pcd.colors = o3d.utility.Vector3dVector(pcd_colors)

# Visualize the point cloud with DBSCAN clusters
o3d.visualization.draw_geometries([pcd], window_name="DBSCAN Clusters")

# Optionally, you can extract points belonging to specific clusters
# For example, if you want to extract the points in the largest cluster (label 0):
cluster_points = points[labels == 0]  # Adjust cluster label as needed
