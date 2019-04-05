## Container Storage Exercise Solutions

## Exercise 1

**Command: Run webserver container**
```
# docker run -d -v <host path>:<container path>:<rw/ro>
docker run -d -p 127.0.0.1:8080:80 --name webserver -v $(pwd)/data:/usr/share/nginx/html:ro nginx:stable-alpine
```

Visit http://127.0.0.1:8080 - You should see a "Welcome to nginx!" message.

**Command: Verify Read-Only**
```
docker exec webserver /bin/sh -c "echo Hello > /usr/share/nginx/html/index.html"
```

**Output: Verify Read-Only**
```
$ docker exec webserver /bin/sh -c "echo Hello > /usr/share/nginx/html/index.html"
/bin/sh: can't create /usr/share/nginx/html/index.html: Read-only file system
```

Visit http://127.0.0.1:8080 - You should see a "Hello there!" message.


## Exercise 2

**Command: Run writer container**
```
# docker run -d -v <host path>:<container path>:<rw/ro>
docker run -d -v $(pwd)/data:/html --name writer alpine /bin/sh -c "while true; do date >> /html/index.html; sleep 5; done"
```
Visit http://127.0.0.1:8080 - You should see a a timestamp below "Hello there!"

**Command: Stop and Delete Containers**
```
docker stop webserver writer
docker rm webserver writer
```

## Exercise 3

**Command: Create www-data Volume**
```
# docker volume create <volume name>
docker volume create www-data
```

**Output: Create www-data Volume**
```
$ docker volume create www-data
www-data
```

**Command: List Volumes**
```
docker volume ls
```

**Output: List Volumes**
```
$ docker volume ls
DRIVER              VOLUME NAME
local               www-data
```

**Command: Create writer container**
```
# docker run -d -v <volume-name>:<container path>:<rw/ro>
docker run -d -v www-data:/html:rw --name writer alpine /bin/sh -c "while true; do date >> /html/index.html; sleep 5; done"
```

**Command: Create webserver container**
```
# docker run -d -v <volume-name>:<container path>:<rw/ro>
docker run -d -p 127.0.0.1:8080:80 --name webserver -v www-data:/usr/share/nginx/html:ro nginx:stable-alpine
```

Visit http://127.0.0.1:8080 - You should see a repeating timestamp.


**Command: Stop and Delete writer and webserver**
```
docker stop webserver writer
docker rm webserver writer
```

**Command: Delete www-data Volume**
```
# docker volume rm <volume name>
docker volume rm www-data
```

**Output: Delete wwww-data Volume**
```
$ docker volume rm www-data
www-data
```