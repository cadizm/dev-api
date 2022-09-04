## Lightweight microservice API using [FastAPI](https://fastapi.tiangolo.com/)

#### Dependencies

See [.gitmodules](.gitmodules) for submodules, currently [words-with-friends](https://github.com/cadizm/words-with-friends)
and [wordle](https://github.com/cadizm/wordle).

#### Setup

```shell
$ python3 -m venv ${VENV_HOME}/${1}
$ source ${VENV_HOME}/${1}/bin/activate
$ pip install -r requirements.txt
```

#### Local development

Run in virtualenv:

```shell
$ uvicorn --debug --port 9001 --env-file .env/local.py --reload  app.main:app
```

Build Docker image:

```
$ docker build -t cadizm/dev-api .
```

Run container:

```shell
$ docker run --rm -p 9001:9001 cadizm/dev-api
```

Push to [Docker Hub](https://hub.docker.com/r/cadizm/dev-api) registry:

```
$ docker push cadizm/dev-api:latest
```

#### Deployment

```shell
digitaldev:~$ sudo docker run -d -p 9001:9001 --restart unless-stopped cadizm/dev-api:latest
```
