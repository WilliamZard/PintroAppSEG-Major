FROM python:3.7


COPY . timeline
WORKDIR /timeline
RUN pip install -r requirements.txt

CMD [ "python", "test.py" ]