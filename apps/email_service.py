from utils.custom_logging import CustomLogger
from kafka import KafkaConsumer
import time


class EmailService():
  logger = CustomLogger().get_logger()

  consumer = KafkaConsumer(
      bootstrap_servers='localhost:9092',
      key_deserializer=str,
      value_deserializer=str,
      group_id='email'
  )

  topics = ["ECOMMERCE_SEND_EMAIL"]
  consumer.subscribe(topics=topics)

  while(True):
    records = consumer.poll(timeout_ms=100)

    if records:
      logger.info(f"{len(records)} Records Found!")
      for r in records:
        logger.info(r)
        time.sleep(3)


if __name__ == '__main__':
  email_service = EmailService()