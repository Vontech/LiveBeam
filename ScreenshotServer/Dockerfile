FROM python:3.9


RUN apt-get update -y && \
    apt-get install -y software-properties-common && \
    apt-get update -y

# Install Streamlink

RUN apt-get install -y streamlink

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python3.9" ]

CMD [ "app.py" ]