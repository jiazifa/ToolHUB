FROM python:3.8.3

ARG pypi_host=pypi.douban.com
ARG pypi_mirror=http://pypi.douban.com/simple

ENV LC_ALL C.UTF-8

ENV LANG C.UTF-8

ENV PIP_INDEX_URL $pypi_mirror

ENV FLASK_ENV production

ENV DISK_PATH /disk

WORKDIR /app

COPY requirements.txt requirements.txt

RUN python -m pip install --upgrade pip --trusted-host pypi.douban.com

RUN pip install --no-cache-dir -r requirements.txt --trusted-host ${pypi_host}

COPY hub hub

COPY celery_tasks celery_tasks

COPY utils utils

COPY celery_worker.py celery_worker.py

COPY config.py config.py

COPY locale_settings.py locale_settings.py
