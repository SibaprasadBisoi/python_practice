import boto3
ec2 = boto3.client('ec2')
required_tag = "Owner"
def get_untagged_instances():
    instances = []
    response = ec2.describe_instances()

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instace_id = instance['InstanceId']
            tags = {tag['Key']: tag['Value'] for tag in instance.get("Tags, []")}
            if required_tag not in tags:
                instances.append(instace_id)
    return instances
def stop_instances(instance_ids):
    if instance_ids:
        print(f"Stop instances without {required_tag} tag: {instance_ids}")
        ec2.stop_insatnces(InstanceIds = instance_ids)
    else:
        print(f"All instances have the required tag")
if __name__ == "__main__":
    untagged_instances = get_untagged_instances()
    stop_instances(untagged_instances)

