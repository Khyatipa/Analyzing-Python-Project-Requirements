import os
import subprocess

# Specify the directory path where the folders exist
directory_path = "C:/Users/Bithy/Desktop/1000 projects"

# Iterate over all subdirectories in the directory path
for root, dirs, files in os.walk(directory_path):
    # Check if there are Python files in the current directory
    python_files = [file for file in files if file.endswith(".py")]
    if python_files:
        # Change the current working directory to the root of the current subdirectory
        os.chdir(root)

        # Run pipreqs command to generate requirements.txt for the current subdirectory
        subprocess.run(["pipreqs", ".", "--force"])

        # Print a message indicating the generation of requirements.txt for the current subdirectory
        print(f"Generated requirements.txt for {root}")
