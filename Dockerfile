FROM alpine:latest

ENV TZ=Europe/Copenhagen
RUN ln -sf /usr/share/zoneinfo/Europe/Copenhagen /etc/localtime
WORKDIR "/app"

RUN \
  apk add --no-cache npm && \
  npm install -g sass @babel/core @babel/cli babel-preset-minify
