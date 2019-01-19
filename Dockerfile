from ubuntu

COPY src/run.sh /run.sh

RUN chmod +x /run.sh

CMD /run.sh

