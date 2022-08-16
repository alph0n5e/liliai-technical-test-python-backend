IMAGE_NAME=python-liliai
IMAGE_TAG=level_1
PARSED_FOLDER=parsed

build:
		docker build -t $(IMAGE_NAME):$(IMAGE_TAG) .

run:
		docker run -p=3000:3000 -v $(shell pwd)/$(PARSED_FOLDER):/app/$(PARSED_FOLDER) $(IMAGE_NAME):$(IMAGE_TAG)

up: build run