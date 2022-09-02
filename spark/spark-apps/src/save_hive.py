def write_to_hive(sdf):
    sdf.write.format("orc") \
    .mode("overwrite") \
    .saveAsTable("event_logs")