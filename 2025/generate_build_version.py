version_file = "version.txt"
try:
    with open(version_file, 'r')as file:
        version = file.read().strip()
except FileNotFoundError:
    version = "1.0.0"
