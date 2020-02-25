# Development Dockefile. See README for how to run.

FROM python:3.7

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ENV FLASK_ENV=development
ENV FLASK_RUN_PORT=8080
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_APP=timeline:create_app

ENTRYPOINT [ "flask" ]
CMD [ "run" ]
