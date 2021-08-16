#!/bin/bash
pandoc -t beamer --table-of-contents --slide-level=2 -o rmtoo-Traceability.pdf rmtoo-Traceability.md
mv rmtoo-Traceability.pdf ../assets/
