#!/usr/bin/python3

import subprocess
import functools
import argparse
import sys

def dpkg_compare(a, b):
    #replace - with ~ to make dpkg compare versions correctly
    a = a.replace('-', '~')
    b = b.replace('-', '~')
    #remove the v prefix if any
    if a.startswith('v'):
        a = a[1:]
    if b.startswith('v'):
        b = b[1:]
    
    ret = subprocess.run(['dpkg', '--compare-versions', a, 'lt', b]).returncode
    if ret == 0:
        return -1
    else:
        return 1

def get_git_tags(repository_path):
    # Get all tags from the repository
    git_tags = subprocess.check_output(['git', 'tag', '-l'], cwd=repository_path).decode().splitlines()

    return git_tags

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="Path to the file containing versions. If not provided, the tags are taken from git tag.")
    parser.add_argument("--repo", help="Repository path")
    parser.add_argument("--debug", action='store_true', help="Print debug information")
    args = parser.parse_args()

    if args.file:
        with open(args.file, 'r') as file:
            tags = file.read().splitlines()
            
        #tranform the tags to remove the prefix 'latest:' if any
        tags = [tag.split(':')[-1] for tag in tags]        
    else:
        tags = get_git_tags(args.repo)

    sorted_tags = sorted(tags, key=functools.cmp_to_key(dpkg_compare))
    
    if args.debug:
        print(sorted_tags)
        print(f'\nLast version is: {sorted_tags[-1]}')
    else:
        print(sorted_tags[-1])
