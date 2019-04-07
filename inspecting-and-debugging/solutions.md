# Inspect and Debugging Solutions

## Exercise 1

**Command: Inspect Webserver Container**
```
# docker <image|network|volume> <ID>
docker inspect webserver
```

The output is a json object of the image. The IP Address field can be from either:
- `.NetworkSettings.IPAddress`
- `.NetworkSettings.Networks.bridge.IPAddress`

**Command: Inspect Formatted Output**
```
docker inspect webserver --format='{{ .NetworkSettings.IPAddress }}'
<or>
docker inspect webserver --format='{{ .NetworkSettings.Networks.bridge.IPAddress }}'
```

## Exercise 2

**Command: Execute within webserver container**
```
# docker exec <container name> <command>
docker exec webserver ps aux
```

**Output: Execute within webserver container**
```
PID   USER     TIME  COMMAND
    1 root      0:00 nginx: master process nginx -g daemon off;
    7 nginx     0:00 nginx: worker process
   35 root      0:00 ps aux
```

**Command: Interactive Session**
```
docker exec -it webserver /bin/sh
```

**Output: ps aux**
```
PID   USER     TIME  COMMAND
    1 root      0:00 nginx: master process nginx -g daemon off;
    7 nginx     0:00 nginx: worker process
   43 root      0:00 /bin/sh
   50 root      0:00 ps aux
```

**Command: Stop and Delete**
```
docker stop webserver
docker rm webserver
```

## Exercise 3

**Ouput: ps aux**
```
PID   USER     TIME  COMMAND
    1 root      0:00 /bin/sh
    7 root      0:00 ps aux
```

**Command: Reattach to Container**
```
# docker attach <container name/container ID>
docker attach webserver
```

**Output: ps aux**
```
PID   USER     TIME  COMMAND
    1 root      0:00 /bin/sh
    8 root      0:00 ps aux
```
