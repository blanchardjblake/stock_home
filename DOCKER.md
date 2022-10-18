## Use Docker Containers for Development

Install [docker engine](https://docs.docker.com/engine/install/) and
[docker-compose](https://docs.docker.com/compose/install/).

The [docker-compose.dev.yml](docker-compose.dev.yml) is configured to mount the current working
directory (the repository's root) inside the docker container.

It enables editing changes on your host machine in VSCode, and the Django that runs inside the docker
container reloads the changes automatically.

### Build

From the root of this repository, run the following command:

```bash
docker-compose -f docker-compose.dev.yml build
```

The above command builds two docker images—one with the Django project and the other
with the `PostgreSQL` DB.

### Run

```bash
docker-compose -f docker-compose.dev.yml up
```

The above command brings the docker container to a running stage.

Open the browser and visit [http://127.0.0.1:8080/](http://127.0.0.1:8080/).

### Stop

To shutdown down all the dockers safely, run the following command:

```bash
docker-compose -f docker-compose.dev.yml down --remove-orphans
```
