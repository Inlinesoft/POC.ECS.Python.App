FROM python:3.6.8-slim-stretch

RUN apt-get -y update && \
    apt-get -y clean

ARG WORKING_DIR=/usr/app

COPY requirements.txt /tmp

RUN pip install -r /tmp/requirements.txt

ADD . ${WORKING_DIR}

WORKDIR ${WORKING_DIR}

RUN sed -i 's/\r//' etc/*.sh

RUN chmod +x etc/*.sh

CMD etc/run.sh