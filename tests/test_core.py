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
import os
import platform
import sys
import unittest

import hl7apy
from hl7apy import DEFAULT_ENCODING_CHARS
from hl7apy.core import Message, Segment, Field, Group, Component, SubComponent, ElementProxy
from hl7apy.exceptions import ChildNotValid, ChildNotFound, OperationNotAllowed, InvalidName, \
    MaxChildLimitReached, UnsupportedVersion, InvalidEncodingChars, \
    MaxLengthReached, MessageProfileNotFound, LegacyMessageProfile
from hl7apy.v2_5 import ST, SI
from hl7apy.validation import VALIDATION_LEVEL
from hl7apy.parser import parse_message, parse_segment


def _get_invalid_encoding_chars():
    return {'COMPONENT': '$',
            'SUBCOMPONENT': '@',
            'REPETITION': 'r',
            'ESCAPE': '@'}


def _get_test_msg():
    return 'MSH|^~\\&|SENDING APP|SENDING FAC|REC APP|REC FAC|20110708162817||OML^O33^OML_O33|978226056138290600|D|2.5|||||USA||EN\r' \
           'PID|||1010110909194822^^^GATEWAY_IL&1.3.6.1.4.1.21367.2011.2.5.17&ISO^PK||PIPPO^PLUTO^^^^^L||19790515|M|||VIA DI TOPOLINO^CAGLIARI^CAGLIARI^^09100^100^H^^092009^^~^^^^^^L^^^|||||||PPPPPP79E15B354I^^^CF|||||CAGLIARI|||100|||||||||||\r' \
           'PV1||O|||||||||||||||||1107080001^^^LIS\r' \
           'SPM|1|100187400201^||SPECIMEN^Blood|||||||PSN^Human Patient||||||20110708162817||20110708162817|||||||1|CONTAINER^CONTAINER DESC\r' \
           'ORC|NW|83428|83428|18740|SC||||20110708162817||||||||^\r' \
           'TQ1|||||||||R\r' \
           'OBR||83428|83428|TPO^ANTI THYROPEROXIDASE ANTIBODIES(TPO)^^TPO||||||||||||ND^UNKNOWN^UNKNOWN\r'


def _get_test_msg_2():
    return 'MSH|^~\\&|SENDING APP|SENDING FAC|REC APP|REC FAC|20110708162817||OML^O33|978226056138290600|D|2.5|||||USA||EN\r' \
           'PID|1||566-554-3423^^^GHH^MR||SURNAME^NAME^A|||M|||1111 SOMEWHERE STREET^^SOMEWHERE^^^USA||555-555-2004~444-333-222|||M\r' \
           'PV1||O|||||||||||||||||1107080001^^^LIS\r' \
           'SPM|1|100187400201||SPECIMEN^Blood|||||||PSN^Human Patient||||||20110708162817||20110708162817|||||||1|CONTAINER^CONTAINER DESC\r' \
           'ORC|NW|83428|83428|18740|SC||||20110708162817||||||||\r' \
           'TQ1|||||||||R\r' \
           'OBR||83428|83428|TPO^ANTI THYROPEROXIDASE ANTIBODIES(TPO)^^TPO||||||||||||ND^UNKNOWN^UNKNOWN\r' \
           'SPM|2|100187400101||SPECIMEN^Blood|||||||PSN^Human Patient||||||20110708162817||20110708162817|||||||1|CONTAINER^CONTAINER DESC\r' \
           'ORC|NW|83425|83425|18740|SC||||20110708162817||||||||\rTQ1|||||||||R\r' \
           'OBR||83425|83425|CA^S-CALCIUM^^CA||||||||||||ND^Sconosciuto^Sconosciuto\rORC|NW|83426|83426|18740|SC||||20110708162817||||||||\r' \
           'TQ1|||||||||R\rOBR||83426|83426|HDL^HDL CHOLESTEROL^^HDL||||||||||||ND^UNKNOWN^UNKNOWN\r' \
           'ORC|NW|83427|83427|18740|SC||||20110708162817||||||||\r' \
           'TQ1|||||||||R\rOBR||83427|83427|LDL^LDL CHOLESTEROL^^LDL||||||||||||ND^UNKNOWN^UNKNOWN'


def _get_fail_test_msg():
    # This message will fail validation because of the OML_O33 message structure
    return 'MSH|^~\\&|SENDING APP|SENDING FAC|REC APP|REC FAC|20110708162817||OML^O33^OML_O33|978226056138290600|D|2.5|||||USA||EN\r' \
           'PID|1||566-554-3423^^^GHH^MR||SURNAME^NAME^A|||M|||1111 SOMEWHERE STREET^^SOMEWHERE^^^USA||555-555-2004~444-333-222|||M\r' \
           'PV1||O|||||||||||||||||1107080001^^^LIS\r' \
           'SPM|1|100187400201||SPECIMEN^Blood|||||||PSN^Human Patient||||||20110708162817||20110708162817|||||||1|CONTAINER^CONTAINER DESC\r' \
           'ORC|NW|83428|83428|18740|SC||||20110708162817||||||||\r' \
           'TQ1|||||||||R\r' \
           'OBR||83428|83428|TPO^ANTI THYROPEROXIDASE ANTIBODIES(TPO)^^TPO||||||||||||ND^UNKNOWN^UNKNOWN\r' \
           'SPM|2|100187400101||SPECIMEN^Blood|||||||PSN^Human Patient||||||20110708162817||20110708162817|||||||1|CONTAINER^CONTAINER DESC\r' \
           'ORC|NW|83425|83425|18740|SC||||20110708162817||||||||\rTQ1|||||||||R\r' \
           'OBR||83425|83425|CA^S-CALCIUM^^CA||||||||||||ND^Sconosciuto^Sconosciuto\rORC|NW|83426|83426|18740|SC||||20110708162817||||||||\r' \
           'TQ1|||||||||R\rOBR||83426|83426|HDL^HDL CHOLESTEROL^^HDL||||||||||||ND^UNKNOWN^UNKNOWN\r' \
           'ORC|NW|83427|83427|18740|SC||||20110708162817||||||||\r' \
           'TQ1|||||||||R\rOBR||83427|83427|LDL^LDL CHOLESTEROL^^LDL||||||||||||ND^UNKNOWN^UNKNOWN'


def _get_rsp_k21_mp_msg():
    return 'MSH|^~\\&|SENDING APP|SENDING FAC|RECEIVING APP|RECEIVING FAC|20140410170011||RSP^K22^RSP_K21|11111111|P|2.5\r' \
           'MSA|AA|20140410170015\r' \
           'QAK|222222222|OK\r' \
           'QPD|IHE PDQ Query|222222222|@PID.3.1.1^3333333|||||^^^IHEFACILITY&1.3.6.1.4.1.21367.3000.1.6&ISO|\r' \
           'PID|1||10101109091948^^^GATEWAY&1.3.6.1.4.1.21367.2011.2.5.17&ISO||JOHN^SMITH^^^^^A||19690113|M|||VIA DELLE VIE^^CAGLIARI^^^ITA^H^^092009||||||||||||CAGLIARI|||\r'


