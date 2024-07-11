#!/usr/bin/env bash

# Create a virtual environment
python3 -m venv /home/ubuntu/env

# Activate the virtual environment
source /home/ubuntu/env/bin/activate

# Upgrade pip, setuptools, and wheel
pip install --upgrade pip setuptools wheel

# Install dependencies
pip install -r /home/ubuntu/blogprojectdrf/requirements.txt

chmod +x /path/to/your/scripts/python_dependencies.sh
