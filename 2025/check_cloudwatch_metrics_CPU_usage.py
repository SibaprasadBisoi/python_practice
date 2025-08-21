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
            metrics = cloudwatch.get_metic_statistics(
                Namespace = "AWS/EC2",
                MetricName = "CPUUtilization",
                Dimensions = [{"Name": "InstanceId", "Value": instance_id}],
                StartTime = start_time,
                EndTime = end_time,
                Period = 86400,
                Statistics =["Average"]
            )
            datapoints = metrics.get["Datapoints", []]
            if datapoints:
                avg_cpu = sum(dp["Average"] for dp in datapoints) / len(datapoints)
                print(f"instance {instance_id} - Avg cpu {avg_cpu:.2f}%")
                if avg_cpu < 2:
                    print(f"stopping idle instances: {instance_id}")
                    ec2.stop_instances(InstanceIds=[instance_id])
            else:
                print(f"No cpu data for instance: {instance_id}")
if __name__=="__main__":
    stop_idle_instances()

