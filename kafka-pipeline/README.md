# data_pipeline

## download kafka
```
pip install wget
python3 -m wget https://archive.apache.org/dist/kafka/2.8.0/kafka_2.12-2.8.0.tgz
tar -xzf kafka_2.12-2.8.0.tgz
```

## start zookeeper
ZooKeeper, as of this version, is required for Kafka to work. ZooKeeper is responsible for the overall management of Kafka cluster. It monitors the Kafka brokers and notifies Kafka if any broker or partition goes down, or if a new broker or partition goes up.
```
cd kafka_2.12-2.8.0
bin/zookeeper-server-start.sh config/zookeeper.properties
```

## start kafka message broker server
```
cd kafka_2.12-2.8.0
bin/kafka-server-start.sh config/server.properties
```

## create a topic named 'news'
```
cd kafka_2.12-2.8.0
bin/kafka-topics.sh --create --topic news --bootstrap-server localhost:9092
```

```Created topic news.```

## create a producer to send messages to Kafka
```
bin/kafka-console-producer.sh --topic news --bootstrap-server localhost:9092
```

When you see the > prompt, try the following
```
Good morning
Good day
Enjoy the Kafka lab
```

## create a consumer to read the messages from kafka
The following will listen to messages in the topic 'news'
```
cd kafka_2.12-2.8.0
bin/kafka-console-consumer.sh --topic news --from-beginning --bootstrap-server localhost:9092
```

Output
```
Good morning
Good day
Enjoy the Kafka lab
```
