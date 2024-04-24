#!/bin/bash

echo "Select and option: "
echo "1 - Start Container"
echo "2 - Remove Container"
echo "3 - Show Logs"
echo "4 - Enter into container"
echo "5 - Clean Docker"
echo "6 - Exit"
read opcion

case $opcion in
  1)
    echo "Create image for the container..."
    # Create a container from the image
    docker build -t apimaestra .

    sleep 5
    
    # Run the container
    echo "Running container..."
    docker run  -d -p 8080:8000 --name apimaestra apimaestra

    sleep 2
    echo "Container running..."
    docker ps -a
    ;;
  2)
    echo "Stoping and remove container ..."
    # Stop the container
    docker stop apimaestra
    sleep 2
    echo "Removing image ..."
    # Remove image
    docker rm apimaestra
    ;;
  3)
    echo "Show container logs ..."
    # Show container logs
    docker logs -f apimaestra
    ;;
  4)
    echo "Enter into container ..."
    # Enter into container
    docker exec -it apimaestra /bin/bash
    ;;
  5)
    echo "Clean Docker ..."
    # Clean Docker
    docker system prune -a
    ;;
  6)
    echo "Exit"
    exit 0
    ;;
  *)
    echo "Invalid option"
    ;;
esac
