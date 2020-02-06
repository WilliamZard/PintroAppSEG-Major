FROM python:3.7

WORKDIR /graph_api

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ENV NEO4J_URI=bolt://35.246.56.244
ENV NEO4J_PASSWORD=L0nd0n&EU


ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
