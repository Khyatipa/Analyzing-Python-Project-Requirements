import subprocess
import shutil

# Specify the path to the directory containing the project files
project_directory = "Github_Project\zemlanin_Libr"  # Replace with the actual path

# Change the working directory to the project directory
subprocess.run(["cd", project_directory], shell=True)

# Generate requirements.txt using pipreqs
subprocess.run(["pipreqs", "."])

# Move requirements.txt to pipreqsReq.txt
shutil.move("requirements.txt", "pipreqsReq.txt")

# Generate requirements.txt using pip freeze
pipfreeze_output = subprocess.check_output(["pip", "freeze"]).decode("utf-8")
with open("pipfreezeReq.txt", "w") as file:
    file.write(pipfreeze_output)

print("requirements.txt files created successfully.")
