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
from distutils.errors import DistutilsSetupError

import hl7apy

def _get_version():
    try:
        with open('VERSION') as f:
            return f.read().strip()
    except IOError:
        raise DistutilsSetupError("failed to read version info")


setup(
    name = 'hl7apy',
    version = _get_version(),
    description = hl7apy.__doc__.strip().splitlines()[0],
    long_description = hl7apy.__doc__.strip(),
    author = hl7apy.__author__,
    author_email = hl7apy.__author_email__,
    url = hl7apy.__url__,
    download_url = 'http://sourceforge.net/projects/hl7apy/files/',
    license = 'MIT License',
    keywords = ['HL7', 'Health Level 7', 'healthcare', 'python'],
    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Intended Audience :: Healthcare Industry',
        'Topic :: Scientific/Engineering :: Medical Science Apps.'
    ],
    packages = ['hl7apy', 'hl7apy.v2_2', 'hl7apy.v2_3', 'hl7apy.v2_3_1', 'hl7apy.v2_4',
                'hl7apy.v2_5', 'hl7apy.v2_5_1', 'hl7apy.v2_6'],
    test_suite = 'tests',
)
