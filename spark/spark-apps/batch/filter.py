import pm4py
from pyspark import SparkContext
from pyspark.sql import SparkSession


spark_context = SparkContext(appName="filter")
# To avoid unncessary logs
spark_context.setLogLevel("WARN")
spark_session = (
    SparkSession.builder.appName("filter event logs")
    .config("spark.sql.warehouse.dir", "/user/hive/warehouse")
    .config("hive.metastore.uris", "thrift://hive-metastore:9083")
    .enableHiveSupport()
    .getOrCreate()
)
sdf = spark_session.sql("select * from event_logs")
# df = sdf.toPandas()
# filtered_log = pm4py.filter_time_range(df, "2011-10-13 00:00:00", "2012-01-18 23:59:59", mode='traces_intersecting')
# sdf = spark_session.createDataFrame(df)
sdf.show()
