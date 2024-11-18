import torch
from pointnet import PointNet  # Assuming you have a PointNet implementation
from torch.utils.data import DataLoader
from my_point_cloud_dataset import MyDataset  # Custom dataset for your point clouds

# Load the pre-trained model (example path)
model = PointNet()
model.load_state_dict(torch.load("/home/shrikar/RnD/dbscan_model.pkl"))

# Set the model to evaluation mode
model.eval()

# Load your dataset
dataset = MyDataset()  # Replace with your own dataset class
dataloader = DataLoader(dataset, batch_size=32)

# Use the model to make predictions
with torch.no_grad():
    for data in dataloader:
        point_cloud = data["points"]
        labels = model(point_cloud)
        print("Predicted labels:", labels)