#!/bin/bash
#!/bin/bash
#!/bin/bash
echo "Starting test_app.sh" >> /home/ubuntu/deploy.log
#!/bin/bash

# Ensure the script is being run
echo "Starting test_app.sh" | tee -a /home/ubuntu/deploy.log

# Check current user
echo "Running as user: $(whoami)" | tee -a /home/ubuntu/deploy.log

# Run the health check
if curl -f http://localhost/health-check; then
  echo "Health check passed" | tee -a /home/ubuntu/deploy.log
else
  echo "Health check failed" | tee -a /home/ubuntu/deploy.log
  exit 1
fi

# Ensure the script finished
echo "Finished test_app.sh" | tee -a /home/ubuntu/deploy.log


# Navigate to the project directory
# cd /home/ubuntu/blogprojectdrf
# echo "start test cases"
# # Activate the virtual environment
# source /home/ubuntu/env/bin/activate

# # Run pytest to execute your tests and generate a report
# pytest /home/ubuntu/blogprojectdrf/ecomapp/tests/test_login.py --html=report.html --self-contained-html --maxfail=1 --disable-warnings > result.log 2>&1

# # Check for failures and notify if needed
# if grep -q "ERROR" result.log || grep -q "FAILED" result.log; then
#     echo "Tests failed. Check the report at report.html and result.log for details."
#     exit 1
# else
#     echo "All tests passed."
#     exit 0
# fi
