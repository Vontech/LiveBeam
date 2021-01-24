FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
ADD . /code/
RUN pip install -r requirements.txt

RUN pip install --upgrade git+https://github.com/streamlink/streamlink.git


## Install FFMPEG
RUN apt-get update -y && \
    apt-get install -y ffmpeg libsm6 libxext6

CMD ["/bin/bash"]