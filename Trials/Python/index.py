import os
import pandas as pd
from tqdm import tqdm

def create_index_csv(input_dir, output_path="Index.csv"):
    index_data = []

    files = [f for f in os.listdir(input_dir) if f.endswith(".csv") and f != "Index.csv"]

    for file in tqdm(files):
        path = os.path.join(input_dir, file)
        try:
            df = pd.read_csv(path)
            num_rows, num_cols = df.shape
            index_data.append([file, num_rows, num_cols])
        except Exception as e:
            print(f"Error reading {file}: {e}")
            index_data.append([file, "Error", "Error"])

    index_df = pd.DataFrame(index_data, columns=["filename", "num_rows", "num_columns"])
    index_csv_path = os.path.join(input_dir, output_path)
    index_df.to_csv(index_csv_path, index=False)
    print(f"\n✅ Index saved at: {index_csv_path}")

# Example usage
input_directory = '/Users/shrikar/Library/Mobile Documents/com~apple~CloudDocs/Sem IV/R&D/RnD/dataset/grids_1.0/padded_1024'
create_index_csv(input_directory)
