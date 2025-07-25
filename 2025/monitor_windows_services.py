import subprocess
from datetime import datetime
services = [
    "Docker Desktop service",
    "MSSQLSERVER",
    "W3SVC",
    "Spooler"
]
def log(msg):
    print(f"[{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}] {msg}")
def check_service_status(service_name):
    """Returns the status of windows service"""
    try:
        result = subprocess.run(
            ["sc", "qurry", service_name],
            stdout= subprocess.PIPE,
            stderr= subprocess.PIPE,
            text= True
        )
        if "RUNNING" in result.stdout:
            return "RUNNING"
        elif "STOPPED" in result.stdout:
            return "STOPPED"
        else:
            return "UNKNOWN"
    except Exception as e:
        return f"Error: {e}"
if __name__ == "__main__":
    log("Checking windows service status" )
    for svc in services:
        status = check_service_status(svc)
        if status == "RUNNING":
            log(f"{svc} is running")
        elif status == "STOPPED":
            log(f"{svc} is STOPPED")
        else:
            log(f"Unable to determine the status of {svc}: {status}")
            
