import os

def count_folders_without_requirements(root_directory, output_file):
    count = 0

    # Open the output file in write mode
    with open(output_file, 'w') as file:
        # Recursively search for folders in the root directory
        for folder_name in os.listdir(root_directory):
            folder_path = os.path.join(root_directory, folder_name)

            # Check if the item is a folder
            if os.path.isdir(folder_path):
                requirements_file = os.path.join(folder_path, 'requirements.txt')

                # Check if requirements.txt file exists in the folder
                if not os.path.isfile(requirements_file):
                    count += 1
                    file.write(f"Missing requirements.txt file in folder: {folder_path}\n")

        file.write(f"Total folders without requirements.txt: {count}\n")

    print(f"Output written to '{output_file}'.")

# Example usage
root_directory = 'C:/Users/Bithy/Desktop/1000 projects'
output_file = 'C:/Users/Bithy/Desktop/missing_requirements.txt'
count_folders_without_requirements(root_directory, output_file)
