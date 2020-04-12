# Development Dockefile. See README for how to run.

FROM python:3.7

WORKDIR /graph_api

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ENV NEO4J_URI=bolt://34.89.108.213
ENV NEO4J_PASSWORD='L0nd0n$EU:test1ng'
ENV NEO4J_USER=neo4j
ENV FLASK_ENV=development
ENV FLASK_RUN_PORT=8080
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_APP=graph_api:create_app
#Environment variable for GCP credentials. Needed for accessing GCP buckets.
ENV GOOGLE_APPLICATION_CREDENTIALS="./pintro-service-key.json" 
ENV IMAGES_BUCKET_NAME=profile-pics-dev
ENTRYPOINT [ "flask" ]
CMD [ "run" ]
