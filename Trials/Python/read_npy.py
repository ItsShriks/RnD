import numpy as np

# Replace 'your_file.npy' with the path to your file
data = np.load('/Users/shrikar/RnD/dataset/npy/ransac.npy', allow_pickle=True)

print(data.shape)  # Check the shape of the array
print(data.dtype)  # Check the data type
print(data[:])

np.savetxt('/Users/shrikar/RnD/dataset/npy/ransac.txt', data, fmt='%.6f')  # Adjust fmt as needed# Print the array
