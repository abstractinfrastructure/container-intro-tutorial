# Networking

### Container Networks

| Command                                | Description                  |
|----------------------------------------|------------------------------|
| `docker network ls`                    | Lists Container networks.    |
| `docker network create <network name>` | Creates a Container network. |
| `docker network rm <network name>`     | Deletes a container network. |

### Using Container Networks

| Command                                  | Description                                         |
|------------------------------------------|-----------------------------------------------------|
| `docker run -d --network <network name>` | Starts container on supplied network.               |
| `docker run -d --name <container name>`  | Assigns the container a friendly name and dns name. |