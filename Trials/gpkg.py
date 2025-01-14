import geopandas as gpd
import open3d as o3d
import numpy as np

# Load the GPKG file (vegetation and stump data)
gpkg = gpd.read_file("../dataset/STUMP.gpkg")
print(gpkg.head())  # Check the attributes

# Load the PLY point cloud file
point_cloud = o3d.io.read_point_cloud("../dataset/filtered_point_cloud.ply")
points = np.asarray(point_cloud.points)

# Visualize the point cloud
o3d.visualization.draw_geometries([point_cloud])

# Now, proceed with segmentation and feature extraction for machine learning
