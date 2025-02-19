# 07 October 2024 13:00
Installing Anaconda

https://repo.anaconda.com/archive/Anaconda3-2024.06-1-Linux-x86_64.sh

## For GUI Anaconda (Optional)
apt-get install libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6

## To Not auto activate conda
conda config --set auto_activate_base false

conda create -n rnd


## pip
sudo apt install python3-pip
pip install open3d
## Open3D
pip install setuptools==60.2.0
# 07 October 2024 13:53
System is Ready !
## Installation of CloudCompare

## 07.10.24, 14:23:17

sudo apt install flatpak
sudo add-apt-repository ppa:flatpak/stable
sudo apt update
sudo apt install flatpak
https://flathub.org/setup/Ubuntu
sudo flatpak install flathub org.cloudcompare.CloudCompare -y
flatpak run org.cloudcompare.CloudCompare

### Error Message
QSocketNotifier: Can only be used with threads started with QThread

Gtk-Message: 14:46:01.445: Failed to load module canberra-gtk-module

Qt: Session management error: None of the authentication protocols specified are supported

libpng warning: iCCP: known incorrect sRGB profile

qt.gui.icc: fromIccProfile: failed minimal tag size sanity

QPngHandler: Failed to parse ICC profile

Language not found for translation file CloudCompare_chs.qm


## 07.10.24, 17:07:41, Smoothened The Surface and Located Region of Interest

# 14 October 2024 13:00

## 14.10.24, 14:07:33 - Cropped by 100X100X100 meters*

# 15.10.24, 14:36:33 - Clustering #1 Successful !

## Points stats:
Min: [-121.80550385 -127.46252441   -8.48567581], Max: [157.43299866 128.68302917  36.19382477]
Contains NaN: True
Contains Inf: True

Number of clusters found: 847
Number of noise points: 26355

Clustering.py:53: UserWarning: *c* argument looks like a single numeric RGB or RGBA sequence, which should be avoided as value-mapping will have precedence in case its length matches with *x* & *y*.
Please use the *color* keyword-argument or provide a 2D array with a single row if you intend to specify the same RGB or RGBA value for all points.ax.scatter(xyz[:, 0], xyz[:, 1], xyz[:, 2], s=20, c=color, label=f'Cluster {label}' if label != -1 else 'Noise')

Rectified NaN and Inf points in Clustering.py

### PCL Installation
sudo apt install libusb-1.0-0-dev
cd ~/pcl/build
cmake ..
make -j32
sudo make install



# 22.10.24, 17:58

Exported a bin file to ply and performed Clustering_2.py

Performed CSF on the Final.ply file

Checked las metadata

As DBSCAN does not accept InF and NaN Points, so removed those NaN Row

Number of clusters: 201
[Open3D WARNING] GLFW Error: Cocoa: Failed to find service port for display

# 28.10.24, 10:25:49
- Get inside the fence
- Removal of NaN and InF points is NOT RECOMMENDED
- How/Why did you perform the normalisation ?
- Why 0.5 if the points are normalized to 0 - 1

# 04.11.24, 15:45:23
- CloudCompare Point Detection and Extract points
Point 1 - [-2.294216, 36.315838, -1.263460]
Point 2 - [16.956844, -44.380180, 3.154053]
Point 3 - [65.558228, 32.719646, -3.185380]
Point 4 - [65.664795, 26.725346, -2.709546]
Point 5 - [50.484165, -21.520457, 0.632474]

# 11.11.24, 13:03:44

## 13:03:44
- Update all Conda and Packages

## 14:49:56
- Cropping the data to be useful

# 18.11.24, 13:28
- DBSCan First Attempt Successfull
- Number of clusters (excluding noise): 631

# 02.11.24, 15:00
CUDA Installation in Progress !!


# 04.12.24, 12:28
I don;t know if i am getting the proper classes !

1. I don;t what is the platform to get data annotated ?
2. IS it right to annoatate the data ?
3. Make Visualisation of the data
4.


1. Entire ply as a input
2. Get the models of one tree trunk and try it with \

Check Kugus for the visualising data


DBSScan adds a parameter in the class

Find a way to visualise
- PCL Viewer
- Simple Class maybe trunk
- Input - be it actual trunk
- How does exaclty PointNet work
- What are the current state of the art methods ot PointCloud Segmentation

DigiCNN


QGIS - Number of Trunks - 131

CC
Load the Model - Normals - SF Scalar Field - PlugINs - KAnnupus - 3dPoint Cloud Segmentation - ICP
HKU Mars Hong Kong University - PointNet

# 16.12.24, 11:34:20

- Contact Pranisha for the data
  - Labelled and Annotated Tree Trunks to use them as a pkl file
- Passthrough Filter
- Elevation Model
  - Digital Surface
  - Digital Terrain - Talha said National Ecological Obsrvatory Netowrk DTM is better
    - For Image Based


# 14.02.25, 11:17:37
TO Read:
- RANSAC
- Scalar Field
- Object Labelling
- HKU Mars
	1.	Transformer-Based Annotation – A trainable Transformer model for automatic 3D point cloud annotation, capturing both local and global dependencies.
	2.	Context-Aware Transformer – Enhances point cloud annotation by addressing sparsity and unstructured data issues.
	3.	3DVG-Transformer – Uses relation modeling for visual grounding, excelling in complex object disambiguation.
	4.	Prototypical VoteNet – A few-shot learning model for object detection in 3D point clouds, requiring minimal labeled data.
	5.	GDANet (Geometry-Disentangled Attention Network) – Improves segmentation by treating different geometric features separately.
	6.	BIM Reconstruction – Uses semantic registration for reconstructing Building Information Models (BIM) from 3D point clouds, aiding smart city applications.

# 18.02.25, 16:04:55

[GPT Result](https://www.perplexity.ai/search/i-have-a-3d-point-cloud-datase-XAZSuJBsQSmXvHkvUmTYWg)

✅ Report Skeleton 


# 19.02.25, 12:46:29

- Find a dataset which is a photogrammetry one
- Overlay the gpkg and slice all the points inside the labelled area
- Consider all of them as STUMP
- Repeat the same with Vegetation
  **~Verified by Ahmad**

