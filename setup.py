#!/usr/bin/env python

from setuptools import setup

setup(
    name='Odyssy',
    version='1.0',
    description='IIIT Vadodara Web Server',
    author='Pratyush Singh',
    author_email='singh.pratyush96@gmail.com',
    url='http://www.python.org/sigs/distutils-sig/',
    install_requires=[
        'Django==1.11.29'
    ],
    dependency_links=[
        'https://pypi.python.org/simple/django/'
    ],
)
