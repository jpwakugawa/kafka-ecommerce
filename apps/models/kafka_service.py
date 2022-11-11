from utils.custom_logging import CustomLogger
from kafka import KafkaConsumer
import random
import time


class KafkaService():
  def __init__(self, topics, group_id) -> None:
    self.topics = topics
    self.consumer = KafkaConsumer(
      bootstrap_servers='localhost:9092',
      key_deserializer=str,
      value_deserializer=str,
      group_id=group_id,
      client_id = random.choice(list(range(1, 101))),
      max_poll_records=1,
    )
    if isinstance(topics, list):
      self.consumer.subscribe(topics=self.topics)
    elif isinstance(topics, str):
      self.consumer.subscribe(pattern=self.topics)
    else:
      raise ValueError(f"Unsupported topics format: {topics}")

  def run(self):
    logger = CustomLogger().get_logger()

    while(True):
      records = self.consumer.poll(timeout_ms=100)

      if records:
        logger.info(f"{len(records)} Records Found!")
        for r in records:
          logger.info(r)
          time.sleep(3)
