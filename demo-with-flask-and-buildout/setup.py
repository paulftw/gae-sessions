# -*- coding: utf-8 -*-
"""Setup script."""

import os
from setuptools import setup, find_packages

setup(
    name='demo-with-flask-and-buildout',
    version='0.1',
    author="Paul Korzhyk",
    author_email="paul@scifiware.com",
    packages=find_packages('app'),
    package_dir = {'': 'app'},
    include_package_data=True,
    install_requires=[
        'flask',
        'gae-sessions',
        'jinja2',
        'werkzeug',
    ],
    zip_safe=False,
)
