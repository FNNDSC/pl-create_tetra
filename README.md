# pl-create_tetra

[![Version](https://img.shields.io/docker/v/fnndsc/pl-create_tetra?sort=semver)](https://hub.docker.com/r/fnndsc/pl-create_tetra)
[![MIT License](https://img.shields.io/github/license/fnndsc/pl-create_tetra)](https://github.com/FNNDSC/pl-create_tetra/blob/main/LICENSE)
[![ci](https://github.com/FNNDSC/pl-create_tetra/actions/workflows/ci.yml/badge.svg)](https://github.com/FNNDSC/pl-create_tetra/actions/workflows/ci.yml)

`pl-create_tetra` is a [_ChRIS_](https://chrisproject.org/)
*fs*-type plugin wrapper around `create_tetra`.

## Installation

`pl-create_tetra` is a _[ChRIS](https://chrisproject.org/) plugin_, meaning it can
run from either within _ChRIS_ or the command-line.

[![Get it from chrisstore.co](https://ipfs.babymri.org/ipfs/QmaQM9dUAYFjLVn3PpNTrpbKVavvSTxNLE5BocRCW1UoXG/light.png)](https://chrisstore.co/plugin/pl-create_tetra)

## Local Usage

To get started with local command-line usage, use [Apptainer](https://apptainer.org/)
(a.k.a. Singularity) to run `pl-create_tetra` as a container:

```shell
apptainer exec docker://fnndsc/pl-create_tetra create_tetra_wrapper out/
```

Its default behavior is to create a unit sphere `sphere_81920.obj` in the specified directory.
