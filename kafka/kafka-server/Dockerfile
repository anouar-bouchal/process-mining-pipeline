FROM kafka-base

RUN mkdir -p /tmp/kafka-logs
COPY ./server.properties config/server.properties

EXPOSE 2181 9092
CMD [ "bin/kafka-server-start.sh", "config/server.properties"]