## Pulling an Image

Before you can begin to run a container, it must be
[pulled and stored locally][pull]. Pulling a container image fetches it from a
remote container Registry.

Images themselves will be further explored in [images tutorial]. For now, you
just need to know how to pull an image and


Download the `alpine` image with the `docker pull` command.
```shell
docker pull alpine
```
This will pull the `alpine` image from the default registry [docker hub] and
cache it for local use.

Once complete, verify it is downloaded by listing the local images with the
`docker image ls` command.

```shell
docker image ls

```
If successful, you should see something similar to the following:

```shell
$ docker image ls
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
alpine              latest              5cb3aa00f899        3 weeks ago         5.53MB
```


- [docker pull command][pull]


[pull]: https://docs.docker.com/engine/reference/commandline/pull/