import csv
import pandas as pd

def get_projects_from_error_log(file_path):
    projects = []
    with open(file_path, 'r') as error_log_file:
        for line in error_log_file:
            if line.startswith("0x"):
                project_name = line.strip().split(": ", 1)[0]
                projects.append(project_name)
    return projects

def parse_error_log(file_path):
    errors_count = {}
    with open(file_path, 'r') as error_log_file:
        for line in error_log_file:
            if line.startswith("0x"):
                # Assuming project name is the part before the first colon (:) and error type is the part after the last colon (:)
                project_name, error_type = line.strip().split(": ", 1)
            elif "Error" in line:
                # If the line contains "Error," consider it as the error type
                error_type = line.strip()
                if error_type in errors_count:
                    errors_count[error_type] += 1
                else:
                    errors_count[error_type] = 1

    return errors_count

def write_to_excel(errors_count, output_file):
    data = {
        'Error Name': list(errors_count.keys()),
        'Count': list(errors_count.values())
    }
    df = pd.DataFrame(data)
    df.to_excel(output_file, index=False)

if __name__ == "__main__":
    error_log_file_path = "error_log.txt"
    output_excel_file = "error_report.xlsx"

    errors_count = parse_error_log(error_log_file_path)
    write_to_excel(errors_count, output_excel_file)

    all_projects = get_projects_from_error_log(error_log_file_path)
    print("List of all projects in the error log:")
    print(all_projects)
    