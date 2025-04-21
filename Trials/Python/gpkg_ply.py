import geopandas as gpd
import pyvista as pv
from shapely.geometry import Polygon, MultiPolygon
import numpy as np

gpkg_file = '/Users/shrikar/Library/Mobile Documents/com~apple~CloudDocs/Sem IV/R&D/RnD/dataset/STUMP.gpkg'
gdf = gpd.read_file(gpkg_file)
extrusion_height = 1
plotter = pv.Plotter()

def create_3d_polygon_mesh(polygon, height):
    if isinstance(polygon, Polygon):
        points = np.array(list(polygon.exterior.coords))
        points_3d = np.hstack([points, np.zeros((points.shape[0], 1))])  # Add z=0 to each point
        points_3d_with_height = np.hstack([points, np.full((points.shape[0], 1), height)])  # Add z=height to each point
        points_3d = np.vstack([points_3d, points_3d_with_height])

        faces = []
        for i in range(len(points) - 1):
            faces.append([4, i, (i + 1) % len(points), i + len(points), (i + 1) % len(points) + len(points)])
        faces = np.array(faces)

        mesh = pv.PolyData(points_3d, faces)
        return mesh
    return None

merged_geometry = gdf.geometry.unary_union
centroid = merged_geometry.centroid
print(f"Centroid of the entire file: {centroid.x}, {centroid.y}, 0")

centroids = np.array([[centroid.x, centroid.y, 0]])

all_meshes = []

for index, row in gdf.iterrows():
    geom = row['geometry']
    if geom.geom_type == 'Polygon':
        mesh = create_3d_polygon_mesh(geom, extrusion_height)
        if mesh:
            all_meshes.append(mesh)
    elif geom.geom_type == 'MultiPolygon':
        for polygon in geom.geoms:
            mesh = create_3d_polygon_mesh(polygon, extrusion_height)
            if mesh:
                all_meshes.append(mesh)


combined_mesh = all_meshes[0] if all_meshes else None
for mesh in all_meshes[1:]:
    combined_mesh = combined_mesh.merge(mesh)

# Add centroid as a red point
centroid_mesh = pv.PolyData(centroids)
centroid_mesh["point_scalars"] = np.array([1])
combined_mesh += centroid_mesh

ply_file_path = '/Users/shrikar/Library/Mobile Documents/com~apple~CloudDocs/Sem IV/R&D/RnD/dataset/Stump_10.ply'
combined_mesh.save(ply_file_path)

print(f"Saved the 3D model with centroid to {ply_file_path}")


bounds = combined_mesh.bounds
width = bounds[1] - bounds[0]
height = bounds[3] - bounds[2]
depth = bounds[5] - bounds[4]

print(f"Bounding box dimensions:")
print(f"Width = {width} meters")
print(f"Height = {height} meters")
print(f"Depth = {depth} meters")

plotter.add_mesh(combined_mesh, show_edges=True, color="lightblue")
plotter.add_points(centroids, color="red", point_size=10)
plotter.show()
