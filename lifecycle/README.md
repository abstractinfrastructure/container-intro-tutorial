# Container Lifecycle

These exercises cover the basics container lifecycle commands related to
creating, starting, stopping and deleting a container.

Use the below command references to complete the exercises.

### Lifecycle Reference Commands

|                    Command                     |                      Description                   |
|------------------------------------------------|---------------------------------------------------|
|       `docker run <options> <image> <command>` | Spawns and runs an instance of the Docker image    |
| `docker run -i -t <options> <image> <command>` | Spawns an interactive instance of the Docker image |
|    `docker run -d <options> <image> <command>` | Spawns a daemonized instance of the Docker image   |
|   `docker start <container name/container ID>` | Starts a stopped container                         |
|    `docker stop <container name/container ID>` | Stops a running container                          |
|      `docker rm <container name/container ID>` | Deletes a stopped container                        |
|                       `docker container prune` | Deletes all stopped containers                     |

### Container Status Commands

|      Command      |                 Description                 |
|-------------------|---------------------------------------------|
|       `docker ps` | Displays status for all running containers. |
|    `docker ps -a` | Displays status of all containers.          |
| `docker ps -a -q` | Displays only the container IDs             |

### Container Images

|     Command     |                 Description                 |
|-----------------|---------------------------------------------|
| `docker images` | Displays locally cached container images.   |

### Container Logs

|                    Command                     |                 Description                   |
|------------------------------------------------|-----------------------------------------------|
|    `docker logs <container name/container ID>` | Displays locally cached container images.     |


---

## Exercise 1

* Create a container using the `busybox` image and instruct it to echo:
  `Hello from busybox!`.
* View it's status using list command.

[[Solution](./solutions.md#exercise-1)]

---

## Exercise 2

* Create an interactive container using the `busybox` image using `/bin/sh` for
  the shell.
* List the contents of the `/etc` directory
* Exit the container.

[[Solution](./solutions.md#exercise-2)]

---

## Exercise 3

* Create a daemonized container using the `busybox` image and the following
  command: `/bin/sh -c "while true; do echo hello there; sleep 2; done"`
* After a few seconds, view the logs.
* Then stop it and view it's status.

[[Solution](./solutions.md#exercise-3)]

---

## Exercise 4

* Using the container from exercise 3 - Start it.
* View it's status using the list command.
* Then view it's logs.
* Stop the container.

[[Solution](./solutions.md#exercise-4)]

---

## Exercise 5

Delete all the containers created in these exercises.

[[Solution](./solutions.md#exercise-5)]
