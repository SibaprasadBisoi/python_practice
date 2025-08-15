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
    try:
        policy = s3.get_bucket_policy(Bucket=bucket_name)
        policy_json = json.loads(policy["Policy"])
        for statement in policy_json.get("Statement", []):
            if statement.get("Effect")=="Allow":
                principal = statement.get("Principal")
                if principal == "*" or principal.get("AWS") == "*":
                    public_access = True
                    details["Reason"] = "Bucket policy allows public access"
    except s3.exceptions.NoSuchBucketPolicy:
        pass
    except Exception as e:
        print(f"Error fetching bucket policy: {e}")
    details["Public"] = public_access
    report.append(details)
    with open("s3_security_report.json", 'w') as f:
        json.dump(report, f, indent=4)
    print(f"S3 bucket acl and policy report prepared")





