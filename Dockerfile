FROM debian:bookworm-slim

RUN apt -y update && \
    apt -y upgrade && \
    DEBIAN_FRONTEND=noninteractive apt-get -yqq -o DPkg::Options::="--force-confnew" install git grep python3 bash

COPY entrypoint.sh /entrypoint.sh
COPY get-last-version.py /get-last-version.py
COPY bump.py /bump.py

ENTRYPOINT ["/entrypoint.sh"]
