import boto3
from datetime import datetime, timezone, timedelta
logs = boto3.client('logs')
log_group = "aws/lambda/my-function"
log_stream = "2025/08/16/[$LATEST]abcd1234efgh5678"
end_time = int(datetime.now(timezone.utc).timestamp() * 1000)
start_time = int((datetime.now(timezone.utc) - timedelta(minutes=15)).timestamp() * 1000)
response = logs.get_log_events(
    logGroupName = log_group,
    logStreamName = log_stream,
    startTime = start_time,
    endTime = end_time,
    startFromHead = True
)
print(f"Recent logs from cloudwatch")
for event in response['events']:
    timestamp = datetime.formattimestamp(event["timestamp"]/1000, tz = timezone.utc)
    print(f"[{timestamp}] {event['messsage'].strip()}")
