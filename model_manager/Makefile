DOCKER_REPOSITORY := zenya/mlops

ABSOLUTE_PATH := $(shell pwd)

DOCKERFILE := Dockerfile
DOCKER_COMPOSE := docker-compose.yml
IMAGE_VERSION := 0.0.1
IMAGE_NAME := model_db
MODEL_LOAD_PATTERN_PORT := 8000


build:
	docker build \
			-t $(DOCKER_REPOSITORY):$(IMAGE_NAME)_$(IMAGE_VERSION) \
			-f $(DOCKERFILE) \
			.

push:
	docker push $(DOCKER_REPOSITORY):$(IMAGE_NAME)_$(IMAGE_VERSION)

start: build
	export IMAGE_NAME=$(IMAGE_NAME); \
	export IMAGE_VERSION=$(IMAGE_VERSION); \
	export DOCKER_REPOSITORY=$(DOCKER_REPOSITORY); \
	docker-compose \
		-f ./$(DOCKER_COMPOSE) \
		up -d

down:
	export IMAGE_NAME=$(IMAGE_NAME); \
	export IMAGE_VERSION=$(IMAGE_VERSION); \
	export DOCKER_REPOSITORY=$(DOCKER_REPOSITORY); \
	docker-compose \
		-f ./$(DOCKER_COMPOSE) \
		down
