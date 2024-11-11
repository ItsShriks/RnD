import open3d as o3d
import numpy as np
from shapely.geometry import Polygon, Point
import matplotlib.pyplot as plt

# Define the 5 points of the polygon (base) and the Z-axis height range
polygon_points = np.array([
    [-2.294216, 36.315838],
    [16.956844, -44.380180],
    [65.558228, 32.719646],
    [65.664795, 26.725346],
    [50.484165, -21.520457],
])

# Ensure the polygon is closed by adding the first point again at the end
polygon_points = np.vstack([polygon_points, polygon_points[0]])

min_z = -4.84553  # Minimum Z value for the height range
max_z = 13.5509  # Maximum Z value for the height range

# Create a Shapely polygon object for the base polygon
polygon = Polygon(polygon_points)

# Load the point cloud
pcd = o3d.io.read_point_cloud("/Users/shrikar/Library/Mobile Documents/com~apple~CloudDocs/Sem III/R&D/RnD/Trials/Final.ply")  # Replace with your file path

# Convert point cloud to numpy array
points = np.asarray(pcd.points)

# Visualize the points in the polygon (to check if they should be inside)
x_vals = points[:, 0]
y_vals = points[:, 1]

# Plot the polygon and points
plt.figure(figsize=(8, 6))
plt.scatter(x_vals, y_vals, c='blue', label='Point Cloud Points')

# Plot the polygon
polygon_x, polygon_y = polygon.exterior.xy  # Get the X, Y coordinates of the polygon
plt.fill(polygon_x, polygon_y, 'r', alpha=0.3, label='Polygon')  # Polygon in red

# Additional plot formatting
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Point Cloud Points and Polygon')
plt.legend()
plt.grid(True)
plt.show()

# Initialize a list for storing filtered points
filtered_points = []

# Loop through each point in the point cloud
for point in points:
    x, y, z = point
    # Check if the point is inside or on the boundary of the polygon on the X-Y plane and if Z is within the specified range
    if polygon.contains(Point(x, y)) or polygon.exterior.intersects(Point(x, y)):  # Also consider boundary points
        if min_z <= z <= max_z:
            filtered_points.append(point)

# Check if filtered_points is empty
if len(filtered_points) == 0:
    print("No points found within the specified polygon and Z range.")
else:
    # Convert filtered points back to a numpy array
    filtered_points = np.array(filtered_points)

    # Check the shape of the filtered points
    print(f"Filtered points shape: {filtered_points.shape}")

    # Convert the filtered points back to an Open3D point cloud
    filtered_pcd = o3d.geometry.PointCloud()
    filtered_pcd.points = o3d.utility.Vector3dVector(filtered_points)

    # Save or display the filtered point cloud
    o3d.io.write_point_cloud("filtered_point_cloud.ply", filtered_pcd)
    o3d.visualization.draw_geometries([filtered_pcd], window_name="Filtered Point Cloud")