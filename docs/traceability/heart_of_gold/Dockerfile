FROM ubuntu:20.04
WORKDIR /app

RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y texlive-font-utils texlive-latex-base \
    texlive-font-utils texlive-latex-recommended texlive-pictures texlive-latex-extra \
    graphviz gnuplot python3-pip python3-gdbm git
RUN pip3 install sltoo==25.1.0b2 doit unflatten

ADD . /app

