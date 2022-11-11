from utils.custom_logging import CustomLogger
from kafka import KafkaProducer
import random
import json


class KafkaDispatcher():
  def __init__(self, topic, value, key) -> None:
    self.topic = topic
    self.key = key
    self.value = value
    if isinstance(value, str):
      self.producer = KafkaProducer(
        bootstrap_servers=['localhost:9092'],
        key_serializer=str.encode,
        value_serializer=str.encode
      )
    if isinstance(value, dict):
      self.producer = KafkaProducer(
        bootstrap_servers=['localhost:9092'],
        key_serializer=str.encode,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
      )
  
  def send(self):
    logger = CustomLogger().get_logger()

    for i in range(10):
      future_record = self.producer.send(self.topic, value=self.value, key=self.key).get(timeout=60)
      logger.info(f"SUCCESS! Order sent to {future_record.topic} | PARTITION {future_record.partition}")


if __name__ == '__main__':
  order = f"Order = {str(random.randint(0, 50))} : {str(random.randint(0, 50))}"
  user_id = str(random.choice(list(range(1, 101))))
  dispatcher = KafkaDispatcher("ECOMMERCE_NEW_ORDER", value=order, key=user_id) 
  dispatcher.send()

  order = {
    "title": "day one",
    "order_number": str(random.choice(list(range(1, 101))))
  }

  user_id = str(random.choice(list(range(1, 101))))
  dispatcher = KafkaDispatcher("ECOMMERCE_NEW_ORDER", value=order, key=user_id) 
  dispatcher.send()

  user_id = str(random.choice(list(range(1, 101))))
  email = "Welcome! We are processing your order!" 
  dispatcher = KafkaDispatcher("ECOMMERCE_SEND_EMAIL", value=email, key=user_id) 
  dispatcher.send()