class TestMessage(unittest.TestCase):

    def setUp(self):
        base_path = os.path.abspath(os.path.dirname(__file__))
        mp_path = os.path.join(base_path, 'profiles/iti_21')
        self.rsp_k21_mp = hl7apy.load_message_profile(mp_path)
        if platform.system() == 'Windows':
            legacy_mp = os.path.join(base_path, 'profiles/old_pharm_h4_win')
        else:
            legacy_mp = os.path.join(base_path, 'profiles/old_pharm_h4')
        self.legacy_mp = hl7apy.load_message_profile(legacy_mp)

    # Message test cases
    def test_create_empty_message(self):
        e = Message()
        self.assertEqual(e.classname, 'Message')
        self.assertRaises(OperationNotAllowed, Message, validation_level=VALIDATION_LEVEL.STRICT)

    def test_create_unknown_message(self):
        self.assertRaises(InvalidName, Message, 'AAA_A01')
        self.assertRaises(InvalidName, Message, 'AAA_A01', version='2.2')
        self.assertRaises(InvalidName, Message, 'AAA_A01', version='2.3')
        self.assertRaises(InvalidName, Message, 'AAA_A01', version='2.3.1')
        self.assertRaises(InvalidName, Message, 'AAA_A01', version='2.4')
        self.assertRaises(InvalidName, Message, 'AAA_A01', version='2.5')
        self.assertRaises(InvalidName, Message, 'AAA_A01', version='2.5.1')
        self.assertRaises(InvalidName, Message, 'AAA_A01', version='2.6')
        self.assertRaises(InvalidName, Message, 'AAA_A01', version='2.7')
        self.assertRaises(InvalidName, Message, 'AAA_A01', validation_level=VALIDATION_LEVEL.STRICT)

    def test_create_unsupported_version_message(self):
        self.assertRaises(UnsupportedVersion, Message, version='2.0')

    def test_create_invalid_encoding_chars_message(self):
        self.assertRaises(InvalidEncodingChars, Message, encoding_chars=_get_invalid_encoding_chars())
        self.assertRaises(InvalidEncodingChars, Message, 'ADT_A01',
                          encoding_chars=_get_invalid_encoding_chars(),
                          validation_level=VALIDATION_LEVEL.STRICT)

    def test_create_insensitive(self):
        e = Message('oml_o35')
        self.assertEqual(e.classname, 'Message')
        self.assertTrue(e.is_named('OML_O35'))

    def test_add_group_to_message(self):
        e = Message('OML_O35')
        self.assertRaises(ChildNotFound, e.add_group, 'UNKNOWN_GROUP')
        g = e.add_group('OML_O35_PATIENT')
        self.assertTrue(g.is_named('OML_O35_PATIENT'))
        self.assertEqual(g.classname, 'Group')
        self.assertIn(g, e.children)

        m = Message('RSP_K21', reference=self.rsp_k21_mp)
        g = m.add_group('rsp_k21_query_response')
        self.assertTrue(g.is_named('RSP_K21_QUERY_RESPONSE'))
        self.assertIn(g, m.children)

    def test_add_child_with_different_validation_level(self):
        m = Message('RSP_K21', validation_level=VALIDATION_LEVEL.STRICT)
        g = Group('RSP_K21_QUERY_RESPONSE', validation_level=VALIDATION_LEVEL.TOLERANT)
        self.assertRaises(OperationNotAllowed, m.add, g)

        m = Message('RSP_K21', validation_level=VALIDATION_LEVEL.TOLERANT)
        g = Group('RSP_K21_QUERY_RESPONSE', validation_level=VALIDATION_LEVEL.STRICT)
        self.assertRaises(OperationNotAllowed, m.add, g)

        m = Message('RSP_K21', validation_level=VALIDATION_LEVEL.STRICT)
        s = Segment('QPD', validation_level=VALIDATION_LEVEL.TOLERANT)
        self.assertRaises(OperationNotAllowed, m.add, s)

        m = Message('RSP_K21', validation_level=VALIDATION_LEVEL.TOLERANT)
        s = Segment('QPD', validation_level=VALIDATION_LEVEL.STRICT)
        self.assertRaises(OperationNotAllowed, m.add, s)

    def test_add_child_with_different_version(self):
        m = Message('RSP_K21', version='2.4')
        g = Group('RSP_K21_QUERY_RESPONSE', version='2.5')
        self.assertRaises(OperationNotAllowed, m.add, g)

        m = Message('RSP_K21', version='2.4')
        s = Segment('QPD', version='2.5')
        self.assertRaises(OperationNotAllowed, m.add, s)

    def test_add_empty_children_to_message(self):
        a = Message('OML_O33', validation_level=VALIDATION_LEVEL.STRICT)
        self.assertRaises(ChildNotValid, a.add, Group())
        b = Message('OML_O33')
        b.add(Group())
        c = Message('RSP_K21', self.rsp_k21_mp)
        c.add(Group())

    def test_add_not_allowed_segment_to_known_message(self):
        a = Message('OML_O33', validation_level=VALIDATION_LEVEL.STRICT)
        self.assertRaises(ChildNotValid, a.add, Segment('MSA'))
        b = Message('OML_O33')
        b.add(Segment('MSA'))

        a = Message('RSP_K21', validation_level=VALIDATION_LEVEL.STRICT, reference=self.rsp_k21_mp)
        self.assertRaises(ChildNotValid, a.add, Segment('SPM'))
        self.assertRaises(ChildNotValid, a.add_segment, 'SPM')

        b = Message('RSP_K21', reference=self.rsp_k21_mp)
        b.add(Segment('SPM'))
        b.add_group('SPM')

    def test_create_z_message(self):
        Message('ZDT_ZDT')
        Message('ZA1_ZB2')
        Message('za1_zb2')
        self.assertRaises(InvalidName, Message, 'za1azb2')
        self.assertRaises(InvalidName, Message, 'z##_azb2')
        self.assertRaises(InvalidName, Message, 'zab_zaba')
        self.assertRaises(InvalidName, Message, 'zaba_zab')
        self.assertRaises(InvalidName, Message, 'OML_ZAB')
        self.assertRaises(InvalidName, Message, 'zab_oml')

        Message('ZDT_ZDT', validation_level=VALIDATION_LEVEL.STRICT)
        Message('ZA1_ZB2', validation_level=VALIDATION_LEVEL.STRICT)
        Message('za1_zb2', validation_level=VALIDATION_LEVEL.STRICT)
        self.assertRaises(InvalidName, Message, 'za1azb2', validation_level=VALIDATION_LEVEL.STRICT)
        self.assertRaises(InvalidName, Message, 'z##_azb2', validation_level=VALIDATION_LEVEL.STRICT)
        self.assertRaises(InvalidName, Message, 'zab_zaba', validation_level=VALIDATION_LEVEL.STRICT)
        self.assertRaises(InvalidName, Message, 'zaba_zab', validation_level=VALIDATION_LEVEL.STRICT)
        self.assertRaises(InvalidName, Message, 'OML_ZAB', validation_level=VALIDATION_LEVEL.STRICT)
        self.assertRaises(InvalidName, Message, 'zab_oml', validation_level=VALIDATION_LEVEL.STRICT)

    def test_add_z_segment(self):
        a = Message('OML_O33', validation_level=VALIDATION_LEVEL.STRICT)
        a.add(Segment('ZIN', validation_level=VALIDATION_LEVEL.STRICT))
        a.add_segment('zap')
        a.zbe = 'ZBE||ab|ab|'

        b = Message('OML_O33', validation_level=VALIDATION_LEVEL.TOLERANT)
        b.add(Segment('ZIN', validation_level=VALIDATION_LEVEL.TOLERANT))
        b.add_segment('zap')
        b.zbe = 'ZBE||ab|ab|'

        a = Message('RSP_K21', validation_level=VALIDATION_LEVEL.STRICT, reference=self.rsp_k21_mp)
        a.add(Segment('ZIN', validation_level=VALIDATION_LEVEL.STRICT))
        a.add_segment('zap')
        a.zbe = 'ZBE||ab|ab|'

        a = Message('RSP_K21', validation_level=VALIDATION_LEVEL.TOLERANT, reference=self.rsp_k21_mp)
        a.add(Segment('ZIN', validation_level=VALIDATION_LEVEL.TOLERANT))
        a.add_segment('zap')
        a.zbe = 'ZBE||ab|ab|'

    def test_add_to_z_message(self):
        m = Message('ZDT_ZDT')
        m.add(Segment('PID'))
        m.add_segment('ZIN')
        m.zap = 'ZAP||21||'
        m.add_group('OML_O33_PATIENT')

        m = Message('ZDT_ZDT', validation_level=VALIDATION_LEVEL.STRICT)
        m.add(Segment('PID', validation_level=VALIDATION_LEVEL.STRICT))
        m.add_segment('ZIN')
        m.zap = 'ZAP||21||'

        m.add_group('OML_O33_PATIENT')

    def test_add_known_segment_to_empty_message(self):
        a = Message('OML_O33')
        a.add(Segment('MSA'))

    def test_add_known_group_to_empty_message(self):
        a = Message('OML_O33')
        a.add(Group('OML_O33_PATIENT'))

    def test_assign_wrong_segment_to_known_position(self):
        a = Message('OML_O33', validation_level=VALIDATION_LEVEL.STRICT)
        b = Message('OML_O33')
        with self.assertRaises(ChildNotValid):
            a.msh = Segment('SPM')
        with self.assertRaises(ChildNotValid):
            a.pid = 'EVN||20080115153000||||20080114003000'
        with self.assertRaises(InvalidName):
            a.zin = 'PAP||abc||'
        with self.assertRaises(InvalidName):
            a.msh = 'PAP||abc||'

        with self.assertRaises(ChildNotValid):
            b.msh = Segment('SPM')
        with self.assertRaises(ChildNotValid):
            b.pid = 'EVN||20080115153000||||20080114003000'
        with self.assertRaises(InvalidName):
            b.zin = 'PAP||abc||'
        with self.assertRaises(InvalidName):
            b.pid = 'PAP||abc||'

    def test_add_segment_to_message_mix(self):
        a = Message('OML_O33',  validation_level=VALIDATION_LEVEL.TOLERANT)
        msh = Segment('MSH', validation_level=VALIDATION_LEVEL.TOLERANT)
        pid = Segment('PID', validation_level=VALIDATION_LEVEL.TOLERANT)
        g = Group('OML_O33_PATIENT')
        g.add(pid)
        a.add(msh)
        a.add(g)

    def test_assign_value(self):
        msg = _get_test_msg()
        a = Message('OML_O33', validation_level=VALIDATION_LEVEL.TOLERANT)
        parsed_a = parse_message(msg, validation_level=VALIDATION_LEVEL.TOLERANT)
        a.value = msg
        self.assertEqual(a.to_er7(), parsed_a.to_er7())

        b = Message('OML_O33', validation_level=VALIDATION_LEVEL.STRICT)
        b.value = msg
        parsed_b = parse_message(msg, validation_level=VALIDATION_LEVEL.STRICT)
        self.assertEqual(b.to_er7(), parsed_b.to_er7())
        self.assertEqual(list(b.children.indexes.keys()), list(parsed_b.children.indexes.keys()))

        c = Message('ADT_A01', validation_level=VALIDATION_LEVEL.TOLERANT)
        with self.assertRaises(OperationNotAllowed):
            c.value = msg

        msg = msg.replace('^', 'x')
        with self.assertRaises(OperationNotAllowed):
            a.value = msg

        c = Message('OML_O33', version='2.6')
        with self.assertRaises(OperationNotAllowed):
            c.value = msg

        msg = _get_rsp_k21_mp_msg()
        a = Message('RSP_K21', validation_level=VALIDATION_LEVEL.TOLERANT, reference=self.rsp_k21_mp)
        parsed_a = parse_message(msg, message_profile=self.rsp_k21_mp,
                                 validation_level=VALIDATION_LEVEL.TOLERANT)
        a.value = msg
        self.assertEqual(a.to_er7(), parsed_a.to_er7())

        msg = _get_rsp_k21_mp_msg()
        a = Message('RSP_K21', validation_level=VALIDATION_LEVEL.STRICT, reference=self.rsp_k21_mp)
        parsed_a = parse_message(msg, message_profile=self.rsp_k21_mp,
                                 validation_level=VALIDATION_LEVEL.STRICT)
        a.value = msg
        self.assertEqual(a.to_er7(), parsed_a.to_er7())

    def test_assign_value_unknown_message(self):
        msg = _get_test_msg_2()
        a = Message()
        parsed_a = parse_message(msg, validation_level=VALIDATION_LEVEL.TOLERANT)
        a.value = msg
        self.assertEqual(a.name, 'OML_O33')
        self.assertEqual(a.to_er7(), parsed_a.to_er7())

    def test_message_profile(self):
        m = Message('RSP_K21', reference=self.rsp_k21_mp)
        # The original qpd_3 is varies
        self.assertEqual(m.qpd.qpd_3.datatype, 'QIP')
        self.assertFalse(m.qpd.allow_infinite_children)

    def test_message_profile_not_found(self):
        self.assertRaises(MessageProfileNotFound, Message, 'ADT_A01', reference=self.rsp_k21_mp)
    # def test_message_ordered_children(self):
    #    m = Message('OML_O33')
    #    m.add(Group('OML_O33_PATIENT'))
    #    ordered_children = m.children.get_ordered_children()
    #    self.assertEqual(ordered_children[0][0].name, 'MSH' )
    #    self.assertIsNone(ordered_children[1])
    #    self.assertEqual(ordered_children[3][0].name, 'OML_O33_PATIENT')
    #    self.assertIsNone(ordered_children[2])
    #    self.assertIsNone(ordered_children[4])

    # def test_message_get_children(self):
    #    m = Message('OML_O33')
    #    children = m.children.get_children()
    #    self.assertEqual(len(children), 1)
    #    m.pid = 'PID|||||bianchi^mario|||'
    #    children = m.children.get_children()
    #    self.assertEqual(len(children), 2)

    def test_bug_13(self):
        m = Message("RSP_K21")
        g = m.rsp_k21_query_response
        self.assertEqual(id(m.rsp_k21_query_response), id(g))  # test that the ElementProxy is the same

        # tests the creation of traversal_indexes item
        pid1 = m.rsp_k21_query_response.pid
        self.assertIn("RSP_K21_QUERY_RESPONSE", m.children.traversal_indexes)

        pid2 = m.rsp_k21_query_response.pid
        pid1.value = 'PID|a|b|'
        # tests that assigning a child to one occurrence affect also the others
        self.assertEqual(pid1.children, pid2.children)
        self.assertEqual(pid1.children, m.rsp_k21_query_response.pid.children)
        self.assertNotIn("RSP_K21_QUERY_RESPONSE", m.children.traversal_indexes)

        sub = m.rsp_k21_query_response.pid.pid_3.cx_10.cwe_1

    def test_create_v27_message(self):
        m = Message('RSP_K21', version='2.7')
        self.assertEqual(m.encoding_chars['TRUNCATION'], '#')
        self.assertEqual(m.msh.msh_2.to_er7(), '^~\\&#')

    def test_create_v27_message_no_truncation(self):
        m = Message('RSP_K21', encoding_chars=DEFAULT_ENCODING_CHARS, version='2.7')
        self.assertNotIn('TRUNCATION', m.encoding_chars)
        self.assertEqual(m.msh.msh_2.to_er7(), '^~\\&')

    def test_legacy_message_profile(self):
        self.assertRaises(LegacyMessageProfile, Message, 'RAS_O17', reference=self.legacy_mp)


