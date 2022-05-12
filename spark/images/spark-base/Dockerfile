FROM openjdk:8-jre

ARG SPARK_VERSION
ARG HADOOP_VERSION

RUN apt-get update -qy
RUN apt-get install -y procps python3 python3-pip
RUN mkdir /usr/bin/spark/
RUN curl https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz -o spark.tgz
RUN tar -xf spark.tgz
RUN mv spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}/* /usr/bin/spark/
RUN rm -rf spark.tgz
RUN rm -rf spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}/

ENV SPARK_HOME /usr/bin/spark
ENV SPARK_NO_DAEMONIZE true
ENV PYSPARK_DRIVER_PYTHON python3
ENV PYSPARK_PYTHON python3
ENV PATH /usr/bin/spark/bin:/usr/bin/spark/sbin:$PATH

WORKDIR ${SPARK_HOME}