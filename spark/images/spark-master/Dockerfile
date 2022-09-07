FROM spark-base

RUN apt install libffi-dev

RUN curl https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tgz -o Python.tgz
RUN tar xzf Python.tgz 
RUN cd Python-3.7.0 && ./configure && make altinstall
RUN rm -rf Python.tgz
RUN mv /usr/local/bin/python3.7 /usr/local/bin/python3
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --upgrade setuptools

RUN python3 -m pip install pm4py
RUN python3 -m pip install kafka-python
RUN python3 -m pip install pyspark

WORKDIR /
ADD spark/spark-apps ./spark-apps

ENV PYSPARK_PYTHON=python3
ENV SPARK_MASTER_PORT 7077
ENV SPARK_MASTER_WEBUI_PORT 4040

EXPOSE 4040 7077
RUN usr/bin/spark/sbin/start-master.sh

# ENTRYPOINT [ "bin/bash", "-c", "tail -f /dev/null" ]
ENTRYPOINT [ "bin/bash", "-c", "usr/bin/spark/bin/spark-submit --jars spark-apps/spark-streaming-kafka-0-8-assembly_2.11-2.1.0.jar spark-apps/stream/persist_stream.py" ]