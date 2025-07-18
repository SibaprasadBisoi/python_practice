import subprocess
from datetime import datetime
def log(msg):
    """Restart the failed containers"""
    print(f"[{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}] {msg}")

def get_exited_containers():
    """Returns list of containers exited 'ids' in exited status"""
    result = subprocess.run(["docker", "ps", "-a", "--filter", "status = exited", "--format", "{{.ID}} {{.Names}}"], 
    stdout = subprocess.PIPE,
    stderr = subprocess.PIPE, 
    text = True
    )
    containers = []
    for line in result.stdout.strip().split("\n"):
        if line:
            container_id, name = line.strip().split()
            containers.append((container_id, name))
    return containers
