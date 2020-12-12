from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
with open('msg_queue.txt', 'r') as f:
	next(f)
	for line in f:
		words = line.split()
		destinator_id = words[0].encode('utf-8')
		phone_nb = words[1].encode('utf-8')
		print(producer.send('stopcovid', 
			b'Notification sent to id #'+ destinator_id + 
			b' on phone number ' + phone_nb + 
			b' about a suspiscious contagion by Covid-19.'
			).get(timeout=30))
