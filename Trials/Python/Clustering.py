import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
import open3d as o3d

# Load the binary file
file_path = 'filtered_point_cloud.ply'

point_cloud = o3d.io.read_point_cloud(file_path)

# Extract points as a NumPy array
points = np.asarray(point_cloud.points)

# Check for NaN or Inf values
print("Points stats:")
print(f"Min: {np.min(points, axis=0)}, Max: {np.max(points, axis=0)}")
print(f"Contains NaN: {np.isnan(points).any()}")
print(f"Contains Inf: {np.isinf(points).any()}")

# Remove NaN or Inf points
points = points[~np.isnan(points).any(axis=1)]
points = points[~np.isinf(points).any(axis=1)]

# Normalize the data
scaler = StandardScaler()
normalized_data = scaler.fit_transform(points)

# Check normalized data for NaN and Inf
if np.isnan(normalized_data).any() or np.isinf(normalized_data).any():
    raise ValueError("Normalized data contains NaN or Inf values.")

# Apply DBSCAN clustering
dbscan = DBSCAN(eps=0.05, min_samples=10)
dbscan_labels = dbscan.fit_predict(normalized_data)

# Count clusters and noise points
num_clusters = len(set(dbscan_labels)) - (1 if -1 in dbscan_labels else 0)
num_noise_points = list(dbscan_labels).count(-1)

print(f'Number of clusters found: {num_clusters}')
print(f'Number of noise points: {num_noise_points}')


# Visualize the clusters
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
unique_labels = set(dbscan_labels)
colors = plt.cm.Spectral(np.linspace(0, 1, len(unique_labels)))

for label, color in zip(unique_labels, colors):
    class_member_mask = (dbscan_labels == label)
    xyz = normalized_data[class_member_mask]
    ax.scatter(xyz[:, 0], xyz[:, 1], xyz[:, 2], s=20, c=color, label=f'Cluster {label}' if label != -1 else 'Noise')

ax.set_title('DBSCAN Clustering Results')
ax.legend()
plt.show()
