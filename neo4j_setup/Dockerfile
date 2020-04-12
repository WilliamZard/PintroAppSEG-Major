FROM python:3.7

COPY . neo4j_setup
WORKDIR /neo4j_setup
RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "neo4j_setup.py" ]
