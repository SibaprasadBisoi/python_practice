import subprocess
from datetime import datetime
def log(msg):
    """prints a timestamped message"""
    print(f"[{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}] {msg}")