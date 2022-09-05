# big-data-process-mining

# Build images for SPARK and KAFKA
* Windows : 
```
./build-images.bat
```

* Linux:
```
./build-images.sh
```

# Create custom network

```
docker network create data-net
```

# Setup hive server

* Launch zookeeper and hive containers
```
cd hive
docker-compose up -d
```

* Open hive shell and create the *Log* Table
```
docker exec -it hive-server hive
```

```sql
CREATE DATABASE If NOT EXISTS process_mining COMMENT 'Database containing tables with event_logs and process models'
```

```sql
use process_mining;
```

```sql
CREATE TABLE If NOT EXISTS event_logs(case_concept_name STRING, case_task_de STRING, case_event_type STRING, case_user STRING, time_timestamp TIMESTAMP, case_task_type STRING, case_task_name STRING, concept_name STRING) ROW FORMAT DELIMITED FIELDS TERMINATED BY ';' STORED AS TEXTFILE;
```

```sql
CREATE TABLE If NOT EXISTS model(id STRING, start_activity STRING, end_activity STRING, updated_at TIMESTAMP)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ';' STORED AS TEXTFILE; 
```

# Setup kafka cluster and create a topic 

* Run the kafka container
```
docker-compose up -d
```

* Open kafka shell and create the topic

```
docker exec -it kafka-server bash
```

>TODO: make topic name an enviroment variable 
```
bin/kafka-topics.sh --create --topic event-logs-stream --bootstrap-server localhost:9092  
```
* check if topic is created  
```
bin/kafka-topics.sh --describe --topic event-logs-stream --bootstrap-server localhost:9092    
```

# Launch spark cluster and submit a job

* cd into apache-spark-docker folder and run  
```
docker-compose up -d  
```
* Submit your app to spark cluster
Open the spark master container's shell  
```
docker exec -it spark-master bash  
```

* Submit the app
```
bin/spark-submit --jars /opt/spark-apps/spark-streaming-kafka-0-8-assembly_2.11-2.1.0.jar /opt/spark-apps/transformer.py
```
# Lunch a consumer container 

```
docker build -t consumer .
```
```
docker-compose up -d
```

# Launch the producer 
```
docker build -t producer .
```

```
docker-compose up
```


# Try now
go to http://localhost:5000 and open the console