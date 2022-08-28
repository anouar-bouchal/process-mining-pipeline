#!/usr/bin/python3

from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import os
import sys


os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable


def handle_rdd(rdd):
    if rdd.isEmpty():
        return    
    global spark_session
    df = None
    try:
        df = spark_session.createDataFrame(
            rdd, schema=["index", "case_id", "task", "event_type", "user", "timestamp"]
        )
    except Exception as e:
        raise e
    print("########################################################")
    print("########################################################")
    print("\n")
    print(df)
    print("\n")
    print("########################################################")
    print("########################################################")


spark_context = SparkContext(appName="discovery")

spark_streaming_context = StreamingContext(spark_context, batchDuration=5)

spark_session = (
    SparkSession.builder.appName("event logs")
    .config("spark.sql.warehouse.dir", "/user/hive/warehouse")
    .config("hive.metastore.uris", "thrift://hive-metastore:9083")
    .enableHiveSupport()
    .getOrCreate()
)


kafka_stream = KafkaUtils.createDirectStream(
    spark_streaming_context,
    ["event-logs-stream"],
    {"metadata.broker.list": "kafka-server:9092"},
)

lines = kafka_stream.map(lambda x: x[1])

transform = lines.map(lambda data: (data.split(";")))

transform.foreachRDD(handle_rdd)

spark_streaming_context.start()

spark_streaming_context.awaitTermination()
