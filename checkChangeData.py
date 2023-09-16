# To find the commit history for the first page in Github

import json
import pandas as pd

# Read the JSON file
with open('commit_history.json', 'r') as file:
    data = json.load(file)

# Prepare the data for the Excel file
rows = []
for commit_data in data:
    repository = commit_data['Repository']
    commit_sha = commit_data['Commit SHA']
    changed_files = commit_data['Changed Files']

    requirements_changes = 0
    for changed_file in changed_files:
        if 'requirements.txt' in changed_file:
            requirements_changes += 1

    rows.append({'Project': repository, 'Commits': 1, 'Requirements Changes': requirements_changes})

# Create a pandas DataFrame from the data
df = pd.DataFrame(rows)

# Group by project and aggregate data
df_grouped = df.groupby('Project', as_index=False).agg({'Commits': 'sum', 'Requirements Changes': 'sum'})

# Save the DataFrame to an Excel file
df_grouped.to_excel('output_final.xlsx', index=False)
