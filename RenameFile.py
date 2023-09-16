import os

# Specify the directory path where the file exists
directory_path = "C:/Users/Bithy/Desktop/Project/infinigen-main/0"

# Specify the file name to be renamed
old_file_name = "requirements.txt"

# Specify the new file name
new_file_name = "Oldrequirments.txt"

# Get the full paths for the old and new file names
old_file_path = os.path.join(directory_path, old_file_name)
new_file_path = os.path.join(directory_path, new_file_name)

# Rename the file
os.rename(old_file_path, new_file_path)
