FROM alpine:latest

RUN apk add --update --no-cache git grep python3 py3-semver

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
