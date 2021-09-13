import json
import time
import pandas as pd
import numpy as np
from settings import DELAY, TRANSACTIONS_TOPIC
from streaming.utils import create_producer

# csv_data = pd.read_csv("data/test-light.csv", index_col=0).to_numpy()
csv_data = pd.read_csv("data/test-part-000.csv", index_col=0).to_numpy()
producer = create_producer()

if producer is not None:
    for data in csv_data:

        record = json.dumps(data.tolist()).encode("utf-8")
        print(record)

        producer.produce(topic=TRANSACTIONS_TOPIC, value=record)
        producer.flush()
        time.sleep(DELAY)