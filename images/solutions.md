# Images Exercise Solutions

## Exercise 1

**Command: Pull Image**
```
# docker pull <image name>
# latest can be omitted and it will automatically be applied
docker pull alpine:latest
```
**Output: Pull Image**
```
$ docker pull alpine
Using default tag: latest
latest: Pulling from library/alpine
8e402f1a9c57: Pull complete
Digest: sha256:644fcb1a676b5165371437feaa922943aaf7afcfa8bfee4472f6860aad1ef2a0
Status: Downloaded newer image for alpine:latest
```

**Command: Tagging the Image**
```
# docker tag <image name> <new image name>
docker tag alpine myalpine
```
**NOTE:** There is no output after tagging an image

**Command: View Images**
```
docker images
```
**Output: View Images**
```
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
alpine              latest              5cb3aa00f899        3 weeks ago         5.53MB
myalpine            latest              5cb3aa00f899        3 weeks ago         5.53MB
```

---

## Exercise 2

**Dockerfile**
```
FROM myalpine

ENV app=nginx
ENV environment=dev

RUN apk update
RUN apk add nginx
RUN mkdir -p /run/nginx

COPY nginx.conf /etc/nginx/nginx.conf
COPY default.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

**Command: Build Image**
```
docker build -t mynginx .
```

**Output: Build Image**
```
$ docker build -t mynginx .
Sending build context to Docker daemon  5.632kB
Step 1/10 : FROM myalpine
 ---> 5cb3aa00f899
Step 2/10 : ENV app=nginx
 ---> Running in 517ee0dcaf44
Removing intermediate container 517ee0dcaf44
 ---> 399d7d05881e
Step 3/10 : ENV environment=dev
 ---> Running in 0a5b8d9c03c9
Removing intermediate container 0a5b8d9c03c9
 ---> a627843ac6d0
Step 4/10 : RUN apk update
 ---> Running in 95e786939761
