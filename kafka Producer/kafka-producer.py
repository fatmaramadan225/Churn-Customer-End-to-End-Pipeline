# kafka_producer.py

import csv
import json
from confluent_kafka import Producer
import time
from admin2 import create_topic  # Importing the topic creation function

# Kafka Producer configuration and sending CSV data to Kafka
def produce_csv_to_kafka(broker_ip, broker_port, file_path, topic_name):
    # Create Kafka topic if not exists
    broker_url = f"{broker_ip}:{broker_port}"
    create_topic(broker_url, topic_name)
    
    # Kafka Producer configuration
    conf = {
        'bootstrap.servers': broker_url,
        'client.id': 'admin-client',
        'log.connection.close': False, 
        'group.id': 'test-group',
        'auto.offset.reset': 'earliest',
        'max.poll.interval.ms': 10000
    }
    producer = Producer(conf)

    def delivery_report(err, msg):
        if err:
            print(f'Message delivery failed: {err}')
        else:
            print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

    # Reading CSV and sending each row as a Kafka message
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            message = json.dumps(row)
            producer.produce(topic_name, key="1", value=message, callback=delivery_report)
            producer.poll(0)
            time.sleep(1)
    
    producer.flush()


if __name__ == "__main__":
    csv_file_path = 'customer_churn_dataset.csv'
    broker_ip = ''  # broker IP
    broker_port = '9092'          # Kafka broker port
    topic = 'testForProducer2'

    produce_csv_to_kafka(broker_ip, broker_port, csv_file_path, topic)
