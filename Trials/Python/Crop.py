import open3d as o3d
import numpy as np
from shapely.geometry import Polygon, Point
import matplotlib.pyplot as plt
from shapely.geometry.polygon import orient

# Define the 5 points of the polygon (base) and the Z-axis height range
polygon_points = np.array([
    [-2.294216, 36.315838],
    [16.956844, -44.380180],
    [50.484165, -21.520457],
    [65.664795, 26.725346],
    [65.558228, 32.719646],
])

# Ensure the polygon is closed by adding the first point again at the end
polygon_points = np.vstack([polygon_points, polygon_points[0]])

min_z = -5  # Minimum Z value for the height range
max_z = 15  # Maximum Z value for the height range

# Create a Shapely polygon object for the base polygon
polygon = Polygon(polygon_points)

# Ensure the polygon is ordered correctly (clockwise or counterclockwise)
polygon = orient(polygon)  # This will make sure the polygon is oriented counterclockwise

# Check polygon validity
if polygon.is_valid:
    print("The polygon is valid.")
else:
    print("The polygon is invalid.")
    print("Polygon issue:", polygon.is_valid)

# Visualize the polygon and points
plt.figure(figsize=(8, 6))

# Extract X and Y coordinates of the points in the point cloud
pcd = o3d.io.read_point_cloud("lio-sam-output-map_field_D_flight-6/GlobalMapply.ply")  # Replace with your file path
points = np.asarray(pcd.points)
x_vals = points[:, 0]
y_vals = points[:, 1]
#Check Final.ply File error

# Plot the point cloud points
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
    # Debugging: Check Z values and point location
    if min_z <= z <= max_z:
        #print(f"Point ({x}, {y}, {z}) is within the Z range ({min_z}, {max_z})")
        pass
    # Check if the point is inside or on the boundary of the polygon on the X-Y plane
    if polygon.contains(Point(x, y)) or polygon.exterior.intersects(Point(x, y)):  # Also consider boundary points
        filtered_points.append(point)

# Debugging: Output number of filtered points
print(f"Number of points inside the polygon: {len(filtered_points)}")

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
    
    # Check the number of points in the point cloud
print(f"Number of points in the point cloud: {len(points)}")
print(f"Sample points: {points[:10]}")  # Print the first 10 points for inspection