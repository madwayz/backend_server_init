FROM python:3.7-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ADD app .
ADD requirements.txt .
ADD uwsgi.ini .

RUN apt-get update
RUN apt-get install -y build-essential python3-dev nano

RUN pip install -r requirements.txt

RUN usermod --non-unique --uid 1000 www-data \
  && groupmod --non-unique --gid 1000 www-data \
  && chown -R www-data:www-data /app

ENV FLASK_APP=app/__init__.py

CMD ["uwsgi", "uwsgi.ini"]
