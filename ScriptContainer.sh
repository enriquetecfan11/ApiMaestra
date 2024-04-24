#!/bin/bash

echo "Select and option: "
echo "1 - Start Cotainer"
echo "2 - Remove Container"
echo "3 - Show Logs"
ecjo "4 - Exit"
read opcion

case $opcion in
  1)
    echo "Starting container..."
    # Create a container from the image
    docker build -t apimaestra .
    # Run the container
    docker run  -d -p 8080:8000 --name apimaestra apimaestra
    ;;
  2)
    echo "Stoping and remove container ..."
    # Stop the container
    docker stop apimaestra
    # Remove image
    docker rm apimaestra
    ;;
  3)
    echo "Show container logs ..."
    # Show container logs
    docker logs -f apimaestra
    ;;
  4)
    echo "Exit"
    ;;
  *)
    echo "Invalid option"
    ;;
esac
