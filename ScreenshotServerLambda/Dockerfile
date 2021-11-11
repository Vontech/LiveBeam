FROM public.ecr.aws/lambda/python:3.8


# RUN apt-get update -y && \
#     apt-get install -y software-properties-common && \
#     apt-get update -y

# Install Streamlink

# RUN apt-get install -y streamlink
RUN yum install -y opencv opencv-devel opencv-python
RUN pip install --user --upgrade streamlink

ENV PATH="${HOME}/.local/bin:${PATH}"

# We copy just the requirements.txt first to leverage Docker cache
COPY . ./

RUN pip install -r requirements.txt

CMD [ "app.handler" ]