import numpy as np
import rasterio
import open3d as o3d
from scipy.spatial import cKDTree
import matplotlib.pyplot as plt

def load_dtm_tif(filename, resolution=0.009, origin=(0.0, 0.0)):
    """
    Load a non-georeferenced DTM raster and generate (x, y, z) points.
    """
    with rasterio.open(filename) as src:
        dtm = src.read(1)

    rows, cols = np.indices(dtm.shape)
    xs = cols * resolution + origin[0]
    ys = rows * resolution + origin[1]

    points = np.vstack((xs.ravel(), ys.ravel(), dtm.ravel())).T

    # Remove NaN or nodata values
    valid_mask = np.isfinite(points[:, 2])
    return points[valid_mask]

def load_ply_file(filename):
    """
    Load PLY point cloud using Open3D.
    """
    pcd = o3d.io.read_point_cloud(filename)
    return np.asarray(pcd.points)

def compare_elevation(dtm_points, ply_points, sample_size=10000):
    """
    Compare elevation between DTM and PLY point clouds using nearest neighbor.
    """
    if len(dtm_points) > sample_size:
        indices = np.random.choice(len(dtm_points), sample_size, replace=False)
        dtm_sample = dtm_points[indices]
    else:
        dtm_sample = dtm_points

    tree = cKDTree(ply_points[:, :2])
    distances, nearest_indices = tree.query(dtm_sample[:, :2])

    matched_ply_z = ply_points[nearest_indices][:, 2]
    dtm_z = dtm_sample[:, 2]

    elevation_diff = dtm_z - matched_ply_z

    return elevation_diff, dtm_sample, matched_ply_z

def print_stats(diff):
    print("Elevation Difference Statistics (DTM - PLY):")
    print(f"Mean Difference: {np.mean(diff):.3f} m")
    print(f"Standard Deviation: {np.std(diff):.3f} m")
    print(f"RMSE: {np.sqrt(np.mean(diff**2)):.3f} m")
    print(f"Min: {np.min(diff):.3f} m")
    print(f"Max: {np.max(diff):.3f} m")

def plot_histogram(diff):
    plt.figure()
    plt.hist(diff, bins=100, color='steelblue', edgecolor='black')
    plt.title("Histogram of Elevation Differences (DTM - PLY)")
    plt.xlabel("Height Difference (m)")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.show()

def plot_elevation_comparison(dtm_z, ply_z):
    plt.figure(figsize=(8, 6))
    plt.scatter(dtm_z, ply_z, s=1, alpha=0.5)
    plt.plot([min(dtm_z), max(dtm_z)], [min(dtm_z), max(dtm_z)], 'r--')
    plt.xlabel("DTM Elevation (m)")
    plt.ylabel("PLY Elevation (m)")
    plt.title("DTM vs PLY Elevation Comparison")
    plt.grid(True)
    plt.axis('equal')
    plt.show()

def plot_spatial_difference(dtm_sample, diff):
    plt.figure(figsize=(10, 8))
    plt.scatter(dtm_sample[:, 0], dtm_sample[:, 1], c=diff, cmap='coolwarm', s=2)
    plt.colorbar(label='Elevation Difference (m)')
    plt.title("Spatial Map of Elevation Differences (DTM - PLY)")
    plt.xlabel("X (Local or UTM)")
    plt.ylabel("Y (Local or UTM)")
    plt.axis('equal')
    plt.grid(True)
    plt.show()

def main():
    # 🔧 Set your file paths here
    dtm_file = '/Users/shrikar/Library/Mobile Documents/com~apple~CloudDocs/Sem IV/R&D/RnD/Large-files/RGB-UTM32/DTM-source-9mm.tif'
    ply_file = '/Users/shrikar/Library/Mobile Documents/com~apple~CloudDocs/Sem IV/R&D/RnD/Trials/terrain/ransac_ground_points.ply'

    # ⚙️ Set resolution (in meters) and optional origin (X0, Y0)
    resolution = 0.009  # 9 mm per pixel
    origin = (0.0, 0.0)  # Change if your DTM starts elsewhere

    print("Loading DTM...")
    dtm_points = load_dtm_tif(dtm_file, resolution=resolution, origin=origin)
    print(f"Loaded {len(dtm_points)} points from DTM")

    print("Loading PLY...")
    ply_points = load_ply_file(ply_file)
    print(f"Loaded {len(ply_points)} points from PLY")

    print("Comparing elevation...")
    diff, dtm_sample, matched_ply_z = compare_elevation(dtm_points, ply_points)

    print_stats(diff)
    plot_histogram(diff)
    plot_elevation_comparison(dtm_sample[:, 2], matched_ply_z)
    plot_spatial_difference(dtm_sample, diff)

if __name__ == "__main__":
    main()
