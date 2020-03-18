# Development Dockefile. See README for how to run.

FROM python:3.7

WORKDIR /graph_api

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ENV NEO4J_URI=bolt://34.89.54.81
ENV NEO4J_PASSWORD='L0nd0n$EU:test1ng'
ENV FLASK_ENV=development
ENV FLASK_RUN_PORT=8080
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_APP=graph_api:create_app

ENTRYPOINT [ "flask" ]
CMD [ "run" ]
