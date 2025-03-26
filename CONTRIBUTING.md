# CONTRIBUTING

## HOW TO RUN THE DOCKERFILE LOCALLY


...
docker run -dp 5005:5000 -w /app -v "${pwd}:/app" --name CONTAINER_NAME IMAGE_NAME sh -c "flask run"
...