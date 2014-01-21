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
from hl7apy.core import Message, Segment, Field, Group, Component, SubComponent, ElementProxy
from hl7apy.exceptions import ChildNotValid, ChildNotFound, OperationNotAllowed, InvalidName, MaxChildLimitReached, \
                              UnsupportedVersion, InvalidEncodingChars

from hl7apy.validation import VALIDATION_LEVEL
from hl7apy.parser import parse_message, parse_segment, parse_field, parse_component

def _get_invalid_encoding_chars():
    return {'COMPONENT' : '$',
            'SUBCOMPONENT' : '@',
            'REPETITION' : 'r',
            'ESCAPE' : '@'}

def _get_test_msg():
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


class TestMessage(unittest.TestCase):

    #Message test cases

    def test_create_empty_message(self):
        e = Message()
        self.assertEqual(e.classname, 'Message')
        self.assertRaises(OperationNotAllowed, Message,
                          validation_level=VALIDATION_LEVEL.STRICT)

    def test_create_unknown_message(self):
        self.assertRaises(InvalidName, Message, 'AAA_A01')
        self.assertRaises(InvalidName, Message, 'AAA_A01', validation_level=VALIDATION_LEVEL.STRICT)

    def test_create_unsupported_version_message(self):
        self.assertRaises(UnsupportedVersion, Message, version='2.0')

    def test_create_invalid_encoding_chars_message(self):
        self.assertRaises(InvalidEncodingChars, Message, encoding_chars=_get_invalid_encoding_chars())
        self.assertRaises(InvalidEncodingChars, Message, 'ADT_A01', encoding_chars=_get_invalid_encoding_chars(),
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

    def test_add_empty_children_to_message(self):
        a = Message('OML_O33', validation_level=VALIDATION_LEVEL.STRICT)
        self.assertRaises(ChildNotValid, a.add, Group())
        b = Message('OML_O33')
        b.add(Group())

    def test_add_not_allowed_segment_to_known_message(self):
        a = Message('OML_O33', validation_level=VALIDATION_LEVEL.STRICT)
        self.assertRaises(ChildNotValid, a.add, Segment('MSA'))
        b = Message('OML_O33')
        b.add(Segment('MSA'))

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
        with self.assertRaises(ChildNotValid):
            b.msh = Segment('SPM')
        with self.assertRaises(ChildNotValid):
            b.pid = 'EVN||20080115153000||||20080114003000'

    def test_add_segment_to_message_mix(self):
        a = Message('OML_O33',  validation_level=VALIDATION_LEVEL.QUIET)
        msh = Segment('MSH', validation_level=VALIDATION_LEVEL.QUIET)
        pid = Segment('PID', validation_level=VALIDATION_LEVEL.QUIET)
        g = Group('OML_O33_PATIENT')
        g.add(pid)
        a.add(msh)
        a.add(g)

    def test_assign_value(self):
        msg = _get_test_msg()
        a = Message('OML_O33', validation_level=VALIDATION_LEVEL.QUIET)
        parsed_a = parse_message(msg, validation_level=VALIDATION_LEVEL.QUIET)
        a.value = msg
        self.assertEqual(a.to_er7(), parsed_a.to_er7())

        b = Message('OML_O33', validation_level=VALIDATION_LEVEL.STRICT)
        b.value = msg
        parsed_b = parse_message(msg, validation_level=VALIDATION_LEVEL.STRICT)
        self.assertEqual(b.to_er7(), parsed_b.to_er7())
        self.assertEqual(b.children.indexes.keys(), parsed_b.children.indexes.keys())

        c = Message('ADT_A01', validation_level=VALIDATION_LEVEL.QUIET)
        with self.assertRaises(OperationNotAllowed):
            c.value = msg

        msg = msg.replace('^', 'x')
        with self.assertRaises(OperationNotAllowed):
            a.value = msg

        c = Message('OML_O33', version='2.6')
        with self.assertRaises(OperationNotAllowed):
            c.value = msg

    def test_assign_value_unknown_message(self):
        msg = _get_test_msg()
        a = Message()
        parsed_a = parse_message(msg, validation_level=VALIDATION_LEVEL.QUIET)
        a.value = msg
        self.assertEqual(a.name, 'OML_O33')
        self.assertEqual(a.to_er7(), parsed_a.to_er7())

    #def test_message_ordered_children(self):
    #    m = Message('OML_O33')
    #    m.add(Group('OML_O33_PATIENT'))
    #    ordered_children = m.children.get_ordered_children()
    #    self.assertEqual(ordered_children[0][0].name, 'MSH' )
    #    self.assertIsNone(ordered_children[1])
    #    self.assertEqual(ordered_children[3][0].name, 'OML_O33_PATIENT')
    #    self.assertIsNone(ordered_children[2])
    #    self.assertIsNone(ordered_children[4])

    #def test_message_get_children(self):
    #    m = Message('OML_O33')
    #    children = m.children.get_children()
    #    self.assertEqual(len(children), 1)
    #    m.pid = 'PID|||||bianchi^mario|||'
    #    children = m.children.get_children()
    #    self.assertEqual(len(children), 2)


class TestGroup(unittest.TestCase):

    #Group test cases

    def setUp(self):
        self.oml_o33_specimen = 'SPM|1|100187400201||SPECIMEN^Blood|||||||PSN^Human Patient||||||20110708162817||20110708162817|||||||1|CONTAINER^CONTAINER DESC\r' \
           'ORC|NW|83428|83428|18740|SC||||20110708162817||||||||\r' \
           'TQ1|||||||||R\r' \
           'OBR||83428|83428|TPO^ANTI THYROPEROXIDASE ANTIBODIES(TPO)^^TPO||||||||||||ND^UNKNOWN^UNKNOWN\r'

    def test_create_unamed_group_strict(self):
        self.assertRaises(OperationNotAllowed,Group, validation_level=VALIDATION_LEVEL.STRICT)

    def test_add_unexpected_child_to_group(self):
        g = Group()
        m = Message()
        f = Field()
        c = Component(datatype='ST')
        sub = SubComponent(datatype='ST')
        self.assertRaises(ChildNotValid, g.add, m)
        self.assertRaises(ChildNotValid, g.add, f)
        self.assertRaises(ChildNotValid, g.add, c)
        self.assertRaises(ChildNotValid, g.add, sub)

    def test_delete_group(self):
        m = Message('OML_O33',  validation_level=VALIDATION_LEVEL.QUIET)
        g = Group ('OML_O33_PATIENT')
        m.add(g)
        self.assertEqual(m.oml_O33_patient.name, 'OML_O33_PATIENT' )
        del m.oml_o33_patient
        self.assertFalse(g in m.children)

    def test_create_supported_version_group(self):
        Group(version='2.5')

    def test_create_unsupported_version_group(self):
        self.assertRaises(UnsupportedVersion, Group, version='2.0')

    def test_assign_value(self):
        g = Group('OML_O33_SPECIMEN')
        g.value = self.oml_o33_specimen

        g = Group('OML_O33_SPECIMEN', validation_level=VALIDATION_LEVEL.STRICT)
        g.value = self.oml_o33_specimen

    def test_assign_value_traversal(self):
        m1 = Message('OML_O33')
        m2 = Message('OML_O33')
        m1.oml_o33_specimen.value = self.oml_o33_specimen
        m2.oml_o33_specimen = self.oml_o33_specimen
        self.assertEqual(m1.to_er7(), m2.to_er7())


    def test_assign_value_unknown_group(self):
        g = Group()
        g.value = self.oml_o33_specimen


class TestSegment(unittest.TestCase):

    #Segment test cases

    #def test_create_empty_segment(self):
    #    s = Segment()
    #    self.assertEqual(s.classname, 'Segment')
    #    self.assertRaises(OperationNotAllowed, Segment, validation_level=VALIDATION_LEVEL.STRICT)

    def test_create_unknown_segment(self):
        self.assertRaises(InvalidName, Segment, 'XXX')
        self.assertRaises(InvalidName, Segment, 'XXX', validation_level=VALIDATION_LEVEL.STRICT)

    def test_create_empty_segment(self):
        self.assertRaises(OperationNotAllowed, Segment)

    def test_create_unsupported_version_segment(self):
        s = Segment('PID', version='2.5')
        self.assertRaises(UnsupportedVersion, Segment, 'PID', version='2.0')

    def test_add_field(self):
        e = Segment('PID')
        pid_5 = e.add_field('PID_5')
        self.assertEqual(pid_5.classname, 'Field')
        self.assertTrue(pid_5.is_named('PID_5'))
        self.assertTrue(pid_5.is_named('PATIENT_NAME'))
        self.assertRaises(ChildNotFound, e.add_field, 'UNKNOWN_FIELD')

    def test_traversal_equality(self):
        obr = Segment('OBR')
        obr.obr_26 = 'xxx&yyy^zzz^www'
        obr_26 = obr.parent_result
        self.assertTrue(isinstance(obr_26, ElementProxy))
        self.assertTrue(obr_26[0] == obr.obr_26[0], 'obr.parent_result != obr.obr_26')

    def test_traversal_by_name(self):
        obr = Segment('OBR')
        obr_26 = obr.parent_result
        self.assertTrue(obr_26.is_named('OBR_26'))
        self.assertTrue(obr_26.is_named('PARENT_RESULT'))

    def test_recursive_traversal(self):
        obr = Segment('OBR')
        obr.obr_26 = 'xxx&yyy^zzz^www'
        by_name = obr.parent_result.parent_observation_identifier
        by_position = obr.obr_26.obr_26_1
        self.assertEqual(by_name[0], by_position[0]) # bug!

    def test_add_empty_field(self):
        s = Segment('SPM', validation_level=VALIDATION_LEVEL.STRICT)
        self.assertRaises(ChildNotValid, s.add, Field())
        s = Segment('SPM')
        s.add(Field())

    #def test_add_known_fields_to_empty_segment(self):
    #   s = Segment()
    #    #self.assertRaises(ChildNotFound, s.add, Field('spm_10')) #This one is not raised!!!!

    def test_add_not_allowed_fields_to_known_segments(self):
        s = Segment('PID', validation_level=VALIDATION_LEVEL.STRICT)
        self.assertRaises(ChildNotValid, s.add, Field('spm_10'))
        s = Segment('PID')
        self.assertRaises(ChildNotValid, s.add, Field('spm_10'))

    def test_assign_wrong_field_to_known_position(self):
        s1 = Segment('MSH',validation_level=VALIDATION_LEVEL.STRICT)
        s2 = Segment('QPD')
        with self.assertRaises(ChildNotValid):
            s1.msh_10 = Field('spm_10')
        with self.assertRaises(ChildNotValid):
            s2.qpd_3 = Field('pid_3')

    def test_access_to_unknown_field(self):
        s1 = Segment('MSH',validation_level=VALIDATION_LEVEL.STRICT)
        s2 = Segment('PID')
        with self.assertRaises(ChildNotFound):
            s1.msh_100
        with self.assertRaises(ChildNotFound):
            s2.pid_100

    def test_delete_segment(self):
        m = Message('OML_O33')
        pid = Segment('PID')
        m.add(pid)
        del m.pid
        self.assertFalse(pid in m.children)

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

    def test_assign_value_traversal(self):
        segment_str = 'PID|1||123-456-789^^^HOSPITAL^MR||SURNAME^NAME^A|||M|||1111 SOMEWHERE STREET^^SOMEWHERE^^^USA||555-555-2004~444-333-222|||M\r'

        m1 = Message('OML_O33')
        m2 = Message('OML_O33')
        m1.pid.value = segment_str
        m2.pid.value = segment_str
        self.assertEqual(m1.to_er7(), m2.to_er7())

    def test_assign_wrong_value(self):
        s = Segment('PID')
        wrong_segment_str = 'EVN|1||123-456-789^^^HOSPITAL^MR||SURNAME^NAME^A|||M|||1111 SOMEWHERE STREET^^SOMEWHERE^^^USA||555-555-2004~444-333-222|||M\r'
        with self.assertRaises(OperationNotAllowed):
            s.value = wrong_segment_str


class TestField(unittest.TestCase):

    #Field test cases

    def test_create_empty_field(self):
        f = Field()
        self.assertEqual(f.classname, 'Field')
        self.assertRaises(OperationNotAllowed, Field, validation_level=VALIDATION_LEVEL.STRICT)

    def test_create_unknown_field(self):
        self.assertRaises(InvalidName, Field, 'ckk_10')
        self.assertRaises(InvalidName, Field, 'ckk_10', validation_level=VALIDATION_LEVEL.STRICT)

    def test_create_unsupported_version_field(self):
        # f = Field(version = '2.5')
        self.assertRaises(UnsupportedVersion, Field, version='2.0')

    def test_create_varies_datatype_field(self):
        f = Field ('PID_1', datatype='varies')
        self.assertEqual(f.datatype, 'varies')

    def test_add_empty_component(self):
        f1 = Field('pid_3', validation_level=VALIDATION_LEVEL.STRICT)
        self.assertRaises(ChildNotValid, f1.add, Component(datatype='ST'))
        f2 =  Field('pid_3')
        f2.add(Component(datatype='ST'))

    def test_add_known_components_to_empty_fields(self):
        f1 = Field('pid_3', validation_level=VALIDATION_LEVEL.STRICT)
        self.assertRaises(ChildNotValid, f1.add, Component(datatype='CX_1'))
        f2 = Field('pid_3')
        #self.assertRaises(ChildNotValid, f2.add, Component(datatype='CX_1')) #this one is not raised!!!

    def test_add_not_allowed_components_to_known_field(self):
        f1 = Field('pid_3', validation_level=VALIDATION_LEVEL.STRICT)
        self.assertRaises(ChildNotValid, f1.add, Component(datatype='ST'))
        f2 = Field('pid_3')
        self.assertRaises(ChildNotValid, f2.add, Component('XPN_1'))

    def test_assign_wrong_component_to_known_position(self):
        f1 = Field('pid_10', validation_level=VALIDATION_LEVEL.STRICT)
        with self.assertRaises(ChildNotValid):
            f1.ce_1 = Component('CX_1')
        f2 = Field('pid_3')
        #with self.assertRaises(ChildNotValid):   #this one is not raised!!!
        #	f2.cx_1 = Component('HD_1')
        f2.cx_1 = Component('CX_1')

    def test_access_to_unknown_component(self):
        f1 = Field('pid_10', validation_level=VALIDATION_LEVEL.STRICT)
        f2 = Field('pid_3')
        with self.assertRaises(ChildNotFound):
            f1.ce_100
        with self.assertRaises(ChildNotFound):
            f2.cx_100

    def test_add_more_components_to_base_datatype_field(self):
        f1 = Field('pid_8', validation_level=VALIDATION_LEVEL.STRICT) #this is a base datatype field
        f1.add(Component(datatype='IS'))
        self.assertRaises(MaxChildLimitReached, f1.add, Component(datatype='ST'))
        f2 = Field('pid_8')
        f2.add(Component(datatype='IS'))
        self.assertRaises(MaxChildLimitReached, f2.add, Component(datatype='ST'))

    def test_override_field_datatype_strict(self):
        a = Field('pid_3',  validation_level=VALIDATION_LEVEL.STRICT)
        with self.assertRaises(OperationNotAllowed):
            a.datatype = 'HD'
        self.assertRaises(OperationNotAllowed, Field, 'pid_3', datatype='HD', validation_level=VALIDATION_LEVEL.STRICT)

    def test_override_field_datatype(self):
        a = Field('pid_3', 'HD')
        self.assertEqual(a.datatype, 'HD')

    def test_override_field_containing_children_datatype(self):
        a = Field('pid_3')
        a.cx_1 = 'cx_1 value'
        a.cx_4 = 'cx_4 value'
        with self.assertRaises(OperationNotAllowed):
            a.datatype = 'HD'

    def test_delete_field(self):
        m = Message('OML_O33')
        msh = m.msh
        msh7 = msh.msh_7
        del msh.msh_7
        self.assertTrue(msh7 not in msh.children)

    #def test_create_fields_by_get(self):
    #    s = Segment('MSH')
    #    s.msh_18

    def test_base_datatype_field_get(self):
        s = Segment('MSH')
        s.msh_10.msh_10_1
        s.msh_10.msh_10_1.value = 'Value'
        s.msh_10.msh_10_1.value = '11111'
        with self.assertRaises(ChildNotFound):
            s.msh_10.msh_10_2

    def test_assign_field_by_get(self):
        s = Segment('MSH')
        s.msh_10 = 'Value'
        s.msh_10.msh_10_1 = 'Value'

    def test_add_component(self):
        f = Field('PID_5')
        f.add_component('XPN_1')
        self.assertEqual(f.children[0].name,'XPN_1')

    def test_assign_value(self):
        field_str = '1010110909194822^^^AUTH&1.3.6.1.4.1.21367.2011.2.5.17&ISO^PK'

        f = Field('PID_3')
        f.value = field_str
        parsed_field = parse_field(field_str, 'PID_3')
        self.assertEqual(f.to_er7(), parsed_field.to_er7())

        f = Field('PID_3', validation_level=VALIDATION_LEVEL.STRICT)
        f.value = field_str
        self.assertEqual(f.to_er7(), parsed_field.to_er7())

        f = Field('PID_1', validation_level=VALIDATION_LEVEL.STRICT)
        with self.assertRaises(MaxChildLimitReached):
            f.value = '1^2'

    def test_assign_value_traversal(self):
        field_str = '1010110909194822^^^AUTH&1.3.6.1.4.1.21367.2011.2.5.17&ISO^PK'

        s1 = Segment('PID')
        s2 = Segment('PID')
        s1.pid_3.value = field_str
        s2.pid_3 = field_str

        self.assertEqual(s1.to_er7(), s2.to_er7())

    def test_assign_value_unknown_field(self):
        field_str = '1010110909194822^^^AUTH&1.3.6.1.4.1.21367.2011.2.5.17&ISO^PK'
        f = Field()
        f.value = field_str

    def test_assign_value_with_field_separator(self):
        field_str = 'xxx|yyy'
        escaped_str = 'xxx\F\yyy'
        f = Field('PID_3')
        f.value = field_str
        self.assertEqual(f.to_er7(), escaped_str)

        f = Field('PID_3', validation_level=VALIDATION_LEVEL.STRICT)
        f.value = field_str
        self.assertEqual(f.to_er7(), escaped_str)

        f = Field()
        f.value = field_str
        self.assertEqual(f.to_er7(), 'xxx\F\yyy')

    def test_assign_value_with_repetition(self):
        field_str = 'xxx~yyy'
        f = Field()
        f.value = field_str
        self.assertEqual(f.to_er7(), 'xxx\R\yyy')

        f = Field('PID_2')
        f.value = field_str
        self.assertEqual(f.to_er7(), 'xxx\R\yyy')

        f = Field('PID_2', validation_level=VALIDATION_LEVEL.STRICT)
        f.value = field_str
        self.assertEqual(f.to_er7(), 'xxx\R\yyy')


class TestComponent(unittest.TestCase):

    #Component test cases

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

    def test_create_invalid_component(self):
        self.assertRaises(InvalidName, Component, 'AD')

    def test_create_unsupported_version_component(self):
        Component(datatype='ST', version='2.5')
        self.assertRaises(UnsupportedVersion, Component, version='2.0')

    def test_add_empty_subcomponent(self):
        c1 = Component('cx_4', validation_level=VALIDATION_LEVEL.STRICT)
        self.assertRaises(ChildNotValid, c1.add, SubComponent(datatype='ST'))
        c2 = Component('cx_4')
        c2.add(SubComponent(datatype='ST'))

    def add_unknown_component_strict(self):
        self.assertRaises(OperationNotAllowed, Component, validation_level=VALIDATION_LEVEL.STRICT)

    def test_add_known_subcomponent_to_empty_component(self):
        c = Component()
        self.assertRaises(ChildNotValid, c.add, SubComponent('fn_1'))

    def test_add_not_allowed_subcomponent_to_known_component(self):
        c = Component('cx_4', validation_level=VALIDATION_LEVEL.STRICT)
        self.assertRaises(ChildNotValid, c.add, SubComponent('fn_1'))
        c1 = Component('cx_4')
        self.assertRaises(ChildNotValid, c1.add, SubComponent('fn_1'))

    def test_assign_wrong_subcomponent_to_known_position(self):
        c = Component('XPN_1')
        with self.assertRaises(ChildNotValid):
            c.fn_1 = SubComponent('hd_1')
        c1 = Component('XPN_1', validation_level=VALIDATION_LEVEL.STRICT)
        with self.assertRaises(ChildNotValid):
            c1.fn_1 = SubComponent('hd_1')

    def test_access_to_unknown_subcomponent(self):
        c1 = Component('XPN_1', validation_level=VALIDATION_LEVEL.STRICT)
        c2 = Component('cx_4')
        with self.assertRaises(ChildNotFound):
            c1.fn_100
        with self.assertRaises(ChildNotFound):
            c2.hd_100

    def test_add_more_subcomponents_to_base_datatype_component(self):
        c = Component(datatype='ST')
        c.add(SubComponent(datatype='ST'))
        self.assertRaises(MaxChildLimitReached, c.add, SubComponent(datatype='ST'))
        #c1 = Component(datatype='ST', validation_level=VALIDATION_LEVEL.STRICT)
        #self.assertRaises(ChildNotValid, c1.add, SubComponent(datatype='ST'))

    def test_override_datatype_strict(self):
        c = Component('CX_1',  validation_level=VALIDATION_LEVEL.STRICT)
        with self.assertRaises(OperationNotAllowed):
            c.datatype = 'TX'
        c1 = Component('CX_1', datatype='ST', validation_level=VALIDATION_LEVEL.STRICT)
        with self.assertRaises(OperationNotAllowed):
            c1.datatype = 'TX'

    def test_override_valued_datatype(self):
        c = Component('CX_1')
        c.datatype = 'TX'
        self.assertEqual(c.datatype, 'TX')

    #def test_override_none_datatype(self):
    #    c = Component('CX_1')
    #    with self.assertRaises(OperationNotAllowed):
    #        c.datatype = 'TX'

    # def test_add_subcomponent_to_unknown_component(self):
    #     c = Component()
    #     self.assertRaises(ChildNotValid, c.add, SubComponent(datatype = 'ST'))

    def test_add_unexpected_child_to_component(self):
        g = Group()
        m = Message()
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
        pid51 = m.pid.pid_5.pid_5_1
        del m.pid.pid_5.pid_5_1

    def test_create_component_by_get(self):
        s = Segment('MSH')
        #no children are created here
        with self.assertRaises(IndexError):
            s.msh_9.msh_9_1
            s.children[0].children[0].name

    def test_assign_complex_field_datatype_by_get(self):
        p = Segment('PID')
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
        c.add_subcomponent('FN_1')
        self.assertEqual(c.children[0].name, 'FN_1')

    def test_assign_value(self):
        cmp_str = 'xxx'
        c = Component('CWE_1')
        c.value = cmp_str
        parsed_cmp = parse_component(cmp_str, 'CWE_1')
        self.assertEqual(c.to_er7(), parsed_cmp.to_er7())

        c = Component('CWE_1', validation_level=VALIDATION_LEVEL.STRICT)
        with self.assertRaises(MaxChildLimitReached):
            c.value = '1&2'

        complex_cmp_str = 'xxx&yyy&zzz'
        c = Component('CX_10', validation_level=VALIDATION_LEVEL.STRICT)
        c.value = complex_cmp_str
        parsed_cmp = parse_component(complex_cmp_str, 'CX_10', datatype='CWE', validation_level=VALIDATION_LEVEL.STRICT)
        self.assertEqual(c.to_er7(), parsed_cmp.to_er7())

    def test_assign_value_traversal(self):
        cmp_str = 'xxx'
        f1 = Field('PID_39')
        f2 = Field('PID_39')
        f1.cwe_1.value = cmp_str
        f2.cwe_1 = cmp_str
        self.assertEqual(f1.to_er7(), f2.to_er7())

        s1 = Segment('PID')
        s2 = Segment('PID')
        s1.pid_39.pid_39_1.value = cmp_str
        s2.pid_39.pid_39_1 = cmp_str

        complex_cmp_str = 'xxx&yyy&zzz'
        f1 = Field('PID_4')
        f2 = Field('PID_4')
        f1.cx_10.value = complex_cmp_str
        f2.cx_10 = complex_cmp_str
        self.assertEqual(f1.to_er7(), f2.to_er7())

        s1.pid_4.pid_4_1.value = complex_cmp_str
        s2.pid_4.pid_4_1 = complex_cmp_str
        self.assertEqual(f1.to_er7(), f2.to_er7())


    def test_assign_value_unknown_component(self):
        cmp_str = 'xxx'
        complex_cmp_str = 'xxx&&&&yyy'
        c = Component()
        c.value = cmp_str
        c.value = complex_cmp_str

    def test_assign_value_with_component_separator(self):
        cmp_str = 'xxx^yyy'
        c = Component()
        c.value = cmp_str
        self.assertEqual(c.to_er7(), 'xxx\S\yyy')

        c = Component('CWE_1')
        c.value = cmp_str
        self.assertEqual(c.to_er7(), 'xxx\S\yyy')

        c = Component('CWE_1', validation_level=VALIDATION_LEVEL.STRICT)
        c.value = cmp_str
        self.assertEqual(c.to_er7(), 'xxx\S\yyy')


class TestSubComponent(unittest.TestCase):

     #SubComponent test cases

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

    def test_change_datatype_strict(self):
        self.assertRaises(OperationNotAllowed, SubComponent, 'HD_1', datatype='TX', validation_level=VALIDATION_LEVEL.STRICT)

    def test_change_datatype_for_valued_subcomponent(self):
        a = SubComponent('HD_1', value='value')
        with self.assertRaises(OperationNotAllowed):
            a.datatype = 'ST'

    def test_change_datatype_subcomponent_strict(self):
        s = SubComponent (datatype='ST', validation_level=VALIDATION_LEVEL.STRICT)
        with self.assertRaises(OperationNotAllowed):
            s.datatype = 'TX'

    def test_assign_not_allowed_datatype_to_subcomponent(self):
        a = SubComponent('HD_1')
        with self.assertRaises(OperationNotAllowed):
            a.datatype = 'CX'

    def test_assign_value_traversal(self):
        subcmp_str = 'xxx'

        c1 = Component('CX_10')
        c2 = Component('CX_10')
        c1.cwe_1 = subcmp_str
        c2.cwe_1.value = subcmp_str
        # c2.cwe_1 = subcmp_str
        self.assertEqual(c1.to_er7(), c2.to_er7())
        #
        # s1 = Segment('PID')
        # s2 = Segment('PID')
        # s1.pid_4.pid_4_10_1.value = subcmp_str
        # s2.pid_4.pid_4_10_1 = subcmp_str
        # self.assertEqual(s1.to_er7(), s2.to_er7())
        # complex_cmp_str = 'xxx&yyy&zzz'
        # f1 = Field('PID_4')
        # f2 = Field('PID_4')
        # f1.cx_10.value = complex_cmp_str
        # f2.cx_10 = complex_cmp_str
        # self.assertEqual(f1.to_er7(), f2.to_er7())
        #
        # s1.pid_4.pid_4_1.value = complex_cmp_str
        # s2.pid_4.pid_4_1 = complex_cmp_str
        # self.assertEqual(f1.to_er7(), f2.to_er7())

    def test_add_child_to_subcomponent(self):
        a = SubComponent('HD_1')
        self.assertRaises(OperationNotAllowed, a.add, SubComponent('HD_2'))

    def test_create_subcomponent_by_get(self):
        p = Segment('PID')
        self.assertEqual(p.pid_5.pid_5_1.fn_1.name, 'FN_1')

    def test_create_base_datatype_subcomponent_by_get(self):
        f = Field('STF_2')
        f.stf_2_10 = 'subcomponent'

        #p = Segment('PID')
        #p.pid_3.cx_4.hd_1.value = 'value'
        #p.pid_3.cx_4.hd_1 = 'value' #this raises exception

    def create_unknown_subcomponent_by_get(self):
        f = Field('STF_2')
        with self.assertRaises(ChildNotFound):
            f.stf_2_10_100 = 'subcomponent'






if __name__ == '__main__':
    unittest.main()
