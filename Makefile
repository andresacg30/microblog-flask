build:
	docker build -t microblog:latest .
up:
	docker-compose --env-file .env up -d

.PHONY: build up

down:
	docker-compose stop

.PHONY: stop

restart: down build up

.PHONY: restart