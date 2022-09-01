#!/usr/bin/python3

from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import os
import sys

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable


line_count = 0


def file_exists(file_name):
    return os.path.isfile(os.path.join(os.getcwd(), file_name))


def log_records(dataframe, file_name):
    path = os.path.join(os.getcwd(), file_name)
    if file_exists(file_name):
        dataframe.to_csv(path, mode='a', index=False, header=False)
    else:
        dataframe.to_csv(path)


def write_to_hive(sdf):
    sdf.write.format("orc") \
    .mode("overwrite") \
    .saveAsTable("event_logs")

def handle_rdd(rdd):
    if rdd.isEmpty():
        return
    global spark_session
    global line_count
    df = None
    try:
        sdf = spark_session.createDataFrame(
            rdd, schema=["index", "case_id", "task", "event_type", "user", "timestamp"]
        )
    except Exception as e:
        raise e
    print("########################       #########################")
    print("######################## Count #########################")
    print("\n")
    # print(rdd)
    df = sdf.toPandas()
    line_count += sdf.count()
    print('[sdf_count]>>>>>>>>>>>>>>>               ', sdf.count())
    print('[tot_count]>>>>>>>>>>>>>>>               ', line_count)
    log_records(df, 'records.csv')
    print("\n")
    print("########################       #########################")
    print("########################################################")




# _StreamingContext_ the main entry point for utilizing the Spark Streaming functionality
# Can be built either by providing:
# *Spark master URL and an appName
# *org.apache.spark.SparkConf configuration
# *org.apache.spark.SparkContext
spark_context = SparkContext(appName="discovery")
spark_streaming_context = StreamingContext(spark_context, 10)

spark_session = (
    SparkSession.builder.appName("event logs")
    .config("spark.sql.warehouse.dir", "/user/hive/warehouse")
    .config("hive.metastore.uris", "thrift://hive-metastore:9083")
    .enableHiveSupport()
    .getOrCreate()
)

# Create an input stream that pulls messages from the Kafka broker
# (every message from Kafka participates in the conversion only once)
kafka_stream = KafkaUtils.createDirectStream(
    spark_streaming_context,
    ["event-logs-stream"],  # Topic
    {"metadata.broker.list": "kafka-server:9092"},  # Storage level
)

print("################# kafka Stream #################")
print("################################################")
print(kafka_stream)
print("######## kafka_stream.map(lambda x: x) #########")
print("################################################")
lines = kafka_stream.map(lambda x: x[1])
print(lines)
print("################################################")
print("################################################")
# for line in lines:
#     print(line)
print("################################################")
print("################################################")
transform = lines.map(lambda data: (data.split(";")))
print(transform)
print("################################################")
print("################################################")

transform.foreachRDD(handle_rdd)

# Start the streaming computation
spark_streaming_context.start()
# allow the current thread to wait for the termination of the context by stop() or by an exception.
spark_streaming_context.awaitTermination()
