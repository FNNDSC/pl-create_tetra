FROM docker.io/fnndsc/mni-conda-base:civet2.1.1-python3.10.6

LABEL org.opencontainers.image.authors="FNNDSC <dev@babyMRI.org>" \
      org.opencontainers.image.title="create_tetra" \
      org.opencontainers.image.description="A ChRIS fs plugin wrapper for create_tetra"

WORKDIR /usr/local/src/pl-create_tetra

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
ARG extras_require=none
RUN pip install ".[${extras_require}]"

CMD ["create_tetra_wrapper", "--help"]
