#!/bin/bash

# Activate the virtual environment
source /home/ubuntu/env/bin/activate

# Navigate to the project directory
cd /home/ubuntu/blogprojectdrf

# Install any additional dependencies if necessary
pip install pytest pytest-django selenium

# Set the DJANGO_SETTINGS_MODULE environment variable
export DJANGO_SETTINGS_MODULE=ecomapp.settings

# Run tests
pytest /home/ubuntu/blogprojectdrf/ecomapp/tests/test_login.py --maxfail=1 --disable-warnings -v

# Deactivate the virtual environment
deactivate
