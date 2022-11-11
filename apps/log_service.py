from models.kafka_service import KafkaService


if __name__ == '__main__':
  pattern = "ECOMMERCE*"
  log_service = KafkaService(topics=pattern, group_id="log")
  log_service.run()
