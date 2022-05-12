FROM openjdk:8-jre

RUN apt-get update -qy
RUN mkdir /usr/bin/kafka/
RUN curl https://archive.apache.org/dist/kafka/2.7.0/kafka_2.13-2.7.0.tgz -o kafka_2.13-2.7.0.tgz
# RUN gzip -dc kafka_2.13-2.7.0.tgz | tar -xf -
RUN tar -xf kafka_2.13-2.7.0.tgz
RUN mv kafka_2.13-2.7.0/* /usr/bin/kafka/
RUN rm kafka_2.13-2.7.0.tgz

ENV KAFKA_HOME /usr/bin/kafka
ENV PATH /usr/bin/kafka/bin:/usr/bin/kafka/bin:$PATH
EXPOSE 9092
WORKDIR /usr/bin/kafka