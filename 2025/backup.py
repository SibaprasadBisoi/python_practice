import os
import shutil
import datetime
source = "c:/users/adminuser/downloads"
curr_time = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
destination = "d:/Backups/"
backup_file= f"{source}_backup_{curr_time}"
backup_path = os.path.join(destination,backup_file)
shutil.make_archive(backup_path, 'zip', source)
print(f"Backup of {source} is taken successfully !")