FROM openjdk:8-jre

ARG SPARK_VERSION=2.4.7
ARG HADOOP_VERSION=2.7

RUN apt-get update -qy && \
    apt-get install -y procps && \
    apt-get install -y build-essential checkinstall && \
    apt-get install -y libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev && \
    wget https://www.python.org/ftp/python/3.5.2/Python-3.5.2.tgz && \
    tar xzf Python-3.5.2.tgz && \
    cd Python-3.5.2 && \
    ./configure && \
    make altinstall && \
    rm -rf Python-3.5.2.tgz

RUN mv /usr/local/bin/python3.5 /usr/local/bin/python3

RUN mkdir /usr/bin/spark/ && \
    curl https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz -o spark.tgz && \
    tar -xf spark.tgz && \
    mv spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}/* /usr/bin/spark/ && \
    rm -rf spark.tgz && \