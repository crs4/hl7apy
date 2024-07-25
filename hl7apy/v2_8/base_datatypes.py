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

import re

from hl7apy import get_default_encoding_chars
from hl7apy.base_datatypes import TextualDataType as BaseTextualDataType


class TextualDataType(BaseTextualDataType):

    def _get_translations(self, encoding_chars):
        escape_char = encoding_chars['ESCAPE']
        try:
            return ((encoding_chars['FIELD'], '{esc}F{esc}'.format(esc=escape_char)),
                    (encoding_chars['COMPONENT'], '{esc}S{esc}'.format(esc=escape_char)),
                    (encoding_chars['SUBCOMPONENT'], '{esc}T{esc}'.format(esc=escape_char)),
                    (encoding_chars['REPETITION'], '{esc}R{esc}'.format(esc=escape_char)),
                    (encoding_chars['TRUNCATION'], '{esc}L{esc}'.format(esc=escape_char)),)
        except KeyError:
            return ((encoding_chars['FIELD'], '{esc}F{esc}'.format(esc=escape_char)),
                    (encoding_chars['COMPONENT'], '{esc}S{esc}'.format(esc=escape_char)),
                    (encoding_chars['SUBCOMPONENT'], '{esc}T{esc}'.format(esc=escape_char)),
                    (encoding_chars['REPETITION'], '{esc}R{esc}'.format(esc=escape_char)),)

    def _get_escape_char_regex(self, escape_char):
        return r'(?<!%s[HNFSTREL])%s(?![HNFSTREL]%s)' % tuple(3 * [re.escape(escape_char)])

    def to_er7(self, encoding_chars=None):
        if encoding_chars is None:
            encoding_chars = get_default_encoding_chars('2.7')
        return self._escape_value(self.value, encoding_chars)


class ST(TextualDataType):
    """
    Class for ST datatype. It extends :class:`hl7apy.base_datatypes.TextualDatatype` and the parameters are
    the same of the superclass

    :attr:`max_length` is 199
    """
    def __init__(self, value, highlights=None,
                 validation_level=None):
        super(ST, self).__init__(value, 199, highlights, validation_level)


class FT(TextualDataType):
    """
    Class for FT datatype. It extends :class:`hl7apy.base_datatypes.TextualDataType` and the parameters are
    the same of the superclass

    :attr:`max_length` is 65536
    """
    def __init__(self, value, highlights=None,
                 validation_level=None):
        super(FT, self).__init__(value, 65536, highlights, validation_level)


class ID(TextualDataType):
    """
    Class for ID datatype. It extends :class:`hl7apy.base_datatypes.TextualDataType` and the parameters are
    the same of the superclass

    :attr:`max_length` None
    """
    def __init__(self, value, highlights=None,
                 validation_level=None):
        # max_length is None bacause it depends from the HL7 table
        super(ID, self).__init__(value, None, highlights, validation_level)
        # TODO: check for tables of allowed values: are we strict or not?


class IS(TextualDataType):
    """
    Class for IS datatype. It extends :class:`hl7apy.base_datatypes.TextualDataType` and the parameters are
    the same of the superclass

    :attr:`max_length` is 20
    """
    def __init__(self, value, highlights=None,
                 validation_level=None):
        super(IS, self).__init__(value, 20, highlights, validation_level)
        # TODO: check for tables of allowed values (also defined on site): are we strict or not?


class TX(TextualDataType):
    """
    Class for TX datatype. It extends :class:`hl7apy.base_datatypes.TextualDataType` and the parameters are
    the same of the superclass

    :attr:`max_length` is 65536
    """
    def __init__(self, value, highlights=None,
                 validation_level=None):
        super(TX, self).__init__(value, 65536, highlights, validation_level)


class GTS(TextualDataType):
    """
    Class for GTS datatype. It extends :class:`hl7apy.base_datatypes.TextualDataType` and the parameters are
    the same of the superclass

    :attr:`max_length` is 199
    """
    def __init__(self, value, highlights=None,
                 validation_level=None):
        super(GTS, self).__init__(value, 199, highlights, validation_level)


class SNM(TextualDataType):
    """
    :attr:`max_length` is 199
    """
    def __init__(self, value, highlights=None, validation_level=None):
        super(SNM, self).__init__(value, None, highlights, validation_level)
