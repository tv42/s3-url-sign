#!/usr/bin/python
from setuptools import setup, find_packages

setup(
    name='s3-url-sign',
    version='0.0.1',
    packages=find_packages(),

    author='Tommi Virtanen',
    author_email='tommi.virtanen@dreamhost.com',
    description='Sign a URL for use with S3',
    license='MIT',
    keywords='s3 web authentication',

    install_requires=[
        'boto >=2.0b4',
        'argparse >=1.2.1',
        ],

    entry_points={
        'console_scripts': [
            's3-url-sign = s3_url_sign:main',
            ],
        },

    )
