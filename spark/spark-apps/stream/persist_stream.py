from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from pm4py.streaming.stream.live_event_stream import LiveEventStream
from pm4py.streaming.algo.discovery.dfg import algorithm as dfg_discovery


live_event_stream = LiveEventStream()
streaming_dfg = dfg_discovery.apply()
live_event_stream.register(streaming_dfg)

live_event_stream.start()


def handle_rdd(rdd):
    if rdd.isEmpty():
        return
    global spark_session
    global live_event_stream
    global streaming_dfg
    df = None
    sdf = None
    try:
        sdf = spark_session.createDataFrame(
            rdd,
            schema=[
                "case:concept:name",
                "case:task:de",
                "case:event:type",
                "case:user",
                "time:timestamp",
                "case:task:type",
                "case:task:name",
                "concept:name",
            ],
        )
    except Exception as e:
        raise e
    df = sdf.toPandas()
    print("\n")
    for event in df.to_dict(orient="records"):
        live_event_stream.append(event)
        # print("############################ Event ###########################")
        # print(event)
        # event_values = ",".join(["'" + str(i) + "'"  for i in event.values()])
        # spark_session.sql(f"INSERT INTO event_logs VALUES ({event_values})")
        # print(event_values)
    print("######################### Activities #########################")
    print(streaming_dfg.get())
    print("##############################################################")


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

lines = kafka_stream.map(lambda x: x[1])
transform = lines.map(lambda data: (data.split(";")))
transform.foreachRDD(handle_rdd)
# Start the streaming computation
spark_streaming_context.start()
# allow the current thread to wait for the termination of the context by stop() or by an exception.
spark_streaming_context.awaitTermination()
