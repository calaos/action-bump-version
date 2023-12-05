#!/bin/sh

set -e

repo='/github/workspace'

git config --global --add safe.directory $repo

git fetch --tags
# This suppress an error occurred when the repository is a complete one.
git fetch --prune --unshallow || true

last_tag='0.0.0'

#get last tag in the shape of semver
cd $repo
for ref in $(git for-each-ref --sort=-creatordate --format '%(refname)' refs/tags); do
    tag="${ref#refs/tags/}"

    # skip if tag starts with a letter
    case "$tag" in
        [a-zA-Z]*)
            continue
            ;;
    esac

    last_tag="${tag}"
    break
done

echo "::notice::Last version: $last_tag"

release=$(pysemver bump "${INPUT_VERSION_FRAGMENT}" "${last_tag}")
echo "::notice::Bumped version: $release"

echo "version_bumped=${release}" >> $GITHUB_OUTPUT
