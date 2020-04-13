FROM python:3.7


COPY . tag_generation
WORKDIR /tag_generation
RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "upload_tags_to_db.py", "tags.csv" ]