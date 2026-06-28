import psycopg2
from confluent_kafka import Consumer
from datetime import datetime
import json
import os
import dotenv
dotenv.load_dotenv()

POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS")

server = 'localhost:9092'
topic_name = 'transactions'

consumer = Consumer({
    "bootstrap.servers": KAFKA_BOOTSTRAP_SERVERS,
    "group.id":"transactions-consumer",
    "auto.offset.reset":"earliest"
})

consumer.subscribe(["transactions"])

conn = psycopg2.connect(
    host=POSTGRES_HOST,
    port=POSTGRES_PORT,
    database=POSTGRES_DB,
    user=POSTGRES_USER,
    password=POSTGRES_PASSWORD
)

conn.autocommit = True
cur = conn.cursor()

while True:
    msg = consumer.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        print(f"Error: {msg.error()}")
        continue

    msg_value = msg.value()
    payload = json.loads(msg_value)
    event_type = payload.get("type")
    cur.execute(
        """
        INSERT INTO transactions_raw (event_type, response, received_at)
        VALUES ( %s, %s::jsonb, %s)""",
        (event_type, json.dumps(payload), datetime.now())
        
    )
