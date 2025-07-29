import os
import time
logfile = "installation.log"
keyword = ["error", "warning"]
intervals = 5
def monitor_log_file():
    print(f"Monitoring {logfile} for {keyword}")

    if not os.path.exists(logfile):
        print(f"file not found")
        return
    with open(logfile, 'r')as file:
        file.seek(0, os.SEEK_END)
        while True:
            line = file.readline()
            if not line:
                time.sleep(intervals)
                continue
            for key in keyword:
                if key in line:
                    print(f"Alert key {key} found in {line.strip()}")
if __name__ == "__main__":
    monitor_log_file()