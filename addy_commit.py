import os
import subprocess
from datetime import datetime, timedelta
import random

# Configuration
REPO_PATH = os.getcwd()  # Uses current directory
FILENAME = "dummy.txt"
COMMITS_PER_DAY = (1, 5)  # Min and max commits per day for randomness

# Change directory to the repo
os.chdir(REPO_PATH)

# Generate commits for the past year
start_date = datetime.now() - timedelta(days=365)

while start_date < datetime.now():
    num_commits = random.randint(*COMMITS_PER_DAY)  # Random commits per day
    
    for _ in range(num_commits):
        with open(FILENAME, "a") as f:
            f.write(f"Commit on {start_date.strftime('%Y-%m-%d %H:%M:%S')}\n")

        # Add, commit with fake date
        subprocess.run(["git", "add", FILENAME], check=True)
        commit_date = start_date.strftime('%Y-%m-%dT%H:%M:%S')
        subprocess.run(["git", "commit", "--date", commit_date, "-m", f"Commit on {commit_date}"], check=True)
    
    start_date += timedelta(days=1)

# Push changes to GitHub
try:
    subprocess.run(["git", "push", "origin", "main"], check=True)  # Change 'main' if using another branch
    print("✅ Successfully pushed to GitHub!")
except subprocess.CalledProcessError as e:
    print(f"❌ Git push failed: {e}")