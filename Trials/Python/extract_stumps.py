import open3d as o3d
import numpy as np

pcd1 = o3d.io.read_point_cloud("/home/shrikar/RnD/dataset/STUMP.ply")
pcd2 = o3d.io.read_point_cloud("/home/shrikar/RnD/dataset/filtered_point_cloud.ply")

o3d.visualization.draw_geometries([pcd1, pcd2], window_name="Original Point Clouds")

threshold = 0.02
reg_icp = o3d.pipelines.registration.registration_icp(
    pcd2, pcd1, threshold, np.eye(4),
    o3d.pipelines.registration.TransformationEstimationPointToPoint()
)

pcd2_aligned = pcd2.transform(reg_icp.transformation)

o3d.visualization.draw_geometries([pcd1, pcd2_aligned], window_name="Aligned Point Clouds")

points1 = np.asarray(pcd1.points)
points2 = np.asarray(pcd2_aligned.points)

tolerance = 0.01
overlapping_points = []

for point1 in points1:
    distances = np.linalg.norm(points2 - point1, axis=1)
    if np.any(distances < tolerance):
        overlapping_points.append(point1)

overlapping_points = np.array(overlapping_points)

print(f"Number of overlapping points: {len(overlapping_points)}")
print("Overlapping points:", overlapping_points)

overlapping_pcd = o3d.geometry.PointCloud()
overlapping_pcd.points = o3d.utility.Vector3dVector(overlapping_points)
o3d.visualization.draw_geometries([overlapping_pcd], window_name="Overlapping Points")

# To save the overlapping points to a PLY file
# o3d.io.write_point_cloud("overlapping_points.ply", overlapping_pcd)
