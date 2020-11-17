FROM python:3.7-slim

WORKDIR /backend/

ARG DEBIAN_FRONTEND=noninteractive

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ADD . .

RUN apt-get update
RUN apt-get install -y build-essential python3-dev nano
RUN apt-get install -y --no-install-recommends apt-utils

RUN pip install -r requirements.txt

RUN usermod --non-unique --uid 1000 www-data \
  && groupmod --non-unique --gid 1000 www-data \
  && chown -R www-data:www-data /backend/app

CMD ["uwsgi", "uwsgi.ini"]
