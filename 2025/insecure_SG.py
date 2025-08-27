import boto3

def find_open_security_groups():
    ec2 = boto3.client("ec2")

    response = ec2.describe_security_groups()
    insecure_groups = []

    for sg in response['SecurityGroups']:
        group_name = sg['GroupName']
        group_id = sg['GroupId']

        for perm in sg.get("IpPermissions", []):
            from_port = perm.get("FromPort")
            to_port = perm.get("ToPort")

            for ip_range in perm.get("IpRanges", []):
                cidr = ip_range.get("CidrIp")
                if cidr == "0.0.0.0/0":
                    insecure_groups.append({
                        "GroupId": group_name,
                        "GroupName": group_name,
                        "FromPort": from_port,
                        "ToPort": to_port
                    })
    return insecure_groups


