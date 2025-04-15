import open3d as o3d
import numpy as np
import pandas as pd
import os

# Load the point cloud
pcd = o3d.io.read_point_cloud('/Users/shrikar/Library/Mobile Documents/com~apple~CloudDocs/Sem III/R&D/RnD/dataset/filtered_point_cloud.ply')
points = np.asarray(pcd.points)

# Parameters
grid_size = 2.0  # Size of square in meters
x_total = 68.0   # Total width in meters
y_total = 80.0   # Total height in meters

# Create DataFrame
df = pd.DataFrame(points, columns=["x", "y", "z"])

# Normalize coordinates
min_x, min_y = df["x"].min(), df["y"].min()
df["x_shifted"] = df["x"] - min_x
df["y_shifted"] = df["y"] - min_y

# Assign grid cell IDs
df["grid_x"] = np.floor(df["x_shifted"] / grid_size).astype(int)
df["grid_y"] = np.floor(df["y_shifted"] / grid_size).astype(int)

# Grid dimensions
x_cells = int(np.ceil(x_total / grid_size))
y_cells = int(np.ceil(y_total / grid_size))
print(f"Grid layout: {x_cells} columns × {y_cells} rows")

# Group by grid cell
grid_groups = df.groupby(["grid_x", "grid_y"])

# Create 'grids' output directory
output_dir = "grids_2.0"
os.makedirs(output_dir, exist_ok=True)

# Save each grid cell as .ply file
for (gx, gy), group in grid_groups:
    cell_points = group[["x", "y", "z"]].values
    if len(cell_points) == 0:
        continue
    cell_pcd = o3d.geometry.PointCloud()
    cell_pcd.points = o3d.utility.Vector3dVector(cell_points)
    filename = os.path.join(output_dir, f"cell_{gx}_{gy}.ply")
    o3d.io.write_point_cloud(filename, cell_pcd)
    print(f"Saved: {filename} with {len(cell_points)} points")
