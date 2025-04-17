import numpy as np
import os
import random

# --- Configuration ---
file1_path = '/Users/shrikar/RnD/dataset/npy/ground_points_ransac.npy'
file2_path = '/Users/shrikar/RnD/dataset/npy/non_ground_points_ransac.npy'
output_dir = '/Users/shrikar/RnD/dataset/npy/dataset_ransac'
min_rows_per_file = 1024
target_num_files = 300

# --- Load both .npy files ---
data1 = np.load(file1_path)
data2 = np.load(file2_path)

# --- Check shape consistency ---
assert data1.shape[1] == 6 and data2.shape[1] == 6, "Both files must have 6 columns"
print(f"Loaded {data1.shape[0]} rows from file1 and {data2.shape[0]} rows from file2")

# --- Combine and shuffle ---
combined_data = np.vstack((data1, data2))
np.random.shuffle(combined_data)
total_rows = combined_data.shape[0]

# --- Prepare output folder ---
os.makedirs(output_dir, exist_ok=True)

# --- Compute average chunk size ---
avg_chunk_size = total_rows // target_num_files

# --- Split into balanced chunks ---
start_idx = 0
rows_left = total_rows
chunk_id = 0

while rows_left >= min_rows_per_file:
    # Keep chunks around average ± 20%
    min_size = int(avg_chunk_size * 0.8)
    max_size = int(avg_chunk_size * 1.2)
    chunk_size = random.randint(min_size, max_size)

    if rows_left - chunk_size < min_rows_per_file:
        chunk_size = rows_left  # dump the rest in the last file

    chunk = combined_data[start_idx:start_idx + chunk_size]
    np.save(os.path.join(output_dir, f'chunk_{chunk_id}.npy'), chunk)

    start_idx += chunk_size
    rows_left -= chunk_size
    chunk_id += 1

print(f"✅ Done! Created {chunk_id} files in '{output_dir}' from total {total_rows} rows.")
