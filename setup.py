#!/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2015-2016 Dileep Eduri <d.eduri@yahoo.com>
#
# This file is part of codelabs/WunderGround.
#
# This is free software; you can redistribute it and/or modify it under
# the terms of the Lesser GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# THis is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# Lesser GNU General Public License for more details.
#
# You should have received a copy of the Lesser GNU General Public License
# along with this.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup, find_packages

setup(
    name      = "WunderGround",
    version   = "0.1",
    url       = "https://github.com/codelabs/WunderGround",
    packages  = find_packages(exclude=['contrib', 'docs', 'tests*']),
    license   = "LGPLv3",
    platforms = ['OS Independent'],

    install_requires = [
        'requests>=2.6.0',
        'logging>=0.4.9.6',
    ],
    package_data     = {
        '' : ['*.md']
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

