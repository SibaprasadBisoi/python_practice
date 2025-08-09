import boto3
ec2 = boto3.cient('ec2')
ec2_list = []
ec2_dict = {}
response = ec2.describe_instances()
