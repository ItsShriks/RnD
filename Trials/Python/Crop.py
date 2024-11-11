import open3d as o3d
import numpy as np
from shapely.geometry import Polygon, Point

# Define the 5 points of the polygon (base) and the Z-axis height range
polygon_points = np.array([
    [-2.294216, 36.315838],
    [16.956844, -44.380180],
    [65.558228, 32.719646],
    [65.664795, 26.725346],
    [50.484165, -21.520457],
])

min_z = -4.84553  # Minimum Z value for the height range
max_z = 13.5509  # Maximum Z value for the height range

# Create a Shapely polygon object for the base polygon
polygon = Polygon(polygon_points)

# Load the point cloud
pcd = o3d.io.read_point_cloud("/Users/shrikar/Library/Mobile Documents/com~apple~CloudDocs/Sem III/R&D/RnD/Trials/Final.ply")  # Replace with your file path

# Convert point cloud to numpy array
points = np.asarray(pcd.points)

# Initialize a list for storing filtered points
filtered_points = []

# Loop through each point in the point cloud
for point in points:
    x, y, z = point
    # Check if the point is inside the polygon on the X-Y plane and if Z is within the specified range
    if polygon.contains(Point(x, y)) and (min_z <= z <= max_z):
        filtered_points.append(point)

# Convert filtered points back to a numpy array
filtered_points = np.array(filtered_points)

# Convert the filtered points back to an Open3D point cloud
filtered_pcd = o3d.geometry.PointCloud()
filtered_pcd.points = o3d.utility.Vector3dVector(filtered_points)

# Save or display the filtered point cloud
o3d.io.write_point_cloud("filtered_point_cloud.ply", filtered_pcd)
o3d.visualization.draw_geometries([filtered_pcd], window_name="Filtered Point Cloud")