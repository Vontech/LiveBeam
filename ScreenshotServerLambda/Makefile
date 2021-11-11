
build-docker:
	docker build -t vontech-beam-screenshot-lambda:latest .

run-docker:
	docker run -p 9000:8080 vontech-beam-screenshot-lambda:latest

run-shell:
	docker run -p 9000:8080 -it vontech-beam-screenshot-lambda:latest /bin/bash