from kafka import KafkaProducer
import random
from time import sleep
import sys
import os
import uuid
import datetime

dir = os.path.dirname(os.path.realpath(__file__))

BROKER = "kafka-server:9092"
TOPIC = "event-logs-stream"

EVENT_LOGS = dir + "/logs.csv"

try:
    producer = KafkaProducer(bootstrap_servers=BROKER)
except Exception as e:
    print(f"ERROR --> {e}")
    sys.exit(1)

while True:
    with open(EVENT_LOGS) as file:
        random_line = min(file, key=lambda L: random.random()).replace("\n", "")
    event = random_line.replace(",", ";")

    print(f">>> '{event}'")
    producer.send(TOPIC, bytes(event, encoding="utf8"))
    sleep(random.randint(1, 2))
