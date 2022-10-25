import logging
import time
from kafka import KafkaConsumer

logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

consumer = KafkaConsumer(
    bootstrap_servers='localhost:9092',
    key_deserializer=str,
    value_deserializer=str,
    group_id='fraud_detector'
)

if __name__ == '__main__':
  topics = ["ECOMMERCE_NEW_ORDER"]
  consumer.subscribe(topics=topics)

  while(True):
    records = consumer.poll(timeout_ms=100)

    if records:
      logger.info("Record Found!")
      for r in records:
        print(r)
        time.sleep(3)