FROM spark-base

#RUN pip install --upgrade pip
#RUN pip install pyspark 
#RUN pip install kafka-python 
RUN mkdir /usr/bin/submit/ 
RUN mkdir /opt/spark-apps

COPY submit.sh /usr/bin/submit/

ENTRYPOINT [ "tail", "-f", "/dev/null" ]