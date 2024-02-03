FROM alpine:latest

RUN apk add --update --no-cache git grep python3 py3-semver bash

COPY entrypoint.sh /entrypoint.sh
COPY mysemver.py /mysemver.py
COPY bump.py /bump.py

ENTRYPOINT ["/entrypoint.sh"]
