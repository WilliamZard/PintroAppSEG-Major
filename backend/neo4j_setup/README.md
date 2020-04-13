# Script for running admin queries to Neo4j databases

## To Run
1. Open a command line session
2. Enter the `SEG-Major-BlueJ/backend/neo4j_setup` directory
3. If not already done, build the Docker image with `docker build -f Dockerfile -t neo4j_setup .`
4. Run the Docker image with this command, replacing the variables with the credentials of the database you want to write to: `docker run --rm -it neo4j_setup <BOLT_URI> <DB_PASSWORD>` where BOLT_URI is `bolt://<EXTERNAL_IP>` and DB_PASSWORD is the new password you just created.