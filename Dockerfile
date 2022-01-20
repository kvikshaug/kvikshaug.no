FROM python:3.10-slim
ENV PYTHONUNBUFFERED=1

ENV TZ=Europe/Copenhagen
RUN ln -sf /usr/share/zoneinfo/Europe/Copenhagen /etc/localtime

ENV USER=user
RUN useradd --system --no-create-home --user-group ${USER}

ARG CWD="/app"
WORKDIR "${CWD}"
ENV PYTHONPATH="${CWD}/src"
EXPOSE 8000

COPY requirements.txt ./requirements.txt
RUN \
  apt-get update && \
  apt-get install -y --no-install-recommends npm && \
  npm install -g sass @babel/core @babel/cli babel-preset-minify && \
  apt-get autoremove -y && \
  rm -rf /var/lib/apt/lists/* && \
  pip install --upgrade pip setuptools pip-tools && \
  pip-sync requirements.txt

COPY . "${CWD}/"
RUN chown -R "${USER}:${USER}" "${CWD}"
