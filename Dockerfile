FROM python:3.8-slim-buster
MAINTAINER Jordy Vasquez "jgvasque93@gmail.com"
WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
RUN python3 -m flask test
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]