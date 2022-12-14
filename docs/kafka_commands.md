# Tutorial


### Default Variables
KAFKA_SERVER=localhost:9092
ZOOKEEPER_SERVER=localhost:2181


### Up Kafka-Server
- Zookeeper Up
```bash
bin/zookeeper-server-start.sh config/zookeeper.properties
```

- Kafka Up
```bash
bin/kafka-server-start.sh config/server.properties
```


### Manage topics
- Create new topic LOJA_NOVO_PEDIDO
```bash
bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic LOJA_NOVO_PEDIDO
```

- Topic Flags
```bash
bin/kafka-topics.sh --bootstrap-server localhost:9092 
--list     # List Topics
--describe # Describre Topics 
```

- Alter existing partition of ECOMMERCE_NEW_ORDER to 3
```bash
bin/kafka-topics.sh --alter --bootstrap-server localhost:9092 --topic ECOMMERCE_NEW_ORDER --partitions 3
```


### Produce && Consumer
- Producer - LOJA_NOVO_PEDIDO
```bash
bin/kafka-console-producer.sh --broker-list localhost:9092 --topic LOJA_NOVO_PEDIDO
```

- Consumer - LOJA_NOVO_PEDIDO
```bash
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic LOJA_NOVO_PEDIDO --from-beginning
```


### Configure Partitions
```bash
vim config/server.properties 
```
```vim
# The default number of log partitions per topic. More partitions allow greater
# parallelism for consumption, but this will also result in more files across
# the brokers.
num.partitions=3
```


### Configure Kafka & Zookeeper Logs
- Kafka Logs
```bash
vim config/server.properties
```
```vim
############################# Log Basics #############################

# A comma separated list of directories under which to store log files
log.dirs=$YOUR_DIR
```

- Zookeeper Logs
```bash
vim config/zookeeper.properties
```
```vim
# the directory where the snapshot is stored.
dataDir=$YOUR_DIR
```
