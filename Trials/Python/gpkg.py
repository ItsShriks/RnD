import geopandas as gpd
import open3d as o3d
import numpy as np

# Load the GPKG file (vegetation and stump data)
gpkg = gpd.read_file("../../dataset/STUMP.gpkg")
print(gpkg.head())  # Check the attributes
print(f"GPKG CRS: {gpkg.crs}")  # Check CRS


# Load the PLY point cloud file
point_cloud = o3d.io.read_point_cloud("../../dataset/filtered_point_cloud.ply")
points = np.asarray(point_cloud.points)

vis = o3d.visualization.Visualizer()
vis.create_window()

# Add the point cloud to the visualizer
vis.add_geometry(point_cloud)

# Iterate over the rows in GPKG to extract and visualize vegetation/stump data
for idx, row in gpkg.iterrows():
    # Check if the data is points or polygons and handle accordingly
    geom = row.geometry

    if geom.geom_type == 'Point':  # If the geometry is a point (e.g., a stump or tree location)
        # Create a PointCloud from the GPKG point and add it to the visualizer
        stump_point = o3d.geometry.PointCloud()
        stump_point.points = o3d.utility.Vector3dVector(np.array([[geom.x, geom.y, 0]]))  # Assuming 2D point, z = 0
        stump_point.paint_uniform_color([1, 0, 0])  # Red color for stumps/vegetation
        vis.add_geometry(stump_point)

    elif geom.geom_type == 'Polygon':  # If the geometry is a polygon (e.g., vegetation boundary)
        # Convert polygon to a mesh or lineset to visualize
        vertices = np.array([list(geom.exterior.coords)])
        lines = [[i, i + 1] for i in range(len(vertices[0]) - 1)] + [[len(vertices[0]) - 1, 0]]
        
        # Create a LineSet for the polygon
        line_set = o3d.geometry.LineSet()
        line_set.points = o3d.utility.Vector3dVector(vertices[0])
        line_set.lines = o3d.utility.Vector2iVector(lines)
        line_set.paint_uniform_color([0, 1, 0])  # Green color for vegetation polygons
        vis.add_geometry(line_set)

# Run the visualization
vis.run()
vis.destroy_window()

print(f"Point cloud contains {len(points)} points")
print(f"GPKG contains {len(gpkg)} features")
