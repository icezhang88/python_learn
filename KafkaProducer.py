from kafka import KafkaProducer
import json

producer = KafkaProducer(bootstrap_servers=['39.98.161.145:9092'], value_serializer=lambda m: json.dumps(m).encode('ascii'))
future = producer.send('my_topic' ,  value= 'aaaaaaaaaa', partition= 0)
future.get(timeout= 10)

