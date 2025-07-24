import os
from datetime import datetime
path = "c:/logs"
os.makedirs(path, exist_ok=True)
log_path = os.path.join(path, "build.log")
def log(msg):
    '''write a message'''
    timestamped_msg = (f"[{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}] {msg}")
    return timestamped_msg
build_status = input("enter the build status: ").strip().lower()
if build_status == "completed":
    with open(log_path, 'a')as file:
        file.write(log('Build completed'))        
else:
    log(f'Build status is unknown: {build_status}')