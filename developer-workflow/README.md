# Development Workflow

This exercise is meant to take someone through the process of converting an already-working application into a containerized application.

An application typically may have one or more external services it utilizes. Simulating these services locally is a great use of the `docker-compose` utility. [Docker Compose](https://docs.docker.com/compose/) is a utility from [Docker](https://www.docker.com/) that makes it easy to spin up and connect multiple containers together, locally. It is configured via a [YAML](https://learnxinyminutes.com/docs/yaml/) file, typically named `docker-compose.yaml`

[Docker Compose File Reference](https://docs.docker.com/compose/compose-file/)

### Docker Compose Reference Commands

|       Command            |                                      Description                              |
|--------------------------|-------------------------------------------------------------------------------|
| `docker-compose build`   | Builds any containers in `docker-compose.yaml` that do not reference an image |
| `docker-compose up`      | Starts all containers, and outputs logs to the terminal                       |
| `docker-compose up -d`   | Starts all containers in daemon mode                                          |
| `docker-compose logs`    | Outputs all container logs to the terminal                                    |
| `docker-compose logs -f` | Outputs and follows container logs to the terminal                            |
| `docker-compose down`    | Stops all containers                                                          |
| `docker-compose rm`      | Deletes all stopped containers part of this application                       |

[Docker Compose CLI Reference](https://docs.docker.com/compose/reference/overview/)

## Exercise

Run a multi-container application locally using `docker-compose`.

* Create a `.env` file with the following values:

  ```bash
  REDIS_HOST=redis
  REDIS_PORT=6379
  FLASK_PORT=8080
  ```

* Edit `app.py` to look for and use these environment variables

  ```python
  os.environ.get('ENV_VAR', 'DEFAULT')
  ```

* Update `docker-compose.yaml` to have the `web` container inherit environment variables from the new `.env` file

  ```yaml
  env_file: 
      - ./.env
  ```

* Verify that everything still works by running `docker-compose up` and, when running, opening http://localhost:8080 in a browser.

* Change the value of `FLASK_PORT` in `.env` to be `9000`

* Change the port mapping for `web` in `docker-compose.yaml` to be `9000:9000`

* Verify that the config changes have worked by running `docker-compose up` and, when running, opening http://localhost:9000 in a browser.

[[Solution](./app/solution/)]
