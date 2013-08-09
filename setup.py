#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2012-2013, CRS4
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
    version = '1.0',
    description = 'Python library for handling HL7 v2.x messages',
    license = 'MIT License',
    keywords = ['HL7', 'Health Level 7', 'healthcare'],
    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Intended Audience :: Information Technology'
        'Intended Audience :: Developers',
        'Intended Audience :: Healthcare Industry',
        'Topic :: Scientific/Engineering :: Medical Science Apps.'
    ],
    packages = ['hl7apy', 'hl7apy.v2_2', 'hl7apy.v2_3', 'hl7apy.v2_3_1', 'hl7apy.v2_4', 'hl7apy.v2_5', 'hl7apy.v2_5_1', 'hl7apy.v2_6'],
    test_suite = 'tests',
)
