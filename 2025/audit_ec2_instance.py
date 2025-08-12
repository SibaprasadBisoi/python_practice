import boto3
import json
ec2_client = boto3.client('ec2')
regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]
inventory = {}
for region in regions:
    ec2 = boto3.client('ec2', region_name = region)
    instances = ec2.describe_instances()
    region_instances = []
    for reservation in instances["Reservations"]:
        for instance in reservation["Instances"]:
            name_tag = next((tag["Value"] for tag in instance.get('Tags', []) if tag["Key"] == "Name"), "No-Name")
            region_instances.append({
                "InstanceID": instance["InstanceID"],
                "Name": name_tag,
                "Type": instance["InstanceType"],
                "State": instance["State"]["Name"],
                "LaunchTime": str(instance["LaunchTime"])
            })
    if region_instances:
        inventory[region] = region_instances        
            

