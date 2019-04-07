# Best Practices and Tips Exercises

This section does not include any exercises, but several examples you may use
as references to build better containers and improve your experience while
working with them.

---

## Multi-stage build

[multi-stage build](./multi-stage/)


## Read-only Container

[Use tmpfs mounts](https://docs.docker.com/v17.12/storage/tmpfs/)


**Read Only Example**
```
docker run -d -p 80:80 --read-only \
--tmpfs /run:rw,noexec,nosuid,size=1m \
--tmpfs /var/cache/nginx:rw,noexec,nosuid,size=5m \
nginx:stable-alpine
```


## Capabilities

[List of Linux Capabilities](http://man7.org/linux/man-pages/man7/capabilities.7.html)
[Article on Container Capabilities](https://www.redhat.com/en/blog/secure-your-containers-one-weird-trick)

| Command                                | Description                                  |
|----------------------------------------|----------------------------------------------|
|  `docker run --cap-add <capabilitity>` | Adds a capability to a container context.    |
| `docker run --cap-drop <capabilitity>` | Drops a capability from a container context. |



## Cleaning up

| Command                              | Description                                                              |
|--------------------------------------|--------------------------------------------------------------------------|
| `docker container prune < --force >` | Remove all stopped containers. Optional: --force removes ALL containers. |
| `docker images prune < --force >`    | Removes all unused images. Optional: --force removes ALL images.         |
| `docker system prune < --force >`    | Removes all unused data. Optional: --force removes EVERYTHING.           |