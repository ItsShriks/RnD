import open3d as o3d
import numpy as np
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt

# Load the point cloud file
pcd = o3d.io.read_point_cloud("Final.ply")

# Convert the point cloud to numpy array
points = np.asarray(pcd.points)

# Visualize original point cloud
o3d.visualization.draw_geometries([pcd], window_name="Original Point Cloud")

# DBSCAN clustering for terrain and tree trunks
# Parameters: eps is the max distance between points in the same cluster, and min_samples is the min number of points to form a cluster
clustering = DBSCAN(eps=0.5, min_samples=10).fit(points)

# Get labels for each point
labels = clustering.labels_

# Number of clusters in labels, ignoring noise if present (-1 label)
n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
print(f"Number of clusters: {n_clusters}")

# Visualize the clusters
max_label = labels.max()
colors = plt.get_cmap("tab20")(labels / (max_label if max_label > 0 else 1))
colors[labels < 0] = 0  # Assign noise to black color
pcd.colors = o3d.utility.Vector3dVector(colors[:, :3])

# Visualize the clustered point cloud
o3d.visualization.draw_geometries([pcd], window_name="DBSCAN Clustered Point Cloud")

# Separate the clusters for further analysis (e.g., filtering terrain vs tree trunks)
for i in range(n_clusters):
    cluster_points = points[labels == i]
    print(f"Cluster {i} has {len(cluster_points)} points.")
    # You can apply additional heuristics here to distinguish terrain from tree trunks based on height, etc.

# Save the clustered point cloud (optional)
o3d.io.write_point_cloud("/mnt/data/clustered_point_cloud.ply", pcd)
