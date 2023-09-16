import csv

def read_csv_column(file_path, column_index):
    data = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header row
        for row in csv_reader:
            if len(row) > column_index:
                cell_data = row[column_index]
                cleaned_data = cell_data.split("=")[0]  # Remove everything after the "=" character
                data.append(cleaned_data)
    return data

def compare_values(data):
    different_values = set(data)
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if data[i] == data[j]:
                different_values.discard(data[i])
                different_values.discard(data[j])
    return different_values

def get_values_from_other_column(file_path, column_index, different_values, target_column_index):
    values = {}
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header row
        for row in csv_reader:
            if len(row) > column_index:
                cell_data = row[column_index]
                cleaned_data = cell_data.split("=")[0]  # Remove everything after the "=" character
                if cleaned_data in different_values:
                    target_value = row[target_column_index]
                    values[cleaned_data] = target_value
    return values

# Example usage
file_path = 'C:/Users/Bithy/Desktop/gitprojects/project/005/highlight_diff.csv'
column_index = 2  # Index of the column (0-based index)
target_column_index = 1  # Index of the target column (0-based index)

column_data = read_csv_column(file_path, column_index)
different_values = compare_values(column_data)
values_from_target_column = get_values_from_other_column(file_path, column_index, different_values, target_column_index)

if len(different_values) == 0:
    print("All values in the column are the same.")
else:
    print("Values in the column that are different:")
    for value in different_values:
        print("Different value:", value)
        if value in values_from_target_column:
            print("Corresponding value from target column:", values_from_target_column[value])
        print()
