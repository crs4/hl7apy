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

import importlib

from messages import MESSAGES
from segments import SEGMENTS
from fields import FIELDS
from datatypes import DATATYPES
from groups import GROUPS

from hl7apy.v2_6.base_datatypes import ST
from hl7apy.exceptions import ChildNotFound

ELEMENTS = {'Message': MESSAGES, 'Segment': SEGMENTS, 'Field': FIELDS,
            'Component': DATATYPES, 'Group': GROUPS, 'SubComponent': DATATYPES}

def get(name, element_type):
    return ELEMENTS[element_type][name]

def find(name, where):
    for cls in where:
        try:
            return {'ref': get(name, cls.__name__), 'name': name, 'cls': cls}
        except:
            pass
    raise ChildNotFound(name)

def is_base_datatype(datatype):
    return datatype in BASE_DATATYPES

def get_base_datatypes():
    return BASE_DATATYPES

def _load_base_datatypes():
    base_datatypes = ('ID', 'DT', 'DTM', 'FT', 'GTS', 'IS', 'NM', 'SI', 'TM', 'TX')
    module = importlib.import_module("hl7apy.base_datatypes")
    datatypes = {}
    for cls in base_datatypes:
        cls = getattr(module, cls)
        datatypes[cls.__name__] = cls
    datatypes.update({'ST' : ST})
    return datatypes

BASE_DATATYPES = _load_base_datatypes()
