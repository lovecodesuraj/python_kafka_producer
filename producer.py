from kafka import KafkaProducer
import json 
import time 
from data import get_registered_user




def json_serializer(data):
    return json.dumps(data).encode('utf-8')

producer = KafkaProducer(bootstrap_servers=['19.168.160.1:9092'],
                          value_serializer=json_serializer)



if __name__ == "__main__":
    while 1==1:
        registered_user = get_registered_user()
        producer.send('python_producer_demo',registered_user)
        time.sleep(1)