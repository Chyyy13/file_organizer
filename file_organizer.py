import os
import shutil

#PATH (important!)
path = "C:/Users/Patricia/samplesystem"

# Loop through files
for file in os.listdir(path):

    full_path = os.path.join(path, file)

    # Skip folders
    if os.path.isdir(full_path):
        continue

    # Images
    if file.endswith((".jpg", ".png", ".jpeg")):
        os.makedirs(path + "/Images", exist_ok=True)
        shutil.move(full_path, path + "/Images/" + file)

    # Documents
    elif file.endswith((".pdf", ".docx", ".txt")):
        os.makedirs(path + "/Documents", exist_ok=True)
        shutil.move(full_path, path + "/Documents/" + file)

    # Videos
    elif file.endswith((".mp4", ".mkv")):
        os.makedirs(path + "/Videos", exist_ok=True)
        shutil.move(full_path, path + "/Videos/" + file)

print("Files Organized Successfully!")