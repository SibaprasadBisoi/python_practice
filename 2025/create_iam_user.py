import boto3
import json
iam = boto3.client('iam')
username = "interviewer"
policyname = "DevopsS3fullaccess"
policy_document = {
    "Version": "2025-08-08",
    "statement": [
        {
        "Effect": "Allow",
        "Action": ["s3.*"],
        "Resourc": "*"
        }
    ]
}
try:
    print(f"Creating iam user: {username}")
    iam.creat_user(UserName=username)
    print(f"User created successfully!")
    print(f"Attaching inline policy {policyname}")
    iam.put_user_policy(UserName=username,
                        PolicyName = policyname,
                        PolicyDocument= json.dumps(policy_document))
    print(f"inline policy attached successfully!")
except Exception as e:
    print(f"Error: {e}")

