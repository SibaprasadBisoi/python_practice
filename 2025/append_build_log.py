import os
from datetime import datetime
path = "c:/logs"
os.makedirs(path, exist_ok=True)
log_path = os.path.join(path, "build.log")
