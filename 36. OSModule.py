# The os module in Python is a build-in library that provides functions for interacting with
# the operating system. It allows you to perform a wide variety of task, such as reading and wrting fies, interacting
# with the file system and running system commands.

import os

# f =os.open("myfile.txt")
if not os.path.exists("data"):
    os.mkdir("data")

# for i in range(0, 5):
# os.mkdir(f"data/Day{i+1}")

folders = os.listdir("data")
print(folders)
