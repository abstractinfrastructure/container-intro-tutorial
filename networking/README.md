# Networking

### Exposing a Workload

| Command                                              | Description                                           |
|------------------------------------------------------|-------------------------------------------------------|
| `docker run -d -p [ip]:<host port>:<container port>` | Expose a port from a container to a port on the host. |


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


---

## Exercise 1

- Use either the `mynginx` image from the [Images exercises] or pull the image
  `nginx:stable-alpine` to create a daemonized container.
   - It should listen on `127.0.0.1`
   - It should and maps port `8080` from the host to port `80` of the container.
- Get the status of the container and note the address in the `PORTS` field.
- Verify the container is exposed on port 8080 by visiting the address listed
  in the container's status.
- Stop and delete the container.

[[Solution](./solutions.md#exercise-1)]

## Exercise 2

- Create a new `bridge` (default) network called `mynetwork`.
- List the networks and ensure it is configured correctly.
- Start a named container on the network using the same image as the previous
  exercise and call it `webserver`.
- Start an interactive container attached to the `mynetwork` network using the
  `alpine` image. It's command should be `/bin/sh`
  - From within the container perform the following:
    - ping `webserver`
    - Execute: `echo -e "GET http://webserver HTTP/1.1\nHost:webserver\n" | nc webserver 80`
      (Uses netcat (`nc`) in a fashion similar to curl)
  - Exit and remove the interactive container.

[[Solution](./solutions.md#exercise-2)]

## Exercise 3

- Remove the network `mynetwork`. **HINT:** This may involve more than just
  deleting the network.

[[Solution](./solutions.md#exercise-3)]