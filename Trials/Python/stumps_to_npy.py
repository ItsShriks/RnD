import os
import numpy as np

def convert_txt_dir_to_npy(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if not filename.endswith(".txt"):
            continue

        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename.replace(".txt", ".npy"))

        data = []
        data_started = False  # flag to detect actual data lines

        with open(input_path, 'r') as file:
            for idx, line in enumerate(file):
                line = line.strip()

                # Skip empty lines or header lines
                if not line or line.startswith('//') or line.isdigit():
                    continue

                parts = line.split(';')
                if len(parts) < 15:
                    continue  # malformed line

                try:
                    x = float(parts[0].strip())
                    y = float(parts[1].strip())
                    z = float(parts[2].strip())
                    intensity = float(parts[6].strip())
                    return_number = float(parts[7].strip())
                    classification = float(parts[14].strip())
                    data.append([x, y, z, classification, intensity, return_number])
                except (ValueError, IndexError) as e:
                    print(f"[WARN] Skipped line {idx+1} in {filename}: {e}")
                    continue

        if data:
            np_data = np.array(data, dtype=np.float32)
            np.save(output_path, np_data)
            print(f"[OK] Processed: {filename} → {output_path} ({len(np_data)} points)")
        else:
            print(f"[EMPTY] No valid data in {filename}!")

# Example usage
input_directory = "/Users/shrikar/RnD/dataset/Stumps_labelled"
output_directory = "/Users/shrikar/RnD/dataset/Stumps_labelled_npy"
convert_txt_dir_to_npy(input_directory, output_directory)
