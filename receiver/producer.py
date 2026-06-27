from confluent_kafka import Producer

KAFKA_TOPIC = "transactions"

producer = Producer({"bootstrap.servers":"localhost:9092"})

def publish(message: bytes):
    try:
        producer.produce(topic = KAFKA_TOPIC, value = message)
        producer.flush()
    except Exception as ex:
        print("Exception happened :",ex)

    print(f"Published message to {KAFKA_TOPIC}")
