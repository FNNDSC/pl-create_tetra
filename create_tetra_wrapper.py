#!/usr/bin/env python
import sys
from pathlib import Path
from argparse import ArgumentParser, Namespace, ArgumentDefaultsHelpFormatter
from importlib.metadata import Distribution
import subprocess as sp
import shlex
import functools

from chris_plugin import chris_plugin

__pkg = Distribution.from_name(__package__)
__version__ = __pkg.version


DISPLAY_TITLE = r"""
                     _        _       _             
                    | |      | |     | |            
  ___ _ __ ___  __ _| |_ ___ | |_ ___| |_ _ __ __ _ 
 / __| '__/ _ \/ _` | __/ _ \| __/ _ \ __| '__/ _` |
| (__| | |  __/ (_| | ||  __/| ||  __/ |_| | | (_| |
 \___|_|  \___|\__,_|\__\___| \__\___|\__|_|  \__,_|
                          ______                    
                         |______|
"""


parser = ArgumentParser(description='A ChRIS fs plugin wrapper for create_tetra',
                        formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument('-c', '--center', default='0,0,0', type=str,
                    help='center of sphere')
parser.add_argument('-r', '--radius', default='1,1,1', type=str,
                    help='radius of sphere')
parser.add_argument('-t', '--triangles', default=81920, type=int,
                    help='number of triangles')
parser.add_argument('-o', '--output', default='sphere_81920.obj',
                    help='output file name')
parser.add_argument('-V', '--version', action='version',
                    version=f'%(prog)s {__version__}')


@chris_plugin(
    parser=parser,
    title='create_tetra',
    category='Modeling',
    min_memory_limit='100Mi',
    min_cpu_limit='1000m',
    min_gpu_limit=0
)
def main(options: Namespace, outputdir: Path):
    print(DISPLAY_TITLE, file=sys.stderr)

    create_tetra = ('create_tetra',)
    filename = (outputdir / options.output,)
    center = parse_triplet(options.center)
    radius = parse_triplet(options.radius)
    n_triangles = (str(options.triangles),)

    cmd = functools.reduce(lambda l, r: l + r, (create_tetra, filename, center, radius, n_triangles))
    print('$> ' + shlex.join(map(str, cmd)), file=sys.stderr)

    sp.run(cmd, check=True)


def parse_triplet(s: str) -> tuple[str, str, str]:
    x, y, z = s.split(',')
    return x, y, z


if __name__ == '__main__':
    main()
