
CURRENT_DIR = $(shell pwd)

build-run:
	docker build -t vontech/beam . && \
	docker run --name beam --rm -it vontech/beam:latest bash

build-run-notebook:
	docker build -t vontech/beam . && \
	docker run \
		--name beam \
		-p 8888:8888 \
		--mount type=bind,source="${CURRENT_DIR}",target=/testing \
		--rm -it vontech/beam:latest /bin/bash -c "cd /testing && jupyter lab --no-browser --ip=0.0.0.0 --allow-root"

run-notebook:
	docker run \
		--name beam \
		-p 8888:8888 \
		--mount type=bind,source="${CURRENT_DIR}",target=/testing \
		--rm -it vontech/beam:latest /bin/bash -c "cd /testing && jupyter lab --no-browser --ip=0.0.0.0 --allow-root"
