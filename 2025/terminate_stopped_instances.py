import boto3
from datetime import datetime, timezone, timedelta
ec2 = boto3.client('ec2')
cutoff = datetime.now(timezone.utc) - timedelta(days=7)
reservations = ec2.describe_instances()['Reservations']
stale_instances = []
for reservation in reservations:
    for instance in reservation['Instances']:
        state = instance['State']['Name']
        instance_id = instance['InstanceID']
        launch_time = instance['LaunchTime']
        if state == "Stopped" and launch_time < cutoff:
            stale_instances.append({
                "InstanceID": instance_id,
                "State": state,
                "LaunchTime": launch_time
            })
if stale_instances:
    print(f"Terminating the stale instances (Stopped > 7 days): ")
    for inst_id in stale_instances:
        print(f"Terminating the stales")
        ec2.terminate_instances(InstanceID = stale_instances)
        print(f"Termination request submitted")
else:
    print(f"No stale instances found")