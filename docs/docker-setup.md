# Docker Setup


### Starting Kafka-server
```bash
docker-compose up -d
```


### Creating topics
```bash
docker exec broker \
kafka-topics --bootstrap-server broker:9092 --create --if-not-exists --topic ECOMMERCE_SEND_EMAIL
```
