# Container Lifecycle Exercise Solutions

## Exercise 1

Create a container using the `busybox` image and instruct it to echo:
`Hello from busybox!`. Then view it's status using list command. **HINT:**
Remember to view **all**.

**Run command:**
```
# docker run <options> <image> <command>
docker run busybox echo Hello from busybox!`
```
**Command output:**
```
Hello from busybox!
```

**Viewing the container status:**
```
docker ps -a
```

**Status output:**
```
$ docker ps -a
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                      PORTS               NAMES
db65431a9339        busybox             "echo Hello from bus…"   5 minutes ago       Exited (0) 5 minutes ago                        priceless_noyce
accd7e14ae5a        alpine              "/bin/sh"                19 minutes ago      Exited (0) 19 minutes ago                       trusting_tharp
c6ddaad1d6e4        alpine              "echo hello from alp…"   13 hours ago        Exited (0) 13 hours ago                         upbeat_archimedes
```

---

## Exercise 2

Create an interactive container using the `busybox` image using `/bin/sh` for
the command. Then list the contents of the `/etc` directory then exit the
container.

**Command:**
```
# docker run -i -t <options> <image> <command>
docker run -it busybox /bin/sh
```
**Listing the contents of `/etc`**
```
ls /etc
```

**ls output:**
```
group        hostname     hosts        localtime    mtab         network      passwd       resolv.conf  shadow
```

Exit the container by typing `exit` and pressing `Enter`.

---

## Exercise 3

Create a daemonized container using the `busybox` image and use the following
command: `/bin/sh -c "while true; do echo hello there; sleep 2; done"` After
a few seconds, view the logs. Then stop it and view it's status.

**Run command:**
```
# docker run -d <options> <image> <command>
docker run -d busybox /bin/sh -c "while true; do echo hello there; sleep 2; done"
```

**Viewing container logs:**
```
# docker logs <container name | container ID>
docker logs loving_panini
```
**Output:**
```
$ docker logs -f loving_panini
hello there
hello there
hello there
hello there
hello there
```

**Stop command:**
```
# docker stop <contaienr name | container ID>
docker stop loving_panini
```

**Stop output:**
```
$ docker stop loving_panini
loving_panini
```

---

## Exercise 4

Using the container from exercise 3 - Start it. View it's status using the
list command, then view it's logs. Lastly, stop it.

**Start command:**
```
# docker start <container name | container ID>
docker start loving_panini
```

**Start output:**
```
$ docker start loving_panini
loving_panini
```

**View status:**
```
docker ps
```

**View output:**
```
$ docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS               NAMES
c77fb79df112        busybox             "/bin/sh -c 'while t…"   8 minutes ago       Up 8 minutes                            loving_panini
```

**View logs:**
```
# docker logs <container name | container ID>
docker logs loving_panini
```

**Log output:**
```
$ docker logs loving_panini
hello there
hello there
hello there
hello there
hello there
hello there
```

**Stopping the container:**
```
docker stop loving_panini
```
**Stop output:**
```
$ docker stop loving_panini
loving_panini
```

**Viewing container status:**
```
docker ps -a
```

**Status output:**
```
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS               NAMES
c77fb79df112        busybox             "/bin/sh -c 'while t…"   8 minutes ago       Exited (137) 15 seconds ago             loving_panini
```


---

## Exercise 5

Delete all the containers created in these exercises.

**Command**
```
docker rm loving_panini
<or>
docker rm $(docker ps -a -q)
<or>
docker container prune
```