#!/bin/bash

for file in test_tags_*
do
    echo "Using test file: $file"
    last_version=$(< "$file" grep 'latest' | cut -d':' -f2)
    python3 get-last-version.py --file "$file" --debug
    echo "Last version should be: $last_version"
    echo
done
