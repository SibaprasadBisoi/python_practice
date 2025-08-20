import boto3
ec2 = boto3.client('ec2')
def cleanup_unused_sgs():
    all_sgs = ec2.describe_security_groups()["SecurityGroups"]
    interfaces = ec2.describe_network_interfaces()["NetworkInterfaces"]
    used_sgs = set()
    for iface in interfaces:
        for sg in iface["Groups"]:
            used_sgs.add(sg["GroupId"])