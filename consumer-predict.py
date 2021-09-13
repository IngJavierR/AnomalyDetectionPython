from settings import ANOMALIES_TOPIC, TRANSACTIONS_CONSUMER_GROUP, TRANSACTIONS_TOPIC
from streaming.utils import create_consumer, create_producer
import pandas as pd
import numpy as np
import logging
import json
from joblib import load

clf = load("models/isolation_forest.joblib")

consumer = create_consumer(topic=TRANSACTIONS_TOPIC, group_id=TRANSACTIONS_CONSUMER_GROUP)

producer = create_producer()

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

    test_data = np.delete(record, 0)
    data = np.array(test_data, dtype=float).reshape(1, -1)

    prediction = clf.predict(data)
    if prediction == -1:
        print("prediction")
        print(prediction)

        score = clf.score_samples(data)
        print("score")
        print(score)

        roundes_score = np.round(score, 3).tolist()
        print("roundes_score")
        print(roundes_score)

        record_bytes = json.dumps(record).encode("utf-8")
        producer.produce(topic=ANOMALIES_TOPIC,
                            value=record_bytes)
        producer.flush()
consumer.flush()
    