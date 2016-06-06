import os, sys
from setuptools import Command, setup

long_description = open('README.md').read()

setup(
    author = 'Iwan Budi Kusnanto',
    url = 'https://github.com/iwanbk/nyamuk',
    author_email ='iwan.b.kusnanto@gmail.com',
    version ='0.2.0',
    packages = ['nyamuk'],
    name = 'nyamuk',
    description = 'Python MQTT Client Library',
    long_description = long_description,
    license = "BSD",
    scripts = ['test/pubnya.py','test/subnya.py'],
)
