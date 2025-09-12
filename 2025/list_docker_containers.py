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

