import random
import time
from datetime import datetime
from git import Repo
import schedule

# Path to your local repository
# Path to your local repository
REPO_PATH = r"C:\\Users\\Marsh\\Downloads\]github\\long"
REPO = Repo(REPO_PATH)

def make_changes():
    """Make random changes to a file in the repository."""
    filename = "auto_generated.txt"
    content = f"Auto-updated on {datetime.now()}\nRandom number: {random.randint(1, 1000)}"

    with open(filename, "w") as file:
        file.write(content)
    
    return filename

def commit_and_push():
    """Commit and push changes to the repository."""
    filename = make_changes()

    # Stage changes
    REPO.git.add(filename)

    # Commit changes
    REPO.index.commit(f"Auto commit at {datetime.now()}")

    # Push changes
    origin = REPO.remote(name="origin")
    origin.push()

    print(f"Committed and pushed changes to {filename}")

# Schedule the task every 15 minutes
schedule.every(15).minutes.do(commit_and_push)

if __name__ == "__main__":
    print("Starting automation...")
    while True:
        schedule.run_pending()
        time.sleep(1)

def commit_and_push():
    try:
        print("Making changes...")
        filename = make_changes()

        print("Staging changes...")
        REPO.git.add(filename)

        print("Committing changes...")
        REPO.index.commit(f"Auto commit at {datetime.now()}")

        print("Pushing changes...")
        origin = REPO.remote(name="origin")
        origin.push()

        print(f"Successfully committed and pushed changes to {filename}")
    except Exception as e:
        print(f"Error occurred: {e}")

import os 
REPO_PATH = "C:\\Users\\Marsh\\Downloads\\github\\long"

if os.path.exists(REPO_PATH):
    print("path is valid!")
else:
    print("Path is invalid. Please check it.")
