import open3d as o3d
import numpy as np



def compute_curvature(pcd, k=30):
    """Estimate curvature based on eigenvalues of the local neighborhood."""
    pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamKNN(k))
    
    curvatures = []
    kd_tree = o3d.geometry.KDTreeFlann(pcd)

    points = np.asarray(pcd.points)
    
    for i, point in enumerate(points):
        _, idx, _ = kd_tree.search_knn_vector_3d(point, k)
        neighbors = points[idx, :]
        
        covariance_matrix = np.cov(neighbors.T)
        eigenvalues = np.linalg.eigvals(covariance_matrix)
        curvature = min(eigenvalues) / sum(eigenvalues)  # Approximate curvature
        curvatures.append(curvature)
    
    return np.array(curvatures)

def compute_density(pcd, radius=0.1):
    """Estimate point cloud density by counting neighbors within a given radius."""
    kd_tree = o3d.geometry.KDTreeFlann(pcd)
    densities = []

    for point in np.asarray(pcd.points):
        _, idx, _ = kd_tree.search_radius_vector_3d(point, radius)
        densities.append(len(idx))

    return np.array(densities)

def extract_features(pcd, k=30, radius=0.1):
    """Extract point, normal, curvature, and density features."""
    pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamKNN(k))
    
    curvatures = compute_curvature(pcd, k)
    densities = compute_density(pcd, radius)

    points = np.asarray(pcd.points)
    normals = np.asarray(pcd.normals)
    features = np.hstack((points, normals, curvatures.reshape(-1, 1), densities.reshape(-1, 1)))

    return features

pcd = o3d.io.read_point_cloud("/Users/shrikar/Library/Mobile Documents/com~apple~CloudDocs/Sem III/R&D/RnD/dataset/Separated.ply")  # Replace with your file

features = extract_features(pcd)

o3d.visualization.draw_geometries([pcd])
header = "x,y,z,nx,ny,nz,curvature,density"
np.savetxt("/Users/shrikar/Library/Mobile Documents/com~apple~CloudDocs/Sem III/R&D/RnD/Trials/point_cloud_features.csv", features, delimiter=",", header=header, comments="")
