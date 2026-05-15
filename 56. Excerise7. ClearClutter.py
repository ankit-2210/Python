# Write a program to clear the clutter inside a folder on your computer. You
# should use os module to rename all the png images from 1.png all the way
# till n.png where n is the number of png files in that folder. Do the same
# for other file formats. For example:

# sfdsf.png --> 1.png
# vfsf.png --> 2.png
# this.png --> 3.png
# design.png --> 4.png
# name.png --> 5.png

import os

folder_name = "MyFiles"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"Folder '{folder_name}' created successfully.")
else:
    print(f"Folder '{folder_name}' already exists.")

sample_files = [
    "sfdsf.png",
    "vfsf.png",
    "this.png",
    "design.png",
    "name.png",
    "abc.jpg",
    "xyz.jpg",
]

for file in sample_files:
    file_path = os.path.join(folder_name, file)
    with open(file_path, "w") as f:
        pass

print("Sample files created.\n")

files = os.listdir(folder_name)
print(files)

counters = {}
for file in files:
    old_path = os.path.join(folder_name, file)
    if os.path.isdir(old_path):
        continue

    name, ext = os.path.splitext(file)
    ext = ext.lower()
    print(ext)

    if ext not in counters:
        counters[ext] = 1

    new_name = f"{counters[ext]}{ext}"
    # print(new_name)
    new_path = os.path.join(folder_name, new_name)
    os.rename(old_path, new_path)

    print(f"{file} --> {new_name}")
    counters[ext] += 1
