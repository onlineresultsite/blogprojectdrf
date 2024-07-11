#!/usr/bin/env bash

#!/bin/bash

# Update pip and setuptools
pip install --upgrade pip setuptools

# Install necessary build tools and libraries
sudo apt-get update
sudo apt-get install -y build-essential python3-dev libjpeg-dev zlib1g-dev

# Install precompiled wheels for Pillow and ruamel.yaml
pip install Pillow==8.4.0 ruamel.yaml==0.17.21

# Verify installation
if [ $? -ne 0 ]; then
  echo "Failed to install dependencies."
  exit 1
fi

echo "Dependencies installed successfully."


virtualenv /home/ubuntu/env
source /home/ubuntu/env/bin/activate
pip install -r /home/ubuntu/blogprojectdrf/requirements.txt