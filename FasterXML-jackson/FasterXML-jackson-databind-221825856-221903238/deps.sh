#!/bin/bash

# Update system and install necessary packages
apt-get update -y
apt-get install -y software-properties-common
apt-get update -y
apt-get install -y openjdk-8-jdk \
                        git \
                        build-essential \
                        subversion \
                        perl \
                        curl \
                        maven \
                        gradle \
                        ant \
                        unzip \
                        cpanminus \
                        make \
                        python3 \
                        python3-pip

# Clean up APT caches to free space
sudo rm -rf /var/lib/apt/lists/*

# Set Java environment variable
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
export TZ=America/Los_Angeles

cd /

# Clone necessary repositories
git clone https://github.com/nus-apr/bears-benchmark
