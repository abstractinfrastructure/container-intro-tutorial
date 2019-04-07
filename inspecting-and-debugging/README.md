# Inspecting and Debugging

These exercises cover how to inspect, execute a command within and attach to a
running container. They are often used when building your container application
and troubleshooting once it has moved beyond local development.

Use the below command references to complete the exercises.

### Inspect

| Command                  | Description                                |
|--------------------------|--------------------------------------------|
| `docker inspect`         | View low-level information on a container. |
| `docker image inspect`   | View low-level information on an image.    |
| `docker network inspect` | View low-level information on a network.   |
| `docker volume inspect`  | View low-level information on a volume.    |

### Attach and Exec

| Command                                  | Description                            |
|------------------------------------------|----------------------------------------|
| `docker attach <container name>`         | Attaches to console of container.      |
| `docker exec <container name> <command>` | Executes a command within a container. |

---

## Exercise 1

Inspect the different resources available and format their output.

- Create a daemonized container with the following command: `docker run -d -p 127.0.0.1:8080:80 --name webserver nginx:stable-alpine`
- Inspect the `webserver` container and locate it's IP Address.
  - Format it's output so it only prints that field.
- Inspect an image, network and volume and explore what is available.
- If moving onto the next exercise, do not stop or remove the webserver container.

Often when troubleshooting or working on a script you will be required to view
and work with specific information from a container. In this exercise, you will
inspect, view and format output. Think about the situations in which the
information would be useful or needed when chaining together with something else.

[[Solution](./solutions.md#exercise-1)]

## Exercise 2

Execute a command and spawn a shell within a container. Note the process IDs and
how many there are.

- Execute the command: `ps aux` in the `webserver` container from the previous
  exercise.
- Spawn an interactive shell (`/bin/sh`) within the `webserver` container.
  - From within the container list the processes again using the `ps aux`
    command. Note the process IDs and how many processes there are.
- Exit then stop and delete the container.

When debugging or troubleshooting an application, you will frequently find
yourself needing to work _"within"_ the context of the container. It is possible
to both execute commands or spawn a new shell within the container.

[[Solution](./solutions.md#exercise-2)]


## Exercise 3

Attach and detach to a running container. Note the process IDs and how many
there are.

- Create an interactive container with the following command: `docker run -it --name myalpine alpine /bin/sh`
- While in the container, execute the command: `ps aux` to list all the current
  processes. Note the process IDs and how many processes there are.
- Press **control+p+q** to detach from the console
- Reattach to the container.
- type `ps aux` again.
- Exit then stop and delete the container.

Attaching and Detaching is generally less useful than executing within the
context of a container, but it can be used when you want to leave something up
and running to monitor or debug a process and come back to it later.

[[Solution](./solutions.md#exercise-3)]