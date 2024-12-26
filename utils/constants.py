import configparser
import os

parser = configparser.ConfigParser()
parser.read(os.path.join(os.path.dirname(__file__), '../config/config.conf'))

#AWS
AWS_ACCESS_KEY_ID = parser.get('aws', 'aws_access_key_id')
AWS_SECRET_ACCESS_KEY = parser.get('aws', 'aws_secret_access_key')
AWS_REGION = parser.get('aws', 'aws_region')
AWS_BUCKET_NAME = parser.get('aws', 'aws_bucket_name')

OUTPUT_PATH = parser.get('file_paths', 'output_path')

PORT_NUMBER = parser.get('monitor', 'port_number')
BAUDRATE = parser.get('monitor', 'baudrate')

KAFKA_BROKER = parser.get('kafka', 'kafka_broker')
VITAL_TOPIC = parser.get('kafka', 'vital_topic')
ALARM_TOPIC = parser.get('kafka', 'alarm_topic')