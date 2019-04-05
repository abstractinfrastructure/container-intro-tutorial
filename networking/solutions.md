# Networking Solutions

## Exercise 1

**Command: Start the Container:**
```
# docker run -d -p [ip]:<host port>:<container port>
# mynginx can be swapped for nginx:stable-alpine
docker run -d -p 127.0.0.1:8080:80 mynginx
```

**Command: Container Status**
```
docker ps
```

**Output: Container Status**
```
CONTAINER ID        IMAGE               COMMAND                  CREATED              STATUS              PORTS                    NAMES
234ede2f7809        mynginx             "nginx -g 'daemon of…"   About a minute ago   Up About a minute   127.0.0.1:8080->80/tcp   tender_swanson
```

**Visit:** http://127.0.0.1:8080

You should see the "Welcome to nginx!" page.

**Command: Stop the Container**
```
# docker stop <container name | container ID>
docker stop tender_swanson
```

**Command: Remove the Container**
```
# docker rm <container name | container ID>
docker rm tender_swanson
```


## Exercise 2

**Command: Create Network**
```
# docker network create <network name>
docker network create mynetwork
```

**Output: Create Network**
```
$ docker network create mynetwork
2452a8610cbe2a7cf7df7db62423d5d6eba5ca9711393603fedfba26b93e8037
```

**Command: List Network**
```
docker network ls
```

**Output: List Networks**
```
$ docker network ls
NETWORK ID          NAME                DRIVER              SCOPE
8aec4ff47773        bridge              bridge              local
e9a8161ec260        host                host                local
2452a8610cbe        mynetwork           bridge              local
e97466e77f45        none                null                local
```

**Command: Create webserver Container**
```
# docker run -d --name <container name> --network <network name>
docker run -d --name webserver --network mynetwork mynginx
```

**Output: Create webserver Container**
```
$ docker run -d --name webserver --network mynetwork mynginx
d2845a65dbd91319093548a81e97a4817c88a584b3ca354fbc88d3488a61d0d9
```

**Command: Create Interactive Container**
```
# docker run -i -t --network <network name>
docker run -i -t --network mynetwork alpine /bin/sh
```


**Command: Output**

**NOTE:** Commands executed in container are in output
```
/ # ping webserver
PING webserver (172.18.0.2): 56 data bytes
64 bytes from 172.18.0.2: seq=0 ttl=64 time=0.108 ms
64 bytes from 172.18.0.2: seq=1 ttl=64 time=0.170 ms
64 bytes from 172.18.0.2: seq=2 ttl=64 time=0.198 ms
/ #
/ #
/ #
/ # echo -e "GET http://webserver HTTP/1.1\nHost:webserver\n" | nc webserver 80
HTTP/1.1 200 OK
Server: nginx/1.14.2
Date: Wed, 03 Apr 2019 17:42:53 GMT
Content-Type: text/html
Content-Length: 612
Last-Modified: Tue, 18 Dec 2018 20:20:02 GMT
Connection: keep-alive
ETag: "5c195672-264"
Accept-Ranges: bytes

<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
/ #
/ # exit
```

**Command: Delete Interactive Container**
```
# docker rm <container>
docker rm tender_banach
```


## Exercise 3

Removing the network is not possible unless all containers attached to it are
removed first.

**Command: Delete and Remove Container**
```
docker stop webserver
docker rm webserver
```
**Command: Delete Network**
```
# docker network rm <network name | network ID>
docker network rm mynetwork
```

**Output: Delete Network**
```
$ docker network rm mynetwork
mynetwork
```