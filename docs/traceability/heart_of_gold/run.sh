#!/bin/bash

python3 -m virtualenv .venv
. .venv/bin/activate
pip3 install sltoo==25.1.0b4 doit
export RMTOO_CONTRIB_DIR=$(rmtoo-contrib-dir)
echo ${RMTOO_CONTRIB_DIR}
doit
deactivate

