#!docker
FROM amd64/ubuntu
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update
RUN apt-get install build-essential cmake python3 python3-pip python-is-python3 git pkg-config \
libasound2-dev libjack-jackd2-dev \
ladspa-sdk \
libcurl4-openssl-dev  \
libfreetype6-dev \
libx11-dev libxcomposite-dev libxcursor-dev libxcursor-dev libxext-dev libxinerama-dev libxrandr-dev libxrender-dev \
libwebkit2gtk-4.0-dev \
libglu1-mesa-dev mesa-common-dev \
--no-install-recommends -yqq
RUN which python
RUN pip3 install conan
