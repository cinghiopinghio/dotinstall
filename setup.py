#!/usr/bin/env python3
# Author: Cinghio Pinghio 2015
# -------------------------
# |   This is dotinstall  |
# -------------------------
# |    License: GPL3      |
# |   see LICENSE.txt     |
# -------------------------

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import dotinstall


setup(name='dotinstall',
      version=dotinstall.__version__,
      description=dotinstall.__description__,
      long_description = dotinstall.__long_description__, 
      author=dotinstall.__author__,
      author_email=dotinstall.__author_email__,
      url=dotinstall.__url__,
      license=dotinstall.__copyright__,
      packages=['dotinstall'],
      scripts=['bin/dotinstall'],
      requires=[
          'argparse (>=2.7)',
          'subprocess (>=2.7)'],
      provides='dotinstall',
      classifiers      = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: Linux',
        'Programming Language :: Python',
        ],
)
