import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
import open3d as o3d
import numpy as np
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont

# Load point cloud
pcd = o3d.io.read_point_cloud('/Users/shrikar/RnD/dataset/filtered_point_cloud.ply')
points = np.asarray(pcd.points)

# Run DBSCAN
db = DBSCAN(eps=0.5, min_samples=100).fit(points)
labels = db.labels_
unique_labels = set(labels)
num_clusters = len(unique_labels) - (1 if -1 in unique_labels else 0)
print(f"Number of clusters: {num_clusters}")

# Assign colors
colors = plt.colormaps.get_cmap("tab20")
pcd_colors = np.zeros((points.shape[0], 3))

for i, label in enumerate(labels):
    if label == -1:
        pcd_colors[i] = [0, 0, 0]
    else:
        pcd_colors[i] = colors(label / len(unique_labels))[:3]

pcd.colors = o3d.utility.Vector3dVector(pcd_colors)

# Axis (optional)
axis = o3d.geometry.TriangleMesh.create_coordinate_frame(size=1.0)

# Open3D visualization (offscreen rendering)
vis = o3d.visualization.Visualizer()
vis.create_window(visible=True)
vis.add_geometry(pcd)
vis.add_geometry(axis)
vis.poll_events()
vis.update_renderer()
vis.capture_screen_image("clustered_output.png")
vis.destroy_window()

# ---------------------------
# PIL: Add annotation & scale
# ---------------------------

image = Image.open("clustered_output.png")
draw = ImageDraw.Draw(image)
width, height = image.size

# Use a better font if available
try:
    font = ImageFont.truetype("arial.ttf", 64)
except:
    font = ImageFont.load_default()


# 1. Add text annotation (top-left)
text = f"Each color represents a different DBSCAN cluster.\nBlack = Noise. Total clusters: {num_clusters} \neps = 0.5\nmin_samples = 100"
draw.text((10, 10), text, fill="black", font=font)

# 2. Add a scale bar (bottom-right)
bar_length_pixels = 500  # represents 1 meter
bar_height = 10
margin = 20

x_start = width - bar_length_pixels - margin
y_start = height - bar_height - margin
x_end = width - margin
y_end = height - margin

draw.rectangle([(x_start, y_start), (x_end, y_end)], fill="black")

# Label the scale
scale_label = "5 kilometer"
bbox = draw.textbbox((0, 0), scale_label, font=font)
label_width = bbox[2] - bbox[0]
label_height = bbox[3] - bbox[1]

draw.text((x_start + (bar_length_pixels - label_width) / 2, y_start - label_height - 5),
          scale_label, fill="black", font=font)

# Save final image
image.save("/Users/shrikar/RnD/Snaps/clustered_output_with_scale.jpg")
print("✅ Saved image: clustered_output_with_scale.jpg")
