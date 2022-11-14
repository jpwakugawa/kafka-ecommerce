from models.kafka_dispatcher import KafkaDispatcher
from utils.data_generator import generate_message
import random


if __name__ == '__main__':
  for i in range(5):
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

    user_id = str(random.choice(list(range(1, 101))))
    message = generate_message()
    dispatcher = KafkaDispatcher("ECOMMERCE_SEND_EMAIL", value=message, key=user_id) 
    dispatcher.send()
