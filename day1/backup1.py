import os
import shutil

source_file = "/Users/VEDHA/OneDrive/Desktop/Data and AI/data.txt"
target_folder = "/Users/VEDHA/OneDrive/Desktop/Data and AI/my_folder"

if not os.path.exists(target_folder):
    os.makedirs(target_folder)
    print(f"Folder created: {target_folder}")
else:
    print(f"Folder already exists: {target_folder}")
destination_file = os.path.join(target_folder, os.path.basename(source_file))
shutil.copy(source_file, destination_file)  
print(f"File '{source_file}' has been copied to '{destination_file}'")