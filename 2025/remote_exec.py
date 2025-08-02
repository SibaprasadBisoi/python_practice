import paramiko
hostname = "192.168.1.10"
port = 22
username = "ubuntu"
password = "password"
remote_command = "uptime"
try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko, autoAddPolicy())
    print(f"Connecting to {hostname}....")
    ssh.connect(hostname, port, username, remote_command)
    print(f"Running remote command: {remote_command}")
    stdin, stdout, stderr = ssh.exec_command(remote_command)
    output = stdout.read().decode()
    error = stderr.read().decode()
    if output:
        print(f"[OUTPUT]\n{output}")
    if error:
        print(f"[ERROR]\n{error}")
except Exception as e:
    print(f"[Exception]\n str{e}")
