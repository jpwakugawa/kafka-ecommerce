from kafka_service import KafkaService

if __name__ == '__main__':
  topics = ["ECOMMERCE_SEND_EMAIL"] 
  email_service = KafkaService(topics=topics, group_id="email")
  email_service.run()
