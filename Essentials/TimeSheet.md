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

- INput - Batch and Data set and the output will be segmented object
- Input - Dataset and output will also be a dataset

- Downsampling - Open3D
- pointcloud_classification/dataset/dataset_util.py

# 24/03/2025, 10:52:17

- [Preparing JupyterHub Lab Server with Pytorch PointNet](https://github.com/fxia22/pointnet.pytorch)
- quay.io/a2s-institute/ml-notebook:cuda12-pytorch-2.2.2

DEPRECATION: Legacy editable install of pointnet==0.0.1 from file:///home/jovyan/pointnet.pytorch (setup.py develop) is deprecated. pip 25.1 will enforce this behaviour change. A possible replacement is to add a pyproject.toml or enable --use-pep517, and use setuptools >= 64. If the resulting installation is not behaving as expected, try using --config-settings editable_mode=compat. Please consult the setuptools documentation for more information. Discussion can be found at https://github.com/pypa/pip/issues/11457

# 08.04.25, 14:58:05
Grid Size = 2.5
No. of Grids = 656 + 141 + 140 = 937
Grid layout: 34 columns × 40 rows
Saved: grids_2.5/cell_0_36.ply with 17 points
Saved: grids_2.5/cell_0_37.ply with 179 points
Saved: grids_2.5/cell_0_38.ply with 260 points
Saved: grids_2.5/cell_0_39.ply with 280 points
Saved: grids_2.5/cell_0_40.ply with 331 points
Saved: grids_2.5/cell_1_32.ply with 32 points
Saved: grids_2.5/cell_1_33.ply with 361 points
Saved: grids_2.5/cell_1_34.ply with 289 points
Saved: grids_2.5/cell_1_35.ply with 741 points
Saved: grids_2.5/cell_1_36.ply with 438 points
Saved: grids_2.5/cell_1_37.ply with 1140 points
Saved: grids_2.5/cell_1_38.ply with 579 points
Saved: grids_2.5/cell_1_39.ply with 249 points
Saved: grids_2.5/cell_1_40.ply with 101 points
Saved: grids_2.5/cell_2_28.ply with 71 points
Saved: grids_2.5/cell_2_29.ply with 270 points
Saved: grids_2.5/cell_2_30.ply with 634 points
Saved: grids_2.5/cell_2_31.ply with 421 points
Saved: grids_2.5/cell_2_32.ply with 1374 points
Saved: grids_2.5/cell_2_33.ply with 372 points
Saved: grids_2.5/cell_2_34.ply with 493 points
Saved: grids_2.5/cell_2_35.ply with 476 points
Saved: grids_2.5/cell_2_36.ply with 505 points
Saved: grids_2.5/cell_2_37.ply with 577 points
Saved: grids_2.5/cell_2_38.ply with 525 points
Saved: grids_2.5/cell_2_39.ply with 257 points
Saved: grids_2.5/cell_2_40.ply with 48 points
Saved: grids_2.5/cell_3_23.ply with 7 points
Saved: grids_2.5/cell_3_24.ply with 190 points
Saved: grids_2.5/cell_3_25.ply with 704 points
Saved: grids_2.5/cell_3_26.ply with 594 points
Saved: grids_2.5/cell_3_27.ply with 1403 points
Saved: grids_2.5/cell_3_28.ply with 1253 points
Saved: grids_2.5/cell_3_29.ply with 1255 points
Saved: grids_2.5/cell_3_30.ply with 813 points
Saved: grids_2.5/cell_3_31.ply with 549 points
Saved: grids_2.5/cell_3_32.ply with 314 points
Saved: grids_2.5/cell_3_33.ply with 594 points
Saved: grids_2.5/cell_3_34.ply with 215 points
Saved: grids_2.5/cell_3_35.ply with 410 points
Saved: grids_2.5/cell_3_36.ply with 436 points
Saved: grids_2.5/cell_3_37.ply with 524 points
Saved: grids_2.5/cell_3_38.ply with 322 points
Saved: grids_2.5/cell_3_39.ply with 348 points
Saved: grids_2.5/cell_3_40.ply with 50 points
Saved: grids_2.5/cell_4_19.ply with 10 points
Saved: grids_2.5/cell_4_20.ply with 120 points
Saved: grids_2.5/cell_4_21.ply with 272 points
Saved: grids_2.5/cell_4_22.ply with 850 points
Saved: grids_2.5/cell_4_23.ply with 680 points
Saved: grids_2.5/cell_4_24.ply with 2449 points
Saved: grids_2.5/cell_4_25.ply with 1644 points
Saved: grids_2.5/cell_4_26.ply with 1067 points
Saved: grids_2.5/cell_4_27.ply with 1384 points
Saved: grids_2.5/cell_4_28.ply with 2253 points
Saved: grids_2.5/cell_4_29.ply with 1343 points
Saved: grids_2.5/cell_4_30.ply with 898 points
Saved: grids_2.5/cell_4_31.ply with 678 points
Saved: grids_2.5/cell_4_32.ply with 914 points
Saved: grids_2.5/cell_4_33.ply with 339 points
Saved: grids_2.5/cell_4_34.ply with 197 points
Saved: grids_2.5/cell_4_35.ply with 626 points
Saved: grids_2.5/cell_4_36.ply with 228 points
Saved: grids_2.5/cell_4_37.ply with 388 points
Saved: grids_2.5/cell_4_38.ply with 286 points
Saved: grids_2.5/cell_4_39.ply with 141 points
Saved: grids_2.5/cell_4_40.ply with 12 points
Saved: grids_2.5/cell_5_15.ply with 72 points
Saved: grids_2.5/cell_5_16.ply with 455 points
Saved: grids_2.5/cell_5_17.ply with 848 points
Saved: grids_2.5/cell_5_18.ply with 786 points
Saved: grids_2.5/cell_5_19.ply with 1193 points
Saved: grids_2.5/cell_5_20.ply with 1533 points
Saved: grids_2.5/cell_5_21.ply with 1468 points
Saved: grids_2.5/cell_5_22.ply with 1083 points
Saved: grids_2.5/cell_5_23.ply with 1381 points
Saved: grids_2.5/cell_5_24.ply with 1654 points
Saved: grids_2.5/cell_5_25.ply with 2321 points
Saved: grids_2.5/cell_5_26.ply with 1482 points
Saved: grids_2.5/cell_5_27.ply with 2104 points
Saved: grids_2.5/cell_5_28.ply with 1942 points
Saved: grids_2.5/cell_5_29.ply with 1361 points
Saved: grids_2.5/cell_5_30.ply with 1291 points
Saved: grids_2.5/cell_5_31.ply with 1266 points
Saved: grids_2.5/cell_5_32.ply with 1087 points
Saved: grids_2.5/cell_5_33.ply with 374 points
Saved: grids_2.5/cell_5_34.ply with 384 points
Saved: grids_2.5/cell_5_35.ply with 620 points
Saved: grids_2.5/cell_5_36.ply with 339 points
Saved: grids_2.5/cell_5_37.ply with 339 points
Saved: grids_2.5/cell_5_38.ply with 280 points
Saved: grids_2.5/cell_5_39.ply with 203 points
Saved: grids_2.5/cell_5_40.ply with 7 points
Saved: grids_2.5/cell_6_11.ply with 82 points
Saved: grids_2.5/cell_6_12.ply with 154 points
Saved: grids_2.5/cell_6_13.ply with 444 points
Saved: grids_2.5/cell_6_14.ply with 930 points
Saved: grids_2.5/cell_6_15.ply with 1423 points
Saved: grids_2.5/cell_6_16.ply with 1207 points
Saved: grids_2.5/cell_6_17.ply with 785 points
Saved: grids_2.5/cell_6_18.ply with 904 points
Saved: grids_2.5/cell_6_19.ply with 1204 points
Saved: grids_2.5/cell_6_20.ply with 899 points
Saved: grids_2.5/cell_6_21.ply with 1426 points
Saved: grids_2.5/cell_6_22.ply with 981 points
Saved: grids_2.5/cell_6_23.ply with 1053 points
Saved: grids_2.5/cell_6_24.ply with 1468 points
Saved: grids_2.5/cell_6_25.ply with 1038 points
Saved: grids_2.5/cell_6_26.ply with 994 points
Saved: grids_2.5/cell_6_27.ply with 916 points
Saved: grids_2.5/cell_6_28.ply with 724 points
Saved: grids_2.5/cell_6_29.ply with 969 points
Saved: grids_2.5/cell_6_30.ply with 666 points
Saved: grids_2.5/cell_6_31.ply with 1299 points
Saved: grids_2.5/cell_6_32.ply with 891 points
Saved: grids_2.5/cell_6_33.ply with 818 points
Saved: grids_2.5/cell_6_34.ply with 509 points
Saved: grids_2.5/cell_6_35.ply with 607 points
Saved: grids_2.5/cell_6_36.ply with 292 points
Saved: grids_2.5/cell_6_37.ply with 199 points
Saved: grids_2.5/cell_6_38.ply with 190 points
Saved: grids_2.5/cell_6_39.ply with 113 points
Saved: grids_2.5/cell_6_40.ply with 2 points
Saved: grids_2.5/cell_7_7.ply with 22 points
Saved: grids_2.5/cell_7_8.ply with 130 points
Saved: grids_2.5/cell_7_9.ply with 314 points
Saved: grids_2.5/cell_7_10.ply with 1402 points
Saved: grids_2.5/cell_7_11.ply with 1517 points
Saved: grids_2.5/cell_7_12.ply with 1109 points
Saved: grids_2.5/cell_7_13.ply with 1033 points
Saved: grids_2.5/cell_7_14.ply with 1810 points
Saved: grids_2.5/cell_7_15.ply with 1179 points
Saved: grids_2.5/cell_7_16.ply with 1387 points
Saved: grids_2.5/cell_7_17.ply with 1238 points
Saved: grids_2.5/cell_7_18.ply with 1419 points
Saved: grids_2.5/cell_7_19.ply with 1051 points
Saved: grids_2.5/cell_7_20.ply with 2770 points
Saved: grids_2.5/cell_7_21.ply with 1710 points
Saved: grids_2.5/cell_7_22.ply with 1360 points
Saved: grids_2.5/cell_7_23.ply with 2092 points
Saved: grids_2.5/cell_7_24.ply with 2180 points
Saved: grids_2.5/cell_7_25.ply with 1040 points
Saved: grids_2.5/cell_7_26.ply with 987 points
Saved: grids_2.5/cell_7_27.ply with 1169 points
Saved: grids_2.5/cell_7_28.ply with 1246 points
Saved: grids_2.5/cell_7_29.ply with 964 points
Saved: grids_2.5/cell_7_30.ply with 1226 points
Saved: grids_2.5/cell_7_31.ply with 1549 points
Saved: grids_2.5/cell_7_32.ply with 860 points
Saved: grids_2.5/cell_7_33.ply with 1173 points
Saved: grids_2.5/cell_7_34.ply with 868 points
Saved: grids_2.5/cell_7_35.ply with 1011 points
Saved: grids_2.5/cell_7_36.ply with 346 points
Saved: grids_2.5/cell_7_37.ply with 187 points
Saved: grids_2.5/cell_7_38.ply with 216 points
Saved: grids_2.5/cell_7_39.ply with 127 points
Saved: grids_2.5/cell_8_2.ply with 2 points
Saved: grids_2.5/cell_8_3.ply with 16 points
Saved: grids_2.5/cell_8_4.ply with 70 points
Saved: grids_2.5/cell_8_5.ply with 137 points
Saved: grids_2.5/cell_8_6.ply with 306 points
Saved: grids_2.5/cell_8_7.ply with 602 points
Saved: grids_2.5/cell_8_8.ply with 1562 points
Saved: grids_2.5/cell_8_9.ply with 1220 points
Saved: grids_2.5/cell_8_10.ply with 2077 points
Saved: grids_2.5/cell_8_11.ply with 1639 points
Saved: grids_2.5/cell_8_12.ply with 1191 points
Saved: grids_2.5/cell_8_13.ply with 1288 points
Saved: grids_2.5/cell_8_14.ply with 1045 points
Saved: grids_2.5/cell_8_15.ply with 1017 points
Saved: grids_2.5/cell_8_16.ply with 834 points
Saved: grids_2.5/cell_8_17.ply with 1355 points
Saved: grids_2.5/cell_8_18.ply with 1284 points
Saved: grids_2.5/cell_8_19.ply with 1653 points
Saved: grids_2.5/cell_8_20.ply with 2193 points
Saved: grids_2.5/cell_8_21.ply with 1472 points
Saved: grids_2.5/cell_8_22.ply with 1715 points
Saved: grids_2.5/cell_8_23.ply with 1596 points
Saved: grids_2.5/cell_8_24.ply with 1537 points
Saved: grids_2.5/cell_8_25.ply with 1263 points
Saved: grids_2.5/cell_8_26.ply with 840 points
Saved: grids_2.5/cell_8_27.ply with 1090 points
Saved: grids_2.5/cell_8_28.ply with 1253 points
Saved: grids_2.5/cell_8_29.ply with 744 points
Saved: grids_2.5/cell_8_30.ply with 1048 points
Saved: grids_2.5/cell_8_31.ply with 935 points
Saved: grids_2.5/cell_8_32.ply with 930 points
Saved: grids_2.5/cell_8_33.ply with 748 points
Saved: grids_2.5/cell_8_34.ply with 1323 points
Saved: grids_2.5/cell_8_35.ply with 1348 points
Saved: grids_2.5/cell_8_36.ply with 941 points
Saved: grids_2.5/cell_8_37.ply with 449 points
Saved: grids_2.5/cell_8_38.ply with 113 points
Saved: grids_2.5/cell_8_39.ply with 94 points
Saved: grids_2.5/cell_9_0.ply with 127 points
Saved: grids_2.5/cell_9_1.ply with 44 points
Saved: grids_2.5/cell_9_2.ply with 157 points
Saved: grids_2.5/cell_9_3.ply with 309 points
Saved: grids_2.5/cell_9_4.ply with 155 points
Saved: grids_2.5/cell_9_5.ply with 294 points
Saved: grids_2.5/cell_9_6.ply with 695 points
Saved: grids_2.5/cell_9_7.ply with 1127 points
Saved: grids_2.5/cell_9_8.ply with 1232 points
Saved: grids_2.5/cell_9_9.ply with 1394 points
Saved: grids_2.5/cell_9_10.ply with 1720 points
Saved: grids_2.5/cell_9_11.ply with 1519 points
Saved: grids_2.5/cell_9_12.ply with 1350 points
Saved: grids_2.5/cell_9_13.ply with 1108 points
Saved: grids_2.5/cell_9_14.ply with 1249 points
Saved: grids_2.5/cell_9_15.ply with 1801 points
Saved: grids_2.5/cell_9_16.ply with 1488 points
Saved: grids_2.5/cell_9_17.ply with 3708 points
Saved: grids_2.5/cell_9_18.ply with 1369 points
Saved: grids_2.5/cell_9_19.ply with 1707 points
Saved: grids_2.5/cell_9_20.ply with 1467 points
Saved: grids_2.5/cell_9_21.ply with 1149 points
Saved: grids_2.5/cell_9_22.ply with 1500 points
Saved: grids_2.5/cell_9_23.ply with 1636 points
Saved: grids_2.5/cell_9_24.ply with 3453 points
Saved: grids_2.5/cell_9_25.ply with 1283 points
Saved: grids_2.5/cell_9_26.ply with 1074 points
Saved: grids_2.5/cell_9_27.ply with 627 points
Saved: grids_2.5/cell_9_28.ply with 647 points
Saved: grids_2.5/cell_9_29.ply with 756 points
Saved: grids_2.5/cell_9_30.ply with 1058 points
Saved: grids_2.5/cell_9_31.ply with 715 points
Saved: grids_2.5/cell_9_32.ply with 504 points
Saved: grids_2.5/cell_9_33.ply with 1077 points
Saved: grids_2.5/cell_9_34.ply with 1179 points
Saved: grids_2.5/cell_9_35.ply with 759 points
Saved: grids_2.5/cell_9_36.ply with 592 points
Saved: grids_2.5/cell_9_37.ply with 356 points
Saved: grids_2.5/cell_9_38.ply with 421 points
Saved: grids_2.5/cell_9_39.ply with 190 points
Saved: grids_2.5/cell_10_0.ply with 19 points
Saved: grids_2.5/cell_10_1.ply with 35 points
Saved: grids_2.5/cell_10_2.ply with 74 points
Saved: grids_2.5/cell_10_3.ply with 317 points
Saved: grids_2.5/cell_10_4.ply with 251 points
Saved: grids_2.5/cell_10_5.ply with 269 points
Saved: grids_2.5/cell_10_6.ply with 1704 points
Saved: grids_2.5/cell_10_7.ply with 766 points
Saved: grids_2.5/cell_10_8.ply with 1311 points
Saved: grids_2.5/cell_10_9.ply with 604 points
Saved: grids_2.5/cell_10_10.ply with 1038 points
Saved: grids_2.5/cell_10_11.ply with 1388 points
Saved: grids_2.5/cell_10_12.ply with 1279 points
Saved: grids_2.5/cell_10_13.ply with 1470 points
Saved: grids_2.5/cell_10_14.ply with 1005 points
Saved: grids_2.5/cell_10_15.ply with 908 points
Saved: grids_2.5/cell_10_16.ply with 1636 points
Saved: grids_2.5/cell_10_17.ply with 1791 points
Saved: grids_2.5/cell_10_18.ply with 2696 points
Saved: grids_2.5/cell_10_19.ply with 1082 points
Saved: grids_2.5/cell_10_20.ply with 1825 points
Saved: grids_2.5/cell_10_21.ply with 1484 points
Saved: grids_2.5/cell_10_22.ply with 1937 points
Saved: grids_2.5/cell_10_23.ply with 2636 points
Saved: grids_2.5/cell_10_24.ply with 3131 points
Saved: grids_2.5/cell_10_25.ply with 818 points
Saved: grids_2.5/cell_10_26.ply with 1094 points
Saved: grids_2.5/cell_10_27.ply with 1083 points
Saved: grids_2.5/cell_10_28.ply with 807 points
Saved: grids_2.5/cell_10_29.ply with 1042 points
Saved: grids_2.5/cell_10_30.ply with 1538 points
Saved: grids_2.5/cell_10_31.ply with 673 points
Saved: grids_2.5/cell_10_32.ply with 636 points
Saved: grids_2.5/cell_10_33.ply with 651 points
Saved: grids_2.5/cell_10_34.ply with 886 points
Saved: grids_2.5/cell_10_35.ply with 804 points
Saved: grids_2.5/cell_10_36.ply with 704 points
Saved: grids_2.5/cell_10_37.ply with 447 points
Saved: grids_2.5/cell_10_38.ply with 314 points
Saved: grids_2.5/cell_10_39.ply with 261 points
Saved: grids_2.5/cell_11_1.ply with 118 points
Saved: grids_2.5/cell_11_2.ply with 177 points
Saved: grids_2.5/cell_11_3.ply with 547 points
Saved: grids_2.5/cell_11_4.ply with 361 points
Saved: grids_2.5/cell_11_5.ply with 726 points
Saved: grids_2.5/cell_11_6.ply with 1214 points
Saved: grids_2.5/cell_11_7.ply with 1139 points
Saved: grids_2.5/cell_11_8.ply with 722 points
Saved: grids_2.5/cell_11_9.ply with 697 points
Saved: grids_2.5/cell_11_10.ply with 890 points
Saved: grids_2.5/cell_11_11.ply with 551 points
Saved: grids_2.5/cell_11_12.ply with 1310 points
Saved: grids_2.5/cell_11_13.ply with 672 points
Saved: grids_2.5/cell_11_14.ply with 743 points
Saved: grids_2.5/cell_11_15.ply with 967 points
Saved: grids_2.5/cell_11_16.ply with 762 points
Saved: grids_2.5/cell_11_17.ply with 1433 points
Saved: grids_2.5/cell_11_18.ply with 1774 points
Saved: grids_2.5/cell_11_19.ply with 1523 points
Saved: grids_2.5/cell_11_20.ply with 2054 points
Saved: grids_2.5/cell_11_21.ply with 1711 points
Saved: grids_2.5/cell_11_22.ply with 2238 points
Saved: grids_2.5/cell_11_23.ply with 1288 points
Saved: grids_2.5/cell_11_24.ply with 1767 points
Saved: grids_2.5/cell_11_25.ply with 1207 points
Saved: grids_2.5/cell_11_26.ply with 869 points
Saved: grids_2.5/cell_11_27.ply with 1306 points
Saved: grids_2.5/cell_11_28.ply with 849 points
Saved: grids_2.5/cell_11_29.ply with 1547 points
Saved: grids_2.5/cell_11_30.ply with 2364 points
Saved: grids_2.5/cell_11_31.ply with 948 points
Saved: grids_2.5/cell_11_32.ply with 590 points
Saved: grids_2.5/cell_11_33.ply with 1022 points
Saved: grids_2.5/cell_11_34.ply with 714 points
Saved: grids_2.5/cell_11_35.ply with 608 points
Saved: grids_2.5/cell_11_36.ply with 371 points
Saved: grids_2.5/cell_11_37.ply with 483 points
Saved: grids_2.5/cell_11_38.ply with 768 points
Saved: grids_2.5/cell_11_39.ply with 247 points
Saved: grids_2.5/cell_12_1.ply with 13 points
Saved: grids_2.5/cell_12_2.ply with 251 points
Saved: grids_2.5/cell_12_3.ply with 335 points
Saved: grids_2.5/cell_12_4.ply with 490 points
Saved: grids_2.5/cell_12_5.ply with 798 points
Saved: grids_2.5/cell_12_6.ply with 671 points
Saved: grids_2.5/cell_12_7.ply with 707 points
Saved: grids_2.5/cell_12_8.ply with 865 points
Saved: grids_2.5/cell_12_9.ply with 916 points
Saved: grids_2.5/cell_12_10.ply with 907 points
Saved: grids_2.5/cell_12_11.ply with 922 points
Saved: grids_2.5/cell_12_12.ply with 766 points
Saved: grids_2.5/cell_12_13.ply with 1128 points
Saved: grids_2.5/cell_12_14.ply with 908 points
Saved: grids_2.5/cell_12_15.ply with 1140 points
Saved: grids_2.5/cell_12_16.ply with 1404 points
Saved: grids_2.5/cell_12_17.ply with 1123 points
Saved: grids_2.5/cell_12_18.ply with 1065 points
Saved: grids_2.5/cell_12_19.ply with 3184 points
Saved: grids_2.5/cell_12_20.ply with 1759 points
Saved: grids_2.5/cell_12_21.ply with 1613 points
Saved: grids_2.5/cell_12_22.ply with 2453 points
Saved: grids_2.5/cell_12_23.ply with 2262 points
Saved: grids_2.5/cell_12_24.ply with 1873 points
Saved: grids_2.5/cell_12_25.ply with 1527 points
Saved: grids_2.5/cell_12_26.ply with 1059 points
Saved: grids_2.5/cell_12_27.ply with 2244 points
Saved: grids_2.5/cell_12_28.ply with 969 points
Saved: grids_2.5/cell_12_29.ply with 983 points
Saved: grids_2.5/cell_12_30.ply with 1064 points
Saved: grids_2.5/cell_12_31.ply with 894 points
Saved: grids_2.5/cell_12_32.ply with 977 points
Saved: grids_2.5/cell_12_33.ply with 663 points
Saved: grids_2.5/cell_12_34.ply with 473 points
Saved: grids_2.5/cell_12_35.ply with 623 points
Saved: grids_2.5/cell_12_36.ply with 694 points
Saved: grids_2.5/cell_12_37.ply with 495 points
Saved: grids_2.5/cell_12_38.ply with 229 points
Saved: grids_2.5/cell_12_39.ply with 272 points
Saved: grids_2.5/cell_13_2.ply with 72 points
Saved: grids_2.5/cell_13_3.ply with 306 points
Saved: grids_2.5/cell_13_4.ply with 379 points
Saved: grids_2.5/cell_13_5.ply with 450 points
Saved: grids_2.5/cell_13_6.ply with 603 points
Saved: grids_2.5/cell_13_7.ply with 1094 points
Saved: grids_2.5/cell_13_8.ply with 915 points
Saved: grids_2.5/cell_13_9.ply with 1049 points
Saved: grids_2.5/cell_13_10.ply with 722 points
Saved: grids_2.5/cell_13_11.ply with 1265 points
Saved: grids_2.5/cell_13_12.ply with 1052 points
Saved: grids_2.5/cell_13_13.ply with 940 points
Saved: grids_2.5/cell_13_14.ply with 556 points
Saved: grids_2.5/cell_13_15.ply with 907 points
Saved: grids_2.5/cell_13_16.ply with 1211 points
Saved: grids_2.5/cell_13_17.ply with 926 points
Saved: grids_2.5/cell_13_18.ply with 716 points
Saved: grids_2.5/cell_13_19.ply with 1303 points
Saved: grids_2.5/cell_13_20.ply with 2907 points
Saved: grids_2.5/cell_13_21.ply with 1626 points
Saved: grids_2.5/cell_13_22.ply with 3148 points
Saved: grids_2.5/cell_13_23.ply with 1836 points
Saved: grids_2.5/cell_13_24.ply with 1641 points
Saved: grids_2.5/cell_13_25.ply with 1558 points
Saved: grids_2.5/cell_13_26.ply with 1934 points
Saved: grids_2.5/cell_13_27.ply with 1955 points
Saved: grids_2.5/cell_13_28.ply with 1355 points
Saved: grids_2.5/cell_13_29.ply with 1168 points
Saved: grids_2.5/cell_13_30.ply with 1682 points
Saved: grids_2.5/cell_13_31.ply with 872 points
Saved: grids_2.5/cell_13_32.ply with 698 points
Saved: grids_2.5/cell_13_33.ply with 907 points
Saved: grids_2.5/cell_13_34.ply with 1264 points
Saved: grids_2.5/cell_13_35.ply with 857 points
Saved: grids_2.5/cell_13_36.ply with 1069 points
Saved: grids_2.5/cell_13_37.ply with 990 points
Saved: grids_2.5/cell_13_38.ply with 413 points
Saved: grids_2.5/cell_13_39.ply with 71 points
Saved: grids_2.5/cell_14_3.ply with 264 points
Saved: grids_2.5/cell_14_4.ply with 214 points
Saved: grids_2.5/cell_14_5.ply with 575 points
Saved: grids_2.5/cell_14_6.ply with 714 points
Saved: grids_2.5/cell_14_7.ply with 940 points
Saved: grids_2.5/cell_14_8.ply with 845 points
Saved: grids_2.5/cell_14_9.ply with 1266 points
Saved: grids_2.5/cell_14_10.ply with 645 points
Saved: grids_2.5/cell_14_11.ply with 1424 points
Saved: grids_2.5/cell_14_12.ply with 500 points
Saved: grids_2.5/cell_14_13.ply with 1139 points
Saved: grids_2.5/cell_14_14.ply with 749 points
Saved: grids_2.5/cell_14_15.ply with 1367 points
Saved: grids_2.5/cell_14_16.ply with 1036 points
Saved: grids_2.5/cell_14_17.ply with 875 points
Saved: grids_2.5/cell_14_18.ply with 950 points
Saved: grids_2.5/cell_14_19.ply with 733 points
Saved: grids_2.5/cell_14_20.ply with 1230 points
Saved: grids_2.5/cell_14_21.ply with 2255 points
Saved: grids_2.5/cell_14_22.ply with 2924 points
Saved: grids_2.5/cell_14_23.ply with 3178 points
Saved: grids_2.5/cell_14_24.ply with 2367 points
Saved: grids_2.5/cell_14_25.ply with 1527 points
Saved: grids_2.5/cell_14_26.ply with 1559 points
Saved: grids_2.5/cell_14_27.ply with 1586 points
Saved: grids_2.5/cell_14_28.ply with 1792 points
Saved: grids_2.5/cell_14_29.ply with 1321 points
Saved: grids_2.5/cell_14_30.ply with 1801 points
Saved: grids_2.5/cell_14_31.ply with 737 points
Saved: grids_2.5/cell_14_32.ply with 617 points
Saved: grids_2.5/cell_14_33.ply with 1258 points
Saved: grids_2.5/cell_14_34.ply with 1355 points
Saved: grids_2.5/cell_14_35.ply with 577 points
Saved: grids_2.5/cell_14_36.ply with 712 points
Saved: grids_2.5/cell_14_37.ply with 658 points
Saved: grids_2.5/cell_14_38.ply with 375 points
Saved: grids_2.5/cell_14_39.ply with 225 points
Saved: grids_2.5/cell_15_3.ply with 19 points
Saved: grids_2.5/cell_15_4.ply with 200 points
Saved: grids_2.5/cell_15_5.ply with 198 points
Saved: grids_2.5/cell_15_6.ply with 775 points
Saved: grids_2.5/cell_15_7.ply with 874 points
Saved: grids_2.5/cell_15_8.ply with 955 points
Saved: grids_2.5/cell_15_9.ply with 929 points
Saved: grids_2.5/cell_15_10.ply with 856 points
Saved: grids_2.5/cell_15_11.ply with 1080 points
Saved: grids_2.5/cell_15_12.ply with 405 points
Saved: grids_2.5/cell_15_13.ply with 694 points
Saved: grids_2.5/cell_15_14.ply with 668 points
Saved: grids_2.5/cell_15_15.ply with 763 points
Saved: grids_2.5/cell_15_16.ply with 883 points
Saved: grids_2.5/cell_15_17.ply with 1590 points
Saved: grids_2.5/cell_15_18.ply with 817 points
Saved: grids_2.5/cell_15_19.ply with 1031 points
Saved: grids_2.5/cell_15_20.ply with 942 points
Saved: grids_2.5/cell_15_21.ply with 1381 points
Saved: grids_2.5/cell_15_22.ply with 2036 points
Saved: grids_2.5/cell_15_23.ply with 2804 points
Saved: grids_2.5/cell_15_24.ply with 2140 points
Saved: grids_2.5/cell_15_25.ply with 2351 points
Saved: grids_2.5/cell_15_26.ply with 1731 points
Saved: grids_2.5/cell_15_27.ply with 1284 points
Saved: grids_2.5/cell_15_28.ply with 1026 points
Saved: grids_2.5/cell_15_29.ply with 998 points
Saved: grids_2.5/cell_15_30.ply with 905 points
Saved: grids_2.5/cell_15_31.ply with 681 points
Saved: grids_2.5/cell_15_32.ply with 900 points
Saved: grids_2.5/cell_15_33.ply with 596 points
Saved: grids_2.5/cell_15_34.ply with 484 points
Saved: grids_2.5/cell_15_35.ply with 545 points
Saved: grids_2.5/cell_15_36.ply with 759 points
Saved: grids_2.5/cell_15_37.ply with 770 points
Saved: grids_2.5/cell_15_38.ply with 421 points
Saved: grids_2.5/cell_15_39.ply with 214 points
Saved: grids_2.5/cell_16_4.ply with 164 points
Saved: grids_2.5/cell_16_5.ply with 266 points
Saved: grids_2.5/cell_16_6.ply with 221 points
Saved: grids_2.5/cell_16_7.ply with 1116 points
Saved: grids_2.5/cell_16_8.ply with 479 points
Saved: grids_2.5/cell_16_9.ply with 834 points
Saved: grids_2.5/cell_16_10.ply with 801 points
Saved: grids_2.5/cell_16_11.ply with 1433 points
Saved: grids_2.5/cell_16_12.ply with 642 points
Saved: grids_2.5/cell_16_13.ply with 749 points
Saved: grids_2.5/cell_16_14.ply with 1073 points
Saved: grids_2.5/cell_16_15.ply with 947 points
Saved: grids_2.5/cell_16_16.ply with 904 points
Saved: grids_2.5/cell_16_17.ply with 1153 points
Saved: grids_2.5/cell_16_18.ply with 976 points
Saved: grids_2.5/cell_16_19.ply with 1087 points
Saved: grids_2.5/cell_16_20.ply with 1297 points
Saved: grids_2.5/cell_16_21.ply with 1748 points
Saved: grids_2.5/cell_16_22.ply with 1160 points
Saved: grids_2.5/cell_16_23.ply with 2488 points
Saved: grids_2.5/cell_16_24.ply with 2312 points
Saved: grids_2.5/cell_16_25.ply with 2213 points
Saved: grids_2.5/cell_16_26.ply with 2773 points
Saved: grids_2.5/cell_16_27.ply with 2091 points
Saved: grids_2.5/cell_16_28.ply with 1185 points
Saved: grids_2.5/cell_16_29.ply with 1029 points
Saved: grids_2.5/cell_16_30.ply with 923 points
Saved: grids_2.5/cell_16_31.ply with 832 points
Saved: grids_2.5/cell_16_32.ply with 945 points
Saved: grids_2.5/cell_16_33.ply with 701 points
Saved: grids_2.5/cell_16_34.ply with 477 points
Saved: grids_2.5/cell_16_35.ply with 713 points
Saved: grids_2.5/cell_16_36.ply with 403 points
Saved: grids_2.5/cell_16_37.ply with 612 points
Saved: grids_2.5/cell_16_38.ply with 698 points
Saved: grids_2.5/cell_16_39.ply with 123 points
Saved: grids_2.5/cell_17_5.ply with 221 points
Saved: grids_2.5/cell_17_6.ply with 272 points
Saved: grids_2.5/cell_17_7.ply with 1196 points
Saved: grids_2.5/cell_17_8.ply with 931 points
Saved: grids_2.5/cell_17_9.ply with 657 points
Saved: grids_2.5/cell_17_10.ply with 523 points
Saved: grids_2.5/cell_17_11.ply with 1270 points
Saved: grids_2.5/cell_17_12.ply with 727 points
Saved: grids_2.5/cell_17_13.ply with 730 points
Saved: grids_2.5/cell_17_14.ply with 874 points
Saved: grids_2.5/cell_17_15.ply with 878 points
Saved: grids_2.5/cell_17_16.ply with 1085 points
Saved: grids_2.5/cell_17_17.ply with 1768 points
Saved: grids_2.5/cell_17_18.ply with 1235 points
Saved: grids_2.5/cell_17_19.ply with 1568 points
Saved: grids_2.5/cell_17_20.ply with 1111 points
Saved: grids_2.5/cell_17_21.ply with 998 points
Saved: grids_2.5/cell_17_22.ply with 1422 points
Saved: grids_2.5/cell_17_23.ply with 1318 points
Saved: grids_2.5/cell_17_24.ply with 2301 points
Saved: grids_2.5/cell_17_25.ply with 1329 points
Saved: grids_2.5/cell_17_26.ply with 1198 points
Saved: grids_2.5/cell_17_27.ply with 2130 points
Saved: grids_2.5/cell_17_28.ply with 1621 points
Saved: grids_2.5/cell_17_29.ply with 928 points
Saved: grids_2.5/cell_17_30.ply with 915 points
Saved: grids_2.5/cell_17_31.ply with 1097 points
Saved: grids_2.5/cell_17_32.ply with 696 points
Saved: grids_2.5/cell_17_33.ply with 414 points
Saved: grids_2.5/cell_17_34.ply with 573 points
Saved: grids_2.5/cell_17_35.ply with 895 points
Saved: grids_2.5/cell_17_36.ply with 716 points
Saved: grids_2.5/cell_17_37.ply with 809 points
Saved: grids_2.5/cell_17_38.ply with 449 points
Saved: grids_2.5/cell_17_39.ply with 98 points
Saved: grids_2.5/cell_18_5.ply with 18 points
Saved: grids_2.5/cell_18_6.ply with 291 points
Saved: grids_2.5/cell_18_7.ply with 519 points
Saved: grids_2.5/cell_18_8.ply with 536 points
Saved: grids_2.5/cell_18_9.ply with 642 points
Saved: grids_2.5/cell_18_10.ply with 466 points
Saved: grids_2.5/cell_18_11.ply with 516 points
Saved: grids_2.5/cell_18_12.ply with 832 points
Saved: grids_2.5/cell_18_13.ply with 975 points
Saved: grids_2.5/cell_18_14.ply with 1387 points
Saved: grids_2.5/cell_18_15.ply with 938 points
Saved: grids_2.5/cell_18_16.ply with 1133 points
Saved: grids_2.5/cell_18_17.ply with 2269 points
Saved: grids_2.5/cell_18_18.ply with 767 points
Saved: grids_2.5/cell_18_19.ply with 1370 points
Saved: grids_2.5/cell_18_20.ply with 1094 points
Saved: grids_2.5/cell_18_21.ply with 1250 points
Saved: grids_2.5/cell_18_22.ply with 1378 points
Saved: grids_2.5/cell_18_23.ply with 915 points
Saved: grids_2.5/cell_18_24.ply with 1097 points
Saved: grids_2.5/cell_18_25.ply with 1439 points
Saved: grids_2.5/cell_18_26.ply with 1772 points
Saved: grids_2.5/cell_18_27.ply with 1542 points
Saved: grids_2.5/cell_18_28.ply with 2145 points
Saved: grids_2.5/cell_18_29.ply with 842 points
Saved: grids_2.5/cell_18_30.ply with 1128 points
Saved: grids_2.5/cell_18_31.ply with 1088 points
Saved: grids_2.5/cell_18_32.ply with 1199 points
Saved: grids_2.5/cell_18_33.ply with 596 points
Saved: grids_2.5/cell_18_34.ply with 734 points
Saved: grids_2.5/cell_18_35.ply with 812 points
Saved: grids_2.5/cell_18_36.ply with 816 points
Saved: grids_2.5/cell_18_37.ply with 575 points
Saved: grids_2.5/cell_18_38.ply with 546 points
Saved: grids_2.5/cell_18_39.ply with 90 points
Saved: grids_2.5/cell_19_6.ply with 279 points
Saved: grids_2.5/cell_19_7.ply with 556 points
Saved: grids_2.5/cell_19_8.ply with 343 points
Saved: grids_2.5/cell_19_9.ply with 365 points
Saved: grids_2.5/cell_19_10.ply with 452 points
Saved: grids_2.5/cell_19_11.ply with 153 points
Saved: grids_2.5/cell_19_12.ply with 802 points
Saved: grids_2.5/cell_19_13.ply with 699 points
Saved: grids_2.5/cell_19_14.ply with 600 points
Saved: grids_2.5/cell_19_15.ply with 1217 points
Saved: grids_2.5/cell_19_16.ply with 911 points
Saved: grids_2.5/cell_19_17.ply with 1379 points
Saved: grids_2.5/cell_19_18.ply with 771 points
Saved: grids_2.5/cell_19_19.ply with 1025 points
Saved: grids_2.5/cell_19_20.ply with 944 points
Saved: grids_2.5/cell_19_21.ply with 1134 points
Saved: grids_2.5/cell_19_22.ply with 977 points
Saved: grids_2.5/cell_19_23.ply with 905 points
Saved: grids_2.5/cell_19_24.ply with 1186 points
Saved: grids_2.5/cell_19_25.ply with 996 points
Saved: grids_2.5/cell_19_26.ply with 924 points
Saved: grids_2.5/cell_19_27.ply with 1374 points
Saved: grids_2.5/cell_19_28.ply with 1583 points
Saved: grids_2.5/cell_19_29.ply with 1834 points
Saved: grids_2.5/cell_19_30.ply with 1111 points
Saved: grids_2.5/cell_19_31.ply with 875 points
Saved: grids_2.5/cell_19_32.ply with 409 points
Saved: grids_2.5/cell_19_33.ply with 823 points
Saved: grids_2.5/cell_19_34.ply with 566 points
Saved: grids_2.5/cell_19_35.ply with 584 points
Saved: grids_2.5/cell_19_36.ply with 619 points
Saved: grids_2.5/cell_19_37.ply with 333 points
Saved: grids_2.5/cell_19_38.ply with 352 points
Saved: grids_2.5/cell_19_39.ply with 74 points
Saved: grids_2.5/cell_20_7.ply with 333 points
Saved: grids_2.5/cell_20_8.ply with 662 points
Saved: grids_2.5/cell_20_9.ply with 349 points
Saved: grids_2.5/cell_20_10.ply with 368 points
Saved: grids_2.5/cell_20_11.ply with 266 points
Saved: grids_2.5/cell_20_12.ply with 337 points
Saved: grids_2.5/cell_20_13.ply with 345 points
Saved: grids_2.5/cell_20_14.ply with 809 points
Saved: grids_2.5/cell_20_15.ply with 603 points
Saved: grids_2.5/cell_20_16.ply with 739 points
Saved: grids_2.5/cell_20_17.ply with 841 points
Saved: grids_2.5/cell_20_18.ply with 1345 points
Saved: grids_2.5/cell_20_19.ply with 783 points
Saved: grids_2.5/cell_20_20.ply with 1343 points
Saved: grids_2.5/cell_20_21.ply with 966 points
Saved: grids_2.5/cell_20_22.ply with 1621 points
Saved: grids_2.5/cell_20_23.ply with 896 points
Saved: grids_2.5/cell_20_24.ply with 1197 points
Saved: grids_2.5/cell_20_25.ply with 1292 points
Saved: grids_2.5/cell_20_26.ply with 1050 points
Saved: grids_2.5/cell_20_27.ply with 555 points
Saved: grids_2.5/cell_20_28.ply with 775 points
Saved: grids_2.5/cell_20_29.ply with 1205 points
Saved: grids_2.5/cell_20_30.ply with 1266 points
Saved: grids_2.5/cell_20_31.ply with 869 points
Saved: grids_2.5/cell_20_32.ply with 637 points
Saved: grids_2.5/cell_20_33.ply with 605 points
Saved: grids_2.5/cell_20_34.ply with 575 points
Saved: grids_2.5/cell_20_35.ply with 549 points
Saved: grids_2.5/cell_20_36.ply with 537 points
Saved: grids_2.5/cell_20_37.ply with 346 points
Saved: grids_2.5/cell_20_38.ply with 537 points
Saved: grids_2.5/cell_20_39.ply with 18 points
Saved: grids_2.5/cell_21_7.ply with 39 points
Saved: grids_2.5/cell_21_8.ply with 740 points
Saved: grids_2.5/cell_21_9.ply with 462 points
Saved: grids_2.5/cell_21_10.ply with 487 points
Saved: grids_2.5/cell_21_11.ply with 337 points
Saved: grids_2.5/cell_21_12.ply with 423 points
Saved: grids_2.5/cell_21_13.ply with 424 points
Saved: grids_2.5/cell_21_14.ply with 475 points
Saved: grids_2.5/cell_21_15.ply with 875 points
Saved: grids_2.5/cell_21_16.ply with 748 points
Saved: grids_2.5/cell_21_17.ply with 1129 points
Saved: grids_2.5/cell_21_18.ply with 1070 points
Saved: grids_2.5/cell_21_19.ply with 1205 points
Saved: grids_2.5/cell_21_20.ply with 1268 points
Saved: grids_2.5/cell_21_21.ply with 1003 points
Saved: grids_2.5/cell_21_22.ply with 841 points
Saved: grids_2.5/cell_21_23.ply with 618 points
Saved: grids_2.5/cell_21_24.ply with 696 points
Saved: grids_2.5/cell_21_25.ply with 461 points
Saved: grids_2.5/cell_21_26.ply with 449 points
Saved: grids_2.5/cell_21_27.ply with 370 points
Saved: grids_2.5/cell_21_28.ply with 228 points
Saved: grids_2.5/cell_21_29.ply with 216 points
Saved: grids_2.5/cell_21_30.ply with 1013 points
Saved: grids_2.5/cell_21_31.ply with 510 points
Saved: grids_2.5/cell_21_32.ply with 627 points
Saved: grids_2.5/cell_21_33.ply with 560 points
Saved: grids_2.5/cell_21_34.ply with 802 points
Saved: grids_2.5/cell_21_35.ply with 642 points
Saved: grids_2.5/cell_21_36.ply with 652 points
Saved: grids_2.5/cell_21_37.ply with 481 points
Saved: grids_2.5/cell_21_38.ply with 388 points
Saved: grids_2.5/cell_21_39.ply with 85 points
Saved: grids_2.5/cell_22_8.ply with 155 points
Saved: grids_2.5/cell_22_9.ply with 684 points
Saved: grids_2.5/cell_22_10.ply with 390 points
Saved: grids_2.5/cell_22_11.ply with 348 points
Saved: grids_2.5/cell_22_12.ply with 448 points
Saved: grids_2.5/cell_22_13.ply with 620 points
Saved: grids_2.5/cell_22_14.ply with 535 points
Saved: grids_2.5/cell_22_15.ply with 487 points
Saved: grids_2.5/cell_22_16.ply with 558 points
Saved: grids_2.5/cell_22_17.ply with 385 points
Saved: grids_2.5/cell_22_18.ply with 1294 points
Saved: grids_2.5/cell_22_19.ply with 1316 points
Saved: grids_2.5/cell_22_20.ply with 1308 points
Saved: grids_2.5/cell_22_21.ply with 1155 points
Saved: grids_2.5/cell_22_22.ply with 748 points
Saved: grids_2.5/cell_22_23.ply with 797 points
Saved: grids_2.5/cell_22_24.ply with 768 points
Saved: grids_2.5/cell_22_25.ply with 496 points
Saved: grids_2.5/cell_22_26.ply with 911 points
Saved: grids_2.5/cell_22_27.ply with 423 points
Saved: grids_2.5/cell_22_28.ply with 377 points
Saved: grids_2.5/cell_22_29.ply with 489 points
Saved: grids_2.5/cell_22_30.ply with 412 points
Saved: grids_2.5/cell_22_31.ply with 389 points
Saved: grids_2.5/cell_22_32.ply with 687 points
Saved: grids_2.5/cell_22_33.ply with 865 points
Saved: grids_2.5/cell_22_34.ply with 516 points
Saved: grids_2.5/cell_22_35.ply with 256 points
Saved: grids_2.5/cell_22_36.ply with 523 points
Saved: grids_2.5/cell_22_37.ply with 339 points
Saved: grids_2.5/cell_22_38.ply with 168 points
Saved: grids_2.5/cell_22_39.ply with 24 points
Saved: grids_2.5/cell_23_9.ply with 129 points
Saved: grids_2.5/cell_23_10.ply with 479 points
Saved: grids_2.5/cell_23_11.ply with 157 points
Saved: grids_2.5/cell_23_12.ply with 669 points
Saved: grids_2.5/cell_23_13.ply with 230 points
Saved: grids_2.5/cell_23_14.ply with 610 points
Saved: grids_2.5/cell_23_15.ply with 694 points
Saved: grids_2.5/cell_23_16.ply with 491 points
Saved: grids_2.5/cell_23_17.ply with 410 points
Saved: grids_2.5/cell_23_18.ply with 196 points
Saved: grids_2.5/cell_23_19.ply with 635 points
Saved: grids_2.5/cell_23_20.ply with 1351 points
Saved: grids_2.5/cell_23_21.ply with 1548 points
Saved: grids_2.5/cell_23_22.ply with 1213 points
Saved: grids_2.5/cell_23_23.ply with 1641 points
Saved: grids_2.5/cell_23_24.ply with 1024 points
Saved: grids_2.5/cell_23_25.ply with 558 points
Saved: grids_2.5/cell_23_26.ply with 271 points
Saved: grids_2.5/cell_23_27.ply with 430 points
Saved: grids_2.5/cell_23_28.ply with 348 points
Saved: grids_2.5/cell_23_29.ply with 301 points
Saved: grids_2.5/cell_23_30.ply with 104 points
Saved: grids_2.5/cell_23_31.ply with 294 points
Saved: grids_2.5/cell_23_32.ply with 401 points
Saved: grids_2.5/cell_23_33.ply with 611 points
Saved: grids_2.5/cell_23_34.ply with 669 points
Saved: grids_2.5/cell_23_35.ply with 715 points
Saved: grids_2.5/cell_23_36.ply with 373 points
Saved: grids_2.5/cell_23_37.ply with 429 points
Saved: grids_2.5/cell_23_38.ply with 190 points
Saved: grids_2.5/cell_23_39.ply with 24 points
Saved: grids_2.5/cell_24_9.ply with 4 points
Saved: grids_2.5/cell_24_10.ply with 344 points
Saved: grids_2.5/cell_24_11.ply with 285 points
Saved: grids_2.5/cell_24_12.ply with 321 points
Saved: grids_2.5/cell_24_13.ply with 169 points
Saved: grids_2.5/cell_24_14.ply with 307 points
Saved: grids_2.5/cell_24_15.ply with 395 points
Saved: grids_2.5/cell_24_16.ply with 383 points
Saved: grids_2.5/cell_24_17.ply with 727 points
Saved: grids_2.5/cell_24_18.ply with 122 points
Saved: grids_2.5/cell_24_19.ply with 330 points
Saved: grids_2.5/cell_24_20.ply with 329 points
Saved: grids_2.5/cell_24_21.ply with 951 points
Saved: grids_2.5/cell_24_22.ply with 1331 points
Saved: grids_2.5/cell_24_23.ply with 941 points
Saved: grids_2.5/cell_24_24.ply with 1187 points
Saved: grids_2.5/cell_24_25.ply with 784 points
Saved: grids_2.5/cell_24_26.ply with 406 points
Saved: grids_2.5/cell_24_27.ply with 439 points
Saved: grids_2.5/cell_24_28.ply with 365 points
Saved: grids_2.5/cell_24_29.ply with 451 points
Saved: grids_2.5/cell_24_30.ply with 328 points
Saved: grids_2.5/cell_24_31.ply with 337 points
Saved: grids_2.5/cell_24_32.ply with 426 points
Saved: grids_2.5/cell_24_33.ply with 289 points
Saved: grids_2.5/cell_24_34.ply with 613 points
Saved: grids_2.5/cell_24_35.ply with 554 points
Saved: grids_2.5/cell_24_36.ply with 249 points
Saved: grids_2.5/cell_24_37.ply with 480 points
Saved: grids_2.5/cell_24_38.ply with 250 points
Saved: grids_2.5/cell_24_39.ply with 8 points
Saved: grids_2.5/cell_25_10.ply with 33 points
Saved: grids_2.5/cell_25_11.ply with 303 points
Saved: grids_2.5/cell_25_12.ply with 557 points
Saved: grids_2.5/cell_25_13.ply with 254 points
Saved: grids_2.5/cell_25_14.ply with 258 points
Saved: grids_2.5/cell_25_15.ply with 235 points
Saved: grids_2.5/cell_25_16.ply with 228 points
Saved: grids_2.5/cell_25_17.ply with 517 points
Saved: grids_2.5/cell_25_18.ply with 182 points
Saved: grids_2.5/cell_25_19.ply with 542 points
Saved: grids_2.5/cell_25_20.ply with 305 points
Saved: grids_2.5/cell_25_21.ply with 477 points
Saved: grids_2.5/cell_25_22.ply with 457 points
Saved: grids_2.5/cell_25_23.ply with 844 points
Saved: grids_2.5/cell_25_24.ply with 773 points
Saved: grids_2.5/cell_25_25.ply with 951 points
Saved: grids_2.5/cell_25_26.ply with 802 points
Saved: grids_2.5/cell_25_27.ply with 826 points
Saved: grids_2.5/cell_25_28.ply with 562 points
Saved: grids_2.5/cell_25_29.ply with 396 points
Saved: grids_2.5/cell_25_30.ply with 660 points
Saved: grids_2.5/cell_25_31.ply with 290 points
Saved: grids_2.5/cell_25_32.ply with 172 points
Saved: grids_2.5/cell_25_33.ply with 172 points
Saved: grids_2.5/cell_25_34.ply with 448 points
Saved: grids_2.5/cell_25_35.ply with 377 points
Saved: grids_2.5/cell_25_36.ply with 412 points
Saved: grids_2.5/cell_25_37.ply with 584 points
Saved: grids_2.5/cell_25_38.ply with 189 points
Saved: grids_2.5/cell_26_11.ply with 491 points
Saved: grids_2.5/cell_26_12.ply with 327 points
Saved: grids_2.5/cell_26_13.ply with 385 points
Saved: grids_2.5/cell_26_14.ply with 351 points
Saved: grids_2.5/cell_26_15.ply with 200 points
Saved: grids_2.5/cell_26_16.ply with 224 points
Saved: grids_2.5/cell_26_17.ply with 319 points
Saved: grids_2.5/cell_26_18.ply with 278 points
Saved: grids_2.5/cell_26_19.ply with 350 points
Saved: grids_2.5/cell_26_20.ply with 346 points
Saved: grids_2.5/cell_26_21.ply with 293 points
Saved: grids_2.5/cell_26_22.ply with 618 points
Saved: grids_2.5/cell_26_23.ply with 316 points
Saved: grids_2.5/cell_26_24.ply with 284 points
Saved: grids_2.5/cell_26_25.ply with 583 points
Saved: grids_2.5/cell_26_26.ply with 590 points
Saved: grids_2.5/cell_26_27.ply with 310 points
Saved: grids_2.5/cell_26_28.ply with 282 points
Saved: grids_2.5/cell_26_29.ply with 268 points
Saved: grids_2.5/cell_26_30.ply with 337 points
Saved: grids_2.5/cell_26_31.ply with 397 points
Saved: grids_2.5/cell_26_32.ply with 239 points
Saved: grids_2.5/cell_26_33.ply with 268 points
Saved: grids_2.5/cell_26_34.ply with 209 points
Saved: grids_2.5/cell_26_35.ply with 163 points
Saved: grids_2.5/cell_26_36.ply with 245 points
Saved: grids_2.5/cell_26_37.ply with 214 points
Saved: grids_2.5/cell_26_38.ply with 499 points
Saved: grids_2.5/cell_27_13.ply with 34 points
Saved: grids_2.5/cell_27_14.ply with 78 points
Saved: grids_2.5/cell_27_15.ply with 222 points
Saved: grids_2.5/cell_27_16.ply with 224 points
Saved: grids_2.5/cell_27_17.ply with 368 points
Saved: grids_2.5/cell_27_18.ply with 140 points
Saved: grids_2.5/cell_27_19.ply with 202 points
Saved: grids_2.5/cell_27_20.ply with 311 points
Saved: grids_2.5/cell_27_21.ply with 292 points
Saved: grids_2.5/cell_27_22.ply with 306 points
Saved: grids_2.5/cell_27_23.ply with 629 points
Saved: grids_2.5/cell_27_24.ply with 293 points
Saved: grids_2.5/cell_27_25.ply with 307 points
Saved: grids_2.5/cell_27_26.ply with 495 points
Saved: grids_2.5/cell_27_27.ply with 703 points
Saved: grids_2.5/cell_27_28.ply with 348 points
Saved: grids_2.5/cell_27_29.ply with 307 points
Saved: grids_2.5/cell_27_30.ply with 176 points
Saved: grids_2.5/cell_27_31.ply with 92 points
Saved: grids_2.5/cell_27_32.ply with 172 points
Saved: grids_2.5/cell_27_33.ply with 470 points
Saved: grids_2.5/cell_27_34.ply with 241 points
Saved: grids_2.5/cell_27_35.ply with 453 points
Saved: grids_2.5/cell_27_36.ply with 395 points
Saved: grids_2.5/cell_27_37.ply with 241 points
Saved: grids_2.5/cell_27_38.ply with 319 points
Saved: grids_2.5/cell_28_16.ply with 10 points
Saved: grids_2.5/cell_28_17.ply with 254 points
Saved: grids_2.5/cell_28_18.ply with 111 points
Saved: grids_2.5/cell_28_19.ply with 197 points
Saved: grids_2.5/cell_28_20.ply with 236 points
Saved: grids_2.5/cell_28_21.ply with 270 points
Saved: grids_2.5/cell_28_22.ply with 190 points
Saved: grids_2.5/cell_28_23.ply with 281 points
Saved: grids_2.5/cell_28_24.ply with 366 points
Saved: grids_2.5/cell_28_25.ply with 312 points
Saved: grids_2.5/cell_28_26.ply with 290 points
Saved: grids_2.5/cell_28_27.ply with 277 points
Saved: grids_2.5/cell_28_28.ply with 555 points
Saved: grids_2.5/cell_28_29.ply with 521 points
Saved: grids_2.5/cell_28_30.ply with 294 points
Saved: grids_2.5/cell_28_31.ply with 213 points
Saved: grids_2.5/cell_28_32.ply with 320 points
Saved: grids_2.5/cell_28_33.ply with 285 points
Saved: grids_2.5/cell_28_34.ply with 431 points
Saved: grids_2.5/cell_28_35.ply with 279 points
Saved: grids_2.5/cell_28_36.ply with 188 points
Saved: grids_2.5/cell_28_37.ply with 246 points
Saved: grids_2.5/cell_28_38.ply with 363 points
Saved: grids_2.5/cell_29_19.ply with 2 points
Saved: grids_2.5/cell_29_20.ply with 78 points
Saved: grids_2.5/cell_29_21.ply with 122 points
Saved: grids_2.5/cell_29_22.ply with 295 points
Saved: grids_2.5/cell_29_23.ply with 275 points
Saved: grids_2.5/cell_29_24.ply with 108 points
Saved: grids_2.5/cell_29_25.ply with 442 points
Saved: grids_2.5/cell_29_26.ply with 252 points
Saved: grids_2.5/cell_29_27.ply with 91 points
Saved: grids_2.5/cell_29_28.ply with 303 points
Saved: grids_2.5/cell_29_29.ply with 295 points
Saved: grids_2.5/cell_29_30.ply with 367 points
Saved: grids_2.5/cell_29_31.ply with 114 points
Saved: grids_2.5/cell_29_32.ply with 131 points
Saved: grids_2.5/cell_29_33.ply with 249 points
Saved: grids_2.5/cell_29_34.ply with 245 points
Saved: grids_2.5/cell_29_35.ply with 235 points
Saved: grids_2.5/cell_29_36.ply with 243 points
Saved: grids_2.5/cell_29_37.ply with 133 points
Saved: grids_2.5/cell_29_38.ply with 187 points
Saved: grids_2.5/cell_30_22.ply with 2 points
Saved: grids_2.5/cell_30_23.ply with 28 points
Saved: grids_2.5/cell_30_24.ply with 90 points
Saved: grids_2.5/cell_30_25.ply with 276 points
Saved: grids_2.5/cell_30_26.ply with 243 points
Saved: grids_2.5/cell_30_27.ply with 309 points
Saved: grids_2.5/cell_30_28.ply with 233 points
Saved: grids_2.5/cell_30_29.ply with 196 points
Saved: grids_2.5/cell_30_30.ply with 282 points
Saved: grids_2.5/cell_30_31.ply with 424 points
Saved: grids_2.5/cell_30_32.ply with 441 points
Saved: grids_2.5/cell_30_33.ply with 366 points
Saved: grids_2.5/cell_30_34.ply with 220 points
Saved: grids_2.5/cell_30_35.ply with 239 points
Saved: grids_2.5/cell_30_36.ply with 144 points
Saved: grids_2.5/cell_30_37.ply with 213 points
Saved: grids_2.5/cell_30_38.ply with 149 points
Saved: grids_2.5/cell_31_26.ply with 16 points
Saved: grids_2.5/cell_31_27.ply with 28 points
Saved: grids_2.5/cell_31_28.ply with 78 points
Saved: grids_2.5/cell_31_29.ply with 150 points
Saved: grids_2.5/cell_31_30.ply with 83 points
Saved: grids_2.5/cell_31_31.ply with 229 points
Saved: grids_2.5/cell_31_32.ply with 143 points
Saved: grids_2.5/cell_31_33.ply with 208 points
Saved: grids_2.5/cell_31_34.ply with 266 points
Saved: grids_2.5/cell_31_35.ply with 91 points
Saved: grids_2.5/cell_31_36.ply with 104 points
Saved: grids_2.5/cell_31_37.ply with 198 points
Saved: grids_2.5/cell_31_38.ply with 99 points
Saved: grids_2.5/cell_32_29.ply with 1 points
Saved: grids_2.5/cell_32_30.ply with 39 points
Saved: grids_2.5/cell_32_31.ply with 88 points
Saved: grids_2.5/cell_32_32.ply with 39 points
Saved: grids_2.5/cell_32_33.ply with 197 points
Saved: grids_2.5/cell_32_34.ply with 743 points
Saved: grids_2.5/cell_32_35.ply with 263 points
Saved: grids_2.5/cell_32_36.ply with 236 points
Saved: grids_2.5/cell_32_37.ply with 95 points
Saved: grids_2.5/cell_32_38.ply with 88 points
Saved: grids_2.5/cell_33_32.ply with 2 points
Saved: grids_2.5/cell_33_33.ply with 63 points
Saved: grids_2.5/cell_33_34.ply with 66 points
Saved: grids_2.5/cell_33_35.ply with 144 points
Saved: grids_2.5/cell_33_36.ply with 79 points
Saved: grids_2.5/cell_33_37.ply with 284 points
Saved: grids_2.5/cell_33_38.ply with 241 points


# 17.04.25, 09:58

Total points: 887138

filtered_point_cloud.ply: 725669 points → 81.81% of total
Stump.ply: 86655 points → 9.77% of total
Separated.ply: 74814 points → 8.43% of total
