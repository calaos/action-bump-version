#!/usr/bin/python3

import subprocess
import semver
import functools

def semver_compare(a, b):
    if semver.Version.is_valid(a) == False:
        return -1
    verA = semver.Version.parse(a)
    verB = semver.Version.parse(b)
    return verA.compare(verB)

def get_git_tags(repository_path):
    # Get all tags from the repository
    git_tags = subprocess.check_output(['git', 'tag', '-l'], cwd=repository_path).decode().splitlines()

    # Sort the tags using semver.compare function
    sorted_tags = sorted(git_tags, key=functools.cmp_to_key(semver_compare))

    return sorted_tags

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("No repository path given")
        sys.exit(1)

    repository_path = sys.argv[1]
    sorted_tags = get_git_tags(repository_path)

    print(sorted_tags[-1])
