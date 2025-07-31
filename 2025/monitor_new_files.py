import os
import time
from datetime import datetime
path = "c:\logs"
log_file = os.path.join(path, "files_event.log")
known_files = set(os.listdir(path))
print(f"Monitoring log files {path}")
print(f"Logging to : {log_file}")
while True:
    time.sleep(10)
    current_files = set(os.listdir(path))
    new_files = current_files - known_files
    if new_files:
        for file in new_files:
            log_msg = f"[{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}] New file detected: {file}"
            print(log_msg)
            with open(log_file, 'a')as f:
                f.write(log_msg + "\n")
    known_files = current_files
