#!/usr/bin/python3

from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.streaming import StreamingContext
from pyspark.sql.types import *
# from pyspark.sql.SparkSession import readStream
from pm4py.streaming.stream.live_event_stream import LiveEventStream
from pm4py.streaming.algo.discovery.dfg import algorithm as dfg_discovery
import os
import sys
from src.save_csv import log_records
from src.save_hive import write_to_hive

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable


live_event_stream = LiveEventStream()
streaming_dfg = dfg_discovery.apply()
live_event_stream.register(streaming_dfg)
# live_event_stream.start()


def handle_rdd(rdd):
    if rdd.isEmpty():
        return
    global spark_session
    global live_event_stream
    global streaming_dfg
    df = None
    try:
        sdf = spark_session.createDataFrame(
            rdd, schema=["index", "case_id", "task", "event_type", "user", "timestamp"]
        )
    except Exception as e:
        raise e

    df = sdf.toPandas()
    # Append and process events or traces
    for event in df.to_dict(orient='records'):
        live_event_stream.append(event)

    dfg, activities, sa, ea = streaming_dfg.get()

    print("########################       #########################")
    print("######################## Count #########################")
    print("\n")
    log_records(df, 'records.csv')
    print("\n")
    print(activities)
    print("########################       #########################")
    print("########################################################")




# _StreamingContext_ the main entry point for utilizing the Spark Streaming functionality
# Can be built either by providing:
# *Spark master URL and an appName
# *org.apache.spark.SparkConf configuration
# *org.apache.spark.SparkContext
spark_context = SparkContext(appName="discovery")
# To avoid unncessary logs
spark_context.setLogLevel("WARN")
# log4jLogger = spark_context._jvm.org.apache.log4j
# LOGGER = log4jLogger.LogManager.getLogger()

# # same call as you'd make in java, just using the py4j methods to do so
# LOGGER.setLevel(log4jLogger.Level.WARN)


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
# kafka_stream = KafkaUtils.createDirectStream(
#     spark_streaming_context,
#     ["event-logs-stream"],  # Topic
# kafka.bootstrap.servers
#     {"metadata.broker.list": "kafka-server:9092"},  # Storage level
# )

# schema = StructType([StructField('id', StringType(), True),
#                     StructField('id1', StringType(), True),
#                     StructField('id2', StringType(), True),
#                     StructField('event', StringType(), True),
#                     StructField('event_type', StringType(), True),
#                     StructField('ressource', StringType(), True),
#                     StructField('arrived_at', StringType(), True),
#                     StructField('activity', StringType(), True),
#                     StructField('activity_state', StringType(), True),])

df = spark_session \
  .readStream \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "kafka-server:9092") \
  .option("subscribe", "event-logs-stream") \
  .load()

print(" ################################################# ")
print(" ################################################# ")
print(df.printSchema())
print(" ################################################# ")
print(" ################################################# ")



# lines = kafka_stream.map(lambda x: x[1])

# transform = lines.map(lambda data: (data.split(";")))

# print(transform)

# transform.foreachRDD(handle_rdd)

# Start the streaming computation
# spark_streaming_context.start()
# allow the current thread to wait for the termination of the context by stop() or by an exception.
# spark_streaming_context.awaitTermination()
