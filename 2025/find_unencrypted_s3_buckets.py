import boto3
def check_s3_encryption():
    s3 = boto3.client('s3')
    report = {}
    response = s3.list_buckets()
    buckets = [bucket['Name'] for bucket in response["Buckets"]]
    for bucket in buckets:
        try:
            enc = s3.get_bucket_encryption(Bucket=bucket)
            rules = enc['ServerSideEncryptionConfiguration']['Rules']
            report[bucket] = f"Encrypted ({rules[0]['ApplyServerSideEncryptionByDefault']['SSEAlgorithm']})"
        except s3.exceptions.ClientError as e:
            if "ServerSideConfigurationNotFoundError" in str(e):
                report[bucket] = "Not Encrypted"
            else:
                report[bucket] = f"Error checking: {str(e)}"

