import requests
import csv
import json

# Replace with your GitHub token
github_token = "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"

# CSV file path
csv_file_path = "projects_with_requirements1.csv"

# Prepare headers with the authentication token
headers = {
    "Authorization": f"Bearer {github_token}"
}

# Read repository names from the CSV file
repository_names = []
with open(csv_file_path, "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        repository_names.extend(row)

# Base URL for GitHub API
base_url = "https://api.github.com/repos"

num = 0
commit_history = []

# Iterate through repository names
for repo_name in repository_names:
    repo_owner, repo_name = repo_name.split("/")
    num += 1
    print(f"Processing repository {num}/{len(repository_names)}: {repo_owner}/{repo_name}")

    # Get the list of commits for the repository
    commits_url = f"{base_url}/{repo_owner}/{repo_name}/commits"
    response = requests.get(commits_url, headers=headers)
    commits = response.json()

    # Iterate through commits and collect information
    for commit in commits:
        commit_info = {
            "Repository": f"{repo_owner}/{repo_name}",
        }

        if isinstance(commit, dict) and "sha" in commit:
            commit_info["Commit SHA"] = commit["sha"]

            if "commit" in commit and isinstance(commit["commit"], dict) and "committer" in commit["commit"]:
                committer = commit["commit"]["committer"]
                if "date" in committer:
                    commit_info["Commit Date"] = committer["date"]
                else:
                    commit_info["Commit Date"] = "N/A"
            else:
                commit_info["Commit Date"] = "N/A"
        else:
            commit_info["Commit SHA"] = "N/A"
            commit_info["Commit Date"] = "N/A"

        # Fetch commit details to get commit message and changes
        commit_details_url = f"{base_url}/{repo_owner}/{repo_name}/commits/{commit_info['Commit SHA']}"
        commit_details_response = requests.get(commit_details_url, headers=headers)
        commit_details = commit_details_response.json()

        if "commit" in commit_details and "message" in commit_details["commit"]:
            commit_info["Commit Message"] = commit_details["commit"]["message"]
        else:
            commit_info["Commit Message"] = "N/A"

        if "files" in commit_details:
            changed_files = [file_info["filename"] for file_info in commit_details["files"]]
            commit_info["Changed Files"] = changed_files
        else:
            commit_info["Changed Files"] = []

        commit_history.append(commit_info)

    print(f"Processed {len(commits)} commits for {repo_owner}/{repo_name}")

# Save commit history to a JSON file
with open("commit_history.json", "w") as json_file:
    json.dump(commit_history, json_file, indent=4)

print("Commit history saved to commit_history.json")
