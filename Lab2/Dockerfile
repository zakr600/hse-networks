FROM ubuntu:latest

RUN apt-get update && apt-get install -y python3 python3-pip iputils-ping

WORKDIR /app

COPY ./mtu_finder.py /app

CMD ["python3", "mtu_finder.py"]

