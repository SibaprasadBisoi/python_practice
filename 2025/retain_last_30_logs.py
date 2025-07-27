import os
import glob
import time
logs_dir = "C:/store/logs"
retention_count = 30
log_files = glob.glob(os.path.join("*.log"))
log_files.sort(key=os.path.getmtime, reverse=True)
