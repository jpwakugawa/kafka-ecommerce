import logging
import time
from kafka import KafkaConsumer

logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

consumer = KafkaConsumer(
    bootstrap_servers='localhost:9092',
    key_deserializer=str,
    value_deserializer=str,
    group_id='log'
)

if __name__ == '__main__':
  consumer.subscribe(pattern="ECOMMERCE*")

  while(True):
    records = consumer.poll(timeout_ms=100)

    if records:
      logger.info("Record Found!")
      for r in records:
        print(r)
        time.sleep(3)