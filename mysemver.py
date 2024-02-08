#!/usr/bin/python3

import subprocess
import semver
import functools

def get_git_tags(repository_path):
    # Get all tags from the repository
    git_tags = subprocess.check_output(['git', 'tag', '-l'], cwd=repository_path).decode().splitlines()

    # Sort the tags using dpkg --compare-versions command
    sorted_tags = sorted(git_tags, key=lambda x: subprocess.check_output(['dpkg', '--compare-versions', x, 'lt', git_tags[-1]]).decode().strip() == '-1')

    return sorted_tags

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("No repository path given")
        sys.exit(1)

    repository_path = sys.argv[1]
    sorted_tags = get_git_tags(repository_path)

    print(sorted_tags[-1])
