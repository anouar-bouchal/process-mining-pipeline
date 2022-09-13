from pyspark.sql import SparkSession


class EventRepository:
    def __init__(self, table):
        self.table = table
        self.session = (
            SparkSession.builder.appName("event logs")
            .config("spark.sql.warehouse.dir", "/user/hive/warehouse")
            .config("hive.metastore.uris", "thrift://hive-metastore:9083")
            .enableHiveSupport()
            .getOrCreate()
        )

    def add_event(self, event):
        try:
            query = (
                "INSERT INTO "
                + self.table
                + " VALUES ("
                + event.flatten_attributes()
                + ")"
            )
            self.session.sql(query)
        except Exception as e:
            raise e

    def get_all_events(self):
        try:
            query = "SELECT * FROM " + self.table
            return self.session.sql(query)
        except Exception as e:
            raise e

    def get_latest_events(self, number_of_events=5):
        try:
            # FIX: Figure out query
            query = "DUNNO"
            return self.session.sql(query)
        except Exception as e:
            raise e


# FIX: decide on models storage
class ModelRepository:
    def __init__(self, table=models):
        self.table = table
