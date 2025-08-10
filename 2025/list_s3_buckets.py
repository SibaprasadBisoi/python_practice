import boto3
s3 = boto3.client('s3')
bucket_list = []
bucket_dict = {}
response = s3.list_buckets()

