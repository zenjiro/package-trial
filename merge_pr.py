import os
import subprocess
import json

# Get the GitHub token from the environment
token = subprocess.check_output("gh auth token", shell=True).decode().strip()

# Set up the curl command to merge the PR
curl_command = f'''
curl -X PUT \\
  -H "Authorization: token {token}" \\
  -H "Accept: application/vnd.github.v3+json" \\
  https://api.github.com/repos/zenjiro/package-trial/pulls/8/merge \\
  -d '{{"commit_title": "Merge PR #8: Update Python Version Requirement to 3.10+", "commit_message": "Update Python version requirement from 3.8+ to 3.10+ and add Python 3.13 support", "merge_method": "squash"}}'
'''

# Execute the curl command
print("Attempting to merge PR #8...")
result = subprocess.run(curl_command, shell=True, capture_output=True)

# Print the result
print(f"Status code: {result.returncode}")
print(f"Output: {result.stdout.decode()}")
print(f"Error: {result.stderr.decode()}")