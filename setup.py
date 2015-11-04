#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, with_statement
import os
import sys
import codecs
from setuptools import setup, find_packages


# Change to source's directory prior to running any command
try:
    SETUP_DIRNAME = os.path.dirname(__file__)
except NameError:
    # We're most likely being frozen and __file__ triggered this NameError
    # Let's work around that
    SETUP_DIRNAME = os.path.dirname(sys.argv[0])

if SETUP_DIRNAME != '':
    os.chdir(SETUP_DIRNAME)


def read(fname):
    '''
    Read a file from the directory where setup.py resides
    '''
    file_path = os.path.join(SETUP_DIRNAME, fname)
    with codecs.open(file_path, encoding='utf-8') as rfh:
        return rfh.read()

# Version info -- read without importing
_LOCALS = {}
with open(os.path.join(SETUP_DIRNAME, 'pytestsalt', 'version.py')) as rfh:
    exec(rfh.read(), None, _LOCALS)  # pylint: disable=exec-used

VERSION = _LOCALS['__version__']
LONG_DESCRIPTION = read('README.rst')

setup(
    name='pytest-salt',
    version=VERSION,
    author='Pedro Algarvio',
    author_email='pedro@algarvio.me',
    maintainer='Pedro Algarvio',
    maintainer_email='pedro@algarvio.me',
    license='Apache Software License 2.0',
    url='https://github.com/saltstack/pytest-salt',
    description='Pytest Salt Plugin',
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[
        'pytest >= 2.8.1',
        'pytest-logging',
        'pytest-tempdir'
    ],
    setup_requires=[
        'salt>=2015.8.0',
    ],
    dependency_links=[
        'https://github.com/saltstack/salt/tarball/develop#egg=salt-2015.8.0-587-g6a4d68a'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: Apache Software License',
    ],
    entry_points={
        'pytest11': [
            'salt           = pytestsalt',
            'salt.config    = pytestsalt.fixtures.config',
            'salt.daemons   = pytestsalt.fixtures.daemons',
            'salt.dirs      = pytestsalt.fixtures.dirs',
            'salt.ports     = pytestsalt.fixtures.ports',
        ],
    },
)
