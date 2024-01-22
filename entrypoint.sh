#!/bin/bash -x

set -e

repo='/github/workspace'

git config --global --add safe.directory $repo

git fetch --tags > /dev/null || true
# This suppress an error occurred when the repository is a complete one.
git fetch --prune --unshallow > /dev/null || true

last_tag='0.0.0'

last_tag=$(/mysemver.py $repo)

echo "::notice::Last version: $last_tag"

release=$(pysemver bump "${INPUT_VERSION_FRAGMENT}" "${last_tag}")
echo "::notice::Bumped version: $release"

echo "version_bumped=${release}" >> $GITHUB_OUTPUT
