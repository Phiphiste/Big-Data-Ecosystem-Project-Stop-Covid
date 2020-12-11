# Big Data Ecosystem Project

## About the project

The project has to focus on Open Source distributed systems.
It may be a **technical project** that can be installing a stack of technologies and/or writing code to process data on the stack. It has to include the implementation: code, configuration files. In this case:
- The code has to be hosted on a **Git repository**
- The code has to be **documented** (READMEs, inline comments)
- The **project report** has to include a clear description of the project, the steps to implement it and a list of problems encountered

## Objectives

- Generate database with population informations (id, positions, phone number, health status).
- Compute interactions and update health status
- Set up data streaming with Kafka to notify probably infected people.

## Set up

- Download kafka .tgz file from https://kafka.apache.org/downloads
- Untar the file and go into the kafka directory
- Start the zookeeper server
```
bin/zookeeper-server-start.sh config/zooker.properties
```
- Start the Kafka broker
```
bin/kafka-server-start.sh config/server.properties
```
- Create a topic
```
bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic stopcovid
```
- Install kafka-python package using python package manager
```
pip install kafka-python
```
- Now, we can run the following scripts:
  - Stop_covid.py : creates and updates the database containing people informations and interactions.
  - Producer.py : send message to consumer when interaction with infected people.
  - Consumer.py : see messages and their destinators

## Sources
- How to build real-time streaming data pipelines and applications using Apache kafka ?
  - https://www.cloudiqtech.com/how-to-build-real-time-streaming-data-pipelines-and-applications-using-apache-kafka/
- Kafka-Python explained in 10 lines of code
  - https://towardsdatascience.com/kafka-python-explained-in-10-lines-of-code-800e3e07dad1
