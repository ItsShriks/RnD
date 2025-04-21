import numpy as np

file1 = np.load('/Users/shrikar/RnD/dataset/npy/ground_points_ransac.npy')
file2 = np.load('/Users/shrikar/RnD/dataset/npy/non_ground_points_ransac.npy')

combined = np.concatenate((file1, file2), axis=0)  # axis=0 for row-wise combination

# Save the combined file
np.save('/Users/shrikar/RnD/dataset/npy/ransac.npy', combined)
