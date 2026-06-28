from confluent_kafka import Producer
import os
import dotenv
dotenv.load_dotenv()

KAFKA_TOPIC = "transactions"
KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS")

producer = Producer({"bootstrap.servers":KAFKA_BOOTSTRAP_SERVERS})

def publish(message: bytes):
    try:
        producer.produce(topic = KAFKA_TOPIC, value = message)
        producer.flush()
    except Exception as ex:
        print("Exception happened :",ex)

    print(f"Published message to {KAFKA_TOPIC}")
