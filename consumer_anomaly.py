import json
import logging
from settings import ANOMALIES_CONSUMER_GROUP, ANOMALIES_TOPIC
from streaming.utils import create_consumer


consumer = create_consumer(topic=ANOMALIES_TOPIC, 
                           group_id=ANOMALIES_CONSUMER_GROUP)
while True:
    message = consumer.poll(timeout=50)
    if message is None:
        continue
    if message.error():
        logging.error("Consumer error: {}".format(message.error()))
        continue

    # Message that came from producer
    record = json.loads(message.value().decode('utf-8'))
    print(record)
consumer.flush()