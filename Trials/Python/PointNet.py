import torch
import open3d as o3d
import numpy as np
from pointnet2_pytorch import pointnet2_utils as pn2_utils

# Load your segmentation model
num_classes = 3  # Change this based on your dataset
model = PointNet2SegmentationModel(num_classes)
model.eval()  # Set to evaluation mode

# Load the point cloud file
pcd = o3d.io.read_point_cloud("/Users/shrikar/Library/Mobile Documents/com~apple~CloudDocs/Sem III/R&D/RnD/dataset/Separated.ply")
pcd = pcd.voxel_down_sample(voxel_size=0.02)  # Adjust voxel size for fewer points
points = np.asarray(pcd.points)  # Extract point coordinates (N, 3)

# Convert to PyTorch tensor and add batch dimension
#xyz = torch.tensor(points, dtype=torch.float32).unsqueeze(0)  # Shape: (1, N, 3)
xyz = torch.tensor(points, dtype=torch.float32).unsqueeze(0).permute(0, 2, 1)  # (1, 3, N)
# Run the model for segmentation
with torch.no_grad():
    logits = model(xyz.permute(0, 2, 1))  # Model expects (B, 3, N) format
    predictions = torch.argmax(logits, dim=1).squeeze(0)  # Shape: (N,)

# Convert predictions to NumPy
pred_labels = predictions.cpu().numpy()

# Assign labels as colors for visualization
colors = np.random.rand(num_classes, 3)  # Random colors for each class
pcd.colors = o3d.utility.Vector3dVector(colors[pred_labels])  # Apply colors

# Save the segmented point cloud
#o3d.io.write_point_cloud("segmented_output.ply", pcd)

# Visualize the segmented point cloud
o3d.visualization.draw_geometries([pcd], window_name="Segmented Point Cloud")

print(f"Point Cloud Shape: {xyz.shape}")  # Should be (1, 3, N)
print(f"Min, Max Points: {xyz.min()}, {xyz.max()}")
print(f"Model Input Shape: {xyz.shape}")

with torch.no_grad():
    logits = model(xyz)  # If it crashes here, it's a memory issue
print("Model Forward Pass Successful!")

predictions = torch.argmax(logits, dim=1).squeeze(0)
print(f"Predictions Shape: {predictions.shape}")