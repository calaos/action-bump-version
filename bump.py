#!/usr/bin/python3
import sys

def increment_version(actual_version, fragment):
    if '~' in actual_version:
        ver, pre = actual_version.split('~')
    else:
        ver = actual_version
        pre = None
        
    major, minor, patch = ver.split('.')
    
    if fragment == 'prerelease':
        if pre is None:
            pre = 'dev.0'
            patch = str(int(patch) + 1)
        else:
            pre = pre.split('.')
            pre[1] = str(int(pre[1]) + 1)
            pre = '.'.join(pre)
            
        return f"{major}.{minor}.{patch}~{pre}"
        
    elif fragment == 'major':
        return f"{int(major) + 1}.0.0"
        
    elif fragment == 'minor':
        return f"{major}.{int(minor) + 1}.0"

    elif fragment == 'patch':
        return f"{major}.{minor}.{int(patch) + 1}"
    
    return None


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python bump.py <actual_version> <fragment>")
        sys.exit(1)

    actual_version = sys.argv[1]
    if not actual_version:
        print("actual_version is empty. Please provide a valid actual_version.")
        sys.exit(1)

    fragment = sys.argv[2] if len(sys.argv) > 2 else 'prerelease'

    #remove the v prefix if any
    if actual_version.startswith('v'):
        actual_version = actual_version[1:]
        
    actual_version = actual_version.replace('-', '~')

    new_version = increment_version(actual_version, fragment)
    print(new_version)
