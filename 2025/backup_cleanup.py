import os
import shutil
import tarfile
from datetime import datetime, timedelta
import time
source_dir = "c:/store/logs"
backup_dir = "c:/backups"
retention_days = 7