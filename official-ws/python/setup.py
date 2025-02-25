#!/usr/bin/env python
from setuptools import setup
from os.path import join, dirname

here = dirname(__file__)

setup(name='bitmex-ws-vamber001',
      version='0.4.0',
      description='Sample adapter for connecting to the BitMEX Websocket API.',
      long_description=open(join(here, 'README.md')).read(),
      author='Sam I Am Bead',
      author_email='sammy@beads.com',
      url='',
      install_requires=[
          'websocket-client==0.53.0',
      ],
      packages=['', 'util'],
      )
