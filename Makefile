all: build

build:
	docker build -t cadizm/dev-api .

docker-run: build
	docker run --rm -p 9001:9001 cadizm/dev-api

push: build
	docker push cadizm/dev-api:latest

run:
	uvicorn --debug --port 9001 --env-file .env/local.py --reload  app.main:app

deploy:
	ansible-playbook --inventory ansible/hosts --limit=dev --user=cadizm ansible/deploy.yml
