# !/usr/bin/env python

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

requirements = ['uvicorn, requests', 'fastapi']

setup(
    name='fast-api-server',
    version='1.0',
    description='REST API server using fast API',
    author='Ilam',
    author_email='parithy.s@gmail.com',
    url='',
    include_package_data=True,
    keywords='REST API'
)
