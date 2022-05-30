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

POSITIONS_FILE = dir + "/logs.csv"

try:
    producer = KafkaProducer(bootstrap_servers=BROKER)
except Exception as e:
    print(f"ERROR --> {e}")
    sys.exit(1)

while True:

    id = str(uuid.uuid4())

    with open(POSITIONS_FILE) as fin:
        random_line = min(fin, key=lambda L: random.random()).replace("\n", "")
    alt_long = random_line.replace(",", ";")

    now = datetime.datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    # dd/mm/YY H:M:S
    aff_date = dt_string

    frame_list = [id, alt_long, dt_string]
    frame = ";".join(frame_list)

    print(f">>> '{frame}'")
    producer.send(TOPIC, bytes(frame, encoding="utf8"))
    sleep(random.randint(1, 2))
