import os
import time
import boto3
from botocore.exceptions import NoCredentialsError
watch_dir = "c:/store/logs"
bucket_name = "my-devops-bucket"
upload_interval = 10
s3 = boto3.client('s3')
file_timestamp = {}
def upload_to_s3(file_path):
    try:
        filename = os.path.basename(file_path)
        s3.upload_file(file_path, bucket_name, filename)
        print(f"Uploaded {filename}")
    except FileNotFoundError:
        print(f"No files found")
    except NoCredentialsError:
        print(f"AWS credential not found")
        