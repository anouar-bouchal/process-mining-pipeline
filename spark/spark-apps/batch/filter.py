import pm4py
import pytz
import pandas as pd
from pyspark import SparkContext
from pyspark.sql import SparkSession


class Filter:
    def __init__(self, log, filter_type=None):
        self.log = log
        self.filter_type = filter_type

    def apply_filter(self, **kwargs):
        if self.filter_type:
            return self.filter_type(self.log, **kwargs)
        else:
            return get_most_recent(log)


def get_most_recent(log):
    return log


def filter_time_range(log, **kwargs):
    _check_required_args("start_timestamp", "end_timestamp", kwargs)
    mode = "events"
    if "mode" in kwargs.keys():
        mode = kwargs["mode"]
    return pm4py.filter_time_range(
        log, kwargs["start_timestamp"], kwargs[" end_timestamp"], mode=mode
    )


def filter_case_performance(log, **kwargs):
    _check_required_args("min_duration", "max_duration", kwargs)
    return pm4py.filter_case_performance(
        log, kwargs["min_duration"], kwargs["max_duration"]
    )


def filter_start_activities(log, **kwargs):
    _check_required_args("start_activities", kwargs)
    return pm4py.filter_start_activities(log, kwargs["start_activities"])


def filter_end_activities(log, **kwargs):
    _check_required_args("end_activities", kwargs)
    return pm4py.filter_end_activities(log, kwargs["end_activities"])


def _check_required_args(*args, **kwargs):
    if not args in kwargs.keys():
        raise ValueError("must provide all required arguments : ", args)


if __name__ == "__main__":

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
    log = spark_session.sql("select * from event_logs")
    log = log.toPandas()
    log.columns = [
        "case:concept:name",
        "case:task:de",
        "case:event:type",
        "case:user",
        "time:timestamp",
        "case:task:type",
        "case:task:name",
        "concept:name",
    ]
    log["time:timestamp"] = log["time:timestamp"].apply(
        lambda t: t.replace(tzinfo=pytz.utc)
    )
    filtered_log = Filter(log, filter_type=filter_time_range).apply_filter(
        "2009-10-13 00:00:00", "2012-01-18 23:59:59"
    )
    print(filtered_log)
