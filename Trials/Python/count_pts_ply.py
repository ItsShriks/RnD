import os
import open3d as o3d

def count_points_in_ply_files(directory, threshold=1000000):
    ply_files = [f for f in os.listdir(directory) if f.endswith('.ply')]
    total_files = len(ply_files)
    below_threshold_count = 0

    print(f"Checking .ply files in: {directory}")
    for ply_file in ply_files:
        file_path = os.path.join(directory, ply_file)
        try:
            pcd = o3d.io.read_point_cloud(file_path)
            num_points = len(pcd.points)
            if num_points < threshold:
                print(f"{ply_file} has {num_points} points (less than {threshold})")
                below_threshold_count += 1
        except Exception as e:
            print(f"Failed to read {ply_file}: {e}")

    print(f"\nSummary: {below_threshold_count} out of {total_files} files have less than {threshold} points.")

# Example usage:
directory_path = '/Users/shrikar/Library/Mobile Documents/com~apple~CloudDocs/Sem IV/R&D/RnD/dataset'
count_points_in_ply_files(directory_path)
