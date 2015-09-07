#!/bin/python

from setuptools import setup, find_packages

setup(
    name     = "WunderGround",
    version  = "0.1",
    packages = find_packages(exclude=['contrib', 'docs', 'tests*']),

    install_requires = [ 'requests>=2.6.0' ],
    package_data     = {
        '' : ['*.rst']
    },

    extras_require = {
        'test' : ['coverage'],
    },

    test_suite = "tests",

    author = "Dileep Eduri",
    author_email = "d.eduri@yahoo.com",
    description  = "Package provides API to query Wunderground public webservices",
    keywords     = "wunderground weather underground api",
)

