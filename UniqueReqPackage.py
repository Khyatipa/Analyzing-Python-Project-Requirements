import os
import re
import difflib
import csv


def normalize_package_name(package_name):
    return re.sub(r'[^a-zA-Z]', '', package_name)


def read_package_list(filename):
    with open(filename, 'r') as file:
        return set(normalize_package_name(line.strip().lower()) for line in file)


def compare_package_lists(package_list, requirements):
    unique_to_package_list = package_list - requirements
    unique_to_requirements = requirements - package_list
    common_packages = package_list & requirements  # Calculate common packages
    return unique_to_package_list, unique_to_requirements, common_packages


def find_differences(text1, text2):
    text1_cleaned = [normalize_package_name(package) for package in text1]
    text2_cleaned = [normalize_package_name(package) for package in text2]

    diff = difflib.unified_diff(text1_cleaned, text2_cleaned, fromfile='package_list.txt', tofile='requirements.txt')
    return list(diff)


def main():
    project_directory = 'G:/ReqProject/gitprojects/project'  # Update with your project directory
    output_filename = 'trial.csv'

    with open(output_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Project Path", "Unique to package list", "Unique to requirements", "Common packages"])

        for project in os.listdir(project_directory):
            project_path = os.path.join(project_directory, project)
            package_list_path = os.path.join(project_path, 'package_list.txt')
            requirements_path = os.path.join(project_path, 'requirements.txt')

            if os.path.exists(package_list_path) and os.path.exists(requirements_path):
                package_list = read_package_list(package_list_path)
                requirements = read_package_list(requirements_path)

                unique_to_package_list, unique_to_requirements, common_packages = compare_package_lists(package_list,
                                                                                                        requirements)
                differences = find_differences(package_list, requirements)

                csv_writer.writerow(
                    [project_path, len(unique_to_package_list), len(unique_to_requirements), len(common_packages)])


if __name__ == '__main__':
    main()
