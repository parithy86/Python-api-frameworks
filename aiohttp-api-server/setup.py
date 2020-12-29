# !/usr/bin/env python

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

requirements = ['requests, gunicorn', 'aiohttp']

setup(
    name='api-server',
    version='1.0',
    description='REST API server using AIOHTTP',
    author='Ilamparithy Subbiah',
    author_email='parithy.s@gmail.com',
    url='',
    include_package_data=True,
    keywords='REST API'
)
