import docker
def list_containers():
    client = docker.from_env()
    
    containers = client.containers.list(all=True)
    container_info = []

    for container in containers:
        container_info.append({
            "Name": container.name,
            "ID": container.short_id,
            "Status": container.status,
            "Image": container.image.tags[0] if container.image.tags else "untagged"
        })
    return container_info

if __name__ == "__main__":
    try:
        info = list_containers()
        if not info:
            print(f"No containers found")
        else: 
            print(f"Docker containers")
            for c in info:
                print(f"{c["Name"]} ({c['ID']}) | image: {c['Image']} | status: {c['status']}")
    except Exception as e:
        print(f"Error: {e}")