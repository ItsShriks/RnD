import numpy as np
import h5py
import glob
import os

csv_files = glob.glob('/Users/shrikar/Library/Mobile Documents/com~apple~CloudDocs/Sem IV/R&D/RnD/dataset/grids_2.5/padded_4096_validate/*.csv')
all_data = []
all_labels = []

for csv_file in csv_files:
    data = np.loadtxt(csv_file, delimiter=',', skiprows=1)  # shape: (4096, 8)
    data = data.reshape(1, 4096, 8)  # add batch dimension
    all_data.append(data)
    label = 0  # replace with your logic
    all_labels.append(label)

all_data = np.vstack(all_data)
all_labels = np.array(all_labels, dtype=np.int64)

with h5py.File('validate.h5', 'w') as f:
    f.create_dataset('data', data=all_data)
    f.create_dataset('label', data=all_labels)
