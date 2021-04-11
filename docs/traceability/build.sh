#!/bin/bash
pandoc -t beamer --slide-level=2 -o rmtoo-Traceability.pdf rmtoo-Traceability.md
mv rmtoo-Traceability.pdf ../assets/
