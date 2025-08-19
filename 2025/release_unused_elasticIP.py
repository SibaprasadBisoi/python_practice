import boto3
ec2 = boto3.client('ec2')
def relaese_unused_eips():
    addresses = ec2.describe_addresses()['Addresses']
    unused_eips = [addr['AllocationId'] for addr in addresses if "InstanceID" not in addr]
    if unused_eips:
        print(f"Found {len(unused_eips)} unsed Elastic Ip's")
        for eip in unused_eips:
            print(f"Releasing eip with allocationID: {eip}")
            ec2.release_address(AllocationId=eip)
    else:
        print(f"No eips found!")
if __name__=="__main__":
    relaese_unused_eips()