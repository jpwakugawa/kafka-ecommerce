#!/bin/bash

cd kafka
KAFKA_SERVER=localhost:9092

# Up Zookeeper
bin/zookeeper-server-start.sh config/zookeeper.properties

# Up Kafka
bin/kafka-server-start.sh config/server.properties

# Create new topic LOJA_NOVO_PEDIDO
bin/kafka-topics.sh --create --bootstrap-server $KAFKA_SERVER --replicatio-factor 1 --partitions 1 --topic LOJA_NOVO_PEDIDO

# List topics
bin/kafka-topics.sh --list --bootstrap-server $KAFKA_SERVER 

# Producer - LOJA_NOVO_PEDIDO
bin/kafka-console-producer.sh --broker-list localhost:9092 --topic LOJA_NOVO_PEDIDO

# Consumer - LOJA_NOVO_PEDIDO
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic LOJA_NOVO_PEDIDO --from-beginning