from setuptools import setup, find_packages
import sys, os

version = '0.1.2'

setup(name='webpype',
      version=version,
      description="Python library for WebPipes",
      long_description=open('README.md').read(),
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords="web json webpipe",
      author="AJ Bahnken",
      author_email="aj@ajvb.me",
      url="https://github.com/ajvb/webpype",
      license="Apache License v2",
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
)
