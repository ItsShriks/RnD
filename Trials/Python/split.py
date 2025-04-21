import os
import shutil
import random

def split_files_into_folders(input_dir, output_dir, train_ratio=0.7, validate_ratio=0.15, test_ratio=0.15):
    # Get the last part of the input_dir (e.g., "npy")
    base_name = os.path.basename(os.path.normpath(input_dir))

    # Create output subfolder names with prefix
    train_dir = os.path.join(output_dir, f'{base_name}_train')
    validate_dir = os.path.join(output_dir, f'{base_name}_validate')
    test_dir = os.path.join(output_dir, f'{base_name}_test')

    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(validate_dir, exist_ok=True)
    os.makedirs(test_dir, exist_ok=True)

    # Get all files in the input directory
    files = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]
    random.shuffle(files)

    # Calculate the number of files for each split
    total_files = len(files)
    train_count = int(total_files * train_ratio)
    validate_count = int(total_files * validate_ratio)
    test_count = total_files - train_count - validate_count  # Remaining files go to test

    # Split the files
    train_files = files[:train_count]
    validate_files = files[train_count:train_count + validate_count]
    test_files = files[train_count + validate_count:]

    # Copy/move the files to their respective directories
    for file in train_files:
        shutil.copy(os.path.join(input_dir, file), os.path.join(train_dir, file))
    for file in validate_files:
        shutil.copy(os.path.join(input_dir, file), os.path.join(validate_dir, file))
    for file in test_files:
        shutil.copy(os.path.join(input_dir, file), os.path.join(test_dir, file))

    print(f"Files have been split into:\n"
          f"{len(train_files)} files in {train_dir}\n"
          f"{len(validate_files)} files in {validate_dir}\n"
          f"{len(test_files)} files in {test_dir}")

input_dir = '/Users/shrikar/Library/Mobile Documents/com~apple~CloudDocs/Sem IV/R&D/RnD/dataset/grids_5.0/grids_5.0_csv'
output_dir = '/Users/shrikar/Library/Mobile Documents/com~apple~CloudDocs/Sem IV/R&D/RnD/dataset/grids_5.0'

split_files_into_folders(input_dir, output_dir)
