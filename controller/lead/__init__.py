import subprocess

def get_commits_in_tag(tag_name, previous_tag=None):
    """
    Get a list of commits for a specific tag.
    If previous_tag is given, returns only commits between previous_tag and tag_name.
    """
    try:
        if previous_tag:
            cmd = ["git", "log", "--oneline", f"{previous_tag}..{tag_name}"]
        else:
            cmd = ["git", "log", "--oneline", tag_name]

        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        commits = result.stdout.strip().split("\n") if result.stdout else []
        return commits

    except subprocess.CalledProcessError as e:
        print(f"Error runn

