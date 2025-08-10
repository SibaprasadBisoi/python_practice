import boto3
s3 = boto3.client('s3')
bucket_list = []
bucket_dict = {}
response = s3.list_buckets()
for bucket in response["Buckets"]:
    bucket_name = bucket["Name"]
    object_response = s3.list_objects_v2(Bucket=bucket_name)
    object_count = object_response.get('KeyCount', 0)
    bucket_list.append({
        "BucketName": bucket_name,
        "ObjectCount": object_count
    })
    bucket_dict[bucket_name]=object_count
print(bucket_list)
print(bucket_dict)

