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

- Find a dataset which is a photogrammetry one - /Volumes/nfs/datasets/garrulus-arnsberg-forest/post-processing-results/processed-until-2024-07/2022-11-10_field-D/RGB-UTM32/RGB-pointcloud-143M.laz
- Use this laz file and extract all the points inside the labelled area
- Now use this extracted points file and the lidar file
- Use ICP and align them both and then extract all the points which match (Can be done in Cloud Compare)
- Assign a Index 1 to all the points which are matching and 9 to all the points which are not matching
- Repeat the same for all VEGETATION
- Assign a Index 2 to all the points which are matching and 9 to all the points which are not matching

By now i should have
Class Lable Index 0 - Terrain
Class Lable Index 1 - Stumps
Class Lable Index 2 - Vegetation
Class Lable Index 9 - Everything Else
  **~Verified by Ahmad**


PointNet does not directly accept csv data but it accepts the ply data and Charles the author of pointnet has published the code for the same.
[CSV to Pointnet](https://github.com/charlesq34/3dmodel_feature/blob/master/io/write_hdf5.py)

- CVAT Documentation
-
# 05.03.25, 16:45:34

CSF -
Resolution - 0.15
Iterations - 1000
Threshold - 0.1

# 09.03.2025, 14:56
Label - Connected Components
- Octree Level - 9
- Min Points per component - 50
- Clusters - 205

Label - Connected Components
- Octree Level - 9
- Min Points per component - 100
- Clusters - 212

CC0

Final RMS: 1.00611e-5 (computed on 5362 points)
----------------
Transformation matrix
1.000	0.000	-0.000	-0.221
-0.000	1.000	0.000	1.931
0.000	-0.000	1.000	0.024
0.000	0.000	0.000	1.000
----------------
Scale: fixed (1.0)
----------------
Theoretical overlap: 100%
----------------
This report has been output to Console (F8)


CC 1
Final RMS: 0.0870366 (computed on 3733 points)
----------------
Transformation matrix
0.293	-0.081	-0.155	-8.707
0.033	0.323	-0.107	4.864
0.172	0.077	0.285	1.062
0.000	0.000	0.000	1.000
----------------
Scale: 0.341431 (already integrated in above matrix!)
----------------
Theoretical overlap: 100%
----------------
This report has been output to Console (F8)


CC 2

Final RMS: 4.03817e-6 (computed on 3547 points)
----------------
Transformation matrix
1.000	-0.000	0.000	0.221
0.000	1.000	0.000	-1.931
-0.000	-0.000	1.000	-0.024
0.000	0.000	0.000	1.000
----------------
Scale: fixed (1.0)
----------------
Theoretical overlap: 100%
----------------
This report has been output to Console (F8)
Terrain

| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| 0     | 1.00      | 1.00   | 1.00     | 36,349  |
| 1     | 1.00      | 1.00   | 1.00     | 108,785 |
| **Accuracy** |       |        | **1.00** | 145,134 |
| **Macro Avg** | 1.00 | 1.00   | 1.00     | 145,134 |
| **Weighted Avg** | 1.00 | 1.00 | 1.00     | 145,134 |


# 10.03.25, 12:03:17
- Professor Houben - Have the Validation/Evaluation ready by the next week
- Don't Use RGB Data

- The data is not a RGB-D Data, it is just a photogrammetry dataset

- Make Visulisations proper

- Always have at least 3 different views
