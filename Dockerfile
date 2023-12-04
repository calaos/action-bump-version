FROM alpine:latest

RUN apk add --update --no-cache git grep python3 py3-semver py3-gitpython

COPY entrypoint.sh /entrypoint.sh
COPY get_last_tag.py /get_last_tag.py

ENTRYPOINT ["/entrypoint.sh"]
