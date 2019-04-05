# Storage


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

- From within the storage directory create a container that does the following:
  - Uses the `nginx:stable-alpine` image.
  - Binds to `127.0.0.1`.
  - Maps the host port `8080` to container port `80`
  - Name the container `webserver`.
  - Mounts the `data` directory on the host to `/usr/share/nginx/html` in the
    container as read-only(`ro`). **HINT:** Use the absolute host path.
- Visit http://127.0.0.1:8080 and note the message.
- Verify it is mounted read-only by executing the following command:
  `docker exec webserver /bin/sh -c "echo Hello > /usr/share/nginx/html/index.html"`
- Edit `data/index.html` and replace "Welcome to nginx!" with "Hello there!"
- Visit http://127.0.0.1:8080 and note the change.
- Do **not** stop or delete the container if moving onto Exercise 2.


## Exercise 2

- From within the storage directory create a container that does the following:
  - Uses the `alpine` image.
  - Name the container `writer`.
  - Mounts the `data` directory on the host to `/html` as read-write (`rw`).
    **HINT:** Use the absolute host path.
  - It should execute the following command:
    `/bin/sh -c "while true; do date >> /html/index.html; sleep 5; done"`
- Visit http://127.0.0.1:8080 and note the change.
- Stop and delete both the `writer` and `webserver` containers.


## Exercise 3

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



