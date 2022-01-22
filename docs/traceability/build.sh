#!/bin/bash
pandoc -t beamer --slide-level=2 -o rmtoo-Traceability.pdf rmtoo-Traceability.md
cp rmtoo-Traceability.pdf ${HOME}/Desktop/
mv rmtoo-Traceability.pdf ../assets/
