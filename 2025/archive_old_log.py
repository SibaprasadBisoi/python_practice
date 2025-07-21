import os
import shutil
from datetime import datetime
import time
logs_directory = r"c:/logs"
archive_directory = r"c:/archive/logs"
days_old = 7
os.makedirs(archive_directory, exist_ok=True)
time_stamp = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
archive_name= os.path.join(archive_directory, f"archived_logs_{time_stamp}")
temp_dir = os.path.join(archive_directory, "temp_logs")
os.makedirs(temp_dir, exist_ok=True)