class TestGroup(unittest.TestCase):

    # Group test cases
    def setUp(self):
        self.oml_o33_specimen = 'SPM|1|100187400201||SPECIMEN^Blood|||||||PSN^Human Patient||||||20110708162817||20110708162817|||||||1|CONTAINER^CONTAINER DESC\r' \
           'ORC|NW|83428|83428|18740|SC||||20110708162817\r' \
           'TQ1|||||||||R\r' \
           'OBR||83428|83428|TPO^ANTI THYROPEROXIDASE ANTIBODIES(TPO)^^TPO||||||||||||ND^UNKNOWN^UNKNOWN'

        self.rsp_k21_query_response = 'PID|1||10101109091948^^^GATEWAY&1.3.6.1.4.1.21367.2011.2.5.17&ISO||JOHN^SMITH^^^^^A||19690113|M|||VIA DELLE VIE^^CAGLIARI^^^ITA^H^^092009||||||||||||CAGLIARI'

        base_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(base_path, 'profiles/iti_21')
        self.rsp_k21_mp = hl7apy.load_message_profile(path)

    def test_create_unknown_group(self):
        self.assertRaises(InvalidName, Group, 'UNKNOWN')
        self.assertRaises(InvalidName, Group, 'UNKNOWN', validation_level=VALIDATION_LEVEL.STRICT)

    def test_create_unamed_group_strict(self):
        self.assertRaises(OperationNotAllowed, Group, validation_level=VALIDATION_LEVEL.STRICT)

    def test_add_child_with_different_validation_level(self):
        g = Group('RSP_K21_QUERY_RESPONSE', validation_level=VALIDATION_LEVEL.STRICT)
        s = Segment('PID', validation_level=VALIDATION_LEVEL.TOLERANT)
        self.assertRaises(OperationNotAllowed, g.add, s)

        g = Group('RSP_K21_QUERY_RESPONSE', validation_level=VALIDATION_LEVEL.TOLERANT)
        s = Segment('PID', validation_level=VALIDATION_LEVEL.STRICT)
        self.assertRaises(OperationNotAllowed, g.add, s)

    def test_add_child_with_different_version(self):
        g = Group('RSP_K21_QUERY_RESPONSE', version='2.5')
        s = Segment('QPD', version='2.4')
        self.assertRaises(OperationNotAllowed, g.add, s)

    def test_add_unexpected_child_to_group(self):
        g = Group()
        m = Message('OML_O33')
        f = Field()
        c = Component(datatype='ST')
        sub = SubComponent(datatype='ST')
        self.assertRaises(ChildNotValid, g.add, m)
        self.assertRaises(ChildNotValid, g.add, f)
        self.assertRaises(ChildNotValid, g.add, c)
        self.assertRaises(ChildNotValid, g.add, sub)

    def test_delete_group(self):
        m = Message('OML_O33', validation_level=VALIDATION_LEVEL.TOLERANT)
        g = Group('OML_O33_PATIENT', validation_level=VALIDATION_LEVEL.TOLERANT)
        m.add(g)
        self.assertTrue(g in m.children)
        del m.oml_o33_patient
        self.assertFalse(g in m.children)

        m = Message('OML_O33', validation_level=VALIDATION_LEVEL.STRICT)
        g = Group('OML_O33_PATIENT', validation_level=VALIDATION_LEVEL.STRICT)
        m.add(g)
        self.assertTrue(g in m.children)
        del m.oml_o33_patient
        self.assertFalse(g in m.children)

        m = Message('RSP_K21', validation_level=VALIDATION_LEVEL.TOLERANT, reference=self.rsp_k21_mp)
        g = m.add_group('RSP_K21_QUERY_RESPONSE')
        self.assertTrue(g in m.children)
        del m.rsp_k21_query_response
        self.assertFalse(g in m.children)

        m = Message('RSP_K21', validation_level=VALIDATION_LEVEL.STRICT, reference=self.rsp_k21_mp)
        g = m.add_group('RSP_K21_QUERY_RESPONSE')
        self.assertTrue(g in m.children)
        del m.rsp_k21_query_response
        self.assertFalse(g in m.children)

    def test_create_supported_version_group(self):
        Group(version='2.5')

    def test_create_unsupported_version_group(self):
        self.assertRaises(UnsupportedVersion, Group, version='2.0')

    def test_add_z_segment(self):
        a = Group('OML_O33_PATIENT', validation_level=VALIDATION_LEVEL.STRICT)
        a.add(Segment('ZIN', validation_level=VALIDATION_LEVEL.STRICT))
        a.add_segment('zap')
        a.zbe = 'ZBE||ab|ab|'

        b = Group('OML_O33_PATIENT', validation_level=VALIDATION_LEVEL.TOLERANT)
        b.add(Segment('ZIN', validation_level=VALIDATION_LEVEL.TOLERANT))
        b.add_segment('zap')
        b.zbe = 'ZBE||ab|ab|'

        m = Message('RSP_K21', validation_level=VALIDATION_LEVEL.STRICT, reference=self.rsp_k21_mp)
        g = m.add_group('RSP_K21_QUERY_RESPONSE')
        g.add(Segment('ZIN', validation_level=VALIDATION_LEVEL.STRICT))
        g.add_segment('zap')
        g.zbe = 'ZBE||ab|ab|'

        m = Message('RSP_K21', validation_level=VALIDATION_LEVEL.TOLERANT, reference=self.rsp_k21_mp)
        g = m.add_group('RSP_K21_QUERY_RESPONSE')
        g.add(Segment('ZIN'))
        g.add_segment('zap')
        g.zbe = 'ZBE||ab|ab|'

    def test_assign_value(self):
        g = Group('OML_O33_SPECIMEN')
        g.value = self.oml_o33_specimen
        self.assertEqual(g.to_er7(), self.oml_o33_specimen)

        g = Group('OML_O33_SPECIMEN', validation_level=VALIDATION_LEVEL.STRICT)
        g.value = self.oml_o33_specimen
        self.assertEqual(g.to_er7(), self.oml_o33_specimen)

        m = Message('RSP_K21', validation_level=VALIDATION_LEVEL.STRICT, reference=self.rsp_k21_mp)
        g = m.add_group('RSP_K21_QUERY_RESPONSE')
        g.value = self.rsp_k21_query_response
        self.assertEqual(g.to_er7(), self.rsp_k21_query_response)

        m = Message('RSP_K21', validation_level=VALIDATION_LEVEL.TOLERANT, reference=self.rsp_k21_mp)
        g = m.add_group('RSP_K21_QUERY_RESPONSE')
        g.value = self.rsp_k21_query_response
        self.assertEqual(g.to_er7(), self.rsp_k21_query_response)

    def test_assign_value_traversal(self):
        m1 = Message('OML_O33')
        m2 = Message('OML_O33')
        m1.oml_o33_specimen.value = self.oml_o33_specimen
        m2.oml_o33_specimen = self.oml_o33_specimen
        self.assertEqual(m1.to_er7(), m2.to_er7())

        m1 = Message('RSP_K21', reference=self.rsp_k21_mp)
        m2 = Message('RSP_K21', reference=self.rsp_k21_mp)
        m1.rsp_k21_query_response.value = self.rsp_k21_query_response
        m2.rsp_k21_query_response = self.rsp_k21_query_response
        self.assertEqual(m1.to_er7(), m2.to_er7())
        self.assertEqual(m1.to_er7(), m2.to_er7())

    def test_bug_13(self):
        g = Group('RSP_K21_QUERY_RESPONSE')
        pid = g.pid
        self.assertEqual(id(g.pid), id(pid))

        pid_31 = g.pid.pid_3
        self.assertIn('PID', g.children.traversal_indexes)

        pid_32 = pid.pid_3
        pid_31.value = 'a'
        self.assertNotIn('PID', g.children.traversal_indexes)
        self.assertEqual(pid_31.children, pid_32.children)
        self.assertEqual(pid_31.children, g.pid.pid_3.children)

    def test_assign_value_unknown_group(self):
        g = Group()
        g.value = self.oml_o33_specimen


