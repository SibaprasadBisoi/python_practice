import os
import subprocess
from datetime import datetime
service = "nginx"
log_dir = './logs'
os.makedirs(log_dir)
log_file = os.path.join(log_dir, "service_status.log")
def log_status(msg):
    timestamp = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    with open(log_file,'a')as file:
        file.write(f"[{timestamp}] {msg}\n")
        
