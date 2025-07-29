import psutil
import time
def cpu_usage(interval=1):
    usage = psutil.cpu_percent(interval=interval)
    print(f'Cpu usage: {usage}')
if __name__ == "__main__":
    print("Checking cpu usage......")
    cpu_usage(interval=5)