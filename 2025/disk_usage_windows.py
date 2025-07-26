import os
import shutil
target_path = "c://" 
threshold_percentage = 80
total, used, free = shutil.disk_usage(target_path)
print(f"total disk space is: {total} and used is: {used} and free space is {free}")
used_in_percentage = round((used / total) * 100)
print(f"Total used space in percentage is: {used_in_percentage}")