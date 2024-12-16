import open3d as o3d
import numpy as np
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load the point cloud file
pcd = o3d.io.read_point_cloud("filtered_point_cloud.ply")

# Convert the point cloud to numpy array
points = np.asarray(pcd.points)

# DBSCAN clustering for terrain and tree trunks
clustering = DBSCAN(eps=0.5, min_samples=100).fit(points)

# Get labels for each point
labels = clustering.labels_

# Number of clusters in labels, ignoring noise if present (-1 label)
n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
print(f"Number of clusters: {n_clusters}")

# Prepare colors for visualization
unique_labels = set(labels)
colors = plt.get_cmap("tab20")(np.linspace(0, 1, len(unique_labels)))
cluster_colors = np.array([colors[label] if label != -1 else [0, 0, 0, 1] for label in labels])

# Visualize the clusters in matplotlib with a legend
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")
for label, color in zip(unique_labels, colors):
    if label == -1:
        label_name = "Noise"
        cluster_points = points[labels == label]
    else:
        label_name = f"Cluster {label}"
        cluster_points = points[labels == label]
    
    ax.scatter(
        cluster_points[:, 0],
        cluster_points[:, 1],
        cluster_points[:, 2],
        c=[color[:3]],  # Use RGB only
        label=label_name,
        s=1
    )

# Set plot details
ax.set_title("DBSCAN Clustered Point Cloud")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.legend(loc="best", title="Clusters", markerscale=5)
plt.show()