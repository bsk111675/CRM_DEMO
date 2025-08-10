import subprocess

def get_previous_tag(current_tag):
    """Find the tag that comes before the given tag in history."""
    try:
        cmd = ["git", "describe", "--tags", "--abbrev=0", f"{current_tag}^"]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return None

def get_commits_between_tags(old_tag, new_tag):
    """Get commit messages between two tags."""
    cmd = ["git", "log"]()

