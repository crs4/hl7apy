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


DATATYPES = {
    'AD_1': ['leaf', None, 'ST', 'STREET_ADDRESS', None, -1],
    'AD_2': ['leaf', None, 'ST', 'OTHER_DESIGNATION', None, -1],
    'AD_3': ['leaf', None, 'ST', 'CITY', None, -1],
    'AD_4': ['leaf', None, 'ST', 'STATE_OR_PROVINCE', None, -1],
    'AD_5': ['leaf', None, 'ID', 'ZIP_OR_POSTAL_CODE', None, -1],
    'AD_6': ['leaf', None, 'ID', 'COUNTRY', None, -1],
    'CE_1': ['leaf', None, 'ID', 'IDENTIFIER', None, -1],
    'CE_2': ['leaf', None, 'ST', 'TEXT', None, -1],
    'CE_3': ['leaf', None, 'ST', 'NAME_OF_CODING_SYSTEM', None, -1],
    'CE_4': ['leaf', None, 'ST', 'ALTERNATE_IDENTIFIER', None, -1],
    'CE_5': ['leaf', None, 'ST', 'ALTERNATE_TEXT', None, -1],
    'CE_6': ['leaf', None, 'ST', 'NAME_OF_ALTERNATE_CODING_SYSTEM', None, -1],
    'CK_1': ['leaf', None, 'NM', 'ID_NUMBER', None, -1],
    'CK_2': ['leaf', None, 'NM', 'CHECK_DIGIT', None, -1],
    'CK_3': ['leaf', None, 'ID', 'CODE_IDENTIFYING_CHECK_DIGIT_SCHEME_EMPLOYED', None, -1],
    'CM_MSG_1': ['leaf', None, 'ID', 'MESSAGE_TYPE', None, -1],
    'CM_MSG_2': ['leaf', None, 'ID', 'TRIGGER_EVENT', None, -1],
    'CN_1': ['leaf', None, 'ID', 'ID', None, -1],
    'CN_2': ['leaf', None, 'ST', 'FAMILIY_NAME', None, -1],
    'CN_3': ['leaf', None, 'ST', 'GIVEN_NAME', None, -1],
    'CN_4': ['leaf', None, 'ST', 'MIDDLE_INITIAL_OR_NAME', None, -1],
    'CN_5': ['leaf', None, 'ST', 'DEGREE', None, -1],
    'CQ_1': ['leaf', None, 'ST', 'QUANTITY', None, -1],
    'CQ_2': ['leaf', None, 'ST', 'UNITS', None, -1],
    'PN_1': ['leaf', None, 'ST', 'FAMILIY_NAME', None, -1],
    'PN_2': ['leaf', None, 'ST', 'GIVEN_NAME', None, -1],
    'PN_3': ['leaf', None, 'ST', 'MIDDLE_INITIAL_OR_NAME', None, -1],
    'PN_4': ['leaf', None, 'ST', 'SUFFIX', None, -1],
    'PN_5': ['leaf', None, 'ST', 'PREFIX', None, -1],
    'PN_6': ['leaf', None, 'ST', 'DEGREE', None, -1],
    'TS_1': ['leaf', None, 'ST', 'TIME_OF_EVENT', None, -1],
    'TS_2': ['leaf', None, 'ST', 'DEGREE_OF_PRECISION', None, -1],
}


DATATYPES_STRUCTS = {
    'AD': (
           ('AD_1', DATATYPES['AD_1'], (0, 1), 'CMP'),
           ('AD_2', DATATYPES['AD_2'], (0, 1), 'CMP'),
           ('AD_3', DATATYPES['AD_3'], (0, 1), 'CMP'),
           ('AD_4', DATATYPES['AD_4'], (0, 1), 'CMP'),
           ('AD_5', DATATYPES['AD_5'], (0, 1), 'CMP'),
           ('AD_6', DATATYPES['AD_6'], (0, 1), 'CMP'),),
    'CE': (
           ('CE_1', DATATYPES['CE_1'], (0, 1), 'CMP'),
           ('CE_2', DATATYPES['CE_2'], (0, 1), 'CMP'),
           ('CE_3', DATATYPES['CE_3'], (0, 1), 'CMP'),
           ('CE_4', DATATYPES['CE_4'], (0, 1), 'CMP'),
           ('CE_5', DATATYPES['CE_5'], (0, 1), 'CMP'),
           ('CE_6', DATATYPES['CE_6'], (0, 1), 'CMP'),),
    'CK': (
           ('CK_1', DATATYPES['CK_1'], (0, 1), 'CMP'),
           ('CK_2', DATATYPES['CK_2'], (0, 1), 'CMP'),
           ('CK_3', DATATYPES['CK_3'], (0, 1), 'CMP'),),
    'CM_MSG': (
           ('CM_MSG_1', DATATYPES['CM_MSG_1'], (0, 1), 'CMP'),
           ('CM_MSG_2', DATATYPES['CM_MSG_2'], (0, 1), 'CMP'),),
    'CN': (
           ('CN_1', DATATYPES['CN_1'], (0, 1), 'CMP'),
           ('CN_2', DATATYPES['CN_2'], (0, 1), 'CMP'),
           ('CN_3', DATATYPES['CN_3'], (0, 1), 'CMP'),
           ('CN_4', DATATYPES['CN_4'], (0, 1), 'CMP'),
           ('CN_5', DATATYPES['CN_5'], (0, 1), 'CMP'),),
    'CQ': (
           ('CQ_1', DATATYPES['CQ_1'], (0, 1), 'CMP'),
           ('CQ_2', DATATYPES['CQ_2'], (0, 1), 'CMP'),),
    'PN': (
           ('PN_1', DATATYPES['PN_1'], (0, 1), 'CMP'),
           ('PN_2', DATATYPES['PN_2'], (0, 1), 'CMP'),
           ('PN_3', DATATYPES['PN_3'], (0, 1), 'CMP'),
           ('PN_4', DATATYPES['PN_4'], (0, 1), 'CMP'),
           ('PN_5', DATATYPES['PN_5'], (0, 1), 'CMP'),
           ('PN_6', DATATYPES['PN_6'], (0, 1), 'CMP'),),
    'TS': (('TS_1', DATATYPES['TS_1'], (1, 1), 'CMP'),
           ('TS_2', DATATYPES['TS_2'], (1, 1), 'CMP'),),
}
