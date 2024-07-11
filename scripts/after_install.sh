echo "Pull Finished"

# Test Nginx configuration before reloading
sudo nginx -t
if [ $? -ne 0 ]; then
  echo "Nginx configuration error. Aborting."
  exit 1
fi

# Reload systemd manager configuration
sudo systemctl daemon-reload
if [ $? -ne 0 ]; then
  echo "Systemctl daemon-reload failed. Aborting."
  exit 1
fi

# Restart Nginx
sudo systemctl restart nginx
if [ $? -ne 0 ]; then
  echo "Failed to restart Nginx. Aborting."
  exit 1
fi

echo "Deployment successful"
