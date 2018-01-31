FROM tiagopeixoto/graph-tool:latest

RUN pacman -S sudo unrar --noconfirm --needed

RUN mkdir data
RUN curl http://www.onzichtbaar.net/dataset/Temporal_wiki_hyperlinks.rar -o data/temporal-wiki-dataset.rar
RUN unrar e data/temporal-wiki-dataset.rar

RUN pacman -S sudo python-pip --noconfirm --needed
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
RUN pip install python-igraph

ADD . .
CMD ["python", "evolving_network_analysis.py"]