import boto3
ec2 = boto3.cient('ec2')
ec2_list = []
ec2_dict = {}
response = ec2.describe_instances()
for reservation in response['Reservations']:
    for instance in reservation['instances']:
        instance_type = instance['InstanceType']
        name = None
        if 'Tags' in instance:
            for tag in instance['Tags']:
                if tag['key'] == "Name":
                    name = tag[Value]
                    break
                
