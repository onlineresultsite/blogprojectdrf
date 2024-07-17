#!/bin/bash

# Navigate to the project directory
cd /home/ubuntu/blogprojectdrf
echo "start test cases"
# Activate the virtual environment
source /home/ubuntu/env/bin/activate

# Run pytest to execute your tests and generate a report
pytest /home/ubuntu/blogprojectdrf/ecomapp/tests/test_login.py --html=report.html --self-contained-html --maxfail=1 --disable-warnings > result.log 2>&1

# Check for failures and notify if needed
if grep -q "ERROR" result.log || grep -q "FAILED" result.log; then
    echo "Tests failed. Check the report at report.html and result.log for details."
    exit 1
else
    echo "All tests passed."
    exit 0
fi
