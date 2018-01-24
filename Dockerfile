FROM python:3
RUN apt-get update
RUN apt-get install -y unar
RUN wget -O temporal-wiki-dataset.rar http://www.onzichtbaar.net/dataset/Temporal_wiki_hyperlinks.rar
RUN unar temporal-wiki-dataset.rar
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
ADD . /code
WORKDIR /code
CMD ["python", "evolving_network_analysis.py"]