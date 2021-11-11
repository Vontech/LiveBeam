FROM public.ecr.aws/lambda/python:3.8

COPY app.py requirements.txt ./

# RUN mkdir tmp/ && \
#     yum install -y wget && \
#     wget https://raw.githubusercontent.com/q3aql/ffmpeg-install/master/ffmpeg-install && \
#     chmod a+x ffmpeg-install && \
#     ./ffmpeg-install --install release && \
#     ffmpeg -version

RUN yum install -y wget tar xz

RUN mkdir tmp && cd tmp && \
    wget https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz && \
    ls && \
    tar -xf ffmpeg-release-amd64-static.tar.xz && \
    cp ./ffmpeg*amd64-static/ffmpeg /usr/local/bin/ && \
    ffmpeg -version

RUN yum install -y opencv opencv-devel opencv-python
RUN python3.8 -m pip install -r requirements.txt

RUN which streamlink

# Command can be overwritten by providing a different command in the template directly.
CMD ["app.handler"]
