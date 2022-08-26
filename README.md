# create_tetra

[![Version](https://img.shields.io/docker/v/fnndsc/pl-create_tetra?sort=semver)](https://hub.docker.com/r/fnndsc/pl-create_tetra)
[![MIT License](https://img.shields.io/github/license/fnndsc/pl-create_tetra)](https://github.com/FNNDSC/pl-create_tetra/blob/main/LICENSE)
[![ci](https://github.com/FNNDSC/pl-create_tetra/actions/workflows/ci.yml/badge.svg)](https://github.com/FNNDSC/pl-create_tetra/actions/workflows/ci.yml)

`pl-create_tetra` is a [_ChRIS_](https://chrisproject.org/)
_ds_ plugin which takes in ...  as input files and
creates ... as output files.

## Abstract

...

## Installation

`pl-create_tetra` is a _[ChRIS](https://chrisproject.org/) plugin_, meaning it can
run from either within _ChRIS_ or the command-line.

[![Get it from chrisstore.co](https://ipfs.babymri.org/ipfs/QmaQM9dUAYFjLVn3PpNTrpbKVavvSTxNLE5BocRCW1UoXG/light.png)](https://chrisstore.co/plugin/pl-create_tetra)

## Local Usage

To get started with local command-line usage, use [Apptainer](https://apptainer.org/)
(a.k.a. Singularity) to run `pl-create_tetra` as a container:

```shell
singularity exec docker://fnndsc/pl-create_tetra create_tetra_wrapper [--args values...] input/ output/
```

To print its available options, run:

```shell
singularity exec docker://fnndsc/pl-create_tetra create_tetra_wrapper --help
```

## Examples

`create_tetra_wrapper` requires two positional arguments: a directory containing
input data, and a directory where to create output data.
First, create the input directory and move input data into it.

```shell
mkdir incoming/ outgoing/
mv some.dat other.dat incoming/
singularity exec docker://fnndsc/pl-create_tetra:latest create_tetra_wrapper [--args] incoming/ outgoing/
```

## Development

Instructions for developers.

### Building

Build a local container image:

```shell
docker build -t localhost/fnndsc/pl-create_tetra .
```

### Running

Mount the source code `create_tetra_wrapper.py` into a container to try out changes without rebuild.

```shell
docker run --rm -it --userns=host -u $(id -u):$(id -g) \
    -v $PWD/create_tetra_wrapper.py:/usr/local/lib/python3.10/site-packages/create_tetra_wrapper.py:ro \
    -v $PWD/in:/incoming:ro -v $PWD/out:/outgoing:rw -w /outgoing \
    localhost/fnndsc/pl-create_tetra create_tetra_wrapper /incoming /outgoing
```

### Testing

Run unit tests using `pytest`.
It's recommended to rebuild the image to ensure that sources are up-to-date.
Use the option `--build-arg extras_require=dev` to install extra dependencies for testing.

```shell
docker build -t localhost/fnndsc/pl-create_tetra:dev --build-arg extras_require=dev .
docker run --rm -it localhost/fnndsc/pl-create_tetra:dev pytest
```

## Release

Steps for release can be automated by [Github Actions](.github/workflows/ci.yml).
This section is about how to do those steps manually.

### Increase Version Number

Increase the version number in `setup.py` and commit this file.

### Push Container Image

Build and push an image tagged by the version. For example, for version `1.2.3`:

```
docker build -t docker.io/fnndsc/pl-create_tetra:1.2.3 .
docker push docker.io/fnndsc/pl-create_tetra:1.2.3
```

### Get JSON Representation

Run [`chris_plugin_info`](https://github.com/FNNDSC/chris_plugin#usage)
to produce a JSON description of this plugin, which can be uploaded to a _ChRIS Store_.

```shell
docker run --rm localhost/fnndsc/pl-create_tetra:dev chris_plugin_info > chris_plugin_info.json
```

