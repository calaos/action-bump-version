#!/usr/bin/python3
import sys

def increment_version(actual_version, fragment):
    major, minor, patch = actual_version.split('.')

    if fragment == 'prerelease':
        if int(minor) % 2 == 0:
            minor = str(int(minor) + 1)
            patch = '0'
        else:
            patch = str(int(patch) + 1)

    elif fragment == 'major':
        minor = '0'
        patch = '0'

    elif fragment == 'minor':
        if int(minor) % 2 == 0:
            minor = str(int(minor) + 2)
        else:
            minor = str(int(minor) + 1)
            patch = '0'

    new_version = f"{major}.{minor}.{patch}"
    return new_version

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python bump.py <actual_version> <fragment>")
        sys.exit(1)

    actual_version = sys.argv[1]
    if not actual_version:
        print("actual_version is empty. Please provide a valid actual_version.")
        sys.exit(1)

    fragment = sys.argv[2] if len(sys.argv) > 2 else 'prerelease'

    #revomve the v prefix if any
    if actual_version.startswith('v'):
        actual_version = actual_version[1:]
    
    #remove anything after - if any
    actual_version = actual_version.split('-')[0]

    new_version = increment_version(actual_version, fragment)
    print(new_version)
