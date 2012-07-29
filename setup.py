#!/usr/bin/env python
"""
Installation script:

To release a new version to PyPi:
- Run: python setup.py sdist upload
"""

from setuptools import setup, find_packages

setup(name='pious',
      version='0.0.1',
      url='https://github.com/a-musing-moose/pious',
      author="Jonathan Moss",
      author_email="jonathan.moss@tangentsnowball.com.au",
      description="A python package for dealing with basic input/output processes",
      long_description=open('README.rst').read(),
      keywords="Data, Processing, Pipelines",
      license='BSD',
      platforms=['linux'],
      packages=find_packages(exclude=["*.tests"]),
      include_package_data = True,
      install_requires=[],
      # See http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=['Environment :: Console',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: Unix',
                   'Programming Language :: Python']
      )
