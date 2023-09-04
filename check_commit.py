import os
import requests
import subprocess
import shutil
from git import Repo
from importlib.machinery import SourceFileLoader

credentials = SourceFileLoader("credentials", "credentials.py").load_module()
owner = credentials.owner
repo = credentials.repo
branch = credentials.branch
local_repo_path = credentials.local_repo_path
access_token = credentials.access_token

# GitHub repository details
owner = 'AdarshIITDH'
repo = 'CI-CD_Pipeline_Tool'
branch = 'main'

# Paths
local_repo_path = '/home/hero/CI-CD_Pipeline_Tool/'

# # GitHub Personal Access Token
access_token = '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'


# API request headers
headers = {
    'Authorization': f'Bearer {access_token}'
}

# API URL to get latest commit
url = f'https://api.github.com/repos/{owner}/{repo}/branches/{branch}'
response = requests.get(url, headers=headers)

if response.status_code == 200:
    latest_commit_hash = response.json()['commit']['sha']
else:
    print("Error fetching commit hash:", response.text)
    latest_commit_hash = None

# Check if there's a new commit
previous_commit_hash_file = '84d3df4a5fa1e609dfa5a7775522fb427fb4d82'
if os.path.exists(previous_commit_hash_file):
    with open(previous_commit_hash_file, 'r') as file:
        previous_commit_hash = file.read().strip()
else:
    previous_commit_hash = None

if latest_commit_hash and latest_commit_hash != previous_commit_hash:
    print("New commit detected:", latest_commit_hash)
    subprocess.run(["bash","/home/hero/cicdtool/deploy.sh"])

else:
    print("No new commits.")
