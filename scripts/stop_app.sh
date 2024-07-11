#!/bin/bash
# Script to stop the application
echo "Stopping application..."
sudo systemctl stop gunicorn
chmod +x /home/ubuntu/blogprojectdrf/scripts/*.sh