import os
import shutil
import tarfile
from datetime import datetime, timedelta
import time
source_dir = "c:/store/logs"
backup_dir = "c:/backups"
retention_days = 7
def create_backup():
    timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
    backup_file = f"backup_{timestamp}.tar.gz"
    backup_path = os.path.join(backup_dir, backup_file)
    with tarfile.open(backup_path, 'w:gz')as tar:
        for src in source_dir:
            arcname = os.path.basename(src)
            print(f"Adding {src} to backup as {arcname}")
            tar.add(src, arcname=arcname)
    print(f"Backup created {backup_path}")
    return backup_path
def cleanup_old_backups():
    now = time.time()
    cutoff = now - (retention_days * 86400)
    for filename in os.listdir(backup_dir):
        filepath = os.path.join(backup_dir, filename)
        if os.path.isfile(filepath) and filename.endswith(".tar.gz"):
            if os.path.getmtime(filepath) < cutoff:
                print(f"Deleting old backup: {filepath}")
                os.remove(filepath)
if __name__ =="__main__":
    os.makedirs(backup_dir,exist_ok=True)
    print(f"Starting backup process...")
    create_backup()
    cleanup_old_backups()
    print(f"Deleted old backups")
