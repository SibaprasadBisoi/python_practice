import boto3
from datetime import datetime, timezone, timedelta
ec2 = boto3.client('ec2')
cutoff = datetime.now(timezone.utc) - timedelta(days=7)
reservations = ec2.describe_instances()["Reservations"]
stale_instances = []