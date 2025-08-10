if __name__ == "__main__":
    # Example usage
    tag = "v1.0.0"  # Change to your tag name
    previous_tag = "v0.9.0"  # Optional

    commits = get_commits_in_tag(tag, previous_tag)
    print(f"Commits in {tag}:" if not previous_tag else f"Commits between {previous_tag} and {tag}:")
    for commit in commits:
        print(commit)
