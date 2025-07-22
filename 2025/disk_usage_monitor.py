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