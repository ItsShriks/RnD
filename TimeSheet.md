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
## 07 October 2024 13:53
System is Ready !
## Installation of CloudCompare

07.10.24, 14:23:17 Tutorial PCL
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


07.10.24, 17:07:41, Smoothened The Surface and Located Region of Interest

# 14 October 2024 13:00



14.10.24, 14:07:33 - Cropped by 100X100X100 meters*

15.10.24, 14:36:33 - Clustering Successful !

##Points stats:
Min: [-121.80550385 -127.46252441   -8.48567581], Max: [157.43299866 128.68302917  36.19382477]
Contains NaN: False
Contains Inf: False
Number of clusters found: 847
Number of noise points: 26355
Clustering.py:53: UserWarning: *c* argument looks like a single numeric RGB or RGBA sequence, which should be avoided as value-mapping will have precedence in case its length matches with *x* & *y*.  Please use the *color* keyword-argument or provide a 2D array with a single row if you intend to specify the same RGB or RGBA value for all points.
  ax.scatter(xyz[:, 0], xyz[:, 1], xyz[:, 2], s=20, c=color, label=f'Cluster {label}' if label != -1 else 'Noise')sudo apt install libusb-1.0-0-dev
cd ~/pcl/build
cmake ..
make -j32
sudo make install



