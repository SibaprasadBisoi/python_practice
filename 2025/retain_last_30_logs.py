import os
import glob
import time
logs_dir = "C:/store/logs"
retention_count = 30
log_files = glob.glob(os.path.join("*.log"))
log_files.sort(key=os.path.getmtime, reverse=True)
for file in log_files[retention_count:]:
    try:
        os.removedirs(file)
        print(f"Deleted old log file: {file}")
    except Exception as e:
        print(f"Error deleting the file {file}: {e}") 
    
