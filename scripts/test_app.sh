#!/bin/bash

# Navigate to the project directory
cd /home/ubuntu/blogprojectdrf
# Activate the virtual environment
source /home/ubuntu/env/bin/activate

# Run pytest to execute your tests and generate a report
pytest --html=report.html --self-contained-html --maxfail=1 --disable-warnings > result.log

# Optionally, print the result to the console
cat result.log

# Check for failures and notify if needed
if grep -q "FAILURES" result.log; then
    echo "Tests failed. Check the report at report.html for details."
    exit 1
else
    echo "All tests passed."
    exit 0
fi
# # Install any additional dependencies if necessary
# pip install pytest pytest-django selenium

# # Set the DJANGO_SETTINGS_MODULE environment variable
# export DJANGO_SETTINGS_MODULE=ecomapp.settings

# # Run tests
# pytest /home/ubuntu/blogprojectdrf/ecomapp/tests/test_login.py --maxfail=1 --disable-warnings -v

# # Deactivate the virtual environment
# deactivate
