from python:3.7-alpine3.7

COPY src/run.py /run.py

RUN find /

CMD python run.py

