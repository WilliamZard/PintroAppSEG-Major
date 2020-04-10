FROM python:3.7
ARG NEO4J_URI=bolt://35.246.41.58	
ARG NEO4J_PASSWORD='L0nd0n£EU!.dev'


COPY . tag_generation
WORKDIR /tag_generation
RUN pip install -r requirements.txt

ENV NEO4J_URI=$NEO4J_URI
ENV NEO4J_PASSWORD=$NEO4J_PASSWORD
ENV NEO4J_USER=neo4j

ENTRYPOINT [ "python" ]
CMD [ "upload_tags_to_db.py", "tags.csv" ]

