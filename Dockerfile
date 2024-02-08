FROM debian:bookworm-slim

RUN apt -y update && \
    apt -y upgrade && \
    DEBIAN_FRONTEND=noninteractive apt-get -yqq -o DPkg::Options::="--force-confnew" install git grep python3 python3-semver bash

COPY entrypoint.sh /entrypoint.sh
COPY mysemver.py /mysemver.py
COPY bump.py /bump.py

ENTRYPOINT ["/entrypoint.sh"]
