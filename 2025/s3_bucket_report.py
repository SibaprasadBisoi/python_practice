import boto3
import json
s3 = boto3.client('s3')
buckets = s3.list_buckets()['Buckets']
report = []
for bucket in buckets:
    bucket_name = bucket['Name']
    public_access = False
    details = {"Bucket": bucket_name, "Public": False, "Reason": ""}
    try:
        acl = s3.get_bucket_acl(Bucket = bucket_name)
        for grant in acl["Grants"]:
            grantee = grant.get("grantee", {})
            if grantee.get("URI") == "http://acs.amazon.com/groups/global/allusers":
                public_access = True
                details["Reason"] = "ACL allows public read/write acces"
                break
    except Exception as e:
        print("acl check failed: {e}")
