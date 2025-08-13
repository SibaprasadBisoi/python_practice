import psutil
import subprocess
import datetime
log_file = "C:/store/logs"
def log_message(message):
    time_stamp = datetime.now().strftime('%Y%m%d-%H%M%S')
    with open("log_file", 'r')as f:
        f.write(f"[{time_stamp}] {message}\n")
    print(f"[{time_stamp}] {message}")
def check_system_usage():
    cpu_percent = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage()
    log_message(f"CPU usage: {cpu_percent}%")
    log_message(f"Memory usage: {mem.percen}% ({mem.used // (1024**2)}MB / {mem.total // (1024**2)}MB )")
    log_message(f"Disk usage: {disk.percent}%")
