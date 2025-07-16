import os
import shutil
from datetime import datetime
THRESHOLD_PERCENT = 80
MONITORED_PATH = "/"
def log(msg):
    '''sample timestamped message'''
    print(f"[{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}] {msg}")
def check_disk_usage(path):
    """Returns the disk usage as a percentage"""
    total, used, free = shutil.disk_usage(path)
    percent_used = used / total * 100
    return round(percent_used ,2), total, used, free