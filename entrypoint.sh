#!/bin/sh

set -e

git config --global --add safe.directory /github/workspace

git fetch --tags
# This suppress an error occurred when the repository is a complete one.
git fetch --prune --unshallow || true

last_tag=$(python3 /get_last_tag.py /github/workspace)

release=$(pysemver bump "${INPUT_VERSION_FRAGMENT}" "${last_tag}")
echo "::debug::Bumped version: $release"

echo "version_bumped=${release}" >> $GITHUB_OUTPUT
