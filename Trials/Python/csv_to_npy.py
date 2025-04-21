import os
import numpy as np

def convert_csvs_to_npys(input_dir, output_dir):

    os.makedirs(output_dir, exist_ok=True)

    print(f"\n📁 Input Directory: {input_dir}")
    print(f"💾 Output Directory: {output_dir}\n")

    # Count how many files converted
    converted_count = 0

    for filename in os.listdir(input_dir):
        if filename.endswith('.csv'):
            try:
                csv_path = os.path.join(input_dir, filename)
                npy_filename = filename.replace('.csv', '.npy')
                npy_path = os.path.join(output_dir, npy_filename)

                data = np.loadtxt(csv_path, delimiter=',', skiprows=1)

                # Save as .npy
                np.save(npy_path, data)
                print(f"✅ Converted: {filename} → {npy_filename}")
                converted_count += 1

            except Exception as e:
                print(f"❌ Error converting {filename}: {e}")

    print(f"\n🎉 Done! {converted_count} files converted.\n")

# === USER CONFIGURATION ===
input_directory = '/Users/shrikar/Library/Mobile Documents/com~apple~CloudDocs/Sem IV/R&D/RnD/dataset/grids_2.5/padded_4096'
output_directory = '/Users/shrikar/Library/Mobile Documents/com~apple~CloudDocs/Sem IV/R&D/RnD/dataset/grids_2.5/npy'

convert_csvs_to_npys(input_directory, output_directory)
