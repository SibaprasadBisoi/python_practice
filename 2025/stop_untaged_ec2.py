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
                
