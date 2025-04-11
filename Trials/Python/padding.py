import os
import pandas as pd
import numpy as np
from tqdm import tqdm

def pad_csv_to_4096(input_csv_path, output_csv_path):
    df = pd.read_csv(input_csv_path)
    current_rows, cols = df.shape

    if current_rows >= 4096:
        # Just copy the original file if it has enough rows
        df.head(4096).to_csv(output_csv_path, index=False)
        print(f"✅ {os.path.basename(input_csv_path)} already has {current_rows} rows. Copied first 4096 rows.")
        return

    missing_rows = 4096 - current_rows
    zero_data = np.zeros((missing_rows, cols))
    zero_df = pd.DataFrame(zero_data, columns=df.columns)

    padded_df = pd.concat([df, zero_df], ignore_index=True)
    padded_df.to_csv(output_csv_path, index=False)
    print(f"📝 Padded and saved: {os.path.basename(output_csv_path)}")

def pad_all_csvs_in_dir(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    csv_files = [f for f in os.listdir(input_dir) if f.endswith(".csv") and f != "Index.csv"]

    print(f"\n📂 Found {len(csv_files)} CSV files. Saving padded versions to '{output_dir}'...\n")

    for csv_file in tqdm(csv_files):
        input_path = os.path.join(input_dir, csv_file)
        output_path = os.path.join(output_dir, csv_file)
        pad_csv_to_4096(input_path, output_path)

# --- ✅ USAGE ---
input_directory = '/Users/shrikar/Library/Mobile Documents/com~apple~CloudDocs/Sem IV/R&D/RnD/Trials/Python/grids_2.5/grids_2.5_csv'
output_directory = '/Users/shrikar/Library/Mobile Documents/com~apple~CloudDocs/Sem IV/R&D/RnD/Trials/Python/grids_2.5/padded_4096'

pad_all_csvs_in_dir(input_directory, output_directory)
