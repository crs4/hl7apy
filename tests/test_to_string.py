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

import unittest
from hl7apy.core import Message, Field, Component, SubComponent
from hl7apy.parser import parse_segment, parse_message
from hl7apy.base_datatypes import *
from hl7apy.exceptions import InvalidHighlightRange
from hl7apy.consts import MLLP_ENCODING_CHARS

class ToStringTestCase(unittest.TestCase):
    """
    TestCase class which tests the functionalities of the API converting the
    HL7 elements to string
    """
    def setUp(self):
        self.custom_encoding_chars = {'SEGMENT' : '\r',
                                      'FIELD' :  '!',
                                      'COMPONENT' : '$',
                                      'SUBCOMPONENT' : '@',
                                      'REPETITION' : 'r',
                                      'ESCAPE' : '?'}
        self.msh_values_standard = ['|', '^~\&', 'LIP', 'LIP', 'LB', 'LB', '20111207121030', '', 'RSP^SLI^RSP_K11', '430102569308795840', 'D', '2.5', '', '', '', '', 'IT', '', 'EN', '', '']
        self.msh_standard = 'MSH|^~\\&|LIP|LIP|LB|LB|20111207121030||RSP^SLI^RSP_K11|430102569308795840|D|2.5|||||IT||EN'
        self.msh_values_custom = ['!', '$r?@', 'LIP', 'LIP', 'LB', 'LB', '20111207121030', '', 'RSP^SLI^RSP_K11', '430102569308795840', 'D', '2.5', '', '', '', '', 'IT', '', 'EN', '', '']
        self.msh_custom = 'MSH!$r?@!LIP!LIP!LB!LB!20111207121030!!RSP^SLI^RSP_K11!430102569308795840!D!2.5!!!!!IT!!EN'
        self.msh_highlighted = 'MSH|^~\\&|LIP|LIP|LB|LB|20111207121030|\\H\\HIGHLIGHTED\\N\\TEXT\\H\\IMPORTANT\\N\\|RSP^SLI^RSP_K11|430102569308795840|D|2.5|||||IT||EN'

    def _get_msh(self, values):
        encoding_chars = {'SEGMENT' : '\r',
                          'FIELD' :  values[0],
                          'COMPONENT' : values[1][0],
                          'SUBCOMPONENT' : values[1][1],
                          'REPETITION' : values[1][2],
                          'ESCAPE' : values[1][3]}
        msh = parse_segment('MSH{0}{1}'.format(encoding_chars['FIELD'], encoding_chars['FIELD'].join(values[1:])), encoding_chars=encoding_chars)
        return msh

    def _get_test_msg(self, trailing_children=False):
        if trailing_children is False:
            return 'MSH|^~\\&|SENDING APP|SENDING FAC|REC APP|REC FAC|20110708162817||OML^O33^OML_O33|978226056138290600|D|2.5|||||USA||EN\r' \
                   'PID|1||566-554-3423^^^GHH^MR||SURNAME^NAME^A|||M|||1111 SOMEWHERE STREET^^SOMEWHERE^^^USA||555-555-2004~444-333-222|||M\r' \
                   'PV1||O|||||||||||||||||1107080001^^^LIS\r' \
                   'SPM|1|100187400201||SPECIMEN^Blood|||||||PSN^Human Patient||||||20110708162817||20110708162817|||||||1|CONTAINER^CONTAINER DESC\r' \
                   'ORC|NW|83428|83428|18740|SC||||20110708162817\r' \
                   'TQ1|||||||||R\r' \
                   'OBR||83428|83428|TPO^ANTI THYROPEROXIDASE ANTIBODIES(TPO)^^TPO||||||||||||ND^UNKNOWN^UNKNOWN'
        else:
            return 'MSH|^~\\&|SENDING APP|SENDING FAC|REC APP|REC FAC|20110708162817||OML^O33^OML_O33|978226056138290600|D|2.5|||||USA||EN||\r' \
                   'PID|1||566-554-3423^^^GHH^MR||SURNAME^NAME^A|||M|||1111 SOMEWHERE STREET^^SOMEWHERE^^^USA||555-555-2004~444-333-222|||M|||||||||||||||||||||||\r' \
                   'PV1||O|||||||||||||||||1107080001^^^LIS|||||||||||||||||||||||||||||||||\r' \
                   'SPM|1|100187400201||SPECIMEN^Blood|||||||PSN^Human Patient||||||20110708162817||20110708162817|||||||1|CONTAINER^CONTAINER DESC||\r' \
                   'ORC|NW|83428|83428|18740|SC||||20110708162817|||||||||||||||||||||\r' \
                   'TQ1|||||||||R|||||\r' \
                   'OBR||83428|83428|TPO^ANTI THYROPEROXIDASE ANTIBODIES(TPO)^^TPO||||||||||||ND^UNKNOWN^UNKNOWN|||||||||||||||||||||||||||||||||'


    def _create_test_message(self, msh_values):
        """
        Create a test message - RSP_K11 - with only the msh segment.
        The msh is filled with the sent in input
        """
        msg = Message('RSP_K11')
        msg.msh = self._get_msh(msh_values)
        return msg

    def test_msg_to_string_standard_encoding_chars(self):
        """
        It tests the to_er7 message functionality using default encoding chars
        """
        msg = self._create_test_message(self.msh_values_standard)
        self.assertEqual(msg.to_er7(), self.msh_standard)

    def test_msg_to_string_custom_encoding_chars(self):
        """
        It tests the to_er7 message functionality using custom encoding chars
        """
        msg = self._create_test_message(self.msh_values_custom)
        msg.to_er7(self.custom_encoding_chars)
        self.assertEqual(msg.to_er7(self.custom_encoding_chars), self.msh_custom)

    def test_msg_to_string_empty(self):
        """
        It tests the to_er7 message for an empty message
        """
        from datetime import datetime

        msg = Message('RSP_K11')
        self.assertEqual(msg.to_er7(), 'MSH|^~\\&|||||%s|||||2.5' % datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')
)

    def test_highlights(self):
        """
        It tests the highlighting functionaly
        """
        msg = self._create_test_message(self.msh_values_standard)
        value = ST('HIGHLIGHTEDTEXTIMPORTANT', highlights=((0,11), (15,24)))
        s = SubComponent(datatype='ST', value=value)
        c = Component(datatype='ST')
        c.add(s)
        msg.msh.msh_8.msh_8_1 = c
        self.assertEqual(msg.to_er7(), self.msh_highlighted)

        value = ST('HIGHLIGHTEDTEXTIMPORTANT', highlights=((15,24), (0,11)))
        s = SubComponent(datatype='ST', value=value)
        c = Component(datatype='ST')
        c.add(s)
        msg.msh.msh_8.msh_8_1 = c
        self.assertEqual(msg.to_er7(), self.msh_highlighted)

    def test_invalid_highlights(self):
        """
        It tests that highlighting functionality raises the
        :exc:`InvalidHighlightRange` exception in case of invalid range
        """
        data = ST('HIGHLIGHTEDTEXTIMPORTANT', highlights=((0,11), (4,24)))
        self.assertRaises(InvalidHighlightRange, data.to_er7)
        data = ST('HIGHLIGHTEDTEXTIMPORTANT', highlights=((4,24), (0,11)))
        self.assertRaises(InvalidHighlightRange, data.to_er7)
        data = ST('HIGHLIGHTEDTEXTIMPORTANT', highlights=((5,11), (0,11)))
        self.assertRaises(InvalidHighlightRange, data.to_er7)
        data = ST('HIGHLIGHTEDTEXTIMPORTANT', highlights=((0,11), (0,4)))
        self.assertRaises(InvalidHighlightRange, data.to_er7)

    def test_to_string_msh_field(self):
        m = Message('OML_O33')
        msh = m.msh
        self.assertEqual(msh.msh_1.to_er7(), '|')
        self.assertEqual(msh.msh_2.to_er7(), '^~\\&')
        msh_1 = Field('MSH_1')
        msh_2 = Field('MSH_2')
        self.assertRaises(IndexError, msh_1.to_er7)
        self.assertRaises(IndexError, msh_2.to_er7)

    def test_trailing_children(self):
        test_msg = self._get_test_msg(trailing_children=False)
        test_msg_with_trailing = self._get_test_msg(trailing_children=True)
        msg = parse_message(test_msg)
        self.assertEqual(msg.to_er7(trailing_children=True), test_msg_with_trailing)
        self.assertEqual(msg.to_er7(trailing_children=False), test_msg)

    def test_to_mllp(self):
        test_msg = self._get_test_msg()
        mllp_msg = '{0}{1}{2}{3}{2}'.format(MLLP_ENCODING_CHARS.SB, test_msg,
                                            MLLP_ENCODING_CHARS.CR, MLLP_ENCODING_CHARS.EB)

        msg = parse_message(test_msg)
        self.assertEqual(msg.to_mllp(), mllp_msg)

    def test_to_mllp_with_trailing(self):
        test_msg = self._get_test_msg(trailing_children=True)
        mllp_msg = '{0}{1}{2}{3}{2}'.format(MLLP_ENCODING_CHARS.SB, test_msg,
                                            MLLP_ENCODING_CHARS.CR, MLLP_ENCODING_CHARS.EB)

        msg = parse_message(test_msg)
        self.assertEqual(msg.to_mllp(trailing_children=True), mllp_msg)


if __name__ == '__main__':
    unittest.main()
