#!/usr/bin/python3

from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils


def handle_rdd(rdd):
    if not rdd.isEmpty():
        global ss       
        df = None

        try:
            df = ss.createDataFrame(rdd, schema=["id", "lat", "lng", "aff_date"])
        except Exception as e:
            pass

        print("########################################################")
        print("########################################################")
        print("\n")
        print("\n")
        print("\n")

        print(df)
        # df.write.saveAsTable(name='default.covid', format='hive', mode='append')

        print("\n")
        print("\n")
        print("\n")
        print("########################################################")
        print("########################################################")


sc = SparkContext(appName="Something")
ssc = StreamingContext(sc, 5)

ss = (
    SparkSession.builder.appName("covid streaming")
    .config("spark.sql.warehouse.dir", "/user/hive/warehouse")
    .config("hive.metastore.uris", "thrift://hive-metastore:9083")
    .enableHiveSupport()
    .getOrCreate()
)


# ss.sparkContext.setLogLevel('WARN')

ks = KafkaUtils.createDirectStream(
    ssc, ["covid-new-cases"], {"metadata.broker.list": "kafka-server:9092"}
)

lines = ks.map(lambda x: x[1])

transform = lines.map(lambda data: (data.split(";")))

transform.foreachRDD(handle_rdd)

ssc.start()
ssc.awaitTermination()
