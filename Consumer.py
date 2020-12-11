from kafka import KafkaConsumer
consumer = KafkaConsumer(bootstrap_servers=['localhost:9092'], auto_offset_reset='earliest')
consumer.subscribe(['stopcovid'])
for msg in consumer:
    print(msg)

