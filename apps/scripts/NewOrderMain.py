import logging
import time
from kafka import KafkaProducer

logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

producer = KafkaProducer(
  bootstrap_servers=['localhost:9092'],
  key_serializer=str.encode,
  value_serializer=str.encode
)

if __name__ == '__main__':
  value = "1111,2222,3333"
  producer.send("ECOMMERCE_NEW_ORDER", value=value, key=value)
  time.sleep(3)