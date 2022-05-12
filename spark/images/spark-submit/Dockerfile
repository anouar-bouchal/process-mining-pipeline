FROM spark-base

RUN pip3 install --upgrade pip
RUN pip3 install pyspark 
RUN pip3 install kafka-python 
RUN mkdir /usr/bin/submit/ 
RUN mkdir /opt/spark-apps

COPY submit.sh /usr/bin/submit/

ENTRYPOINT [ "/usr/bin/submit/submit.sh" ]