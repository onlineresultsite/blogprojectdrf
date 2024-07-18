#!/bin/bash

# Navigate to your app directory
cd /your-app-directory

# Set up Python environment
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install selenium

# Run tests
pytest tests/test_login.py

# Upload test report to S3 (optional)
aws s3 cp report.html s3://your-s3-bucket/report.html
