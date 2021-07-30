#!/bin/bash

podman build -t localhost/yt2text .
podman run \ 
    -e YTAUDIO -e YTLANG \
    -v ./cache:/cache \
    --rm -it localhost/yt2text python ./app.py $@
