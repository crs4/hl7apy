#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2012-2018, CRS4
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


from __future__ import absolute_import

from setuptools import setup

import hl7apy

desc = "HL7apy: a lightweight Python library to parse, create and handle HL7 v2.x messages"

long_desc = """
HL7apy: a lightweight Python library to parse, create and handle HL7 v2.x messages
----------------------------------------------------------------------------------

HL7apy is a lightweight Python package to intuitively handle `HL7 <http://www.hl7.org>`_ v2 messages according to HL7 specifications.

The main features includes:
 * Message parsing
 * Message creation
 * Message validation following the HL7 xsd specifications
 * Access to elements by name, long name or position
 * Support to all simple and complex datatypes
 * Encoding chars customization
 * Message encoding in ER7 format and compliant with MLLP protocol
"""


def _get_version():
    with open('VERSION') as f:
        return f.read().strip()


setup(
    name='hl7apy',
    version=_get_version(),
    author=hl7apy.__author__,
    author_email=hl7apy.__author_email__,
    description=desc,
    long_description=long_desc,
    url=hl7apy.__url__,
    download_url='http://sourceforge.net/projects/hl7apy/files/',
    license='MIT License',
    keywords=['HL7', 'Health Level 7', 'healthcare', 'python'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Healthcare Industry',
        'Topic :: Scientific/Engineering',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    packages=['hl7apy', 'hl7apy.v2_1', 'hl7apy.v2_2', 'hl7apy.v2_3', 'hl7apy.v2_3_1', 'hl7apy.v2_4', 'hl7apy.v2_5',
              'hl7apy.v2_5_1', 'hl7apy.v2_6', 'hl7apy.v2_7', 'hl7apy.v2_8', 'hl7apy.v2_8_1', 'hl7apy.v2_8_2'],
    scripts=['utils/hl7apy_profile_parser'],
    test_suite='tests',
)
