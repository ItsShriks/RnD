import open3d as o3d
import numpy as np

pcd1 = o3d.io.read_point_cloud("/home/shrikar/RnD/dataset/rgb-d.ply")
pcd2 = o3d.io.read_point_cloud("/home/shrikar/RnD/dataset/STUMP.ply")

distances = np.asarray(pcd1.compute_point_cloud_distance(pcd2))

threshold = 0.01  

overlapping_indices = np.where(distances < threshold)[0]
overlapping_pcd = pcd1.select_by_index(overlapping_indices)

o3d.visualization.draw_geometries([overlapping_pcd])

#o3d.io.write_point_cloud("overlapping.ply", overlapping_pcd)
