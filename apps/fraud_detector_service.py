from models.kafka_service import KafkaService


if __name__ == '__main__':
  topics = ["ECOMMERCE_NEW_ORDER"]
  fraud_detector_service = KafkaService(topics=topics, group_id="fraud_detector")
  fraud_detector_service.run()
