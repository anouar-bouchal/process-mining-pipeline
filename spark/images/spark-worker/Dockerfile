FROM spark-base

ENV SPARK_WORKER_WEBUI_PORT 4041

ENV SPARK_MASTER_URI=spark://spark-master:7077

EXPOSE 4041

RUN usr/bin/spark/sbin/start-slave.sh ${SPARK_MASTER_URI}

# ENTRYPOINT usr/bin/spark/sbin/start-slave.sh ${SPARK_MASTER_URI}
ENTRYPOINT [ "tail", "-f", "/dev/null" ]