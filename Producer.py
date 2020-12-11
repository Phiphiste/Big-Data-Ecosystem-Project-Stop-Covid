from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
#with open('inputext.txt') as f:
 #    lines = f.readlines()
print(producer.send('stopcovid',b'message').get(timeout=30))
#for line in lines:
#   producer.send('test', line)
