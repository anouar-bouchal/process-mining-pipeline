FROM spark-base

ENV PYSPARK_PYTHON=python3
ENV SPARK_MASTER_PORT 7077
ENV SPARK_MASTER_WEBUI_PORT 4040

EXPOSE 4040 7077

RUN usr/bin/spark/sbin/start-master.sh

ENTRYPOINT [ "tail", "-f", "/dev/null" ]