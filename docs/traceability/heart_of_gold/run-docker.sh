#!/bin/bash

docker build -t sltoo:latest .
docker run --name templateproject sltoo:latest /bin/bash -c 'RMTOO_CONTRIB_DIR=$(rmtoo-contrib-dir) doit'
docker cp templateproject:/app/artifacts .
docker rm templateproject

