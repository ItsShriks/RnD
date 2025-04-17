import numpy as np
import open3d as o3d
from sklearn.neighbors import NearestNeighbors
import rasterio
import logging

# Set up logging for debugging purposes
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def load_ply(file_path):
    """ Load a PLY point cloud and handle errors. """
    try:
        pcd = o3d.io.read_point_cloud(file_path)
        if not pcd.is_empty():
            logging.info(f"Successfully loaded PLY file: {file_path}")
            return pcd
        else:
            raise ValueError("Loaded PLY is empty!")
    except Exception as e:
        logging.error(f"Error loading PLY file: {file_path} - {e}")
        raise

def load_dtm_as_point_cloud(dtm_file):
    """ Load DTM (GeoTIFF) and convert it into a point cloud. """
    try:
        with rasterio.open(dtm_file) as src:
            dtm_array = src.read(1)  # Read the first band (elevation)
            transform = src.transform
            rows, cols = np.meshgrid(np.arange(dtm_array.shape[0]), np.arange(dtm_array.shape[1]), indexing='ij')
            xs, ys = rasterio.transform.xy(transform, rows, cols)
            xs = np.array(xs).flatten()
            ys = np.array(ys).flatten()
            zs = dtm_array.flatten()

            # Filter out invalid points (NaN or zero values)
            valid_points = ~np.isnan(zs)
            xs, ys, zs = xs[valid_points], ys[valid_points], zs[valid_points]

            dtm_points = np.vstack((xs, ys, zs)).T
            dtm_cloud = o3d.geometry.PointCloud()
            dtm_cloud.points = o3d.utility.Vector3dVector(dtm_points)

            logging.info(f"Successfully loaded and converted DTM: {dtm_file}")
            return dtm_cloud
    except Exception as e:
        logging.error(f"Error loading or processing DTM file: {dtm_file} - {e}")
        raise

def apply_transformation(pcd, transformation_matrix):
    """ Apply a transformation matrix to the point cloud. """
    try:
        pcd.transform(transformation_matrix)
        logging.info("Transformation applied successfully to the PLY point cloud.")
    except Exception as e:
        logging.error(f"Error applying transformation to point cloud: {e}")
        raise

def compute_rms_error(pcd, dtm_cloud):
    """ Compute RMS error between two point clouds. """
    try:
        distances = pcd.compute_point_cloud_distance(dtm_cloud)
        rms_error = np.sqrt(np.mean(np.array(distances) ** 2))
        logging.info(f"RMS Error: {rms_error}")
        return rms_error
    except Exception as e:
        logging.error(f"Error computing RMS error: {e}")
        raise

def compare_z_values(pcd, dtm_cloud):
    """ Compare Z-values (elevation) between transformed PLY and DTM. """
    try:
        ply_xyz = np.asarray(pcd.points)
        dtm_xyz = np.asarray(dtm_cloud.points)

        nn = NearestNeighbors(n_neighbors=1)
        nn.fit(dtm_xyz[:, :2])  # Use only X, Y coordinates for matching
        dist, indices = nn.kneighbors(ply_xyz[:, :2])

        z_diff = ply_xyz[:, 2] - dtm_xyz[indices, 2]
        rms_z_diff = np.sqrt(np.mean(z_diff ** 2))

        logging.info(f"RMS Z-Error: {rms_z_diff}")
        return z_diff, rms_z_diff
    except Exception as e:
        logging.error(f"Error comparing Z-values: {e}")
        raise

def calculate_statistical_analysis(z_diff):
    """ Perform statistical analysis on the Z-difference. """
    try:
        mean_z_diff = np.mean(z_diff)
        std_z_diff = np.std(z_diff)
        max_z_diff = np.max(z_diff)
        min_z_diff = np.min(z_diff)

        logging.info(f"Mean Z-Difference: {mean_z_diff}")
        logging.info(f"Standard Deviation of Z-Difference: {std_z_diff}")
        logging.info(f"Maximum Z-Difference: {max_z_diff}")
        logging.info(f"Minimum Z-Difference: {min_z_diff}")
    except Exception as e:
        logging.error(f"Error performing statistical analysis: {e}")
        raise

def main():
    try:
        # Load the original PLY file
        pcd = load_ply('/Users/shrikar/Library/Mobile Documents/com~apple~CloudDocs/Sem IV/R&D/RnD/Trials/terrain/ransac_ground_points.ply')

        # Define the ICP transformation matrix
        transformation_matrix = np.array([
            [0.999, 0.018, 0.039, -105.120],
            [-0.021, 0.998, 0.057, 7.501],
            [-0.037, -0.058, 0.998, 4.196],
            [0, 0, 0, 1]
        ])

        # Apply the transformation to the point cloud
        apply_transformation(pcd, transformation_matrix)

        # Save the transformed PLY (optional)
        o3d.io.write_point_cloud("transformed_ply.ply", pcd)

        # Visualize the transformed point cloud
        o3d.visualization.draw_geometries([pcd])

        # Load the DTM (GeoTIFF)
        dtm_cloud = load_dtm_as_point_cloud('/Users/shrikar/Library/Mobile Documents/com~apple~CloudDocs/Sem IV/R&D/RnD/Large-files/RGB-UTM32/DTM-source-9mm.tif')

        # Compute RMS error between the PLY and DTM
        rms_error = compute_rms_error(pcd, dtm_cloud)

        # Compare Z-values (elevation) between transformed PLY and DTM
        z_diff, rms_z_diff = compare_z_values(pcd, dtm_cloud)

        # Perform statistical analysis on the Z-difference
        calculate_statistical_analysis(z_diff)

    except Exception as e:
        logging.error(f"An error occurred in the main process: {e}")

if __name__ == "__main__":
    main()
