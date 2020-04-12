FROM python:3.7

COPY . neo4j_setup
WORKDIR /neo4j_setup
RUN pip install -r requirements.txt

ENV NEO4J_URI=bolt://35.246.41.58	
ENV NEO4J_PASSWORD=L0nd0n£EU!.dev
ENV NEO4J_USER=neo4j

CMD [ "python", "neo4j_setup.py" ]
