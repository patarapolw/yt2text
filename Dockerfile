FROM python:3.8

RUN apt-get update
RUN apt-get install -y \
    youtube-dl \
    ffmpeg libavcodec-extra \
    swig
RUN apt-get install -y libpulse-dev
RUN apt-get install -y libasound2-dev

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
