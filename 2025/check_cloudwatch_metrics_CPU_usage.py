import boto3
from datetime import datetime, timezone, timedelta
ec2 = boto3.client('ec2')
cloudwatch = boto3.client('cloudwatch')
def stop_idle_instances():
    reservations = ec2.describe_instances(
        Filters = [{"Name": "Instance-state-name", "Values": ["running"]}]
    )["Reservations"]
    for reservation in reservations:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            end_time = datetime.now(timezone.utc)
            start_time = end_time - timedelta(days= 7)
            
