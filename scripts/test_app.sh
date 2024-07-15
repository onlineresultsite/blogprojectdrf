#!/bin/bash

# Activate the virtual environment
source /home/ubuntu/env/bin/activate

cd /home/ubuntu/blogprojectdrf

# Install any additional dependencies if necessary
pip install pytest pytest-django selenium

chmod +x /home/ubuntu/blogprojectdrf/scripts/test_app.sh

export DJANGO_SETTINGS_MODULE=ecomapp.settings
# Run tests
pytest /home/ubuntu/blogprojectdrf/ecomapp/tests/test_login.py
