import subprocess
from datetime import datetime
services = [
    "Docker Desktop service",
    "MSSQLSERVER",
    "W3SVC",
    "Spooler"
]
def log(msg):
    print(f"[{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}] {msg}")