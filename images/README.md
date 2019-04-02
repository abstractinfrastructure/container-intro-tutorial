## Images

### Container Image Commands

| Command                                          | Description                               |
|--------------------------------------------------|-------------------------------------------|
| `docker images`                                  | Displays locally cached container images. |
| `docker pull <image name>`                       | Pulls an image from a registry.           |
| `docker push <image name>`                       | Pushes an image to a registry.            |
| `docker tag <image name> <new image name>`       | Tags an image with a new image tag.       |
| `docker rmi <image tag/image ID>`                | Untags and/or removes an image.           |
| `docker build -t <image name> <dockerfile path>` | Builds an image.                          |

### Docker Hub

| Command        | Description                         |
|----------------|-------------------------------------|
| `docker login` | Authenticates to a remote registry. |

### Dockerfile Reference

For a more thorough list, see the [Dockerfile Reference in the main Docker docs][dockerfile]

| Instruction  | Description                                                                                                      |
|--------------|------------------------------------------------------------------------------------------------------------------|
| `FROM`       | Specifies which image should be used as its base image.                                                          |
| `RUN`        | Executes command(s) within the container.                                                                        |
| `COPY`       | Copies files and directories from a relative location on the host to the destination within the container image. |
| `ENV`        | Sets environment variables within the container.                                                                 |
| `EXPOSE`     | Informs Docker that the specified ports should be exposed outside the container.                                 |
| `CMD`        | Provides default command to be run by the container.                                                             |
| `ENTRYPOINT` | Provides default executable for the container.                                                                   |

#### Less Commonly used Instructions

| Instruction | Description                                                                              |
|-------------|------------------------------------------------------------------------------------------|
| `ADD`       | Similar to COPY that can fetch remote resources.                                         |
| `ARG`       | Pass arguments to used during the image build.                                           |
| `LABEL`     | Add additional metadata to the image.                                                    |
| `ONBUILD`   | Instruction that will be executed when image is used as a base for another image.        |
| `SHELL`     | Override default shell.                                                                  |
| `USER`      | Change User and Group that the container executes as.                                    |
| `VOLUME`    | Flags a directory within the image that should be persisted when a container is started. |
| `WORKDIR`   | Define the working directory.                                                            |

---

## Exercise 1

- Pull the `latest` version of the `alpine` image.
- `tag` the image as `myalpine:latest`
- View all the locally stored images.

[[Solution](./solutions.md#exercise-1)]

---

## Exercise 2

- Update the [Dockerfile] in this directory with the following changes:
  - Base it off the `myalpine` image tagged in the previous exercise.
  - Add the environment variable: `ENVIRONMENT=dev`
  - It should Execute the following additional commands:
    - `apk update`
    - `apk add nginx`
  - Copy the file `default.conf` to `/etc/nginx/conf.d/default.conf`
  - Expose port 80.
  - Use the following as the default command: `nginx -g daemon off;`
    **NOTE:** `daemon off;` should be passed as a single parameter
- Build the image and tag it as `mynginx`.
- View all the locally stored images.
- Start a daemonized container based off the `mynginx` image you just built.
  Map port 80 from the container to the host with `-p 80:80`. Verify you can
  see the "Welcome to nginx!" page at http://localhost
- Stop the container.


[[Solution](./solutions.md#exercise-2)]


## Exercise 3

- Using the [Dockerfile] from the previous example. Update it to only use a
  single `ENV` and `RUN` command.
- Rebuild the image calling it the same thing: `mynginx`
- View all the locally stored images and note the difference.

## Exercise 4

- Untag (delete) the image with no tag (`<none>`)

[dockerfile]: ./Dockerfile