class TestSegment(unittest.TestCase):

    def setUp(self):
        base_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(base_path, 'profiles/iti_21')
        self.rsp_k21_mp = hl7apy.load_message_profile(path)

    def test_create_unknown_segment(self):
        self.assertRaises(InvalidName, Segment, 'ABC')
        self.assertRaises(InvalidName, Segment, 'ABC', validation_level=VALIDATION_LEVEL.STRICT)

    def test_create_empty_segment(self):
        self.assertRaises(OperationNotAllowed, Segment)

    def test_create_unsupported_version_segment(self):
        s = Segment('PID', version='2.5')
        self.assertRaises(UnsupportedVersion, Segment, 'PID', version='2.0')

    def test_create_z_segment(self):
        Segment('ZIN', validation_level=VALIDATION_LEVEL.STRICT)
        Segment('ZIN', validation_level=VALIDATION_LEVEL.TOLERANT)
        self.assertRaises(InvalidName, Segment, 'ZDSW', validation_level=VALIDATION_LEVEL.STRICT)
        self.assertRaises(InvalidName, Segment, 'ZDSW', validation_level=VALIDATION_LEVEL.TOLERANT)

    def test_add_field_to_z_segments(self):
        zin = Segment('ZIN')
        zin.add(Field('ZIN_10'))
        zin.zin_12 = 'abc'
        zin.add_field('zin_2')

        with self.assertRaises(ChildNotFound):
            zin.add(Field('ZAP_10'))
            zin.zap_12 = 'abc'
            zin.add_field('zap_2')

    def test_allow_infinite_children(self):
        qpd = Segment('QPD', validation_level=VALIDATION_LEVEL.STRICT)  # last field is varies
        self.assertTrue(qpd.allow_infinite_children)
        pid = Segment('PID', validation_level=VALIDATION_LEVEL.STRICT)  # last field is not varies
        self.assertFalse(pid.allow_infinite_children)
        zin = Segment('ZIN', validation_level=VALIDATION_LEVEL.STRICT)  # z segment
        self.assertTrue(zin.allow_infinite_children)

        qpd.qpd_4 = 'abc'
        qpd.add_field('qpd_4')

        zin.add(Field('ZIN_100', validation_level=VALIDATION_LEVEL.STRICT))
        zin.zin_4 = 'abc'
        zin.add_field('zin_4')

    def test_add_field(self):
        e = Segment('PID', validation_level=VALIDATION_LEVEL.STRICT)
        pid_5 = e.add_field('PID_5')
        self.assertEqual(pid_5.classname, 'Field')
        self.assertIn(pid_5, e.children)
        self.assertRaises(ChildNotFound, e.add_field, 'UNKNOWN_FIELD')

        e = Segment('PID', validation_level=VALIDATION_LEVEL.TOLERANT)
        pid_5 = e.add_field('PID_5')
        self.assertEqual(pid_5.classname, 'Field')
        self.assertIn(pid_5, e.children)
        self.assertRaises(ChildNotFound, e.add_field, 'UNKNOWN_FIELD')

        m = Message('RSP_K21', validation_level=VALIDATION_LEVEL.STRICT, reference=self.rsp_k21_mp)
        m.add_segment('msa')
        s = m.msa
        msa_1 = s.add_field('MSA_1')
        self.assertEqual(msa_1.classname, 'Field')
        self.assertIn(msa_1, s.children)

        m = Message('RSP_K21', validation_level=VALIDATION_LEVEL.TOLERANT, reference=self.rsp_k21_mp)
        m.add_segment('msa')
        s = m.msa
        msa_1 = s.add_field('MSA_1')
        self.assertEqual(msa_1.classname, 'Field')
        self.assertIn(msa_1, s.children)

    def test_add_child_with_different_validation_level(self):
        s = Segment('PID', validation_level=VALIDATION_LEVEL.TOLERANT)
        f = Field('PID_1', validation_level=VALIDATION_LEVEL.STRICT)
        self.assertRaises(OperationNotAllowed, s.add, f)

        s = Segment('PID', validation_level=VALIDATION_LEVEL.STRICT)
        f = Field('PID_1', validation_level=VALIDATION_LEVEL.TOLERANT)
        self.assertRaises(OperationNotAllowed, s.add, f)

    def test_add_child_with_different_version(self):
        s = Segment('QPD', version='2.4')
        f = Field('QPD_3', version='2.5')
        self.assertRaises(OperationNotAllowed, s.add, f)

    def test_traversal_equality(self):
        obr = Segment('OBR')
        obr.obr_26 = 'xxx&yyy^zzz^www'
        obr_26 = obr.parent_result
        self.assertTrue(isinstance(obr_26, ElementProxy))
        self.assertTrue(obr_26[0] == obr.obr_26[0], 'obr.parent_result != obr.obr_26')

        m = Message('RSP_K21', validation_level=VALIDATION_LEVEL.STRICT, reference=self.rsp_k21_mp)
        m.msa.msa_1 = 'a'
        msa_1 = m.msa.ACKNOWLEDGMENT_CODE
        self.assertTrue(isinstance(msa_1, ElementProxy))
        self.assertTrue(msa_1[0] == m.msa.msa_1[0], 'obr.parent_result != obr.obr_26')

    def test_traversal_by_name(self):
        obr = Segment('OBR')
        obr_26 = obr.parent_result
        self.assertTrue(obr_26.is_named('OBR_26'))
        self.assertTrue(obr_26.is_named('PARENT_RESULT'))

        m = Message('RSP_K21', reference=self.rsp_k21_mp)
        msa = m.msa
        msa_1 = msa.acknowledgment_code
        self.assertTrue(msa_1.is_named('MSA_1'))
        self.assertTrue(msa_1.is_named('ACKNOWLEDGMENT_CODE'))

    def test_recursive_traversal(self):
        obr = Segment('OBR')
        obr.obr_26 = 'xxx&yyy^zzz^www'
        by_name = obr.parent_result.parent_observation_identifier
        by_position = obr.obr_26.obr_26_1
        self.assertEqual(by_name[0], by_position[0])

        m = Message('RSP_K21', reference=self.rsp_k21_mp)
        qpd = m.add_segment('qpd')
        qpd.qpd_8 = '^^^IHEFACILITY&1.3.6.1.4.1.21367.3000.1.6&ISO'

        by_name = qpd.what_domains_returned.assigning_authority
        by_position = qpd.qpd_8.qpd_8_4
        self.assertEqual(by_name[0], by_position[0])

    def test_add_empty_field(self):
        s = Segment('SPM', validation_level=VALIDATION_LEVEL.STRICT)
        self.assertRaises(ChildNotValid, s.add, Field())
        s = Segment('SPM')
        s.add(Field())

        m = Message('RSP_K21', reference=self.rsp_k21_mp)
        s = m.qpd
        s.add(Field())

    # def test_add_known_fields_to_empty_segment(self):
    #     s = Segment()
    #     self.assertRaises(ChildNotFound, s.add, Field('spm_10'))  # This one is not raised!!!!

    def test_add_not_allowed_fields_to_known_segments(self):
        s = Segment('PID', validation_level=VALIDATION_LEVEL.STRICT)
        self.assertRaises(ChildNotValid, s.add, Field('spm_10'))
        s = Segment('PID')
        self.assertRaises(ChildNotValid, s.add, Field('spm_10'))

        m = Message('RSP_K21', validation_level=VALIDATION_LEVEL.STRICT, reference=self.rsp_k21_mp)
        s = m.add_segment('QPD')
        self.assertRaises(ChildNotValid, s.add, Field('spm_10'))

        m = Message('RSP_K21', validation_level=VALIDATION_LEVEL.TOLERANT, reference=self.rsp_k21_mp)
        s = m.add_segment('QPD')
        self.assertRaises(ChildNotValid, s.add, Field('spm_10'))

    def test_assign_wrong_field_to_known_position(self):
        s1 = Segment('MSH', validation_level=VALIDATION_LEVEL.STRICT)
        s2 = Segment('QPD')
        with self.assertRaises(ChildNotValid):
            s1.msh_10 = Field('spm_10')
        with self.assertRaises(ChildNotValid):
            s2.qpd_3 = Field('pid_3')

        m = Message('RSP_K21', validation_level=VALIDATION_LEVEL.STRICT, reference=self.rsp_k21_mp)
        s1 = m.add_segment('QPD')
        with self.assertRaises(ChildNotValid):
            s1.qpd_8 = Field('SPM_10')

        m = Message('RSP_K21', validation_level=VALIDATION_LEVEL.TOLERANT, reference=self.rsp_k21_mp)
        s1 = m.add_segment('QPD')
        with self.assertRaises(ChildNotValid):
            s1.qpd_8 = Field('SPM_10')

    def test_access_to_unknown_field(self):
        s1 = Segment('MSH', validation_level=VALIDATION_LEVEL.STRICT)
        s2 = Segment('PID')
        with self.assertRaises(ChildNotFound):
            s1.msh_100
        with self.assertRaises(ChildNotFound):
            s2.pid_100

        m1 = Message('RSP_K21', validation_level=VALIDATION_LEVEL.STRICT, reference=self.rsp_k21_mp)
        m2 = Message('RSP_K21', validation_level=VALIDATION_LEVEL.TOLERANT, reference=self.rsp_k21_mp)
        s1 = m1.add_segment('QPD')
        s2 = m2.add_segment('QPD')
        with self.assertRaises(ChildNotFound):
            s1.qpd_100
        with self.assertRaises(ChildNotFound):
            s2.qpd_100

    def test_delete_segment(self):
        m = Message('OML_O33')
        pid = Segment('PID')
        m.add(pid)
        self.assertIn(pid, m.children)
        del m.pid
        self.assertNotIn(pid, m.children)

        m = Message('RSP_K21', validation_level=VALIDATION_LEVEL.STRICT, reference=self.rsp_k21_mp)
        qpd = m.add_segment('QPD')
        self.assertIn(qpd, m.children)
        del m.qpd
        self.assertNotIn(qpd, m.children)

    def test_assign_value(self):
        segment_str = 'PID|1||123-456-789^^^HOSPITAL^MR||SURNAME^NAME^A|||M|||1111 SOMEWHERE STREET^^SOMEWHERE^^^USA||555-555-2004~444-333-222|||M\r'

        s = Segment('PID')
        parsed_s = parse_segment(segment_str)
        s.value = segment_str
        self.assertEqual(s.to_er7(), parsed_s.to_er7())

        s = Segment('PID', validation_level=VALIDATION_LEVEL.STRICT)
        parsed_a = parse_segment(segment_str)
        s.value = segment_str
        self.assertEqual(s.to_er7(), parsed_a.to_er7())

        qpd_str = 'QPD|IHE PDQ Query|222222222|@PID.3.1.1^3333333|||||^^^IHEFACILITY&1.3.6.1.4.1.21367.3000.1.6&ISO'
        m = Message('RSP_K21', validation_level=VALIDATION_LEVEL.STRICT, reference=self.rsp_k21_mp)
        s = m.add_segment('QPD')

        s.value = qpd_str
        self.assertEqual(s.to_er7(), qpd_str)

    def test_assign_value_traversal(self):
        segment_str = 'PID|1||123-456-789^^^HOSPITAL^MR||SURNAME^NAME^A|||M|||1111 SOMEWHERE STREET^^SOMEWHERE^^^USA||555-555-2004~444-333-222|||M\r'

        m1 = Message('OML_O33')
        m2 = Message('OML_O33')
        m1.pid.value = segment_str
        m2.pid.value = segment_str
        self.assertEqual(m1.to_er7(), m2.to_er7())

        segment_str = 'QPD|IHE PDQ Query|222222222|@PID.3.1.1^3333333|||||^^^IHEFACILITY&1.3.6.1.4.1.21367.3000.1.6&ISO'
        m1 = Message('RSP_K21', reference=self.rsp_k21_mp)
        m2 = Message('RSP_K21', reference=self.rsp_k21_mp)
        m1.qpd.value = segment_str
        m2.qpd.value = segment_str
        self.assertEqual(m1.to_er7(), m2.to_er7())

    def test_bug_13(self):
        p = Segment('PID')
        f = p.pid_3
        self.assertEqual(id(p.pid_3), id(f))
        self.assertEqual(id(p.patient_identifier_list), id(f))

        c1 = p.pid_3.cx_10
        self.assertIn('PID_3', p.children.traversal_indexes)

        p.ALTERNATE_PATIENT_ID_PID.cx_10
        self.assertIn('PID_4', p.children.traversal_indexes)

        c2 = f.cx_10
        c1.value = 'a'
        self.assertNotIn('PID_3', p.children.traversal_indexes)
        self.assertEqual(c1.children, c2.children)
        self.assertEqual(c1.children, p.pid_3.cx_10.children)

    def test_assign_wrong_value(self):
        s = Segment('PID')
        wrong_segment_str = 'EVN|1||123-456-789^^^HOSPITAL^MR||SURNAME^NAME^A|||M|||1111 SOMEWHERE STREET^^SOMEWHERE^^^USA||555-555-2004~444-333-222|||M\r'
        with self.assertRaises(OperationNotAllowed):
            s.value = wrong_segment_str

        m = Message('RSP_K21', reference=self.rsp_k21_mp)
        s = m.add_segment('qpd')
        with self.assertRaises(OperationNotAllowed):
            s.value = wrong_segment_str


