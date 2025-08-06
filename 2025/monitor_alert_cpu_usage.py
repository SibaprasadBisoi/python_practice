import psutil
import shutil
from datetime import datetime
import smtplib
# import platfrom
from email.mime.text import MIMEText
total, used, free = shutil.disk_usage("c:/")
used_in_percentage = (used / total) * 100
print(round(used_in_percentage))
cpu_usage = psutil.cpu_percent(interval=1)
print(round(cpu_usage))
memory_usage = psutil.virtual_memory()
print(memory_usage)
