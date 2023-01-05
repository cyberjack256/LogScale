import requests
import json

from faker import Faker
from kafka import KafkaProducer

fake = Faker()

# Kafka producer settings
kafka_topic = 'fake-logs'
kafka_server = 'localhost:9092'

producer = KafkaProducer(bootstrap_servers=kafka_server)

# HEC settings
hec_url = 'http://localhost:8088/services/collector/event'
hec_token = 'YOUR-HEC-TOKEN'

def send_log_to_kafka(log):
  """
  Sends a log to Kafka.
  """
  producer.send(kafka_topic, log.encode())

def send_log_to_hec(log):
  """
  Sends a log to Splunk HEC.
  """
  headers = {
    'Authorization': 'Splunk ' + hec_token,
    'Content-Type': 'application/json'
  }
  
  data = {
    'event': log
  }
  
  requests.post(hec_url, headers=headers, data=json.dumps(data))

# Generate fake logs and send them to Kafka and Splunk HEC
for _ in range(5):
  log = generate_fake_log(sample_log, regex)
  send_log_to_kafka(log)
  send_log_to_hec(log)

producer.flush()
