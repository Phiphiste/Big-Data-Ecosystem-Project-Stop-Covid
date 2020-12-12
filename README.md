# Big Data Ecosystem Project

## About the project

The project has to focus on Open Source distributed systems.
It may be a **technical project** that can be installing a stack of technologies and/or writing code to process data on the stack. It has to include the implementation: code, configuration files. In this case:
- The code has to be hosted on a **Git repository**
- The code has to be **documented** (READMEs, inline comments)
- The **project report** has to include a clear description of the project, the steps to implement it and a list of problems encountered

## Objectives

The objective is to reproduce a kind of **"Stop Covid"** application, based on positions.

A database is filled with **people positions**, **phone number** and **health status**. It is constantly update (randomly change a bit the positions of people). Then it checks if some people met and based on their health status, update each others status.

List of possible health status:
- **0: No problem**.
- **1: Suspicious**
- **2: Got the virus**

Every interaction with someone "1" or "2" will lead to become a "1". And the person will be notified and asked to test herself.

This schema is possible thanks a **data streaming pipeline made with Kafka made with Python**.

## Set up

- Verify you have JRE on your computer, if not:
```
sudo apt install default-jre
```
- Download kafka .tgz file from https://kafka.apache.org/downloads
- Untar the file and go into the kafka directory
- Start the zookeeper server
```
bin/zookeeper-server-start.sh config/zookeeper.properties
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
- Now, we can run the following scripts in separeted terminals:
  - Stop_covid.py : creates and updates the database containing people informations and suspicious interactions.
  - Producer.py : send message to consumer when interaction with suspicious/infected people.
  - Consumer.py : view sent messages
```
python Stop_covid.py # can stop by pressing CTLR-C
python Producer.py
python Consumer.py
``` 

When Stop_covid.py is running it will never stop updating positions of people. If two people have same position, if one of them is 1 or 2 and the other 0, then the second one become 1.Then a msg is add to the msg_queue.txt file and the Producer can now send a message to the consumer.
You can send messages with Producer.py and verify receptions with Consumer.py.

## Sources
- How to build real-time streaming data pipelines and applications using Apache kafka ?
  - https://www.cloudiqtech.com/how-to-build-real-time-streaming-data-pipelines-and-applications-using-apache-kafka/
- Kafka-Python explained in 10 lines of code
  - https://towardsdatascience.com/kafka-python-explained-in-10-lines-of-code-800e3e07dad1
