#!/bin/bash

for file in test_tags_*
do
    echo "Using test file: $file"
    last_version=$(< "$file" grep 'latest' | cut -d':' -f2)
    python3 get-last-version.py --file "$file" --debug
    echo "Last version should be: $last_version"
    echo
done

function bump()
{
    v=$1
    echo "Version: $v"
    python3 bump.py "$v" major
    python3 bump.py "$v" minor
    python3 bump.py "$v" patch
    python3 bump.py "$v" prerelease
}

bump "1.0.0"
bump "1.5.6"
bump "4.2.0~dev.0"
bump "1.0.0~dev.1"
bump "1.0.0-rc.1"
bump "1.4.1-dev.0"
