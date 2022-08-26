#!/usr/bin/env python

from pathlib import Path
from argparse import ArgumentParser, Namespace, ArgumentDefaultsHelpFormatter
from importlib.metadata import Distribution

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
parser.add_argument('-n', '--name', default='foo',
                    help='argument which sets example output file name')
parser.add_argument('-V', '--version', action='version',
                    version=f'%(prog)s {__version__}')


# documentation: https://fnndsc.github.io/chris_plugin/chris_plugin.html#chris_plugin
@chris_plugin(
    parser=parser,
    title='create_tetra',
    category='',                 # ref. https://chrisstore.co/plugins
    min_memory_limit='100Mi',    # supported units: Mi, Gi
    min_cpu_limit='1000m',       # millicores, e.g. "1000m" = 1 CPU core
    min_gpu_limit=0              # set min_gpu_limit=1 to enable GPU
)
def main(options: Namespace, inputdir: Path, outputdir: Path):
    print(DISPLAY_TITLE)

    output_file = outputdir / f'{options.name}.txt'
    output_file.write_text('did nothing successfully!')


if __name__ == '__main__':
    main()
