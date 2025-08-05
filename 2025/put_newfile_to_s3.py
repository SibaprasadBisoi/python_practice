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
while True:
    for root, dirs, files in os.walk(watch_dir):
        for file in files:
            file_path = os.path.join(root, file)
            last_modified = os.path.getmtime(file_path)
            if file_path not in file_timestamp or file_timestamp[file_path] < last_modified:
                upload_to_s3(file_path)
                file_timestamp[file_path] = last_modified
    time.sleep(upload_interval)