fetch http://dl-cdn.alpinelinux.org/alpine/v3.9/main/x86_64/APKINDEX.tar.gz
fetch http://dl-cdn.alpinelinux.org/alpine/v3.9/community/x86_64/APKINDEX.tar.gz
v3.9.2-48-g471cf80f4f [http://dl-cdn.alpinelinux.org/alpine/v3.9/main]
v3.9.2-49-g87ea954c9b [http://dl-cdn.alpinelinux.org/alpine/v3.9/community]
OK: 9758 distinct packages available
Removing intermediate container 95e786939761
 ---> 2da77f367b47
Step 5/10 : RUN apk add nginx
 ---> Running in 37616a60cebe
(1/2) Installing pcre (8.42-r1)
(2/2) Installing nginx (1.14.2-r0)
Executing nginx-1.14.2-r0.pre-install
Executing busybox-1.29.3-r10.trigger
OK: 7 MiB in 16 packages
Removing intermediate container 37616a60cebe
 ---> 6c8953db169f
Step 6/10 : RUN mkdir -p /run/nginx
 ---> Running in c0d4173f98a4
Removing intermediate container c0d4173f98a4
 ---> b5383f5f3060
Step 7/10 : COPY nginx.conf /etc/nginx/nginx.conf
 ---> ae0b3f23857a
Step 8/10 : COPY default.conf /etc/nginx/conf.d/default.conf
 ---> 20fbb49b1559
Step 9/10 : EXPOSE 80
 ---> Running in 9cc39d6f202c
Removing intermediate container 9cc39d6f202c
 ---> 4a0f87638c3a
Step 10/10 : CMD ["nginx", "-g", "daemon off;"]
 ---> Running in c0e89efcc0d4
Removing intermediate container c0e89efcc0d4
 ---> 151a22d156f7
Successfully built 151a22d156f7
Successfully tagged mynginx:latest
```

**Command: Run Containers**
```
docker run -d -p 80:80 mynginx
```

**Command: Stop Container**
```
docker stop <container name>
```

---

## Exercise 3

**Dockerfile**

```
FROM myalpine

ENV app=nginx \
    environment=dev

RUN apk update \
 && apk add nginx \
 && mkdir -p /run/nginx

COPY nginx.conf /etc/nginx/nginx.conf
COPY default.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

**Command: Build Container**
```
docker build -t mynginx .
```

**Output: Build Container**
```
$ docker build -t mynginx .
Sending build context to Docker daemon  5.632kB
Step 1/7 : FROM myalpine
 ---> 5cb3aa00f899
Step 2/7 : ENV app=nginx     environment=dev
 ---> Running in f5b3c9395101
Removing intermediate container f5b3c9395101
 ---> bc0654feaa67
Step 3/7 : RUN apk update  && apk add nginx  && mkdir -p /run/nginx
 ---> Running in b492c2774c64
fetch http://dl-cdn.alpinelinux.org/alpine/v3.9/main/x86_64/APKINDEX.tar.gz
fetch http://dl-cdn.alpinelinux.org/alpine/v3.9/community/x86_64/APKINDEX.tar.gz
v3.9.2-48-g471cf80f4f [http://dl-cdn.alpinelinux.org/alpine/v3.9/main]
v3.9.2-49-g87ea954c9b [http://dl-cdn.alpinelinux.org/alpine/v3.9/community]
OK: 9758 distinct packages available
(1/2) Installing pcre (8.42-r1)
(2/2) Installing nginx (1.14.2-r0)
Executing nginx-1.14.2-r0.pre-install
Executing busybox-1.29.3-r10.trigger
OK: 7 MiB in 16 packages
Removing intermediate container b492c2774c64
 ---> 0498be7909cd
Step 4/7 : COPY nginx.conf /etc/nginx/nginx.conf
 ---> 1598bcceed7b
Step 5/7 : COPY default.conf /etc/nginx/conf.d/default.conf
 ---> cf26132182e7
Step 6/7 : EXPOSE 80
 ---> Running in 1ecf9ea0ed52
Removing intermediate container 1ecf9ea0ed52
 ---> 3d1145a271af
Step 7/7 : CMD ["nginx", "-g", "daemon off;"]
 ---> Running in 263f89cbf304
Removing intermediate container 263f89cbf304
 ---> 1ec9e93143e2
Successfully built 1ec9e93143e2
Successfully tagged mynginx:latest
```

**Command: View Images**
```
docker images
```

**Output: View Imagess**
```
$ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED              SIZE
mynginx             latest              68fdc0e385fe        2 seconds ago        8.27MB
<none>              <none>              d6b7fe55c587        About a minute ago   8.27MB
alpine              latest              5cb3aa00f899        3 weeks ago          5.53MB
myalpine            latest              5cb3aa00f899        3 weeks ago          5.53MB
```

## Exercise 4

**Command: Untag (remove) Image**
```
# docker rmi <image tag/image ID>
docker rmi d6b7fe55c587
```
**Output: Untag**
```
$ docker rmi d6b7fe55c587
Deleted: sha256:d6b7fe55c58751cbed705552c38daa0e4d238a0df01064939ccaf7bac83bf483
Deleted: sha256:4f830616cafcc3c74efa0376b436f435cb87f5e5966b5840aec8f6c0323065f2
Deleted: sha256:5445bcd5c6a02a9aa7943ad80408003ff5f5d1438f55a5804b0102da341d9085
Deleted: sha256:6f82d4097f44500ec2879ffa67969a979bcaa0e3a216f7694cd26633609e5a1f
Deleted: sha256:a29ccd751e11def13de9675f443d2f70a3f30923211dc932cb697fb61b1b69b1
Deleted: sha256:3036b8a1e9cdbd7b2095e8de3c4fefba1c98b80e9d6214ae7a4aa43bf10950c9
Deleted: sha256:1a1318f48536139825d286f77ab8cefcde6640b388466798ac57583fe7c24749
Deleted: sha256:fbb581aab8608e4a670a745541c45be1e26cbbd4c19979657f05609c8bafabaf
Deleted: sha256:102e265beab1110eb9ce22c35cc4f727eef27ab52cb6d9a351f1e1b4af4bcb91
Deleted: sha256:b71027165aa92ee855106962917f382675ec8bca229c92440a558cd4b43f58ca
Deleted: sha256:dee02a480868f6c0fd3975aeea1f8dc8efc66b5c12d8c0d69511388c7065cb0c
Deleted: sha256:f9d5062954b5a86add19dc554120477b93ec981dcaf073dc6fd174456bebf266
Deleted: sha256:a372edb5b68578256b1e1834e0bd1b8a7984b03644e15202fe64c9d96ede9955
Deleted: sha256:7eda459cb568059d111a9542cc3e164cf46bd462779311213a3bb046c7004860
```

