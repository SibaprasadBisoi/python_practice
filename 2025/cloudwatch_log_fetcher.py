import boto3
from datetime import datetime, timezone, timedelta
logs = boto3.client('logs')
log_group = "aws/lambda/my-function"
log_stream = "2025/08/16/[$LATEST]abcd1234efgh5678"
