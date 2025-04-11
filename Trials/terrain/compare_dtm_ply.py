import numpy as np
import rasterio
import open3d as o3d
from scipy.spatial import cKDTree
import matplotlib.pyplot as plt

def load_dtm_tif(filename):
    with rasterio.open(filename) as src:
        dtm = src.read(1)
        transform = src.transform

        rows, cols = np.indices(dtm.shape)
        xs, ys = rasterio.transform.xy(transform, rows, cols)
        xs = np.array(xs)
        ys = np.array(ys)

        points = np.vstack((xs.ravel(), ys.ravel(), dtm.ravel())).T

    # Remove NaN or nodata values
    valid_mask = np.isfinite(points[:, 2])
    return points[valid_mask]

def load_ply_file(filename):
    pcd = o3d.io.read_point_cloud(filename)
    return np.asarray(pcd.points)

def compare_elevation(dtm_points, ply_points, sample_size=10000):
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
    plt.hist(diff, bins=100, color='steelblue', edgecolor='black')
    plt.title("Histogram of Elevation Differences (DTM - PLY)")
    plt.xlabel("Height Difference (m)")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.show()

def main():
    dtm_file = '/Users/shrikar/Library/Mobile Documents/com~apple~CloudDocs/Sem IV/R&D/RnD/Large-files/RGB-UTM32/DTM-source-9mm.tif'
    ply_file = '/Users/shrikar/Library/Mobile Documents/com~apple~CloudDocs/Sem IV/R&D/RnD/Trials/terrain/ground_points.ply'

    print("Loading DTM...")
    dtm_points = load_dtm_tif(dtm_file)
    print(f"Loaded {len(dtm_points)} points from DTM")

    print("Loading PLY...")
    ply_points = load_ply_file(ply_file)
    print(f"Loaded {len(ply_points)} points from PLY")

    print("Comparing elevation...")
    diff, _, _ = compare_elevation(dtm_points, ply_points)

    print_stats(diff)
    plot_histogram(diff)

if __name__ == "__main__":
    main()
