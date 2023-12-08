FROM ubuntu:20.04

LABEL maintainer="Marti2203 <mmirchev@comp.nus.edu.sg>"

#############################################################################
# Requirements
#############################################################################

RUN \
  apt-get update -y && \
  apt-get install software-properties-common -y && \
  apt-get update -y && \
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
        python3-pip \
                && \
  rm -rf /var/lib/apt/lists/*

# Java version
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64

# Timezone
ENV TZ=America/Los_Angeles
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /

RUN git clone https://github.com/nus-apr/bears-benchmark 
