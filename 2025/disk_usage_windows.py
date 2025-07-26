import os
import shutil
target_path = "c://" 
threshold_percentage = 80
total, used, free = shutil.disk_usage(target_path)
print(f"total disk space is: {total} and used is: {used} and free space is {free}")
used_in_percentage = round((used / total) * 100)
print(f"Total used space in percentage is: {used_in_percentage}")
if used_in_percentage >= 80:
    print(f"Disk usage is: {used_in_percentage}, so it is critical!")
elif used_in_percentage >= 70 and used_in_percentage <80:
    print(f"Disk usage is: {used_in_percentage}, so delete some old folders ")
elif used_in_percentage >= 60 and used_in_percentage < 70:
    print(f"Disk usage is: {used_in_percentage}, please optimize the data")
else: 
    print(f"Disk usage is: {used_in_percentage}, it is ideal state.")