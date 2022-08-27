FROM openjdk:8-jre

ARG SPARK_VERSION=2.4.7
ARG HADOOP_VERSION=2.7

RUN apt-get update -qy
RUN apt-get install -y procps 
RUN apt-get install -y build-essential checkinstall 
RUN apt-get install -y libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev

#RUN wget https://www.python.org/ftp/python/3.5.2/Python-3.5.2.tgz 
#RUN tar xzf Python-3.5.2.tgz 
#RUN cd Python-3.5.2 && ./configure && make altinstall 
#RUN rm -rf Python-3.5.2.tgz
#RUN mv /usr/local/bin/python3.5 /usr/local/bin/python3
RUN mkdir /usr/bin/spark/
#RUN curl https://dlcdn.apache.org/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz -o spark.tgz
RUN curl https://archive.apache.org/dist/spark/spark-2.4.7/spark-2.4.7-bin-hadoop2.7.tgz -o spark.tgz
RUN tar -xf spark.tgz
RUN mv spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}/* /usr/bin/spark/
RUN rm -rf spark.tgz