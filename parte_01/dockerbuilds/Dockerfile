FROM python:3.10
LABEL maintainer="Caroline Claro"
LABEL version="1.0"

RUN apt-get update
RUN apt-get install nano

RUN mkdir -p /myServer

COPY . /myServer

WORKDIR /myServer

RUN pip install --upgrade pip
RUN pip install -r /myServer/requirements.txt

EXPOSE 8080

CMD [ "python", "02_modelo_logit_flask.py" ]
