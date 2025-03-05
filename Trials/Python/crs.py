import open3d as o3d
import numpy as np
from pyproj import Proj, Transformer

# Load the PLY file
ply_file = "/home/shrikar/RnD/dataset/RGB-D_wihtout ground.ply"
pcd = o3d.io.read_point_cloud(ply_file)

# Get the points from the point cloud
points = np.asarray(pcd.points)

# Define the source CRS (assumed WGS84 - EPSG:4326) and target CRS (EPSG:25832)
# We will use the Transformer object instead of Proj directly for better compatibility with newer versions of pyproj
src_proj = Proj(init="epsg:4326")  # Assumed WGS84 (lat, lon)
target_proj = Proj(init="epsg:25832")  # Target CRS (EPSG:25832, local projection)

transformer = Transformer.from_proj(src_proj, target_proj)

# Reproject the points (assumed WGS84 to EPSG:25832)
reprojected_points = []
for point in points:
    lon, lat, z = point  # Assuming lat, lon, and z
    x, y = transformer.transform(lon, lat)  # Transform lon, lat to x, y (in meters)
    reprojected_points.append([x, y, z])  # Keep z as is, or modify if needed

# Convert the reprojected points back into a point cloud
reprojected_points = np.array(reprojected_points)
reprojected_pcd = o3d.geometry.PointCloud()
reprojected_pcd.points = o3d.utility.Vector3dVector(reprojected_points)

# Save the reprojected point cloud to a new PLY file
o3d.io.write_point_cloud("/home/shrikar/RnD/dataset/RGB-D_wihtout ground_reprojected.ply", reprojected_pcd)

print("Reprojection completed and saved to reprojected.ply")
