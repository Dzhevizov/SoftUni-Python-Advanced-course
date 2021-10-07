import os
file_path = "some_file.txt"

if os.path.exists(file_path):
    os.remove(file_path)
else:
    print("File already deleted!")
