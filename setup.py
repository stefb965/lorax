# -*- coding: utf-8 -*-
'''
lorax -- I speak for the (phylogenetic) trees.
'''

# Developers, install with
#    pip install --editable .
# and execute as a module.

from setuptools import setup

from distutils.util import convert_path
import os
import sys

name = 'lorax'

# restrict to python 3.4 or later
if sys.version_info < (3,4,0,'final',0):
    raise SystemExit('Python 3.4 or later is required!')

# get version from version.py
version_dict = {}
version_path = convert_path(name+'/version.py')
with open(version_path) as version_file:
    exec(version_file.read(), version_dict)
version = version_dict['version']

# data_files will be tree in examples/ directory
exampledir = os.path.join(name, 'examples')
examplefiles = [(root, [os.path.join(root, f) for f in files])
    for root, dirs, files in os.walk(exampledir)]

setup(
    name=name,
    version=version,
    data_files=examplefiles,
    url='http://github.com/ncgr/lorax',
    keywords=['science', 'biology', 'bioinformatics', 'genomics',
              'sequence', 'curation'],
    license='BSD',
    description='Server for phylogenetic tree generation and extension',
    long_description=open('README.rst').read(),
    author='Joel Berendzen',
    author_email='joelb@ncgr.org',
    packages=[name],
    package_data = {'lorax': ['test/*',
                              'templates/*',
                              'static/js/*',
                              'static/css/*,'
                              'static/favicon.ico']},
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask-RQ2',
                      'biopython',
                      'rq_dashboard'
                      ],
    entry_points={
                 'console_scripts':['lorax = lorax.cli:cli']
                },
    classifiers=['Development Status :: 4 - Beta',
                 'Environment :: Console',
                 'Intended Audience :: Science/Research',
                 'License :: OSI Approved :: BSD License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: 3.6',
                 'Topic :: Scientific/Engineering :: Bio-Informatics'
                 ]
)
