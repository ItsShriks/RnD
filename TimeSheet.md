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



27.10.24, 20:58:10
Number of clusters: 201
[Open3D WARNING] GLFW Error: Cocoa: Failed to find service port for display
Cluster 0 has 1131027 points.
Cluster 1 has 1054 points.
Cluster 2 has 149 points.
Cluster 3 has 495 points.
Cluster 4 has 26 points.
Cluster 5 has 1470 points.
Cluster 6 has 135 points.
Cluster 7 has 219 points.
Cluster 8 has 464 points.
Cluster 9 has 127 points.
Cluster 10 has 112 points.
Cluster 11 has 79 points.
Cluster 12 has 248 points.
Cluster 13 has 332 points.
Cluster 14 has 115 points.
Cluster 15 has 84 points.
Cluster 16 has 810 points.
Cluster 17 has 53 points.
Cluster 18 has 46 points.
Cluster 19 has 73 points.
Cluster 20 has 97 points.
Cluster 21 has 22 points.
Cluster 22 has 306 points.
Cluster 23 has 599 points.
Cluster 24 has 165 points.
Cluster 25 has 79 points.
Cluster 26 has 85 points.
Cluster 27 has 78 points.
Cluster 28 has 23 points.
Cluster 29 has 366 points.
Cluster 30 has 180 points.
Cluster 31 has 47 points.
Cluster 32 has 126 points.
Cluster 33 has 58 points.
Cluster 34 has 1179 points.
Cluster 35 has 160 points.
Cluster 36 has 1170 points.
Cluster 37 has 335 points.
Cluster 38 has 314 points.
Cluster 39 has 217 points.
Cluster 40 has 65 points.
Cluster 41 has 171 points.
Cluster 42 has 31 points.
Cluster 43 has 20 points.
Cluster 44 has 63 points.
Cluster 45 has 28 points.
Cluster 46 has 83 points.
Cluster 47 has 19 points.
Cluster 48 has 145 points.
Cluster 49 has 49 points.
Cluster 50 has 33 points.
Cluster 51 has 41 points.
Cluster 52 has 21 points.
Cluster 53 has 217 points.
Cluster 54 has 73 points.
Cluster 55 has 344 points.
Cluster 56 has 151 points.
Cluster 57 has 17 points.
Cluster 58 has 35 points.
Cluster 59 has 152 points.
Cluster 60 has 38 points.
Cluster 61 has 52 points.
Cluster 62 has 81 points.
Cluster 63 has 28 points.
Cluster 64 has 19 points.
Cluster 65 has 20 points.
Cluster 66 has 11 points.
Cluster 67 has 112 points.
Cluster 68 has 16 points.
Cluster 69 has 154 points.
Cluster 70 has 58 points.
Cluster 71 has 57 points.
Cluster 72 has 58 points.
Cluster 73 has 37 points.
Cluster 74 has 36 points.
Cluster 75 has 169 points.
Cluster 76 has 95 points.
Cluster 77 has 364 points.
Cluster 78 has 20 points.
Cluster 79 has 13 points.
Cluster 80 has 47 points.
Cluster 81 has 13 points.
Cluster 82 has 98 points.
Cluster 83 has 14 points.
Cluster 84 has 45 points.
Cluster 85 has 9 points.
Cluster 86 has 14 points.
Cluster 87 has 23 points.
Cluster 88 has 38 points.
Cluster 89 has 41 points.
Cluster 90 has 79 points.
Cluster 91 has 41 points.
Cluster 92 has 14 points.
Cluster 93 has 15 points.
Cluster 94 has 24 points.
Cluster 95 has 11 points.
Cluster 96 has 66 points.
Cluster 97 has 33 points.
Cluster 98 has 17 points.
Cluster 99 has 10 points.
Cluster 100 has 19 points.
Cluster 101 has 15 points.
Cluster 102 has 25 points.
Cluster 103 has 10 points.
Cluster 104 has 14 points.
Cluster 105 has 17 points.
Cluster 106 has 10 points.
Cluster 107 has 13 points.
Cluster 108 has 10 points.
Cluster 109 has 49 points.
Cluster 110 has 10 points.
Cluster 111 has 11 points.
Cluster 112 has 19 points.
Cluster 113 has 42 points.
Cluster 114 has 42 points.
Cluster 115 has 35 points.
Cluster 116 has 8 points.
Cluster 117 has 33 points.
Cluster 118 has 18 points.
Cluster 119 has 11 points.
Cluster 120 has 60 points.
Cluster 121 has 9 points.
Cluster 122 has 34 points.
Cluster 123 has 43 points.
Cluster 124 has 54 points.
Cluster 125 has 54 points.
Cluster 126 has 17 points.
Cluster 127 has 10 points.
Cluster 128 has 14 points.
Cluster 129 has 16 points.
Cluster 130 has 12 points.
Cluster 131 has 43 points.
Cluster 132 has 21 points.
Cluster 133 has 12 points.
Cluster 134 has 13 points.
Cluster 135 has 15 points.
Cluster 136 has 17 points.
Cluster 137 has 18 points.
Cluster 138 has 27 points.
Cluster 139 has 12 points.
Cluster 140 has 17 points.
Cluster 141 has 10 points.
Cluster 142 has 16 points.
Cluster 143 has 10 points.
Cluster 144 has 12 points.
Cluster 145 has 10 points.
Cluster 146 has 51 points.
Cluster 147 has 27 points.
Cluster 148 has 12 points.
Cluster 149 has 31 points.
Cluster 150 has 20 points.
Cluster 151 has 33 points.
Cluster 152 has 105 points.
Cluster 153 has 60 points.
Cluster 154 has 11 points.
Cluster 155 has 62 points.
Cluster 156 has 25 points.
Cluster 157 has 14 points.
Cluster 158 has 35 points.
Cluster 159 has 10 points.
Cluster 160 has 15 points.
Cluster 161 has 24 points.
Cluster 162 has 35 points.
Cluster 163 has 24 points.
Cluster 164 has 14 points.
Cluster 165 has 40 points.
Cluster 166 has 15 points.
Cluster 167 has 17 points.
Cluster 168 has 24 points.
Cluster 169 has 86 points.
Cluster 170 has 16 points.
Cluster 171 has 18 points.
Cluster 172 has 20 points.
Cluster 173 has 11 points.
Cluster 174 has 10 points.
Cluster 175 has 13 points.
Cluster 176 has 10 points.
Cluster 177 has 10 points.
Cluster 178 has 14 points.
Cluster 179 has 10 points.
Cluster 180 has 26 points.
Cluster 181 has 19 points.
Cluster 182 has 23 points.
Cluster 183 has 16 points.
Cluster 184 has 16 points.
Cluster 185 has 26 points.
Cluster 186 has 50 points.
Cluster 187 has 5 points.
Cluster 188 has 11 points.
Cluster 189 has 9 points.
Cluster 190 has 38 points.
Cluster 191 has 11 points.
Cluster 192 has 9 points.
Cluster 193 has 4 points.
Cluster 194 has 9 points.
Cluster 195 has 16 points.
Cluster 196 has 11 points.
Cluster 197 has 10 points.
Cluster 198 has 10 points.
Cluster 199 has 11 points.
Cluster 200 has 10 points.
