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
def check_service(name):
    try:
        result = subprocess.run(["systemctl", "is_active", name], capture_output=True, text=True)
        status = result.stdout.strip()
        if status == "is_active":
            log_status(f'service {name} is runnig')
        else:
            log_status(f"service {name} is not running")
    except Exception as e:
        log_status(f"error checking the the log {name}")
if __name__ == "__main__":
    check_service(service)
