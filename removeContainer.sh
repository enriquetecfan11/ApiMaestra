#!/bin/bash

echo "Stop API Maestra container"
# Stop the container
docker stop apimaestra

echo "Remove API Maestra container"
# Remove image
docker rm apimaestra
