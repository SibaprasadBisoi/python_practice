version_file = "version.txt"
try:
    with open(version_file, 'r')as file:
        version = file.read().strip()
except FileNotFoundError:
    version = "1.0.0"
major, minor, patch = map(int(version.split('.')))
patch +=1
new_version = f"{major}.{minor}.{patch}"
with open(version_file, 'w')as f:
    f.write(new_version)
print(f"version updated from {version} to {new_version}")