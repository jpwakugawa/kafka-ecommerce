<h1 align="center">Kafka-Ecommerce</h1>
<h3 align="center">
(POC) Project that simulates a ecommerce running several micro-services with Kafka.
</h3>
<p align="center">
<img src = https://img.shields.io/badge/Apache-Kafka-blue>
<img src = https://img.shields.io/badge/Python3-Language%20-brightgreen>
</p>

---

## Step-by-step (Local)
- Download Kafka Scala 2.13 at [Apache Kafka](https://kafka.apache.org/downloads)

- Extract the folder inside the project

- Start Zookeeper:
  ```bash
  bin/zookeeper-server-start.sh config/zookeeper.properties
  ```

- Start Kafka:
  ```bash
  bin/kafka-server-start.sh config/server.properties
  ```
  
- Go to **/apps** and start consumers:
  ```bash
  python3 email_service.py
  python3 fraud_detector_service.py
  python3 log_service.py
  ```
- Go to **/apps** and try sendind orders:
  ```bash
  python3 new_order_service.py
  ```

## Step-by-step (Docker)
- Start Kafka Broker and UI:
  ```bash
  docker-compose up -d
  ```

- See the process running at [Kafka UI](http://localhost:8080)

- Go to **/apps** and start consumers:
  ```bash
  python3 email_service.py
  python3 fraud_detector_service.py
  python3 log_service.py
  ```
- Go to **/apps** and try sendind orders:
  ```bash
  python3 new_order_service.py
  ```


## Resources
- [Quickstart](https://kafka.apache.org/quickstart)
- [Apache Kafka Docs](https://kafka.apache.org/documentation/)
- [Course: Apache Kafka 101](https://developer.confluent.io/learn-kafka/apache-kafka/events/)
- [Kafka-Python Docs](https://kafka-python.readthedocs.io/en/master/)
- [Kafka-Python Github](https://github.com/dpkp/kafka-python)
- [Kafka UI](https://github.com/provectus/kafka-ui)
- [Kafka Docker](https://developer.confluent.io/quickstart/kafka-docker/)
