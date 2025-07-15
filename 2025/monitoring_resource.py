import os
from datetime import datetime
import subprocess
SERVICE_NAME = "nginx"
def log(msg):
    '''Sample message logger'''
    # print(f"[{datetime.now().strftime('%m%Y%H%M%S')]{msg}")
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}")