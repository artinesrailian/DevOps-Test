#!/bin/bash
set -x

# Variables
GITHUB_REPO="artinesrailian/DevOps-Test"
RELEASE_VERSION="1.0.$BUILD_NUMBER"
RELEASE_NAME="DevOps-Test-$RELEASE_VERSION"
RELEASE_NOTES="Release notes for version $RELEASE_VERSION"
ARTIFACT_PATH="DevOps-test.tar.gz"
GITHUB_TOKEN="$GITHUB_TOKEN"

# Create Release
curl --request POST \
  --url "https://api.github.com/repos/$GITHUB_REPO/releases" \
  --header "Authorization: token $GITHUB_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
    "tag_name": "'"$RELEASE_VERSION"'",
    "target_commitish": "master",
    "name": "'"$RELEASE_NAME"'",
    "body": "'"$RELEASE_NOTES"'",
    "draft": false,
    "prerelease": false
}'

# Upload Asset
upload_url=$(curl --request GET \
  --url "https://api.github.com/repos/$GITHUB_REPO/releases/latest" \
  --header "Authorization: token $GITHUB_TOKEN" \
  | grep "upload_url" | cut -d'"' -f4)
upload_url=${upload_url%\{?name,label\}}
filename=$(basename "$ARTIFACT_PATH")

curl --request POST \
  --url "$upload_url?name=$filename" \
  --header "Authorization: token $GITHUB_TOKEN" \
  --header "Content-Type: application/zip" \
  --data-binary @"$ARTIFACT_PATH"
