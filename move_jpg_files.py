import os
import shutil
source_folder = "C:\\Users\\shaik\\OneDrive\\Desktop\\Images(source)"
destination_folder = "C:\\Users\\shaik\\OneDrive\\Desktop\\only_jpg(destination)"
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)
for filename in os.listdir(source_folder):
    if filename.lower().endswith(".jpg"):
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)
        shutil.move(source_path, destination_path)
        print(f"Moved: {filename}")
print("All .jpg files moved successfully.")
