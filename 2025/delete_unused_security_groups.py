import boto3
ec2 = boto3.client('ec2')
def cleanup_unused_sgs():
    all_sgs = ec2.describe_security_groups()["SecurityGroups"]
    interfaces = ec2.describe_network_interfaces()["NetworkInterfaces"]
    used_sgs = set()
    for iface in interfaces:
        for sg in iface["Groups"]:
            used_sgs.add(sg["GroupId"])
    default_sgs = {sg["GroupId"] for sg in all_sgs if sg["GroupName"] == "defautl"}
    unused_sgs = {sg for sg in all_sgs if sg["GroupId"] not in used_sgs and sg["GroupId"] not in default_sgs}
    