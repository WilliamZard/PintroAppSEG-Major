# Graph API

## Developing
__Requirements__
 * Docker installed locally
 * Neo4j database credentials(ask Giulio or Seb for now)
 * Nothing else!
#TODO: update README with new setup
 __To run container locally__
 1) Open your command line and cd into graph/graph_api directory
 2) Build the Docker Image by running: `docker build .. -t graph_api`
    * Note you must be in graph/graph_api directory
    * This builds the Docker image and gives it a name "graph_api"
 3) Run the Docker Image with: ``docker run --rm -it -v `pwd`:/graph_api -p 5000:5000 graph_api``
    * This creates a Docker Container based on the image we just built.
    * `--rm` cleans up and removes the Container's filesystem when you stop using it. This stop your computer from getting clogged up.
    * `-it`makes this an interactive process. This means you can see the output of the Docker container as it's running.
    * The `-v`flag and subsequent arguments mount your working directory(graph_api/) with the Docker container's own working directory. This means that any changes you make to your code will be instantly reflected in the Docker container, and thus in the application your container is running.
    * `-p 5000:5000` binds the container and host machine's port 5000. So the host machine can send requests to the container and receive responses.
 4) Now you have your application running in a completely isolated docker container that could be used for development, as well as deployment on any number of machines.
