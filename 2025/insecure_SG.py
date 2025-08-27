import boto3

def find_open_security_groups():
    ec2 = boto3.client("ec2")

    response = ec2.describe_security_groups()
    insecure_groups = []