#!/bin/bash

GITHUB_TOKEN="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"
REPO_OWNER="onlineresultsite"
REPO_NAME="blogprojectdrf"
API_URL="https://api.github.com/repos/$REPO_OWNER/$REPO_NAME/dispatches"
# https://api.github.com/repos/onlineresultsite/blogprojectdrf



curl -X POST -H "Authorization: token $GITHUB_TOKEN" \
     -H "Accept: application/vnd.github.v3+json" \
     --data '{"event_type": "run-pytest"}' \
     $API_URL


# chmod +x scripts/trigger_github_workflow.sh      run manually