from setuptools import setup

setup(
    name='create_tetra',
    version='1.0.0',
    description='A ChRIS fs plugin wrapper for create_tetra',
    author='Jennings Zhang',
    author_email='Jennings.Zhang@childrens.harvard.edu',
    url='https://github.com/FNNDSC/pl-create_tetra',
    py_modules=['create_tetra_wrapper'],
    install_requires=['chris_plugin'],
    license='MIT',
    entry_points={
        'console_scripts': [
            'create_tetra_wrapper = create_tetra_wrapper:main'
        ]
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Medical Science Apps.'
    ],
    extras_require={
        'none': [],
        'dev': [
            'pytest~=7.1',
            'pytest-mock~=3.8'
        ]
    }
)
