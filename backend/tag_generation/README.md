# Tag Generation

## Access

The `SEG-Major-BlueJ/backend/tag_generation` folder is not deployed in any remote service. It just provides functionality for populating a Neo4j graph database with tag nodes.

## Deployment

To deploy a new collection of tags to a Neo4j graph database:

1. Make sure Docker is running
2. Open a command line session
3. Enter the `SEG-Major-BlueJ/backend/tag_generation` directory
4. Keep or replace the existings tags.csv file. This is the file the tag nodes will be constructred from.
5. If the Docker image is not built yet, run `docker build -f Dockerfile -t tag_generation .`
6. Run the Docker image with `docker run --rm -it tag_generation:dev <BOLT_URI> <PASSWORD>`, replacing the relevant variables. While it runs there will be no terminal output. Once it completes running, the tags have been successfully written to the database.

Keep in mind that this will completely delete the previous tags that existed in the database.

Please also note that the current tag labels are hardcoded in the `upload_tags_to_db.py` script. Any changes to the column names, or their order will require changes to that Python script.

## Development

Given that this code is not deployed in production,  is only ran manually by a human, and is very simple, there are no existing tests for this code.

However, manual testing can be achieved as follows:

1. If you made any source code changes, rebuild the Docker image with `docker build -f Dockerfile -t tag_generation:dev .`
2. Run the Docker container with `docker run --rm -it tag_generation:dev <BOLT_URI> <PASSWORD>`, replacing the variables with the credentials of the database you wish to write to.
3. Once it completes uploading the new tags, inspect the relevant database.
4. From here, continue developing based on what you see in the database. Remember, whenever you change the source code, you will need to rebuild the docker image.