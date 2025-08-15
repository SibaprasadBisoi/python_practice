import boto3
import json
s3 = boto3.client('s3')
buckets = s3.list_buckets()['Buckets']
report = []
