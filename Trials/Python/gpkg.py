import geopandas as gpd
import open3d as o3d
from shapely.geometry import Point, MultiPolygon
import numpy as np

gpkg_file = "/home/shrikar/RnD/dataset/STUMP.gpkg"
gdf = gpd.read_file(gpkg_file)

print(f"GPKG CRS: {gdf.crs}")

ply_file = "/home/shrikar/RnD/dataset/RGB-D_wihtout ground_reprojected.ply"
pcd = o3d.io.read_point_cloud(ply_file)

print("Extracting points from ply")
points = np.asarray(pcd.points)

ply_crs = "EPSG:25832"
print(f"Assumed PLY CRS: {ply_crs}")

if gdf.crs != ply_crs:
    print("Reprojecting GPKG geometries to match PLY CRS...")
    gdf = gdf.to_crs(ply_crs)
else:
    print("CRS is already the same for both files.")

polygons = gdf['geometry']

print("Checking first few points from the PLY file:")
print(points[:5])  # Print first 5 points for debugging

print("Extracting inside points")
inside_points = []
for point in points:
    x, y, z = point
    shapely_point = Point(x, y)
    
    point_inside = False
    for polygon in polygons:
        if isinstance(polygon, MultiPolygon):
            for subpolygon in polygon.geoms:
                if subpolygon.contains(shapely_point):
                    inside_points.append(point)
                    point_inside = True
                    break
        elif polygon.contains(shapely_point):
            inside_points.append(point)
            point_inside = True
            break
    
    # Debugging if a point is inside any polygon
    if point_inside:
        print(f"Point inside polygon: {point}")

print(f"Total points inside polygons: {len(inside_points)}")

print("Saving the new ply")
inside_points = np.array(inside_points)
if inside_points.shape[0] > 0:
    inside_pcd = o3d.geometry.PointCloud()
    inside_pcd.points = o3d.utility.Vector3dVector(inside_points)
    o3d.io.write_point_cloud("inside_points.ply", inside_pcd)
else:
    print("No points inside the labeled regions.")
