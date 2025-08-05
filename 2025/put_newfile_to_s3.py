import os
import time
import boto3
from botocore.exceptions import NoCredentialsError
watch_dir = "c:/store/logs"
bucket_name = "my-devops-bucket"
upload_interval = 10
s3 = boto3.client('s3')
file_timestamp = {}