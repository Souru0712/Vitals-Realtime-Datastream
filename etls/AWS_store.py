import boto3
from utils.constants import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION, AWS_BUCKET_NAME

def connect_to_AWS():
    s3 = boto3.resource(
        service_name = 's3',
        region_name= AWS_REGION,
        aws_access_key_id= AWS_ACCESS_KEY_ID,
        aws_secret_access_key= AWS_SECRET_ACCESS_KEY
    )
    return s3

def print_all_buckets(s3:boto3.resource):
    for bucket in s3.buckets.all():
        print(bucket.name)

def upload_to_bucket(file_name:str, s3:boto3.resource, s3_name: str):
    s3.Bucket(AWS_BUCKET_NAME).upload_file(
        Filename= file_name,
        Key= s3_name
    )