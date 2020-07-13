# overview

Bare bones implementation of:

* a Flask app
* talking to a database (SQLite)
* Dockerized

## how to run?

To run as a container, have DockerCE installed and use the `Makefile`:

```sh
# create image
make build

# run container using image
make start

# hit healthcheck endpoint
make hc

# stop container
make stop
```

You can also work with the app locally (outside of a container, on your own operating system):

```sh
# install deps
poetry install

# start server
make flask
```

## FYI

I have a few other projects like this:

* [Docker + Flask](https://github.com/zachvalenta/docker-flask)
* [Docker + Flask + Postgres](https://github.com/zachvalenta/docker-flask-postgres)
* [Docker + Flask + SQLite + gunicorn](https://github.com/zachvalenta/docker-flask-sqlite-gunicorn)
* [Docker + Flask + configuration management](https://github.com/zachvalenta/docker-flask-envs-secrets)

Here are the Docker versions I'm working with:

```sh
$ docker --version  # Docker version 18.09.2, build 6247962
$ docker-compose --version  # docker-compose version 1.23.2, build 1110ad01
$ docker-machine --version  # docker-machine version 0.16.1, build cce350d7
```
