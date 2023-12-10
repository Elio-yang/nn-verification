# Use the official Ubuntu 20.04 image
FROM ubuntu:20.04

# Install necessary packages
RUN apt-get update && \
    apt-get install -y \
    wget \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install Anaconda
RUN wget https://repo.anaconda.com/archive/Anaconda3-2021.05-Linux-x86_64.sh -O /tmp/anaconda.sh && \
    /bin/bash /tmp/anaconda.sh -b -p /opt/conda && \
    rm /tmp/anaconda.sh

# Add Anaconda to the PATH
ENV PATH="/opt/conda/bin:${PATH}"

# Create a Conda virtual environment named fenv with Python 3.8
RUN conda create -y --name fenv python=3.8

# Set the default conda environment to fenv
RUN echo "conda activate fenv" >> /root/.bashrc

# Set the working directory to /home
WORKDIR /home

# Clone the repository from GitHub
RUN git clone https://github.com/Elio-yang/nn-verification.git
