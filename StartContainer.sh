#!/bin/bash

echo "Create API Maestra container"
# Create a container from the image
docker build -t apimaestra .

echo "Run API Maestra container"
# Run the container
docker run  -d -p 8080:8000 --name apimaestra apimaestra