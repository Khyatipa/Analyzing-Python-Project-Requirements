import csv
import requests
import time
import json
import pandas as pd

csv_file = "projects_with_requirements1.csv"
outputFile = ""
# Replace with your GitHub token
key1 = "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"
key2 = "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"
key3 = "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"
key4 = "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"
key5 = "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"

github_token = key1

# Define the file path you want to check for modifications
file_path = "requirements.txt"

# Prepare headers with the authentication token

def fetch_all_commits(repo_owner, repo_name):
    base_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits"

    all_commits = []
    page = 1
    per_page = 100  # You can adjust this value based on your needs

    global github_token

    while True:
        try:
            response = requests.get(base_url, headers={"Authorization": f"Bearer {github_token}"}, params={"page": page, "per_page": per_page}, timeout=30)
            
            # Check for rate limit exceeded
            if response.status_code == 403:
                print("Rate limit exceeded.Changing token")
                if(github_token==key1):
                    github_token=key2
                elif(github_token==key2):
                    github_token=key3
                elif(github_token==key3):
                    github_token=key4
                elif(github_token==key4):
                    github_token=key5
                else:
                    github_token=key1
                continue

            response.raise_for_status()

            commits = response.json()

            if not commits:
                break

            all_commits.extend(commits)
            page += 1
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            break
        except requests.exceptions.RequestException as req_err:
            print(f"Request error occurred: {req_err}")
            break

    return all_commits

with open(csv_file, 'r') as file:
    csv_reader = csv.reader(file)
    row = next(csv_reader)  # Read the first row

revisions = []
repo_revisions = []

outputCSV = 'output_temp.csv'

indexNum = 1
# for column in row:
for column in row[]:
    repo_owner, repo_name = column.split('/')

    all_commits = fetch_all_commits(repo_owner, repo_name)

    num = 0
        
    # Iterate through all commits to find changes to the requirements.txt file
    print("Total commits ", len(all_commits)," -- ",repo_owner+"/"+repo_name)

    for commit in all_commits:
        commit_sha = commit["sha"]
        commit_date = commit["commit"]["committer"]["date"]

        # Get the details of the specific file in the commit
        commit_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits/{commit_sha}"
        commit_response = requests.get(commit_url, headers={"Authorization": f"Bearer {github_token}"})
        commit_data = commit_response.json()

        # Check if the key 'files' exists in commit_data dictionary
        if "files" in commit_data:
            # Check if the file exists in the commit and if its content has changed
            for file in commit_data.get("files", []):
                if file.get("filename") == file_path and file.get("status") == "modified":
                    num += 1

                    repo_revision = {
                        "Commit Date": commit_date,
                        "Commit SHA": commit_sha,
                        "File Status": file.get("status"),
                        "File Patch": file.get("patch", "Patch not available")
                    }
                    repo_revisions.append(repo_revision)
                    
        revisions.append({
            "Repository": f"{repo_owner}/{repo_name}",
            "Revisions": repo_revisions
        })

    print("Changed req ", num)
    with open(outputCSV, 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([indexNum,repo_owner+"/"+repo_name, len(all_commits),num])
        indexNum+=1

# Save the revisions data to a JSON file
output_file_path = "revisions_final.json"
with open(output_file_path, "w") as json_file:
    json.dump(revisions, json_file, indent=4)

print("Data saved to revisions_final.json")
