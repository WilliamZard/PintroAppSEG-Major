# Production Dockerfile.

FROM python:3.7
#docker run --rm -it -p 8080:8080 graph_api:prod
COPY graph_api graph_api


COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ENV NEO4J_URI=bolt://35.246.41.58	
ENV NEO4J_PASSWORD=L0nd0n£EU!.dev
ENV NEO4J_USER=neo4j
ENV ENV=prod
ENV FLASK_APP=graph_api:create_app
ENV FLASK_RUN_PORT=8080
ENV FLASK_RUN_HOST=0.0.0.0
ENV IMAGES_BUCKET_NAME=profile-pics-prod

EXPOSE 8080:8080 

ENTRYPOINT [ "flask" ]
CMD [ "run" ]
