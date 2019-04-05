# Container Lifecycle Exercise Solutions

## Exercise 1

**Command: Run the Container**
```
# docker run <options> <image> <command>
docker run busybox echo Hello from busybox!`
```
**Output**
```
Hello from busybox!
```

**Command: Container Status**
```
docker ps -a
```

**Output: Container Status**
```
$ docker ps -a
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                      PORTS               NAMES
db65431a9339        busybox             "echo Hello from bus…"   5 minutes ago       Exited (0) 5 minutes ago                        priceless_noyce
accd7e14ae5a        alpine              "/bin/sh"                19 minutes ago      Exited (0) 19 minutes ago                       trusting_tharp
c6ddaad1d6e4        alpine              "echo hello from alp…"   13 hours ago        Exited (0) 13 hours ago                         upbeat_archimedes
```

---

## Exercise 2

**Command: Run the Container**
```
# docker run -i -t <options> <image> <command>
docker run -it busybox /bin/sh
```

**Command: Listing the contents of `/etc`**
```
ls /etc
```

**Output: ls**
```
group        hostname     hosts        localtime    mtab         network      passwd       resolv.conf  shadow
```

Exit the container by typing `exit` and pressing `Enter`.

---

## Exercise 3

**Command: Run Container**
```
# docker run -d <options> <image> <command>
docker run -d busybox /bin/sh -c "while true; do echo hello there; sleep 2; done"
```

**Command: Viewing Container Logs**
```
# docker logs <container name | container ID>
docker logs loving_panini
```
**Output: Viewing Container Logs**
```
$ docker logs -f loving_panini
hello there
hello there
hello there
hello there
hello there
```

**Command: Stop Container**
```
# docker stop <contaienr name | container ID>
docker stop loving_panini
```

**Output: Stop Container**
```
$ docker stop loving_panini
loving_panini
```

---

## Exercise 4

**Command: Start Container**
```
# docker start <container name | container ID>
docker start loving_panini
```

**Output: Start Container**
```
$ docker start loving_panini
loving_panini
```

**Command: View Status**
```
docker ps
```

**Output: View Status**
```
$ docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS               NAMES
c77fb79df112        busybox             "/bin/sh -c 'while t…"   8 minutes ago       Up 8 minutes                            loving_panini
```

**Command: View logs**
```
# docker logs <container name | container ID>
docker logs loving_panini
```

**Output: View Logs**
```
$ docker logs loving_panini
hello there
hello there
hello there
hello there
hello there
hello there
```

**Command: Stopping the Container:**
```
# docker stop <contaienr name | container ID>
docker stop loving_panini
```

**Command: View Status**
```
docker ps -a
```

**Output: Status**
```
$ docker ps -a
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS               NAMES
c77fb79df112        busybox             "/bin/sh -c 'while t…"   8 minutes ago       Exited (137) 15 seconds ago             loving_panini
```


---

## Exercise 5

**Command: Remove Container**
```
# docker rm <container name/container ID>
docker rm loving_panini
<or>
docker rm $(docker ps -a -q)
<or>
docker container prune
```

**Output: Remove container**
```
docker rm loving_panini
loving_panini
```