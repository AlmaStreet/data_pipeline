# Data Pipeline with Kafka
This README provides step-by-step instructions on setting up and using Kafka for a data pipeline, including Kafka Python library usage and Kafka CLI (Command Line Interface) operations.

## Kafka Python
This section covers how to use the Kafka Python library to create topics and produce/consume events.
### Setup and Basic Operations
1. Install Kafka Python Library:
```
pip3 install kafka-python
```

2. Create a Kafka Topic:

Execute the admin.py script to create a topic.
```
python3 admin.py
```
3. Produce Events to the Topic:

Run the producer.py script to produce events.
```
python3 producer.py
```
4. Consume Events from the Topic:

Use the consumer.py script to start consuming events.
```
python3 consumer.py
```

## Kafka CLI
This section details how to download Kafka, start essential services, and perform basic topic and message operations using Kafka's command-line tools.

### Download and Setup Kafka
1. Download Kafka:
```
pip install wget
python3 -m wget https://archive.apache.org/dist/kafka/2.8.0/kafka_2.12-2.8.0.tgz
tar -xzf kafka_2.12-2.8.0.tgz
```

2. Start ZooKeeper:

ZooKeeper manages the Kafka cluster. Start it using:
```
cd kafka_2.12-2.8.0
bin/zookeeper-server-start.sh config/zookeeper.properties
```

3. Start Kafka Message Broker Server:
```
cd kafka_2.12-2.8.0
bin/kafka-server-start.sh config/server.properties
```

### Basic Topic and Message Operations
1. Create a Topic Named 'news':
```
cd kafka_2.12-2.8.0
bin/kafka-topics.sh --create --topic news --bootstrap-server localhost:9092
```
2. Produce Messages to Kafka:

Start a producer for the 'news' topic.
```
bin/kafka-console-producer.sh --topic news --bootstrap-server localhost:9092
```

3. Consume Messages from Kafka:

Listen to messages in the 'news' topic.
```
cd kafka_2.12-2.8.0
bin/kafka-console-consumer.sh --topic news --from-beginning --bootstrap-server localhost:9092
```

### Advanced Operations
1. Create a Topic with Multiple Partitions:
```
bin/kafka-topics.sh --bootstrap-server localhost:9092 --create --topic bankbranch --partitions 2
```

2. List All Current Topics:

Verify if 'bankbranch' has been created.
```
bin/kafka-topics.sh --bootstrap-server localhost:9092 --list

__consumer_offsets
bankbranch
news
```

3. Describe Topic Details:

Get detailed information about the 'bankbranch' topic.
```
bin/kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic bankbranch

# example output
Topic: bankbranch       TopicId: bZtBs3o8SzKGXdLSH85OZw PartitionCount: 2       ReplicationFactor: 1   Configs: segment.bytes=1073741824
        Topic: bankbranch       Partition: 0    Leader: 0       Replicas: 0     Isr: 0
        Topic: bankbranch       Partition: 1    Leader: 0       Replicas: 0     Isr: 0
```

4. Work with Consumer Groups:

Manage consumer groups and offsets.
```
# Create new consumer in group 'atm-app'
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic bankbranch --group atm-app

# Reset offsets
bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092  --topic bankbranch --group atm-app --reset-offsets --to-earliest --execute
```