class TestField(unittest.TestCase):

    def setUp(self):
        base_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(base_path, 'profiles/iti_21')
        self.rsp_k21_mp = hl7apy.load_message_profile(path)

    def test_create_empty_field(self):
        f = Field()
        self.assertEqual(f.classname, 'Field')
        self.assertRaises(OperationNotAllowed, Field, validation_level=VALIDATION_LEVEL.STRICT)

    def test_create_unknown_field(self):
        self.assertRaises(InvalidName, Field, 'ckk_10')
        self.assertRaises(InvalidName, Field, 'ckk_10', validation_level=VALIDATION_LEVEL.STRICT)

    def test_create_unsupported_version_field(self):
        self.assertRaises(UnsupportedVersion, Field, version='2.0')

    def test_create_varies_datatype_field(self):
        f = Field('PID_1', datatype='varies')
        self.assertEqual(f.datatype, 'varies')

    def test_create_z_field(self):
        Field('ZIN_1', validation_level=VALIDATION_LEVEL.STRICT)
        Field('ZIN_1', validation_level=VALIDATION_LEVEL.TOLERANT)
        Field('zin_1', validation_level=VALIDATION_LEVEL.STRICT)
        Field('zin_1', validation_level=VALIDATION_LEVEL.TOLERANT)

        self.assertRaises(InvalidName, Field, 'ZINQW')
        self.assertRaises(InvalidName, Field, 'ZIN_W')

    def test_z_field_datatype(self):
        s = Segment('zin')
        s.zin_1 = 'zzz'
        self.assertEqual(s.zin_1.datatype, 'ST')

        s.add_field('zin_2')
        self.assertEqual(s.zin_2.datatype, 'ST')

        s.add(Field('zin_3', datatype='ST'))
        self.assertEqual(s.zin_3.datatype, 'ST')

        s.add(Field('zin_4', datatype='CWE'))
        self.assertEqual(s.zin_4.datatype, 'CWE')

        s.zin_5 = 'abc^def'
        self.assertEqual(s.zin_5.datatype, None)

    def test_add_component(self):
        f = Field('PID_5', validation_level=VALIDATION_LEVEL.STRICT)
        c = Component('XPN_1', validation_level=VALIDATION_LEVEL.STRICT)
        f.add(c)
        self.assertIn(c, f.children)

        f = Field('PID_5', validation_level=VALIDATION_LEVEL.STRICT)
        c = f.add_component('XPN_1')
        self.assertEqual(c.name, 'XPN_1')
        self.assertIn(c, f.children)

        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.STRICT)
        f = m.add_segment('QPD').add_field('QPD_3')
        c = f.add_component('QIP_1')
        self.assertEqual(c.name, 'QIP_1')
        self.assertIn(c, f.children)

    def test_add_child_with_different_validation_level(self):
        f = Field('PID_4', validation_level=VALIDATION_LEVEL.STRICT)
        c = Component('CX_10', validation_level=VALIDATION_LEVEL.TOLERANT)
        self.assertRaises(OperationNotAllowed, f.add, c)

        f = Field('PID_4', validation_level=VALIDATION_LEVEL.TOLERANT)
        c = Component('CX_10', validation_level=VALIDATION_LEVEL.STRICT)
        self.assertRaises(OperationNotAllowed, f.add, c)

    def test_add_child_with_different_version(self):
        f = Field('PID_4', version='2.4')
        c = Component('CX_8', version='2.5')
        self.assertRaises(OperationNotAllowed, f.add, c)

    def test_add_empty_component(self):
        f1 = Field('pid_3', validation_level=VALIDATION_LEVEL.STRICT)
        self.assertRaises(ChildNotValid, f1.add, Component(datatype='ST'))
        f2 = Field('pid_3')
        c = Component()
        f2.add(c)
        self.assertIn(c, f2.children)

        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.STRICT)
        f = m.add_segment('QPD').add_field('QPD_3')
        self.assertRaises(ChildNotValid, f.add, Component(datatype='ST'))

        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.STRICT)
        f = m.add_segment('QPD').add_field('QPD_3')
        self.assertRaises(ChildNotValid, f.add, Component(datatype='ST'))

        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.TOLERANT)
        f = m.add_segment('QPD').add_field('QPD_3')
        c = Component()
        f.add(c)
        self.assertIn(c, f.children)

    # def test_add_known_components_to_empty_fields(self):
    #     f2 = Field()
    #     self.assertRaises(ChildNotValid, f2.add, Component('CX_1'))  # this one is not raised!!!

    def test_add_not_allowed_components_to_known_field(self):
        f1 = Field('pid_3', validation_level=VALIDATION_LEVEL.STRICT)
        self.assertRaises(ChildNotValid, f1.add, Component(datatype='ST'))
        f2 = Field('pid_3')
        self.assertRaises(ChildNotValid, f2.add, Component('XPN_1'))

        m = Message('RSP_K21', validation_level=VALIDATION_LEVEL.STRICT, reference=self.rsp_k21_mp)
        f = m.add_segment('QPD').add_field('QPD_3')
        self.assertRaises(ChildNotValid, f.add, Component('XPN_1'))

        m = Message('RSP_K21', validation_level=VALIDATION_LEVEL.TOLERANT, reference=self.rsp_k21_mp)
        f = m.add_segment('QPD').add_field('QPD_3')
        self.assertRaises(ChildNotValid, f.add, Component('XPN_1'))

    def test_assign_wrong_component_to_known_position(self):
        f1 = Field('pid_10', validation_level=VALIDATION_LEVEL.STRICT)
        with self.assertRaises(ChildNotValid):
            f1.ce_1 = Component('CX_1')
        f2 = Field('pid_3')
        with self.assertRaises(ChildNotValid):
            f2.cx_1 = Component('HD_1')
        f2.cx_1 = Component('CX_1')

        m = Message('RSP_K21', validation_level=VALIDATION_LEVEL.STRICT, reference=self.rsp_k21_mp)
        f = m.add_segment('QPD').add_field('QPD_3')
        with self.assertRaises(ChildNotValid):
            f.qip_1 = Component('CX_1')

        m = Message('RSP_K21', validation_level=VALIDATION_LEVEL.TOLERANT, reference=self.rsp_k21_mp)
        f = m.add_segment('QPD').add_field('QPD_3')
        with self.assertRaises(ChildNotValid):
            f.qip_1 = Component('CX_1')

    def test_access_to_z_field_component(self):
        s = Segment('ZIN')
        f = Field('ZIN_1', datatype='CWE')
        f.value = 'abc'
        s.zin_1 = f
        self.assertEqual(s.zin_1.zin_1_1.name, 'CWE_1')
        with self.assertRaises(ChildNotFound):
            s.zin_2.zin_2_2

    def test_access_to_unknown_component(self):
        f1 = Field('pid_10', validation_level=VALIDATION_LEVEL.STRICT)
        f2 = Field('pid_3')
        with self.assertRaises(ChildNotFound):
            f1.ce_100
        with self.assertRaises(ChildNotFound):
            f2.cx_100

        m = Message('RSP_K21', validation_level=VALIDATION_LEVEL.STRICT, reference=self.rsp_k21_mp)
        f = m.add_segment('QPD').add_field('QPD_3')
        with self.assertRaises(ChildNotFound):
            f.qip_100

        m = Message('RSP_K21', validation_level=VALIDATION_LEVEL.TOLERANT, reference=self.rsp_k21_mp)
        f = m.add_segment('QPD').add_field('QPD_3')
        with self.assertRaises(ChildNotFound):
            f.qip_100

    def test_access_to_wrong_component(self):
        f1 = Field('pid_10', validation_level=VALIDATION_LEVEL.STRICT)
        f2 = Field('pid_3')
        with self.assertRaises(ChildNotValid):
            f1.cwe_1  # pid_10 datatype is CE
        with self.assertRaises(ChildNotValid):
            f2.ce_1  # pid_3 datatype is CX

        m = Message('RSP_K21', validation_level=VALIDATION_LEVEL.STRICT, reference=self.rsp_k21_mp)
        f = m.add_segment('QPD').add_field('QPD_3')
        with self.assertRaises(ChildNotValid):
            f.cwe_1  # qpd_3 is QIP

        m = Message('RSP_K21', validation_level=VALIDATION_LEVEL.TOLERANT, reference=self.rsp_k21_mp)
        f = m.add_segment('QPD').add_field('QPD_3')
        with self.assertRaises(ChildNotValid):
            f.cwe_1  # qpd_3 is QIP

    def test_add_more_components_to_base_datatype_field(self):
        f1 = Field('pid_8', validation_level=VALIDATION_LEVEL.STRICT)  # this is a base datatype field
        f1.add(Component(datatype='IS', validation_level=VALIDATION_LEVEL.STRICT))
        self.assertRaises(MaxChildLimitReached, f1.add, Component(datatype='ST'))

        f2 = Field('pid_8')
        f2.add(Component(datatype='IS'))
        self.assertRaises(MaxChildLimitReached, f2.add, Component(datatype='ST'))

        m = Message('RSP_K21', validation_level=VALIDATION_LEVEL.STRICT, reference=self.rsp_k21_mp)
        f = m.add_segment('QPD').add_field('QPD_8')
        f.add_component('CX_1')
        self.assertRaises(MaxChildLimitReached, f.add_component, 'CX_1')

    def test_override_field_datatype_strict(self):
        f = Field('pid_3',  validation_level=VALIDATION_LEVEL.STRICT)
        with self.assertRaises(OperationNotAllowed):
            f.datatype = 'HD'
        self.assertRaises(OperationNotAllowed, Field, 'pid_3', datatype='HD',
                          validation_level=VALIDATION_LEVEL.STRICT)
        # in this case we are assigning the official datatype to the Field, thus no exception should be raised
        b = Field('pid_3', 'CX', validation_level=VALIDATION_LEVEL.STRICT)
        self.assertEqual(b.datatype, 'CX')

        f = Field('pid_3')
        f.datatype = 'HD'
        self.assertEqual(f.datatype, 'HD')

        f = Field('pid_3', datatype='HD')
        self.assertEqual(f.datatype, 'HD')

        # it raises an exception because the field already has some children
        a = Field('pid_3')
        a.cx_1 = 'aaa'
        a.cx_4 = 'bbb'
        with self.assertRaises(OperationNotAllowed):
            a.datatype = 'HD'

        # test that the children's names follow the new datatype name
        a = Field('pid_3', 'CE')  # official datatype is CX
        a.ce_1 = 'xyz'
        self.assertEqual(a.to_er7(), 'xyz')

        m = Message('RSP_K21', validation_level=VALIDATION_LEVEL.STRICT, reference=self.rsp_k21_mp)
        f = m.add_segment('QPD').add_field('QPD_8')
        with self.assertRaises(OperationNotAllowed):
            f.datatype = 'CWE'

    def test_delete_field(self):
        m = Message('OML_O33')
        msh = m.msh
        msh7 = msh.msh_7
        del msh.msh_7
        self.assertNotIn(msh7, msh.children)

        m = Message('RSP_K21', validation_level=VALIDATION_LEVEL.STRICT, reference=self.rsp_k21_mp)
        f = m.add_segment('QPD').add_field('QPD_8')
        self.assertIn(f, m.qpd.children)
        del m.qpd.qpd_8
        self.assertNotIn(f, m.qpd.children)

    def test_assign_value(self):
        field_str = '1010110909194822^^^AUTH&1.3.6.1.4.1.21367.2011.2.5.17&ISO^PK^A^^^^A'

        f = Field('PID_3')
        f.value = field_str
        self.assertEqual(f.to_er7(trailing_children=True), field_str)

        f = Field('PID_3', validation_level=VALIDATION_LEVEL.STRICT)
        f.value = field_str
        self.assertEqual(f.to_er7(trailing_children=True), field_str)

        f = Field('PID_1', validation_level=VALIDATION_LEVEL.STRICT)
        with self.assertRaises(MaxChildLimitReached):
            f.value = '1^2'

        f = Field('PID_1', validation_level=VALIDATION_LEVEL.TOLERANT)
        f.value = SI(1)
        self.assertEqual(f.to_er7(), '1')
        f.value = SI(2)
        self.assertEqual(f.to_er7(), '2')
        with self.assertRaises(ChildNotValid):
            f.value = ST('aaa')

        f = Field('PID_3', validation_level=VALIDATION_LEVEL.TOLERANT) # It is a complex datatype field
        with self.assertRaises(ChildNotValid):
            f.value = ST('aaa')

        f = Field('PID_1', validation_level=VALIDATION_LEVEL.STRICT)
        f.value = SI(1)
        self.assertEqual(f.to_er7(), '1')
        f.value = SI(2)
        self.assertEqual(f.to_er7(), '2')
        with self.assertRaises(ChildNotValid):
            f.value = ST('aaa')

        f = Field('PID_3', validation_level=VALIDATION_LEVEL.STRICT) # It is a complex datatype field
        with self.assertRaises(ChildNotValid):
            f.value = ST('aaa')

    def test_assign_value_message_profile(self):
        field_str = '1010110909194822^^^AUTH&1.3.6.1.4.1.21367.2011.2.5.17&ISO^PK^A^^^^A'

        m = Message('RSP_K21', reference=self.rsp_k21_mp)
        f = m.rsp_k21_query_response.pid.add_field('PID_3')
        f.value = field_str
        self.assertEqual(f.to_er7(trailing_children=True), field_str)

        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.STRICT)
        f = m.rsp_k21_query_response.pid.add_field('PID_3')
        f.value = field_str
        self.assertEqual(f.to_er7(trailing_children=True), field_str)

        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.STRICT)
        f = m.rsp_k21_query_response.pid.add_field('PID_1')
        with self.assertRaises(MaxChildLimitReached):
            f.value = '1^2'

        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.TOLERANT)
        f = m.rsp_k21_query_response.pid.add_field('PID_1')
        f.value = SI(1)
        self.assertEqual(f.to_er7(), '1')
        f.value = SI(2)
        self.assertEqual(f.to_er7(), '2')
        with self.assertRaises(ChildNotValid):
            f.value = ST('aaa')

        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.TOLERANT)
        f = m.rsp_k21_query_response.pid.add_field('PID_3')  # it is a complex datatype field
        with self.assertRaises(ChildNotValid):
            f.value = ST('aaa')

        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.STRICT)
        f = m.rsp_k21_query_response.pid.add_field('PID_1')
        f.value = SI(1)
        self.assertEqual(f.to_er7(), '1')
        f.value = SI(2)
        self.assertEqual(f.to_er7(), '2')
        with self.assertRaises(ChildNotValid):
            f.value = ST('aaa')

        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.STRICT)
        f = m.rsp_k21_query_response.pid.add_field('PID_3')  # it is a complex datatype field
        with self.assertRaises(ChildNotValid):
            f.value = ST('aaa')

    def test_assign_value_traversal(self):
        field_str = '1010110909194822^^^AUTH&1.3.6.1.4.1.21367.2011.2.5.17&ISO^PK'

        # assigns string using value
        s = Segment('PID')
        s.pid_3.value = field_str
        self.assertEqual(s.pid_3.to_er7(), field_str)

        # assigns string
        s = Segment('PID')
        s.pid_3 = field_str
        self.assertEqual(s.pid_3.to_er7(), field_str)

        # assigns base datatype using value
        s = Segment('MSH')
        s.msh_10.value = ST('aaa')
        self.assertEqual(s.msh_10.to_er7(), 'aaa')
        self.assertEqual(s.to_er7(), 'MSH|||||||||aaa')

        # assigns base datatype
        s = Segment('MSH')
        s.msh_10 = ST('aaa')
        self.assertEqual(s.msh_10.to_er7(), 'aaa')

        # same tests with a further level iof traversal

        m = Message('RSP_K21')
        m.pid.pid_3.value = field_str
        self.assertEqual(m.pid.pid_3.to_er7(), field_str)

        m = Message('RSP_K21')
        m.pid.pid_3 = field_str
        self.assertEqual(m.pid.pid_3.to_er7(), field_str)

        m = Message('RSP_K21')
        m.msh.msh_10.value = ST('aaa')
        self.assertEqual(m.msh.msh_10.to_er7(), 'aaa')

        m = Message('RSP_K21')
        m.msh.msh_10 = ST('aaa')
        self.assertEqual(m.msh.msh_10.to_er7(), 'aaa')

    def test_bug_13(self):
        f = Field('PID_3')
        c = f.cx_10
        self.assertEqual(id(f.cx_10), id(c))
        self.assertEqual(id(f.ASSIGNING_AGENCY_OR_DEPARTMENT), id(c))

        s1 = f.cx_10.cwe_1
        self.assertIn('CX_10', f.children.traversal_indexes)

        s2 = f.ASSIGNING_AUTHORITY.HD_1
        self.assertIn('CX_4', f.children.traversal_indexes)

        s2 = c.cwe_1
        s2.value = 'a'
        self.assertNotIn('CX_10', f.children.traversal_indexes)
        self.assertEqual(s1.children, s2.children)
        self.assertEqual(s1.children, f.cx_10.cwe_1.children)

    def test_assign_value_traversal_message_profile(self):
        field_str = '1010110909194822^^^AUTH&1.3.6.1.4.1.21367.2011.2.5.17&ISO^PK'

        # assigns string using value
        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.STRICT)
        s = m.add_group('rsp_k21_query_response').add_segment('pid')
        s.pid_3.value = field_str
        self.assertEqual(s.pid_3.to_er7(), field_str)

        # assigns string
        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.STRICT)
        s = m.add_group('rsp_k21_query_response').add_segment('pid')
        s.pid_3 = field_str
        self.assertEqual(s.pid_3.to_er7(), field_str)

        # assigns base datatype using value
        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.STRICT)
        s = m.msh
        s.msh_10.value = ST('aaa')
        self.assertEqual(s.msh_10.to_er7(), 'aaa')

        # assigns base datatype
        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.STRICT)
        s = m.msh
        m.msh.msh_10 = ST('aaa')
        self.assertEqual(s.msh_10.to_er7(), 'aaa')

        # same tests with a further level iof traversal

        # assigns string using value
        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.STRICT)
        m.rsp_k21_query_response.pid.pid_3.value = field_str
        self.assertEqual(m.rsp_k21_query_response.pid.pid_3.to_er7(), field_str)

        # assigns string
        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.STRICT)
        m.rsp_k21_query_response.pid.pid_3 = field_str
        self.assertEqual(m.rsp_k21_query_response.pid.pid_3.to_er7(), field_str)

        # assigns base datatype using value
        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.STRICT)
        m.msh.msh_10.value = ST('aaa')
        self.assertEqual(m.msh.msh_10.to_er7(), 'aaa')

        # assigns base datatype
        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.STRICT)
        m.msh.msh_10 = ST('aaa')
        self.assertEqual(m.msh.msh_10.to_er7(), 'aaa')

    def test_assign_value_with_encoding_chars(self):
        # using field separator
        field_str = 'xxx|yyy'
        escaped_str = 'xxx\\F\\yyy'
        f = Field('PID_3')
        f.value = field_str
        self.assertEqual(f.to_er7(), escaped_str)

        f = Field('PID_3', validation_level=VALIDATION_LEVEL.STRICT)
        f.value = field_str
        self.assertEqual(f.to_er7(), escaped_str)

        f = Field()
        f.value = field_str
        self.assertEqual(f.to_er7(), 'xxx\\F\\yyy')

        # using repetition
        field_str = 'xxx~yyy'
        f = Field()
        f.value = field_str
        self.assertEqual(f.to_er7(), 'xxx\\R\\yyy')

        f = Field('PID_2')
        f.value = field_str
        self.assertEqual(f.to_er7(), 'xxx\\R\\yyy')

        f = Field('PID_2', validation_level=VALIDATION_LEVEL.STRICT)
        f.value = field_str
        self.assertEqual(f.to_er7(), 'xxx\\R\\yyy')

    def test_field_wgith_three_part_name_bug_39(self):
        """
        Tests that fields with three part name are handled correctly. See issue #39 on github
        """
        f = Field('MSH_9', version='2.3')
        f.value = 'SIU^S12'
        self.assertEqual(f.cm_msg_1.value, 'SIU')
        self.assertEqual(f.cm_msg_2.value, 'S12')


