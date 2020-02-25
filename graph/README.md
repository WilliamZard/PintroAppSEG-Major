# Graph API

## Developing
__Requirements__
 * Docker installed locally
 * Nothing else!

 __To run container locally__
 1) Open your command line and cd into graph directory
 2) Build the Docker Image for development by running: `docker build -f dev.Dockerfile -t graph_api:dev .`
    * Note you must be in graph directory
    * This builds the Docker image and gives it a name "graph_api" and tag "dev"
 3) Run the Docker Image with: ``docker run --rm -it -v `pwd`:/graph_api -p 8080:8080 graph_api:dev``
    * This creates a Docker Container based on the image we just built.
    * `--rm` cleans up and removes the Container's filesystem when you stop using it. This stop your computer from getting clogged up.
    * `-it` makes this an interactive process. This means you can see the output of the Docker container as it's running.
    * The `-v` flag and subsequent arguments mount your working directory(graph_api/) with the Docker container's own working directory. This means that any changes you make to your code will be instantly reflected in the Docker container, and thus in the application your container is running.
    * `-p 8080:8080` binds the container and host machine's port 8080. So the host machine can send requests to the container and receive responses.
    * The final argument specifies which Docker Image to use. In this case you're telling Docker to use the graph_api image with the `dev` tag.
 4) Now you have your application running in a completely isolated docker container that could be used for development, as well as deployment on any number of machines.

## Testing

__Requirements__
   * Local test database setup. To do this install Neo4j Desktop, and create a local database with user `neo4j` and password `test`

__To run tests__

  1) Open Neo4j Desktop and start the databse you've created for this project.
  2) Export the following environment variables:
    
    * NEO4J_URI=bolt://127.0.0.1:7687
    * NEO4J_PASSWORD=test
    * NEO4J_USER=neo4j
  3) Make sure you're in the repo, in a python environement containing the right requirements(see `requirements.txt`) and run `pytest`

## TODOs
 - [ ] Merge dev process to enable TDD. At the moment they are separate, which is not conducive to proper TDD.
 - [ ] Document deployment process.