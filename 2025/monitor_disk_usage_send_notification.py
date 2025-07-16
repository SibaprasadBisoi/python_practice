import os
import shutil
from datetime import datetime
THRESHOLD_PERCENT = 80
MONITORED_PATH = "/"
def log(msg):
    '''sample timestamped message'''
    print(f"[{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}] {msg}")