class TestComponent(unittest.TestCase):

    def setUp(self):
        base_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(base_path, 'profiles/iti_21')
        self.rsp_k21_mp = hl7apy.load_message_profile(path)

    def test_create_empty_component(self):
        c = Component()
        self.assertEqual(c.classname, 'Component')
        c = Component(datatype='ST')

        self.assertEqual(c.classname, 'Component')
        Component(datatype='ST', validation_level=VALIDATION_LEVEL.STRICT)
        self.assertRaises(OperationNotAllowed, Component, validation_level=VALIDATION_LEVEL.STRICT)

    def test_create_unknown_component(self):
        self.assertRaises(InvalidName, Component, 'xxx_1')
        self.assertRaises(InvalidName, Component, 'xxx_1', validation_level=VALIDATION_LEVEL.STRICT)
        self.assertRaises(InvalidName, Component, 'AD') # AD is a datatype but not a correct component name

    def test_create_unsupported_version_component(self):
        self.assertRaises(UnsupportedVersion, Component, version='2.0')

    def test_add_child_with_different_validation_level(self):
        c = Component('CX_10', validation_level=VALIDATION_LEVEL.TOLERANT)
        s = SubComponent('CWE_1', validation_level=VALIDATION_LEVEL.STRICT)
        self.assertRaises(OperationNotAllowed, c.add, s)

        c = Component('CX_10', validation_level=VALIDATION_LEVEL.STRICT)
        s = SubComponent('CWE_1', validation_level=VALIDATION_LEVEL.TOLERANT)
        self.assertRaises(OperationNotAllowed, c.add, s)

    def test_add_child_with_different_version(self):
        c = Component('CX_10', version='2.5')
        s = SubComponent('CWE_1', version='2.6')
        self.assertRaises(OperationNotAllowed, c.add, s)

    def test_add_empty_subcomponent(self):
        c1 = Component('cx_4', validation_level=VALIDATION_LEVEL.STRICT)
        self.assertRaises(ChildNotValid, c1.add, SubComponent(datatype='ST'))

        c2 = Component('cx_4')
        c2.add(SubComponent(datatype='ST'))

        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.STRICT)
        c = m.add_segment('QPD').add_field('QPD_8').add_component('CX_4')
        self.assertRaises(ChildNotValid, c.add, SubComponent(datatype='ST'))

        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.TOLERANT)
        c = m.add_segment('QPD').add_field('QPD_8').add_component('CX_4')
        c.add(SubComponent(datatype='ST'))
        self.assertEqual(c.value, '&&&')

    def test_add_known_subcomponent_to_empty_component(self):
        c = Component()
        self.assertRaises(ChildNotValid, c.add, SubComponent('fn_1'))

    def test_add_not_allowed_subcomponent_to_known_component(self):
        c = Component('cx_4', validation_level=VALIDATION_LEVEL.STRICT)
        self.assertRaises(ChildNotValid, c.add, SubComponent('fn_1'))

        c1 = Component('cx_4')
        self.assertRaises(ChildNotValid, c1.add, SubComponent('fn_1'))

        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.STRICT)
        c = m.add_segment('QPD').add_field('QPD_8').add_component('CX_4')
        self.assertRaises(ChildNotValid, c.add, SubComponent('fn_1'))

        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.TOLERANT)
        c = m.add_segment('QPD').add_field('QPD_8').add_component('CX_4')
        self.assertRaises(ChildNotValid, c.add, SubComponent('fn_1'))

    def test_assign_wrong_subcomponent_to_known_position(self):
        c = Component('XPN_1')
        with self.assertRaises(ChildNotValid):
            c.fn_1 = SubComponent('hd_1')

        c1 = Component('XPN_1', validation_level=VALIDATION_LEVEL.STRICT)
        with self.assertRaises(ChildNotValid):
            c1.fn_1 = SubComponent('hd_1')

        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.TOLERANT)
        c = m.add_segment('QPD').add_field('QPD_8').add_component('CX_10')
        with self.assertRaises(ChildNotValid):
            c.cwe_1 = SubComponent('hd_1')

        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.STRICT)
        c = m.add_segment('QPD').add_field('QPD_8').add_component('CX_10')
        with self.assertRaises(ChildNotValid):
            c.cwe_1 = SubComponent('hd_1')

    def test_access_to_unknown_subcomponent(self):
        c1 = Component('XPN_1', validation_level=VALIDATION_LEVEL.STRICT)
        c2 = Component('cx_4')
        with self.assertRaises(ChildNotFound):
            c1.fn_100
        with self.assertRaises(ChildNotFound):
            c2.hd_100

        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.TOLERANT)
        c = m.add_segment('QPD').add_field('QPD_8').add_component('CX_10')
        with self.assertRaises(ChildNotFound):
            c.cwe_100

        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.STRICT)
        c = m.add_segment('QPD').add_field('QPD_8').add_component('CX_10')
        with self.assertRaises(ChildNotFound):
            c.cwe_100

    def test_access_to_wrong_subcomponent(self):
        c1 = Component('XPN_1', validation_level=VALIDATION_LEVEL.STRICT)
        c2 = Component('cx_4')
        with self.assertRaises(ChildNotValid):
            c1.cwe_1
        with self.assertRaises(ChildNotValid):
            c2.cx_1

        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.TOLERANT)
        c = m.add_segment('QPD').add_field('QPD_8').add_component('CX_4')
        with self.assertRaises(ChildNotValid):
            c.cx_1

        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.STRICT)
        c = m.add_segment('QPD').add_field('QPD_8').add_component('CX_4')
        with self.assertRaises(ChildNotValid):
            c.cx_1

    def test_add_more_subcomponents_to_base_datatype_component(self):
        c = Component(datatype='ST')
        c.add(SubComponent(datatype='ST'))
        self.assertRaises(MaxChildLimitReached, c.add, SubComponent(datatype='ST'))
        # c1 = Component(datatype='ST', validation_level=VALIDATION_LEVEL.STRICT)
        # self.assertRaises(ChildNotValid, c1.add, SubComponent(datatype='ST'))

        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.STRICT)
        c = m.add_segment('QPD').add_field('QPD_8').add_component('CX_2')
        c.add(SubComponent(datatype='ST', validation_level=VALIDATION_LEVEL.STRICT))
        self.assertRaises(MaxChildLimitReached, c.add, SubComponent(datatype='ST'))

    def test_override_datatype(self):
        c = Component('CX_1', validation_level=VALIDATION_LEVEL.TOLERANT)
        c.datatype = 'TX'
        self.assertEqual(c.datatype, 'TX')

        c = Component('CX_1', datatype='TX', validation_level=VALIDATION_LEVEL.TOLERANT)
        self.assertEqual(c.datatype, 'TX')

        c = Component()
        c.value = 'a&b'
        with self.assertRaises(OperationNotAllowed):
            c.datatype = 'TX'

        c = Component('CX_1', validation_level=VALIDATION_LEVEL.STRICT)
        with self.assertRaises(OperationNotAllowed):
            c.datatype = 'TX'

        c1 = Component('CX_1', datatype='ST', validation_level=VALIDATION_LEVEL.STRICT)
        with self.assertRaises(OperationNotAllowed):
            c1.datatype = 'TX'

        self.assertRaises(OperationNotAllowed, Component, 'CX_1', datatype='TX',
                          validation_level=VALIDATION_LEVEL.STRICT)

        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.TOLERANT)
        c = m.add_segment('QPD').add_field('QPD_8').add_component('CX_1')
        c.datatype = 'TX'

        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.STRICT)
        c = m.add_segment('QPD').add_field('QPD_8').add_component('CX_1')
        with self.assertRaises(OperationNotAllowed):
            c.datatype = 'TX'

    def test_add_unexpected_child_to_component(self):
        g = Group()
        m = Message('OML_O33')
        f = Field()
        c_base = Component(datatype='ST')
        c_complex = Component(datatype='CWE')

        self.assertRaises(ChildNotValid, c_base.add, g)
        self.assertRaises(ChildNotValid, c_base.add, m)
        self.assertRaises(ChildNotValid, c_base.add, f)
        self.assertRaises(ChildNotValid, c_complex.add, g)
        self.assertRaises(ChildNotValid, c_complex.add, m)
        self.assertRaises(ChildNotValid, c_complex.add, f)

    def test_delete_component(self):
        m = Message('OML_O33')
        m.pid = 'PID|||||bianchi^mario|||'
        pid_5_1 = m.pid.pid_5.pid_5_1[0]
        self.assertIn(pid_5_1, m.pid.pid_5.children)
        del m.pid.pid_5.pid_5_1
        self.assertNotIn(pid_5_1, m.pid.pid_5.children)

        m = Message('RSP_K21', reference=self.rsp_k21_mp)
        m.qpd = 'QPD|IHE PDQ Query|222222222|@PID.3.1.1^3333333|||||^^^IHEFACILITY&1.3.6.1.4.1.21367.3000.1.6&ISO|'
        qpd_3_1 = m.qpd.qpd_3.qpd_3_1[0]
        self.assertIn(qpd_3_1, m.qpd.qpd_3.children)
        del m.qpd.qpd_3.qpd_3_1
        self.assertNotIn(qpd_3_1, m.qpd.qpd_3.children)

    def test_assign_complex_field_datatype_by_get(self):
        p = Segment('PID')
        p.pid_5 = 'test^test'
        self.assertEqual(p.pid_5.xpn_1.to_er7(), 'test')
        self.assertEqual(p.pid_5.xpn_2.to_er7(), 'test')

        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.TOLERANT)
        p = m.rsp_k21_query_response.add_segment('pid')
        p.pid_5 = 'test^test'
        self.assertEqual(p.pid_5.xpn_1.to_er7(), 'test')
        self.assertEqual(p.pid_5.xpn_2.to_er7(), 'test')

    def test_create_base_datatype_component_by_get(self):
        f = Field('SID_2')
        f.sid_2_1 = 'field'
        self.assertEqual(f.sid_2_1.to_er7(), 'field')

    def test_add_subcomponent_to_unknown_base_dt_component(self):
        c = Component(datatype='ST')
        self.assertRaises(ChildNotValid, c.add_subcomponent, 'HD_1')

    def test_add_subcomponent(self):
        c = Component('XPN_1')
        s = SubComponent('FN_1')
        c.add(s)
        self.assertIn(s, c.children)
        self.assertEqual(c.children[0].name, 'FN_1')

        c = Component('XPN_1')
        s = c.add_subcomponent('FN_1')
        self.assertIn(s, c.children)
        self.assertEqual(c.children[0].name, 'FN_1')

        m = Message('RSP_K21', reference=self.rsp_k21_mp)
        c = m.add_segment('qpd').add_field('qpd_8').add_component('cx_10')
        s = SubComponent('CWE_1')
        c.add(s)
        self.assertIn(s, c.children)
        self.assertEqual(c.children[0].name, 'CWE_1')

    def test_assign_value_string(self):
        # simple string
        cmp_str = 'aaa'

        # tolerant
        c = Component('CWE_1', validation_level=VALIDATION_LEVEL.TOLERANT)
        c.value = cmp_str
        self.assertEqual(c.to_er7(), cmp_str)

        # strict
        c = Component('CWE_1', validation_level=VALIDATION_LEVEL.STRICT)
        c.value = cmp_str
        self.assertEqual(c.to_er7(), cmp_str)

        # unknown
        c = Component()
        c.value = cmp_str
        self.assertEqual(c.to_er7(), cmp_str)

        # complex string
        cmp_str = '1&2'

        # tolerant
        c = Component('CWE_1', validation_level=VALIDATION_LEVEL.TOLERANT) # more child than allowed
        c.value = cmp_str
        self.assertEqual(c.to_er7(), cmp_str)
        self.assertEqual(len(c.children), 2)

        # strict
        c = Component('CWE_1', validation_level=VALIDATION_LEVEL.STRICT)
        with self.assertRaises(MaxChildLimitReached):
            c.value = cmp_str

        # unknown
        c = Component('CWE_1', validation_level=VALIDATION_LEVEL.TOLERANT) # more child than allowed
        c.value = cmp_str
        self.assertEqual(c.to_er7(), cmp_str)
        self.assertEqual(len(c.children), 2)

        # max length
        # tolerant
        for dt in ('ST', 'ID', 'FT', 'GTS', 'IS', 'TX'):
            c = Component(datatype=dt, validation_level=VALIDATION_LEVEL.TOLERANT) # max length reached string type
            c.value = 65537*'a'
        for dt in ('NM', 'SI'):
            c = Component(datatype=dt, validation_level=VALIDATION_LEVEL.TOLERANT)
            c.value = 5*'1'

        # strict
        c = Component(datatype='ID', validation_level=VALIDATION_LEVEL.STRICT) # ID works because its length depends on HL7 table
        c.value = 65537*'a'
        self.assertEqual(c.to_er7(), 65537*'a')
        for dt in ('ST', 'FT', 'GTS', 'IS', 'TX'):
            with self.assertRaises(MaxLengthReached):
                c = Component(datatype=dt, validation_level=VALIDATION_LEVEL.STRICT) # max length reached string type
                c.value = 65537*'a'
        with self.assertRaises(MaxLengthReached):
            c = Component(datatype='NM', validation_level=VALIDATION_LEVEL.STRICT)
            c.value = 17*'1'
        with self.assertRaises(MaxLengthReached):
            c = Component(datatype='SI', validation_level=VALIDATION_LEVEL.STRICT)
            c.value = 5*'1'

        # complex datatypes
        # tolerant
        complex_cmp_str = 'xxx&yyy&zzz'
        c = Component('CX_10', validation_level=VALIDATION_LEVEL.TOLERANT)
        c.value = complex_cmp_str
        self.assertEqual(c.to_er7(), complex_cmp_str)
        self.assertEqual(len(c.children), 3)

        # strict
        complex_cmp_str = 'xxx&yyy&zzz'
        c = Component('CX_10', validation_level=VALIDATION_LEVEL.STRICT)
        c.value = complex_cmp_str
        self.assertEqual(c.to_er7(), complex_cmp_str)
        self.assertEqual(len(c.children), 3)

        # unknown
        complex_cmp_str = 'xxx&yyy&zzz'
        c = Component(validation_level=VALIDATION_LEVEL.TOLERANT)
        c.value = complex_cmp_str
        self.assertEqual(c.to_er7(), complex_cmp_str)
        self.assertEqual(len(c.children), 3)

    def test_assign_value_string_message_profile(self):
        # TODO: test max_ length for every base datatype
        # simple string
        cmp_str = 'aaa'

        # tolerant
        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.TOLERANT)
        c = m.add_segment('qpd').add_field('qpd_8').add_component('cx_2')
        c.value = cmp_str
        self.assertEqual(c.to_er7(), cmp_str)

        # strict
        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.STRICT)
        c = m.add_segment('qpd').add_field('qpd_8').add_component('cx_2')
        c.value = cmp_str
        self.assertEqual(c.to_er7(), cmp_str)

        # complex string
        cmp_str = '1&2'

        # tolerant
        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.TOLERANT)
        c = m.add_segment('qpd').add_field('qpd_8').add_component('cx_2')
        c.value = cmp_str
        self.assertEqual(c.to_er7(), cmp_str)
        self.assertEqual(len(c.children), 2)

        # strict
        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.STRICT)
        c = m.add_segment('qpd').add_field('qpd_8').add_component('cx_2')
        with self.assertRaises(MaxChildLimitReached):
            c.value = cmp_str


        complex_cmp_str = 'xxx&yyy&zzz'

        # tolerant
        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.TOLERANT)
        c = m.add_segment('qpd').add_field('qpd_8').add_component('cx_10')
        c.value = complex_cmp_str
        self.assertEqual(c.to_er7(), complex_cmp_str)
        self.assertEqual(len(c.children), 3)

        # strict
        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.TOLERANT)
        c = m.add_segment('qpd').add_field('qpd_8').add_component('cx_10')
        c.value = complex_cmp_str
        self.assertEqual(c.to_er7(), complex_cmp_str)
        self.assertEqual(len(c.children), 3)

    def test_assign_value_base_datatype(self):
        # tolerant
        c = Component('CX_1', validation_level=VALIDATION_LEVEL.TOLERANT)
        c.value = ST('aaa')
        self.assertEqual(c.to_er7(), 'aaa')
        c.value = ST('bbb')
        self.assertEqual(c.to_er7(), 'bbb')

        with self.assertRaises(ChildNotValid):
            c.value = SI(1)

        # strict
        c = Component('CX_1', validation_level=VALIDATION_LEVEL.STRICT)
        c.value = ST('aaa')
        self.assertEqual(c.to_er7(), 'aaa')
        c.value = ST('bbb')
        self.assertEqual(c.to_er7(), 'bbb')

        with self.assertRaises(ChildNotValid):
            c.value = SI(1)

        # complex datatype
        # tolerant
        c = Component('CX_10', validation_level=VALIDATION_LEVEL.TOLERANT)
        with self.assertRaises(ChildNotValid):
            c.value = ST('aaa')

        # strict
        c = Component('CX_10', validation_level=VALIDATION_LEVEL.STRICT)
        with self.assertRaises(ChildNotValid):
            c.value = ST('aaa')

    def test_assign_value_base_datatype_message_profile(self):
        # tolerant
        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.TOLERANT)
        c = m.add_segment('qpd').add_field('qpd_8').add_component('cx_1')
        c.value = ST('aaa')
        self.assertEqual(c.to_er7(), 'aaa')
        c.value = ST('bbb')
        self.assertEqual(c.to_er7(), 'bbb')

        with self.assertRaises(ChildNotValid):
            c.value = SI(1)

        # strict
        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.STRICT)
        c = m.add_segment('qpd').add_field('qpd_8').add_component('cx_1')
        c.value = ST('aaa')
        self.assertEqual(c.to_er7(), 'aaa')
        c.value = ST('bbb')
        self.assertEqual(c.to_er7(), 'bbb')

        with self.assertRaises(ChildNotValid):
            c.value = SI(1)

        # complex datatype
        # tolerant
        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.TOLERANT)
        c = m.add_segment('qpd').add_field('qpd_8').add_component('cx_10')
        with self.assertRaises(ChildNotValid):
            c.value = ST('aaa')

        # strict
        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.STRICT)
        c = m.add_segment('qpd').add_field('qpd_8').add_component('cx_10')
        with self.assertRaises(ChildNotValid):
            c.value = ST('aaa')

    def test_assign_value_traversal(self):
        cmp_str = 'aaa'

        # name
        f = Field('PID_39')
        f.cwe_1 = cmp_str
        self.assertEqual(f.cwe_1.to_er7(), cmp_str)

        # alternative name
        f = Field('PID_39')
        f.pid_39_1 = cmp_str
        self.assertEqual(f.cwe_1.to_er7(), cmp_str)

        # value
        f = Field('PID_39')
        f.cwe_1.value = cmp_str
        self.assertEqual(f.cwe_1.to_er7(), cmp_str)

        # value alternative name
        f = Field('PID_39')
        f.cwe_1.value = cmp_str
        self.assertEqual(f.cwe_1.to_er7(), cmp_str)

        # name with base datatype
        f = Field('PID_39')
        f.cwe_1 = ST(cmp_str)
        self.assertEqual(f.cwe_1.to_er7(), cmp_str)

        # value with base datatype
        f = Field('PID_39')
        f.cwe_1.value = ST(cmp_str)
        self.assertEqual(f.cwe_1.to_er7(), cmp_str)

        # further level

        # name
        m = Message('RSP_K21')
        m.pid.pid_39.cwe_1 = cmp_str
        self.assertEqual(m.pid.pid_39.cwe_1.to_er7(), cmp_str)

        # value
        m = Message('RSP_K21')
        m.pid.pid_39.cwe_1.value = cmp_str
        self.assertEqual(m.pid.pid_39.cwe_1.to_er7(), cmp_str)

        # name with base datatype
        m = Message('RSP_K21')
        m.pid.pid_39.cwe_1 = ST(cmp_str)
        self.assertEqual(m.pid.pid_39.cwe_1.to_er7(), cmp_str)

        # value with base datatype
        m = Message('RSP_K21')
        m.pid.pid_39.cwe_1.value = ST(cmp_str)
        self.assertEqual(m.pid.pid_39.cwe_1.to_er7(), cmp_str)

        # complex datatype
        complex_cmp_str = 'xxx&yyy&zzz'

        # name
        f = Field('PID_4')
        f.cx_10 = complex_cmp_str
        self.assertEqual(f.cx_10.to_er7(), complex_cmp_str)
        self.assertEqual(len(f.cx_10.children), 3)

        # value
        f = Field('PID_4')
        f.cx_10.value = complex_cmp_str
        self.assertEqual(f.cx_10.to_er7(), complex_cmp_str)
        self.assertEqual(len(f.cx_10.children), 3)

    def test_assign_value_traversal_message_profile(self):
        cmp_str = 'aaa'

        # name
        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.STRICT)
        f = m.add_group('rsp_k21_query_response').add_segment('pid').add_field('pid_39')
        f.cwe_1 = cmp_str
        self.assertEqual(f.cwe_1.to_er7(), cmp_str)

        # alternative name
        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.STRICT)
        f = m.add_group('rsp_k21_query_response').add_segment('pid').add_field('pid_39')
        f.pid_39_1 = cmp_str
        self.assertEqual(f.cwe_1.to_er7(), cmp_str)

        # value
        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.STRICT)
        f = m.add_group('rsp_k21_query_response').add_segment('pid').add_field('pid_39')
        f.cwe_1.value = cmp_str
        self.assertEqual(f.cwe_1.to_er7(), cmp_str)

        # value alternative name
        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.STRICT)
        f = m.add_group('rsp_k21_query_response').add_segment('pid').add_field('pid_39')
        f.pid_39_1.value = cmp_str
        self.assertEqual(f.cwe_1.to_er7(), cmp_str)

        # name with base datatype
        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.STRICT)
        f = m.add_group('rsp_k21_query_response').add_segment('pid').add_field('pid_39')
        f.cwe_1 = ST(cmp_str)
        self.assertEqual(f.cwe_1.to_er7(), cmp_str)

        # value with base datatype
        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.STRICT)
        f = m.add_group('rsp_k21_query_response').add_segment('pid').add_field('pid_39')
        f.cwe_1.value = ST(cmp_str)
        self.assertEqual(f.cwe_1.to_er7(), cmp_str)

        # further level

        # name
        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.STRICT)
        m.rsp_k21_query_response.pid.pid_39.cwe_1 = cmp_str
        self.assertEqual(m.rsp_k21_query_response.pid.pid_39.cwe_1.to_er7(), cmp_str)

        # value
        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.STRICT)
        m.rsp_k21_query_response.pid.pid_39.cwe_1.value = cmp_str
        self.assertEqual(m.rsp_k21_query_response.pid.pid_39.cwe_1.to_er7(), cmp_str)

        # name with base datatype
        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.STRICT)
        m.rsp_k21_query_response.pid.pid_39.cwe_1 = ST(cmp_str)
        self.assertEqual(m.rsp_k21_query_response.pid.pid_39.cwe_1.to_er7(), cmp_str)

        # value with base datatype
        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.STRICT)
        m.rsp_k21_query_response.pid.pid_39.cwe_1.value = ST(cmp_str)
        self.assertEqual(m.rsp_k21_query_response.pid.pid_39.cwe_1.to_er7(), cmp_str)

        # complex datatype
        complex_cmp_str = 'xxx&yyy&zzz'

        # name
        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.STRICT)
        f = m.add_segment('qpd').add_field('qpd_8')
        f.cx_10 = complex_cmp_str
        self.assertEqual(f.cx_10.to_er7(), complex_cmp_str)
        self.assertEqual(len(f.cx_10.children), 3)

        # value
        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.STRICT)
        f = m.add_segment('qpd').add_field('qpd_8')
        f.cx_10.value = complex_cmp_str
        self.assertEqual(f.cx_10.to_er7(), complex_cmp_str)
        self.assertEqual(len(f.cx_10.children), 3)

    def test_assign_value_with_encoding_chars(self):
        cmp_str = 'xxx^yyy'
        c = Component()
        c.value = cmp_str
        self.assertEqual(c.to_er7(), 'xxx\\S\\yyy')

        c = Component('CWE_1')
        c.value = cmp_str
        self.assertEqual(c.to_er7(), 'xxx\\S\\yyy')

        c = Component('CWE_1', validation_level=VALIDATION_LEVEL.STRICT)
        c.value = cmp_str
        self.assertEqual(c.to_er7(), 'xxx\\S\\yyy')

    def test_bug_13(self):
        c = Component('CX_10')
        s = c.cwe_1

        self.assertEqual(id(c.cwe_1), id(s))
        c.cwe_1 = 'b'

        self.assertEqual(s.children, c.cwe_1.children)

    def test_assign_value_with_unknown_subcomponent(self):
        c = Component(datatype='CE')
        c.value = '555-55-5555&PRIMARY&PATRICIA P&6&&MD&UNKN'
        self.assertEqual(c.children[-1].name, 'ST')
        self.assertEqual(c.children[-1].datatype, 'ST')
        self.assertEqual(c.children[-1].to_er7(), 'UNKN')
        self.assertEqual(c.value, '555-55-5555&PRIMARY&PATRICIA P&6&&MD&UNKN')


