FROM spark-base

RUN curl https://www.python.org/ftp/python/3.6.10/Python-3.6.10.tgz -o Python.tgz
RUN tar xzf Python.tgz 
RUN cd Python-3.6.10 && ./configure && make altinstall
RUN rm -rf Python.tgz
RUN mv /usr/local/bin/python3.6 /usr/local/bin/python3

RUN python3 -m pip install pyspark
RUN python3 -m pip install kafka-python

ENV PYSPARK_PYTHON=python3
ENV SPARK_MASTER_PORT 7077
ENV SPARK_MASTER_WEBUI_PORT 4040

EXPOSE 4040 7077

ENTRYPOINT ["bin/bash", "-c", "usr/bin/spark/sbin/start-master.sh && tail -f /dev/null"] 