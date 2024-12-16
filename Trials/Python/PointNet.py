import torch
from pointnet import PointNetSeg  # Assuming you have a correct PointNet class
from torch.utils.data import DataLoader, Dataset
import open3d as o3d
import numpy as np

# Custom Dataset Class
class PointCloudDataset(Dataset):
    def __init__(self, file_path, num_points=1024):
        # Load the point cloud
        pcd = o3d.io.read_point_cloud(file_path)
        self.points = np.asarray(pcd.points)
        print(f"Loaded point cloud with shape: {self.points.shape}")  # Output the shape of the point cloud
        
        # Normalize or preprocess the points if needed
        self.points = (self.points - self.points.mean(axis=0)) / self.points.std(axis=0)
        
        # Ensure that the number of points is consistent (e.g., 1024 points per cloud)
        self.num_points = num_points
        if self.points.shape[0] < self.num_points:
            # Pad with zeros if the point cloud has fewer points than the expected number
            padding = np.zeros((self.num_points - self.points.shape[0], 3))
            self.points = np.vstack([self.points, padding])
        elif self.points.shape[0] > self.num_points:
            # Randomly sample points if the point cloud has more than the expected number
            self.points = self.points[np.random.choice(self.points.shape[0], self.num_points, replace=False)]

    def __len__(self):
        return 1  # Only one point cloud in this dataset

    def __getitem__(self, idx):
        # Return the point cloud as a batch
        return {"points": torch.tensor(self.points, dtype=torch.float32)}

# Load the pre-trained model
model = PointNet()  # Ensure PointNet is implemented and has an STN component if needed
model.load_state_dict(torch.load("/home/shrikar/RnD/dbscan_model.pkl"))
model.eval()

# Load your data as a dataset
dataset = PointCloudDataset("filtered_point_cloud.ply")
dataloader = DataLoader(dataset, batch_size=1, shuffle=False)  # Batch size is 1 as we have only one point cloud

# Make predictions and output results
print("Starting prediction...")
with torch.no_grad():
    for batch_idx, batch in enumerate(dataloader):
        point_cloud = batch["points"]
        print(f"Point cloud shape before model: {point_cloud.shape}")  # Should be (1, num_points, 3)
        labels = model(point_cloud)  # Perform forward pass
        print(f"Batch {batch_idx + 1}: Predicted labels: {labels}")