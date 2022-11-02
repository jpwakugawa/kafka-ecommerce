import logging
import time
from kafka import KafkaConsumer

logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

consumer = KafkaConsumer(
    bootstrap_servers='localhost:9092',
    key_deserializer=str,
    value_deserializer=str,
    group_id='email'
)

if __name__ == '__main__':
  topics = ["ECOMMERCE_SEND_EMAIL"]
  consumer.subscribe(topics=topics)

  while(True):
    records = consumer.poll(timeout_ms=100)

    if records:
      logger.info(f"{len(records)} Records Found!")
      for r in records:
        logger.info(r)
        time.sleep(3)