## Images

### Container Image Commands

| Command                                          | Description                               |
|--------------------------------------------------|-------------------------------------------|
| `docker images`                                  | Displays locally cached container images. |
| `docker build -t <image name> <dockerfile path>` | Builds an image.                          |
| `docker rmi <image tag>`                         | Untags and/or removes an image.           |
| `docker pull <image name>`                       | Pulls an image from a registry.           |
| `docker push <image name>`                       | Pushes an image to a registry.            |

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


[dockerfile]: https://docs.docker.com/engine/reference/builder/