import difflib
import csv
import os

def compare_text_files(folder_path):
    package_list_file = os.path.join(folder_path, 'Oldrequirments.txt')
    requirements_file = os.path.join(folder_path, 'requirements.txt')
    output_file = os.path.join(folder_path, 'highlight_diff.csv')

    # Check if the files exist
    if not os.path.isfile(package_list_file):
        print(f"Error: '{package_list_file}' does not exist.")
        return

    if not os.path.isfile(requirements_file):
        print(f"Error: '{requirements_file}' does not exist.")
        return

    # Read the contents of the files
    with open(package_list_file, 'r') as file1:
        package_list = file1.readlines()

    with open(requirements_file, 'r') as file2:
        requirements = file2.readlines()

    # Compare the files
    differ = difflib.Differ()
    diff_lines = list(differ.compare(package_list, requirements))

    # Prepare the differences as rows in a CSV file
    diff_rows = [['Line', 'Type', 'Package Name']]
    for line in diff_lines:
        diff_type = 'Existing package' if line.startswith('-') else 'Generated package' if line.startswith('+') else ''
        diff_text = line[2:].strip().replace('-', '') if line.startswith('-') else line[2:].strip().replace('+', '')
        diff_rows.append([line[1:].strip(), diff_type, diff_text])

    # Write the differences to a CSV file
    with open(output_file, 'w', newline='') as output:
        writer = csv.writer(output)
        writer.writerows(diff_rows)

    print(f"Differences written to '{output_file}'.")

# Example usage
parent_folder = input("Enter the parent folder path: ")
project_folders = os.listdir(parent_folder)

for project_folder in project_folders:
    project_path = os.path.join(parent_folder, project_folder)
    compare_text_files(project_path)
