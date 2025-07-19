import subprocess
from datetime import datetime
def log(msg):
    """prints a timestamped message"""
    print(f"[{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}] {msg}")
def check_service(service):
    """Checks if a service is active using systemctl"""
    try:
        result =  subprocess.run(
            ["systemctl", "is_active", service],
            stdout= subprocess.PIPE,
            stderr= subprocess.PIPE,
            text=True
        )
        status = result.stdout.strip()
        return status