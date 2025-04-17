import os
import numpy as np
import pandas as pd
from tqdm import tqdm

def create_index_npy(input_dir, output_path="Index.csv"):
    index_data = []

    files = [f for f in os.listdir(input_dir) if f.endswith(".npy") and f != "Index.csv"]

    for file in tqdm(files):
        path = os.path.join(input_dir, file)
        try:
            data = np.load(path)
            if data.ndim == 1:
                num_rows = data.shape[0]
                num_cols = 1
            elif data.ndim == 2:
                num_rows, num_cols = data.shape
            else:
                num_rows = num_cols = f"Unsupported {data.ndim}D"
            index_data.append([file, num_rows, num_cols])
        except Exception as e:
            print(f"Error reading {file}: {e}")
            index_data.append([file, "Error", "Error"])

    index_df = pd.DataFrame(index_data, columns=["filename", "num_rows", "num_columns"])
    index_csv_path = os.path.join(input_dir, output_path)
    index_df.to_csv(index_csv_path, index=False)
    print(f"\n✅ Index saved at: {index_csv_path}")

# Example usage
input_directory = '/Users/shrikar/RnD/dataset/npy/dataset_ransac'
create_index_npy(input_directory)
