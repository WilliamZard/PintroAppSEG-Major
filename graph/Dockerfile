# Production Dockerfile.

FROM python:3.7

COPY graph_api graph_api

WORKDIR /graph_api

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ENV NEO4J_URI=bolt://35.246.56.244
ENV NEO4J_PASSWORD=L0nd0n&EU
ENV FLASK_RUN_PORT=8080
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_APP=app.py

EXPOSE 8080:8080 

ENTRYPOINT [ "flask" ]
CMD [ "run" ]
