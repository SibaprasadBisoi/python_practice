import boto3
import json
s3 = boto3.client('s3')
buckets = s3.list_buckets()['Buckets']
report = []
for bucket in buckets:
    bucket_name = bucket['Name']
    public_access = False
    details = {"Bucket": bucket_name, "Public": False, "Reason": ""}
    