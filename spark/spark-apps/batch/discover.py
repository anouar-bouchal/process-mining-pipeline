import pm4py
from pyspark.sql import SparkSession


class Discoverer:
    def __init__(self, log, algotithm=None):

        self.log = log
        self.algorithm = algotithm

    def discover(self):
        if self.algorithm:
            return self.algorithm(self.log)
        else:
            return heuristic_miner(self.log)


def alpha_miner(log):
    return pm4py.discover_petri_net_alpha(log)


def inductive_miner(log):
    return pm4py.discover_petri_net_inductive(log)


def heuristic_miner(log):
    return pm4py.discover_petri_net_heuristics(log, dependency_threshold=0.99)


if __name__ == "__main__":

    spark_session = (
        SparkSession.builder.appName("event logs")
        .config("spark.sql.warehouse.dir", "/user/hive/warehouse")
        .config("hive.metastore.uris", "thrift://hive-metastore:9083")
        .enableHiveSupport()
        .getOrCreate()
    )
    log = spark_session.sql("SELECT * FROM event_logs")
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

    alpha_model = Discoverer(log, alpha_miner).discover()
    inductive_model = Discoverer(log, inductive_miner).discover()
    heuristic_model = Discoverer(log, heuristic_miner).discover()

    print(alpha_model, inductive_model, heuristic_model)
