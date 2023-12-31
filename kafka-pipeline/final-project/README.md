# Data Pipeline with Kafka

This README outlines the steps for setting up and using Apache Kafka in a data pipeline. It includes instructions for starting Zookeeper and Kafka, running a toll traffic simulator, streaming data reader, and verifying data in a MySQL database.

## Prerequisites

Apache Kafka installed and configured
Python 3 with required libraries installed
MySQL server running with necessary privileges

## Setting Up MySQL Database
Before starting the data pipeline, set up the MySQL database and tables:

1. Connect to MySQL:
- Open your MySQL command line or a MySQL client.
- Log in with your credentials:
```bash
mysql -u username -p
```
2. Create the tolldata Database and livetolldata Table:
- Execute the following commands in MySQL:
```sql
Copy code
CREATE DATABASE tolldata;
USE tolldata;
CREATE TABLE livetolldata(
    timestamp DATETIME,
    vehicle_id INT,
    vehicle_type CHAR(15),
    toll_plaza_id SMALLINT
);
EXIT;
```



## Starting Zookeeper

Zookeeper is a service required by Kafka for cluster management. To start Zookeeper:

```bash
bin/zookeeper-server-start.sh config/zookeeper.properties
```
## Starting Kafka

Start the Kafka server to begin handling message queues:

```bash
bin/kafka-server-start.sh config/server.properties
```
## Running the Toll Traffic Simulator

The toll traffic simulator generates sample data for Kafka. Start it using:

```bash
python3 toll_traffic_generator.py
```
## Starting the Streaming Data Reader

The streaming data reader connects to the database and Kafka, and starts reading from defined topics:

```bash
python3 streaming_data_reader.py
```
## Verifying Data in the Database

To check the data received in the MySQL database:

1. Connect to MySQL Database:

Use the following command to connect. Replace root with your MySQL username and your_password with your actual password.
```bash
mysql --host=127.0.0.1 --port=3306 --user=root --password=your_password
```
2. Query the Database:

Once connected, run these commands to view the data:
```sql
USE tolldata;
SELECT * FROM livetolldata LIMIT 10;
```
This shows the top 10 rows from the livetolldata table.
