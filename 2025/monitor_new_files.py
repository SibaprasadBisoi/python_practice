import os
import time
from datetime import datetime
path = "c:\logs"
log_file = os.path.join(path, "files_event.log")
known_files = set(os.listdir(path))
print(f"Monitoring log files {path}")
print(f"Logging to : {log_file}")