class TestSubComponent(unittest.TestCase):

    def setUp(self):
        base_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(base_path, 'profiles/iti_21')
        self.rsp_k21_mp = hl7apy.load_message_profile(path)

    def test_create_subcomponent(self):
        a = SubComponent('HD_1', datatype='ST')
        self.assertEqual(a.classname, 'SubComponent')
        b = SubComponent(datatype='ST')
        self.assertEqual(b.classname, 'SubComponent')

    def test_create_unknown_subcomponent(self):
        self.assertRaises(InvalidName, SubComponent, 'xxx_1')
        self.assertRaises(InvalidName, SubComponent, 'CX')

    def test_create_invalid_subcomponent_empty(self):
        self.assertRaises(OperationNotAllowed, SubComponent)

    def test_create_invalid_subcomponent_with_complex_component_name(self):
        self.assertRaises(OperationNotAllowed, SubComponent, 'CX_4', datatype='ST')

    def test_create_unsupported_version_subcomponent(self):
        SubComponent(datatype='ST', version='2.5')
        self.assertRaises(UnsupportedVersion, SubComponent, datatype='ST', version='2.0')

    def test_override_datatype(self):
        s = SubComponent('HD_1', datatype='TX', validation_level=VALIDATION_LEVEL.TOLERANT)
        self.assertEqual(s.datatype, 'TX')

        self.assertRaises(OperationNotAllowed, SubComponent, 'HD_1', datatype='TX',
                          validation_level=VALIDATION_LEVEL.STRICT)

        s = SubComponent('HD_1', validation_level=VALIDATION_LEVEL.TOLERANT)
        s.datatype = 'TX'
        self.assertEqual(s.datatype, 'TX')

        s = SubComponent('HD_1', validation_level=VALIDATION_LEVEL.STRICT)
        with self.assertRaises(OperationNotAllowed):
            s.datatype = 'TX'

        s = SubComponent(datatype='ST', validation_level=VALIDATION_LEVEL.STRICT)
        with self.assertRaises(OperationNotAllowed):
            s.datatype = 'TX'

        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.TOLERANT)
        s = m.add_segment('QPD').add_field('QPD_8').add_component('CX_10').add_subcomponent('CWE_1')
        s.datatype = 'TX'
        self.assertEqual(s.datatype, 'TX')

        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.STRICT)
        s = m.add_segment('QPD').add_field('QPD_8').add_component('CX_10').add_subcomponent('CWE_1')
        with self.assertRaises(OperationNotAllowed):
            s.datatype = 'TX'

    def test_change_datatype_for_valued_subcomponent(self):
        a = SubComponent('HD_1', value='value')
        with self.assertRaises(OperationNotAllowed):
            a.datatype = 'ST'

        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.TOLERANT)
        s = m.add_segment('QPD').add_field('QPD_8').add_component('CX_10').add_subcomponent('CWE_1')
        s.value = 'value'
        with self.assertRaises(OperationNotAllowed):
            s.datatype = 'TX'

    def test_assign_not_allowed_datatype_to_subcomponent(self):
        a = SubComponent('HD_1')
        with self.assertRaises(OperationNotAllowed):
            a.datatype = 'CX'

        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.TOLERANT)
        s = m.add_segment('QPD').add_field('QPD_8').add_component('CX_10').add_subcomponent('CWE_1')
        with self.assertRaises(OperationNotAllowed):
            s.datatype = 'CX'

    def test_assign_value_traversal(self):
        subcmp_str = 'aaa'

        c = Component('CX_10')
        c.cwe_1 = subcmp_str
        self.assertEqual(c.to_er7(), subcmp_str)

        c = Component('CX_10')
        c.cwe_1.value = subcmp_str
        self.assertEqual(c.to_er7(), subcmp_str)

        c = Component('CX_10')
        c.cwe_1 = ST(subcmp_str)
        self.assertEqual(c.to_er7(), subcmp_str)

        c = Component('CX_10')
        c.cwe_1.value = ST(subcmp_str)
        self.assertEqual(c.to_er7(), subcmp_str)

        # further level
        segment_str = 'PID||||^^^^^^^^^aaa'
        s = Segment('PID')
        s.pid_4.pid_4_10_1 = subcmp_str
        self.assertEqual(s.to_er7(), segment_str)

        s = Segment('PID')
        s.pid_4.pid_4_10_1.value = subcmp_str
        self.assertEqual(s.to_er7(), segment_str)

        s = Segment('PID')
        s.pid_4.pid_4_10_1.value = ST(subcmp_str)
        self.assertEqual(s.to_er7(), segment_str)

        s = Segment('PID')
        s.pid_4.pid_4_10_1.value = ST(subcmp_str)
        self.assertEqual(s.to_er7(), segment_str)

    def test_assign_value_traversal_message_profile(self):
        subcmp_str = 'aaa'

        # string
        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.STRICT)
        c = m.add_segment('QPD').add_field('QPD_8').add_component('CX_10')
        c.cwe_1 = subcmp_str
        self.assertEqual(c.cwe_1.to_er7(), subcmp_str)

        # string using value
        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.STRICT)
        c = m.add_segment('QPD').add_field('QPD_8').add_component('CX_10')
        c.cwe_1.value = subcmp_str
        self.assertEqual(c.cwe_1.to_er7(), subcmp_str)

        # base datatype
        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.STRICT)
        c = m.add_segment('QPD').add_field('QPD_8').add_component('CX_10')
        c.cwe_1 = ST(subcmp_str)
        self.assertEqual(c.cwe_1.to_er7(), subcmp_str)

        # base datatype using value
        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.STRICT)
        c = m.add_segment('QPD').add_field('QPD_8').add_component('CX_10')
        c.cwe_1.value = ST(subcmp_str)
        self.assertEqual(c.cwe_1.to_er7(), subcmp_str)

        # further levels
        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.STRICT)
        m.qpd.qpd_8.qpd_8_10_1 = subcmp_str
        self.assertEqual(m.qpd.qpd_8.cx_10.cwe_1.to_er7(), subcmp_str)

        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.STRICT)
        m.qpd.qpd_8.qpd_8_10_1.value = subcmp_str
        self.assertEqual(m.qpd.qpd_8.cx_10.cwe_1.to_er7(), subcmp_str)

        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.STRICT)
        m.qpd.qpd_8.qpd_8_10_1 = ST(subcmp_str)
        self.assertEqual(m.qpd.qpd_8.cx_10.cwe_1.to_er7(), subcmp_str)

        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.STRICT)
        m.qpd.qpd_8.qpd_8_10_1.value = ST(subcmp_str)
        self.assertEqual(m.qpd.qpd_8.cx_10.cwe_1.to_er7(), subcmp_str)

    def test_assign_value(self):
        # tolerant
        cmp_str = 'aaa'
        s = SubComponent('CWE_1')
        s.value = cmp_str
        self.assertEqual(s.to_er7(), cmp_str)

        s = SubComponent('CWE_1')  # more child than allowed
        s.value = '1&2'

        for dt in ('ST', 'ID', 'FT', 'GTS', 'IS', 'TX'):
            s = SubComponent(datatype=dt)  # max length reached string type
            s.value = 65537*'a'
        for dt in ('NM', 'SI'):
            s = SubComponent(datatype=dt)
            s.value = 65537*'1'

        # strict
        s = SubComponent('CWE_1', validation_level=VALIDATION_LEVEL.STRICT)
        s.value = cmp_str
        self.assertEqual(s.to_er7(), cmp_str)

        # ID is missing because its max length is None
        for dt in ('ST', 'FT', 'GTS', 'IS', 'TX'):
            # max length reached string type
            s = SubComponent(datatype=dt, validation_level=VALIDATION_LEVEL.STRICT)
            with self.assertRaises(MaxLengthReached):
                s.value = 65537*'a'

        s = SubComponent(datatype='NM', validation_level=VALIDATION_LEVEL.STRICT)
        with self.assertRaises(MaxLengthReached):
            s.value = 17 * '1'

        s = SubComponent(datatype='SI', validation_level=VALIDATION_LEVEL.STRICT)
        with self.assertRaises(MaxLengthReached):
            s.value = 5*'1'

    def test_add_child_to_subcomponent(self):
        a = SubComponent('HD_1')
        self.assertRaises(OperationNotAllowed, a.add, SubComponent('HD_2'))

    def test_create_subcomponent_by_get(self):
        p = Segment('PID')
        self.assertEqual(p.pid_5.pid_5_1.fn_1.name, 'FN_1')
        self.assertEqual(p.pid_5.pid_5_1_1.name, 'FN_1')

        m = Message('RSP_K21', reference=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.STRICT)
        p = m.rsp_k21_query_response.pid
        self.assertEqual(p.pid_5.pid_5_1.fn_1.name, 'FN_1')
        self.assertEqual(p.pid_5.pid_5_1_1.name, 'FN_1')

    def create_unknown_subcomponent_by_get(self):
        f = Field('STF_2')
        with self.assertRaises(ChildNotFound):
            f.stf_2_10_100 = 'subcomponent'


if __name__ == '__main__':
    unittest.main()