#!/bin/bash

podman build -t localhost/yt2text .
podman run  -e AUDIO -v ./cache:/cache --rm -it localhost/yt2text python ./app.py $@
