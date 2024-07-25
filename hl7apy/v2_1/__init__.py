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
import importlib

from .messages import MESSAGES
from .segments import SEGMENTS
from .fields import FIELDS
from .datatypes import DATATYPES, DATATYPES_STRUCTS
from .groups import GROUPS

from hl7apy.v2_1.base_datatypes import CM, ID
from hl7apy.exceptions import ChildNotFound

ELEMENTS = {
    'Message': MESSAGES,
    'Group': GROUPS,
    'Segment': SEGMENTS,
    'Field': FIELDS,
    'Component': DATATYPES,
    'SubComponent': DATATYPES,
    'Datatypes_Structs': DATATYPES_STRUCTS,
    'Table': {},
}


def get(name, element_type):
    try:
        return ELEMENTS[element_type][name]
    except KeyError:
        raise ChildNotFound(name)


def find(name, where):
    """
    >>> from hl7apy.core import Segment
    >>> from hl7apy import find_reference
    >>> find_reference('UNKNOWN', (Segment, ), '2.1')  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    ...
    ChildNotFound: No child named UNKNOWN
    """
    for cls in where:
        try:
            return {'ref': get(name, cls.__name__), 'name': name, 'cls': cls}
        except ChildNotFound:
            pass
    raise ChildNotFound(name)


def is_base_datatype(datatype):
    return datatype in BASE_DATATYPES


def get_base_datatypes():
    return BASE_DATATYPES


def _load_base_datatypes():
    base_dts = ('DT', 'FT', 'NM', 'SI', 'ST', 'TN', 'TX')
    module = importlib.import_module("hl7apy.base_datatypes")
    dts = {}
    for cls in base_dts:
        cls = getattr(module, cls)
        dts[cls.__name__] = cls
    dts.update({'CM': CM})
    dts.update({'ID': ID})
    return dts


BASE_DATATYPES = _load_base_datatypes()

FT = BASE_DATATYPES['FT']
NM = BASE_DATATYPES['NM']
SI = BASE_DATATYPES['SI']
ST = BASE_DATATYPES['ST']
TN = BASE_DATATYPES['TN']
TX = BASE_DATATYPES['TX']
