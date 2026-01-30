import os

folder = "temp_files"

for file in os.listdir(folder):
    os.remove(os.path.join(folder, file))

print("Folder cleaned")