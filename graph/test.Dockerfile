# TODO: finish Dockerfile configuration.
# for now just run tests on host machine. Requires exporting key envs.
FROM python:3.7


WORKDIR /graph_api

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ENV NEO4J_URI=bolt://127.0.0.1:7687
ENV NEO4J_PASSWORD=test
ENV NEO4J_USER=neo4j
ENV ENV=test
ENV FLASK_ENV=testing
ENV FLASK_RUN_PORT=8080
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_APP=graph_api:create_app

CMD [ "pytest" ]
