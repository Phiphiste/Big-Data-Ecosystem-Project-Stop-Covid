from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
with open('inputmsg.txt', 'r') as f:
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


		'''
		if int(words[0]) == 0:
			print(producer.send('stopcovid', destinator).get(timeout=30))
		elif int(words[0]) == 1:
			print(producer.send('stopcovid', b'Suspicion...').get(timeout=30))
		elif int(words[0])	== 2:
			print(producer.send('stopcovid', b'Bon bah ... salut!').get(timeout=30))	
		'''