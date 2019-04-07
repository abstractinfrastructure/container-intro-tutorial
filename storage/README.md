# Storage

Containers are inherently ephemeral. The means of persisting state is done
through exposing storage from another source (host) to locations within the
container. This is essential to running things such as databases in a container
effectively.

Use the below command references to complete the exercises.

### Using Container Volumes

| Command                                           | Description                               |
|---------------------------------------------------|-------------------------------------------|
| `docker run -d -v <host path>:<container path>`   | Mounts a host directory into a container. |
| `docker run -d -v <volume name>:<container path>` | Mounts a volume into a container.         |

### Container Volumes

| Command                               | Description        |
|---------------------------------------|--------------------|
| `docker volume ls`                    | Lists volumes.     |
| `docker volume create <volume name>`  | Creates a volume.  |
| `docker volume inspect <volume name>` | Inspects a volume. |
| `docker volume rm <volume name>`      | Removes a volume.  |


---

## Exercise 1

Create a container that mounts a volume from the host.

- From within the storage directory create a container that does the following:
  - Uses the `nginx:stable-alpine` image.
  - Binds to `127.0.0.1`.
  - Maps the host port `8080` to container port `80`
  - Name the container `webserver`.
  - Mounts the `data` directory on the host to `/usr/share/nginx/html` in the
    container as read-only(`ro`). **HINT:** Use the **absolute** host path.
- Visit http://127.0.0.1:8080 and note the message.
- Verify it is mounted read-only by executing the following command:
  `docker exec webserver /bin/sh -c "echo Hello > /usr/share/nginx/html/index.html"`
- Edit `data/index.html` and replace "Welcome to nginx!" with "Hello there!"
- Visit http://127.0.0.1:8080 and note the change.
- Do **not** stop or delete the container if moving onto Exercise 2.

Mounting directories from a specified location on the host is the most common
means of persisting data when working directly with containers. It is also
useful when developing applications as changes made on the host are immediately
reflected within the container.

[[Solution](./solutions.md#exercise-1)]

## Exercise 2

Explore how to mount persistent storage from the host to a container and its
possibilities with working with more than one at the same time.

- From within the storage directory create a container that does the following:
  - Uses the `alpine` image.
  - Name the container `writer`.
  - Mounts the `data` directory on the host to `/html` as read-write (`rw`).
    **HINT:** Use the absolute host path.
  - It should execute the following command:
    `/bin/sh -c "while true; do date >> /html/index.html; sleep 5; done"`
- Visit http://127.0.0.1:8080 and note the change.
- Stop and delete both the `writer` and `webserver` containers.

Using more than one container mounting the same volume is a common pattern.
The "writer" can be a separate container that is allowed to change the content
that the "webserver" serves up. If for some reason the "webserver" container
was compromised, the data itself could not be manipulated.

[[Solution](./solutions.md#exercise-2)]

## Exercise 3

Mount a pre-created docker volume to a container and discover how it functions
in relation to directly mounting volumes.

- Create a volume called `www-data`
- List the container volumes and verify `www-data` was created.
- Create a container that does the following:
  - Uses the `alpine` image.
  - Name the container `writer`.
  - Mounts the `www-data` volume to `/html` as read-write (`rw`).
  - It should execute the following command:
    `/bin/sh -c "while true; do date >> /html/index.html; sleep 5; done"`
- Create a container that does the following:
  - Uses the `nginx:stable-alpine` image.
  - Binds to `127.0.0.1`.
  - Maps the host port `8080` to container port `80`
  - Name the container `webserver`.
  - Mounts the `www-data` volume to `/usr/share/nginx/html` as read-only (`ro`)
- Visit http://127.0.0.1:8080 to see the content from the `writer` container.
- Delete both the `writer` and `webserver` containers.
- List the container volumes and verify `www-data` was created.
- Delete the `www-data` volume.

[[Solution](./solutions.md#exercise-3)]

It is possible for the docker daemon to be configured with different volume
drivers that allow for storing data externally in a host agnostic way, for
example on NFS. These volumes are mounted with the
`-v <voume name>:<container path>` pattern. If working strictly on one host this
method can be ignored and is often not ideal as it saves the data within a
directory outside of your own control (default: `/var/lib/docker`).
