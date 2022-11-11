from utils.custom_logging import CustomLogger
from kafka import KafkaProducer
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
    elif isinstance(value, dict):
      self.producer = KafkaProducer(
        bootstrap_servers=['localhost:9092'],
        key_serializer=str.encode,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
      )
    else:
      raise ValueError(f"Unsupported value format: {value}")
  
  def send(self):
    logger = CustomLogger().get_logger()

    for i in range(10):
      future_record = self.producer.send(self.topic, value=self.value, key=self.key).get(timeout=60)
      logger.info(f"SUCCESS! Order sent to {future_record.topic} | PARTITION {future_record.partition}")
