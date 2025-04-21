import open3d as o3d
import numpy as np
from pathlib import Path

def convert_ply_dir_to_off(input_dir, output_dir, poisson_depth=9, density_threshold=0.01):
    input_dir = Path(input_dir)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    ply_files = list(input_dir.glob("*.ply"))
    if not ply_files:
        print("No .ply files found in:", input_dir)
        return

    for ply_path in ply_files:
        try:
            print(f"\nProcessing: {ply_path.name}")
            pcd = o3d.io.read_point_cloud(str(ply_path))

            if len(pcd.points) == 0:
                print("  ⚠️ Empty point cloud. Skipping.")
                continue

            if not pcd.has_normals():
                print("  Estimating normals...")
                pcd.estimate_normals()
                pcd.normalize_normals()

            mesh, densities = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(
                pcd, depth=poisson_depth
            )

            densities = np.asarray(densities)
            keep = densities > np.quantile(densities, density_threshold)
            mesh = mesh.select_by_index(np.where(keep)[0])

            off_path = output_dir / ply_path.with_suffix('.off').name
            o3d.io.write_triangle_mesh(str(off_path), mesh, write_ascii=True)
            print(f"  ✅ Saved: {off_path.name}")

        except Exception as e:
            print(f"  ❌ Failed to convert {ply_path.name}: {e}")

# Example usage:
input_folder = "/Users/shrikar/RnD/dataset/dataset_class/else/bad_train"         # Replace with your folder path
output_folder = "/Users/shrikar/RnD/dataset/dataset_class/else/train"       # Desired output folder
convert_ply_dir_to_off(input_folder, output_folder)
