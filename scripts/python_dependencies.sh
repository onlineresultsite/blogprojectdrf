#!/usr/bin/env bash


# Exit immediately if a command exits with a non-zero status.
set -e

# Update pip and setuptools
pip install --upgrade pip setuptools wheel

# Install necessary build tools and libraries
sudo apt-get update
sudo apt-get install -y build-essential python3-dev libjpeg-dev zlib1g-dev

# Install precompiled wheels for Pillow and ruamel.yaml
pip install Pillow==8.4.0 ruamel.yaml==0.17.21

# Install other requirements
pip install -r /home/ubuntu/blogprojectdrf/requirements.txt
virtualenv /home/ubuntu/env
source /home/ubuntu/env/bin/activate
pip install -r /home/ubuntu/blogprojectdrf/requirements.txt
chmod +x /home/ubuntu/blogprojectdrf/scripts/*.sh