import numpy as np
from osgeo import gdal
import open3d as o3d

# Load GeoTIFF
ds = gdal.Open('input.tif')
band = ds.GetRasterBand(1)
elevation = band.ReadAsArray()

# Get geo-transform to convert pixel to coordinates
gt = ds.GetGeoTransform()
cols, rows = ds.RasterXSize, ds.RasterYSize

# Generate coordinates
x_coords = np.arange(cols) * gt[1] + gt[0]
y_coords = np.arange(rows) * gt[5] + gt[3]
xv, yv = np.meshgrid(x_coords, y_coords)

# Flatten all arrays
points = np.stack((xv.flatten(), yv.flatten(), elevation.flatten()), axis=1)

# Create Open3D point cloud
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(points)

# Save to .ply
o3d.io.write_point_cloud("output.ply", pcd)
