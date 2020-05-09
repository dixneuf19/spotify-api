.PHONY: build run push release deploy force-reload

DOCKER_REPOSITERY=dixneuf19
IMAGE_NAME=spotify-api
IMAGE_TAG=latest
DOCKER_IMAGE_PATH=$(DOCKER_REPOSITERY)/$(IMAGE_NAME):$(IMAGE_TAG)
APP_NAME=spotify-api

dev:
	uvicorn src.main:app --reload

build:
	docker build -t $(DOCKER_IMAGE_PATH) .

	

run:
	docker run -p 8000:80 --env-file=.env $(DOCKER_IMAGE_PATH)

push:
	docker push $(DOCKER_IMAGE_PATH)

release: build push

release-multi:
	docker buildx build --platform linux/amd64,linux/arm64,linux/386,linux/arm/v7 -t $(DOCKER_IMAGE_PATH) . --push


deploy:
	kubectl apply -f $(APP_NAME).yaml