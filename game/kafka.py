from kafka import KafkaConsumer
from time import sleep
import json

TOPIC_NAME = "payments"
KAFKA_SERVER = "host.docker.internal:9094"


class MessageConsumer:

    broker = ""
    topic = ""
    group_id = ""
    logger = None

    def activate_listener(self):
        consumer = KafkaConsumer(bootstrap_servers=['host.docker.internal:9094'],
                                 group_id='my-group',
                                 consumer_timeout_ms=60000,
                                 auto_offset_reset='earliest',
                                 enable_auto_commit=False,
                                 value_deserializer=lambda m: json.loads(m.decode('utf-8')))

        consumer.subscribe(TOPIC_NAME)
        print("consumer is listening....")
        try:
            for message in consumer:
                print("received message = ", message)

                # committing message manually after reading from the topic
                consumer.commit()
        except KeyboardInterrupt:
            print("Aborted by user...")
        finally:
            consumer.close()

