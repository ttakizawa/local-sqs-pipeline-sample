FROM python:3.8-bullseye

# update and install library
RUN apt-get update && \
    apt-get install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

WORKDIR /src
COPY . .
RUN pip3 install -r requirements.txt