#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2012-2014, CRS4
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


from distutils.core import setup

setup(
    name = 'hl7apy',
    version = '1.0.0-rc.2',
    description = 'Python library to parse, create and handle HL7 v2.x messages',
    long_description = """
    HL7apy is a Python library to parse, create and handle `HL7 <http://www.hl7.org>`_ v2 messages.

    HL7apy is developed and maintained by `Healthcare Flows <http://www.crs4.it/healthcare-flows>`_ researchers at `CRS4 <http://www.crs4.it>`_.

    Source code on GitHub: https://github.com/crs4/hl7apy

    Documentation can be found here: http://hl7apy.org
    """,
    author = 'Daniela Ghironi, Vittorio Meloni, Alessandro Sulis, Federico Caboni',
    author_email = '<daniela.ghironi@crs4.it>, <vittorio.meloni@crs4.it>, <alessandro.sulis@crs4.it>, <federico.caboni@me.com>',
    url = 'https://github.com/crs4/hl7apy',
    download_url = 'https://github.com/crs4/hl7apy/tarball/v1.0.0-rc.2',
    license = 'MIT License',
    keywords = ['HL7', 'Health Level 7', 'healthcare', 'python'],
    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Intended Audience :: Healthcare Industry',
        'Topic :: Scientific/Engineering :: Medical Science Apps.'
    ],
    packages = ['hl7apy', 'hl7apy.v2_2', 'hl7apy.v2_3', 'hl7apy.v2_3_1', 'hl7apy.v2_4', 'hl7apy.v2_5', 'hl7apy.v2_5_1', 'hl7apy.v2_6'],
    test_suite = 'tests',
)
