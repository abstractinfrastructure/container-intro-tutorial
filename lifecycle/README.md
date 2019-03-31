# Container Lifecycle

This tutorial covers the basics of running and using Docker. It mirrors
the examples used in the presentation and can be used as a reference when
following along. Skip to the [additional exercises] if you are comfortable with
the syntax.

- [Running a Container](#running-a-container)
  - [Running a Container Interactively](#running-a-container-interactively)
  - [Running a Container Daemonized](#running-a-container-daemonized)
- [Starting and Stopping a Container](#starting-and-stopping-a-container)
- [Viewing Container Logs](#viewing-container-logs)
- [Cleaning Up](#cleaning-up)
- [Additional Exercises](#Additional-exercises)
- [Links and References](#links-and-references)

---

## Running a Container

Containers can be [run] several different ways. The easiest to run a container
in the foreground using the the syntax `docker run <options> <image> <command>`.
Take the below example:

**Command:**
```
# docker run <options> <image> <command>
docker run alpine echo hello from alpine!
```

The docker daemon is instructed to create an instance of the `alpine` image and
execute the command `echo hello from alpine!` from within it.

**Output:**
```
$ docker run alpine echo hello from alpine!
hello from alpine!
```
The instance is running just long enough to run the command and exit.

The status of the container can be verified with the `docker ps` command. [PS]
is short for [process status] and serves a similar purpose to the classic
linux/unix command. It displays containers that are currently running.

**Command:**
```
docker ps
```
**Output:**
```
$ docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                      PORTS               NAMES
```

As the container is not currently running, the `-a` or `--all` flag must be
passed to view all containers, including those that are no longer running.

**Command:**
```
docker ps -a
```
**Output:**
```
$ docker ps -a
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                      PORTS               NAMES
c6ddaad1d6e4        alpine              "echo hello from alp…"   10 minutes ago      Exited (0) 10 minutes ago                       upbeat_archimedes
```

The container was created giving it a unique ID (`c6ddaad1d6e4`) and assigned a
randomly generated friendly name (`upbeat_archimedes`). It then executed the
command "`echo hello from alpine!`"and exited successfully (`0`).


### Running a Container Interactively

Just running a single command and terminating is not always useful. You can
optionally run the container in interactive mode by supplying the `-i`
(`--interactive`) and `-t` (`--tty`) flags. Those flags combined will spawn the
container in interactive mode and attach a what is known as a [psudotty]
allowing you to interact with it as if you had just spawned a new shell session.

The below example starts an interactive (`-i -t`) `alpine` based container with
the  command `/bin/sh` and looks at the hostname, user and os-release
information found within the running container.

**Command:**
```
# docker run -i -t <options> <image> <command>
docker run -i -t alpine /bin/sh
```
**Session:**
```
$ docker run -it alpine /bin/sh
/ # hostname
accd7e14ae5a
/ # whoami
root
/ # cat /etc/os-release
NAME="Alpine Linux"
ID=alpine
VERSION_ID=3.9.2
PRETTY_NAME="Alpine Linux v3.9"
HOME_URL="https://alpinelinux.org/"
BUG_REPORT_URL="https://bugs.alpinelinux.org/"
/ # exit
$
```

View the status of the containers and be sure to view all.

**Command:**
```
docker ps -a
```
**Output:**
```
$ docker ps -a
CONTAINER ID        IMAGE               COMMAND                  CREATED              STATUS                          PORTS               NAMES
accd7e14ae5a        alpine              "/bin/sh"                About a minute ago   Exited (0) About a minute ago                       trusting_tharp
c6ddaad1d6e4        alpine              "echo hello from alp…"   12 minutes ago       Exited (0) 12 minutes ago                           upbeat_archimedes
```

The container was created and given the ID `accd7e14ae5a` which also served as
its hostname. Once the container was created, the session was attached to and
could be used interactively.


### Running a Container Daemonized

Daemonized containers are the most frequently used type of containers. They are
used to run a _"daemon"_ or long-running _"detached"_ background service. To
daemonize a container, use the `-d` or `--detach` flag.

**Command:**
```
# docker run -d <options> <image> <command>
docker run -d -p 80:80 nginx:stable-alpine
```

This example creates a daemonized container and maps port 80 from the container
to port 80 on the host. Mapping ports and other networking examples will be
explored in the [networking] section.

**Output:**
```
$ docker run -d -p 80:80 nginx:stable-alpine
Unable to find image 'nginx:stable-alpine' locally
stable-alpine: Pulling from library/nginx
8e402f1a9c57: Pull complete
c797cfb922b7: Pull complete
b691d0a030cb: Pull complete
401ca65c99ae: Pull complete
Digest: sha256:b67e90a1d8088f0e205c77c793c271524773a6de163fb3855b1c1bedf979da7d
Status: Downloaded newer image for nginx:stable-alpine
25cb0f5ceae44ab9f9a87b7c511be629d026d51caf183f0d1e0e3dcd365203f4
```

As the `nginx:stable-alpine` image is not found locally, it is pulled and
cached. The container is then created and daemonized. It can then be accessed
by visiting `localhost` (http://localhost).

It can also be verified as running by viewing the status, this time `-a` can
be omitted as it is a running container.

**Command:**
```
docker ps
```
**Output:**
```
docker ps
CONTAINER ID        IMAGE                 COMMAND                  CREATED             STATUS              PORTS                NAMES
25cb0f5ceae4        nginx:stable-alpine   "nginx -g 'daemon of…"   29 minutes ago      Up 29 minutes       0.0.0.0:80->80/tcp   goofy_stonebraker
```

Note it's status. The container is still running unlike the others that were
executed previously.


## Starting and Stopping a Container

Containers that are daemonized run independently and need to be started or
stopped manually. They do not just run and terminate as did running a command
or interactive container.

The previous container (`goofy_stonebraker`) should still be running from the
previous example. It can be stopped using the `docker stop` command.
**Command:**
```
# docker stop  <container name | container ID>
docker stop goofy_stonebraker
```
**Output:**
```
$ docker stop goofy_stonebraker
goofy_stonebraker
```
There isn't much output when starting or stopping a container, just a simple
message with the container name informing you it has been completed.

View it's status once again (remember to pass `-a` this time).

**Command:**
```
docker ps -a
```
**Output:**
```
CONTAINER ID        IMAGE                 COMMAND                  CREATED             STATUS                      PORTS               NAMES
25cb0f5ceae4        nginx:stable-alpine   "nginx -g 'daemon of…"   About an hour ago   Exited (0) 22 seconds ago                       goofy_stonebraker
```

It's status is now `Exited`.

It can be started back up with the `start` command.

**Command:**
```
# docker start  <container name | container ID>
docker start goofy_stonebraker
```
**Output:**
```
$ docker start goofy_stonebraker
goofy_stonebraker
```

It's status can be verified by getting the container status list.

**Command:**
```
docker ps
```
**Output:**
```
$ docker ps
CONTAINER ID        IMAGE                 COMMAND                  CREATED             STATUS              PORTS                NAMES
25cb0f5ceae4        nginx:stable-alpine   "nginx -g 'daemon of…"   About an hour ago   Up 32 seconds       0.0.0.0:80->80/tcp   goofy_stonebraker
```

The container (`goofy_stonebraker`) should now be started back up.


## Viewing Container Logs

The most common logging pattern for containers is to send the logs to
[`stdout` and `stderr`]. Doing so allows you to view the logs of the container
with the Docker cli.

To view the logs, use the `docker log` command and supply it either the
container name or container ID.

**Command:**
```
# docker logs <container name | container ID>
docker logs goofy_stonebraker
```
**Output:**
```
$ docker logs goofy_stonebraker
172.17.0.1 - - [31/Mar/2019:15:41:43 +0000] "GET / HTTP/1.1" 200 612 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36" "-"
172.17.0.1 - - [31/Mar/2019:15:41:43 +0000] "GET /favicon.ico HTTP/1.1" 404 571 "http://localhost/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36" "-"
2019/03/31 15:41:43 [error] 8#8: *1 open() "/usr/share/nginx/html/favicon.ico" failed (2: No such file or directory), client: 172.17.0.1, server: localhost, request: "GET /favicon.ico HTTP/1.1", host: "localhost", referrer: "http://localhost/"
2019/03/31 16:42:42 [error] 6#6: *1 open() "/usr/share/nginx/html/favicon.ico" failed (2: No such file or directory), client: 172.17.0.1, server: localhost, request: "GET /favicon.ico HTTP/1.1", host: "localhost", referrer: "http://localhost/"
172.17.0.1 - - [31/Mar/2019:16:42:42 +0000] "GET /favicon.ico HTTP/1.1" 404 571 "http://localhost/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36" "-"
172.17.0.1 - - [31/Mar/2019:16:42:42 +0000] "GET / HTTP/1.1" 200 612 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36" "-"
2019/03/31 16:42:42 [error] 6#6: *1 open() "/usr/share/nginx/html/favicon.ico" failed (2: No such file or directory), client: 172.17.0.1, server: localhost, request: "GET /favicon.ico HTTP/1.1", host: "localhost", referrer: "http://localhost/"
172.17.0.1 - - [31/Mar/2019:16:42:42 +0000] "GET /favicon.ico HTTP/1.1" 404 571 "http://localhost/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36" "-"
172.17.0.1 - - [31/Mar/2019:16:42:43 +0000] "GET / HTTP/1.1" 200 612 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36" "-"
172.17.0.1 - - [31/Mar/2019:16:42:43 +0000] "GET /favicon.ico HTTP/1.1" 404 571 "http://localhost/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36" "-"
2019/03/31 16:42:43 [error] 6#6: *1 open() "/usr/share/nginx/html/favicon.ico" failed (2: No such file or directory), client: 172.17.0.1, server: localhost, request: "GET /favicon.ico HTTP/1.1", host: "localhost", referrer: "http://localhost/"
172.17.0.1 - - [31/Mar/2019:16:42:43 +0000] "GET / HTTP/1.1" 200 612 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36" "-"
2019/03/31 16:42:43 [error] 6#6: *1 open() "/usr/share/nginx/html/favicon.ico" failed (2: No such file or directory), client: 172.17.0.1, server: localhost, request: "GET /favicon.ico HTTP/1.1", host: "localhost", referrer: "http://localhost/"
172.17.0.1 - - [31/Mar/2019:16:42:43 +0000] "GET /favicon.ico HTTP/1.1" 404 571 "http://localhost/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36" "-"
```

As `goofy_stonebraker` is based off the `nginx:stable-alpine` image, its output
is the nginx log.

Stop the container:

**Command:**
```
docker stop goofy_stonebraker
```
**Output:**
```
$ docker stop goofy_stonebraker
goofy_stonebraker
```
Then view the logs again.

**Command:**
```
docker logs goofy_stonebraker
```
**Output:**
```
$ docker logs goofy_stonebraker
172.17.0.1 - - [31/Mar/2019:15:41:43 +0000] "GET / HTTP/1.1" 200 612 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36" "-"
172.17.0.1 - - [31/Mar/2019:15:41:43 +0000] "GET /favicon.ico HTTP/1.1" 404 571 "http://localhost/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36" "-"
2019/03/31 15:41:43 [error] 8#8: *1 open() "/usr/share/nginx/html/favicon.ico" failed (2: No such file or directory), client: 172.17.0.1, server: localhost, request: "GET /favicon.ico HTTP/1.1", host: "localhost", referrer: "http://localhost/"
2019/03/31 16:42:42 [error] 6#6: *1 open() "/usr/share/nginx/html/favicon.ico" failed (2: No such file or directory), client: 172.17.0.1, server: localhost, request: "GET /favicon.ico HTTP/1.1", host: "localhost", referrer: "http://localhost/"
172.17.0.1 - - [31/Mar/2019:16:42:42 +0000] "GET /favicon.ico HTTP/1.1" 404 571 "http://localhost/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36" "-"
172.17.0.1 - - [31/Mar/2019:16:42:42 +0000] "GET / HTTP/1.1" 200 612 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36" "-"
2019/03/31 16:42:42 [error] 6#6: *1 open() "/usr/share/nginx/html/favicon.ico" failed (2: No such file or directory), client: 172.17.0.1, server: localhost, request: "GET /favicon.ico HTTP/1.1", host: "localhost", referrer: "http://localhost/"
172.17.0.1 - - [31/Mar/2019:16:42:42 +0000] "GET /favicon.ico HTTP/1.1" 404 571 "http://localhost/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36" "-"
172.17.0.1 - - [31/Mar/2019:16:42:43 +0000] "GET / HTTP/1.1" 200 612 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36" "-"
172.17.0.1 - - [31/Mar/2019:16:42:43 +0000] "GET /favicon.ico HTTP/1.1" 404 571 "http://localhost/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36" "-"
2019/03/31 16:42:43 [error] 6#6: *1 open() "/usr/share/nginx/html/favicon.ico" failed (2: No such file or directory), client: 172.17.0.1, server: localhost, request: "GET /favicon.ico HTTP/1.1", host: "localhost", referrer: "http://localhost/"
172.17.0.1 - - [31/Mar/2019:16:42:43 +0000] "GET / HTTP/1.1" 200 612 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36" "-"
2019/03/31 16:42:43 [error] 6#6: *1 open() "/usr/share/nginx/html/favicon.ico" failed (2: No such file or directory), client: 172.17.0.1, server: localhost, request: "GET /favicon.ico HTTP/1.1", host: "localhost", referrer: "http://localhost/"
172.17.0.1 - - [31/Mar/2019:16:42:43 +0000] "GET /favicon.ico HTTP/1.1" 404 571 "http://localhost/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36" "-"
```

 These logs are stored outside of the container and viewable even if the
 container itself is off. It is even possible to configure the Docker daemon to
 [send the logs to a variety of other log systems].


## Cleaning up

Removing containers after they have been created is straight forward.

**Command:**
```
# docker rm  <container name | container ID>
docker rm goofy_stonebraker
```
**Output:**
```
$ docker rm goofy_stonebraker
goofy_stonebraker
```

You can verify that that container has been deleted by once again checking the
container status list.

**Command:**
```
docker ps -a
```

**Output:**
```
$ docker ps -a
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
```


You can also clean up **all** stopped containers with either of the following
commands.

**Command**
```
docker container prune
<or>
docker rm $(docker ps -a -q)
```

All the containers should then be removed.

## Additional Exercises

1. Create a container using the `busybox` image and instruct it to echo:
   `Hello from busybox!`. Then view it's status using list command. **HINT:**
   Remember to view **all**. [[Solution](./solutions.md#exercise-1)]
2. Create an interactive container using the `busybox` image using `/bin/sh` for
   the shell. Then list the contents of the `/etc` directory then exit the
   container. [[Solution](./solutions.md#exercise-2)]
3. Create a daemonized container using the `busybox` image and the following
   command: `/bin/sh -c "while true; do echo hello there; sleep 2; done"` After
   a few seconds, view the logs. Then stop it and view it's status.
   [[Solution](./solutions.md#exercise-3)]
4. Using the container from exercise 3 - Start it. View it's status using the
   list command, then view it's logs. Lastly, stop it.
   [[Solution](./solutions.md#exercise-4)]
5. Delete all the containers created in these exercises.
   [[Solution](./solutions.md#exercise-5)]


## Links and References

- [docker run command][run]
- [docker ps reference][ps]



[docker hub]: https://hub.docker.com
[run]: https://docs.docker.com/engine/reference/run/
[ps]: https://docs.docker.com/engine/reference/commandline/ps/
[psudotty]: https://en.wikipedia.org/wiki/Pseudoterminal
[images tutorial]: /images/README.md
[`stdout` and `stderr`]: https://en.wikipedia.org/wiki/Standard_streams
[send the logs to a variety of other log systems]: https://docs.docker.com/config/containers/logging/configure/