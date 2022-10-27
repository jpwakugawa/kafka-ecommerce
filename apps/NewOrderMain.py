import logging
import random
from kafka import KafkaProducer

logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

producer = KafkaProducer(
  bootstrap_servers=['localhost:9092'],
  key_serializer=str.encode,
  value_serializer=str.encode
)

if __name__ == '__main__':
  user_id = str(random.choice(list(range(1, 101))))

  value = "1111,2222,5555"
  future_record = producer.send("ECOMMERCE_NEW_ORDER", value=value, key=user_id).get(timeout=60)
  logger.info(f"SUCCESS! Order sent to {future_record.topic} | PARTITION {future_record.partition}")

  email = "Welcome! We are processing your order!" 
  future_record = producer.send("ECOMMERCE_SEND_EMAIL", value=email, key=user_id).get(timeout=60)
  logger.info(f"SUCCESS! Email sent to {future_record.topic} | PARTITION {future_record.partition}")