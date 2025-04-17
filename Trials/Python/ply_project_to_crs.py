import open3d as o3d
import numpy as np
from pyproj import Transformer

# === Load RANSAC PLY point cloud ===
pcd = o3d.io.read_point_cloud('/Users/shrikar/Library/Mobile Documents/com~apple~CloudDocs/Sem IV/R&D/RnD/Trials/terrain/ransac_ground_points.ply')
points = np.asarray(pcd.points)

# === Define source and target CRS ===
source_crs = "EPSG:4326"      # <-- Change if needed (e.g. 4326, 4978, 32632)
target_crs = "EPSG:25832"     # Your DTM's CRS (confirmed)

# === Reproject using pyproj ===
transformer = Transformer.from_crs(source_crs, target_crs, always_xy=True)

x, y, z = points[:, 0], points[:, 1], points[:, 2]
x_new, y_new = transformer.transform(x, y)
points_reprojected = np.column_stack((x_new, y_new, z))

# === Update and save point cloud ===
pcd.points = o3d.utility.Vector3dVector(points_reprojected)
o3d.io.write_point_cloud('/Users/shrikar/Library/Mobile Documents/com~apple~CloudDocs/Sem IV/R&D/RnD/Trials/terrain/ransac_result_reprojected.ply', pcd)

print("✅ Point cloud reprojected to EPSG:25832 and saved.")
