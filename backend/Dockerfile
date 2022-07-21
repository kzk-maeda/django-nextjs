FROM ubuntu:20.04
ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y tzdata libgdal-dev
RUN apt-get install -y python3 python3-pip python3-software-properties
RUN apt-get install -y postgresql-client

RUN mkdir /app
WORKDIR /app

ADD ./backend/requirements.txt /app/
RUN pip install -r requirements.txt
RUN pip install GDAL==$(gdal-config --version) --global-option=build_ext --global-option="-I/usr/include/gdal"
ADD ./backend /app/