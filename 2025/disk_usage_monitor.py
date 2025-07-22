import os
import shutil
import platform
from datetime import datetime
threshold = 70
target_path = "c://" if platform.system() == "windows" else "/"
def check_disk_usage(path):
    total, used, free =shutil.disk_usage(path)
    percent_used = (used / total) * 100
    return round(percent_used, 2), total, used, free
def log(alert_msg):
    timestamp = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    print(f"[{timestamp}] {alert_msg}")
if __name__ == "__main__":
    usage_percent, total, used, free = check_disk_usage(target_path)
    log(f'disk usage for {target_path} is {usage_percent} is used')
    if usage_percent > threshold:
        log(f"Disk usage is critical, warning!")
    else:
        log(f"Disk uasge is within limit")
