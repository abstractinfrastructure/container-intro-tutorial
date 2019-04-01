# Storage

### Container Volumes

| Command                               | Description        |
|---------------------------------------|--------------------|
| `docker volume ls`                    | Lists volumes.     |
| `docker volume create <volume name>`  | Creates a volume.  |
| `docker volume inspect <volume name>` | Inspects a volume. |
| `docker volume rm <volume name>`      | Removes a volume.  |

### Using Container Volumes

| Command                                           | Description                               |
|---------------------------------------------------|-------------------------------------------|
| `docker run -d -v <host path>:<container path>`   | Mounts a host directory into a container. |
| `docker run -d -v <volume name>:<container path>` | Mounts a volume into a container.         |