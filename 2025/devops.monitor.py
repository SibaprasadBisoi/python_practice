import psutil
import subprocess
import datetime
log_file = "C:/store/logs"
def log_message(message):
    time_stamp = datetime.now().strftime('%Y%m%d-%H%M%S')
    with open("log_file", 'r')as f:
        f.write(f"[{time_stamp}] {message}\n")
    print(f"[{time_stamp}] {message}")
    