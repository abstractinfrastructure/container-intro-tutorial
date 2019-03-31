# Container Lifecycle Exercise Solutions

## Exercise 1

**Command:**
```
docker run busybox echo Hello from busybox!`
```
**Output:**
```
Hello from busybox!
```

**Viewing the container status:**
```
docker ps -a
```

**Output:**
```
$ docker ps -a
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                      PORTS               NAMES
db65431a9339        busybox             "echo Hello from bus…"   5 minutes ago       Exited (0) 5 minutes ago                        priceless_noyce
accd7e14ae5a        alpine              "/bin/sh"                19 minutes ago      Exited (0) 19 minutes ago                       trusting_tharp
c6ddaad1d6e4        alpine              "echo hello from alp…"   13 hours ago        Exited (0) 13 hours ago                         upbeat_archimedes
```

## Exercise 2

**Command:**
```
docker run -it busybox /bin/sh
```
**Listing the contents of `/etc`**
```
ls /etc
```

**Output:**
```
group        hostname     hosts        localtime    mtab         network      passwd       resolv.conf  shadow
```


## Exercise 3

## Exercise 4

