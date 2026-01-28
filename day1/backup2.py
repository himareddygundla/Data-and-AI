import os
import shutil

# Source folder
source_folder = r"C:\\Users\\VEDHA\\OneDrive\\Desktop\\Data and AI\\source_image"

# Backup folder (created in the same location as source folder)
backup_folder = os.path.join(os.path.dirname(source_folder), "backup_photos")

# Create backup folder if it doesn't exist
if not os.path.exists(backup_folder):
    os.makedirs(backup_folder)
    print(f"Backup folder created: {backup_folder}")
else:
    print(f"Backup folder already exists: {backup_folder}")

# Supported image file extensions
image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp')

# Copy all image files from source to backup
for file_name in os.listdir(source_folder):
    if file_name.lower().endswith(image_extensions):
        source_file = os.path.join(source_folder, file_name)
        dest_file = os.path.join(backup_folder, file_name)
        shutil.copy(source_file, dest_file)
        print(f"Copied: {file_name}")

print("All photos have been backed up successfully!")