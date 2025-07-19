import subprocess
from datetime import datetime
services = ["nginx", "docker", "sshd", "mysql"]
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
    except Exception as e:
        return f"error: {str(e)}"
if __name__ == "__main__":
    log("Checking critical services statuses...")
    for svc in services:
        status = check_service(svc)
        if status == "active":
            log(f"{svc} is running")
        elif status == "inactive":
            log(f"{svc} is not running")
        elif "error" in status:
            log(f'Error checking {svc}: {status}')
        else:
            log(f"Unknown status for {svc}: {status}")