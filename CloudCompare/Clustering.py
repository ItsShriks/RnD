import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt

# Load the binary file
file_path = 'GlobalMap_Cropped.bin'

# Read the binary file as float32, skipping the first 100 bytes (adjust this based on your file structure)
with open(file_path, 'rb') as file:
    file.seek(100)  # Skip metadata
    data = np.fromfile(file, dtype=np.float32)

# Reshape the data assuming it represents 3D points (x, y, z)
if data.size % 3 == 0:
    reshaped_data = data.reshape(-1, 3)
else:
    reshaped_data = data[:-(data.size % 3)].reshape(-1, 3)  # Trim excess to fit into (n, 3)

# Remove rows containing NaN values
reshaped_data = reshaped_data[~np.isnan(reshaped_data).any(axis=1)]

# Normalize the data for clustering
scaler = StandardScaler()
normalized_data = scaler.fit_transform(reshaped_data)

# Apply DBSCAN clustering
dbscan = DBSCAN(eps=0.05, min_samples=10)  # Adjust eps and min_samples as needed
dbscan_labels = dbscan.fit_predict(normalized_data)

# Count clusters and noise points
num_clusters = len(set(dbscan_labels)) - (1 if -1 in dbscan_labels else 0)
num_noise_points = list(dbscan_labels).count(-1)

print(f'Number of clusters found: {num_clusters}')
print(f'Number of noise points: {num_noise_points}')

# Visualize the clusters (if 3D data)
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plotting the clusters, where noise points are in black
unique_labels = set(dbscan_labels)
colors = plt.cm.Spectral(np.linspace(0, 1, len(unique_labels)))

for label, color in zip(unique_labels, colors):
    if label == -1:  # Noise points
        color = 'k'
        label_name = 'Noise'
    else:
        label_name = f'Cluster {label}'
    
    class_member_mask = (dbscan_labels == label)
    xyz = normalized_data[class_member_mask]
    ax.scatter(xyz[:, 0], xyz[:, 1], xyz[:, 2], s=20, c=[color], label=label_name)

ax.set_title('DBSCAN Clustering Results')
ax.legend()
plt.show()
