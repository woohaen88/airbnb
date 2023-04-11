FROM python:3.10-buster

LABEL maintainer="woohaen88@gmail.com"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
copy ./run.sh /run.sh

WORKDIR /app
EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apt-get -y update && \
    apt-get -y install netcat-openbsd && \
    /py/bin/pip install -r /tmp/requirements.txt &&\
    rm -rf /tmp


ARG USER=wyatt
RUN adduser \
    --disabled-password \ 
    --no-create-home \
    ${USER}

RUN mkdir -p /data/media &&\
    mkdir -p /data/static &&\
    chown -R ${USER}:${USER} /data/media &&\
    chown -R ${USER}:${USER} /data/static

RUN chmod -R 755 /data && \
    chmod +x /run.sh

ENV PATH="/:/py/bin:$PATH"

USER ${USER}

CMD ["run.sh"]