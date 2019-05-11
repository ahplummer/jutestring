FROM alpine:3.9

ADD ./src/* /jutestring/
ADD ./requirements.txt /jutestring/

RUN apk add --no-cache python3 bash

RUN cd /jutestring && pip3 install -r requirements.txt

WORKDIR /jutestring
