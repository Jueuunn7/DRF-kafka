from json import dumps

from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:29092'], api_version=(0,11,5),
              value_serializer=lambda x: dumps(x).encode('utf-8'))

def send_message(msg):
    producer.send('my-topic', msg.encode())