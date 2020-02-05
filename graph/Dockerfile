FROM python:3.7

WORKDIR .

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app.py app.py
COPY transaction_functions.py transaction_functions.py
COPY __init__.py __init__.py
