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

from hl7apy.parser import parse_message, parse_segments, parse_segment, parse_fields, parse_field, parse_components, parse_component, parse_subcomponent, parse_subcomponents
from hl7apy.validation import VALIDATION_LEVEL
from hl7apy.exceptions import ParserError, OperationNotAllowed, InvalidEncodingChars, InvalidName

class TestParser(unittest.TestCase):

    def _get_multiple_segments_groups_message(self):

        msg_o33 = 'MSH|^~\&|SENDING APP|SENDING FAC|REC APP|REC FAC|20110708162817||OML^O33^OML_O33|978226056138290600|D|2.5|||||USA||EN\r' \
                  'PID|||1010110909194822^^^GATEWAY_IL&1.3.6.1.4.1.21367.2011.2.5.17&ISO^PK||PIPPO^PLUTO^^^^^L||19790515|M|||VIA DI TOPOLINO^CAGLIARI^CAGLIARI^^09100^100^H^^092009^^~^^^^^^L^^^|||||||PPPPPP79E15B354I^^^CF|||||CAGLIARI|||100|||||||||||\r' \
                  'PV1||O|||||||||||||||||1107080001^^^LIS\r' \
                  'SPM|1|100187400201^||SPECIMEN^Blood|||||||PSN^Human Patient||||||20110708162817||20110708162817|||||||1|CONTAINER^CONTAINER DESC\r' \
                  'ORC|NW|83428|83428|18740|SC||||20110708162817||||||||^\r' \
                  'TQ1|||||||||R\r' \
                  'OBR||83428|83428|TPO^ANTI THYROPEROXIDASE ANTIBODIES(TPO)^^TPO||||||||||||ND^UNKNOWN^UNKNOWN\r' \
                  'SPM|2|100187400101^||SPECIMEN^Blood|||||||PSN^Human Patient||||||20110708162817||20110708162817|||||||1|CONTAINER^CONTAINER DESC\r' \
                  'ORC|NW|83425|83425|18740|SC||||20110708162817||||||||^\r' \
                  'TQ1|||||||||R\r' \
                  'OBR||83425|83425|CA^S-CALCIUM^^CA||||||||||||ND^UNKNOWN^UNKNOWN\r' \
                  'ORC|NW|83426|83426|18740|SC||||20110708162817||||||||^\r' \
                  'TQ1|||||||||R\r' \
                  'OBR||83426|83426|HDL^HDL CHOLESTEROL^^HDL||||||||||||ND^UNKNOWN^UNKNOWN\r' \
                  'ORC|NW|83427|83427|18740|SC||||20110708162817||||||||^\r' \
                  'TQ1|||||||||R\r' \
                  'OBR||83427|83427|LDL^LDL CHOLESTEROL^^LDL||||||||||||ND^UNKNOWN^UNKNOWN\r'

        return msg_o33

    def _get_invalid_encoding_chars(self):
        return {'COMPONENT' : '$',
                'SUBCOMPONENT' : '@',
                'REPETITION' : 'r',
                'ESCAPE' : '@'}

    def _get_custom_encoding_chars(self):
        return {'SEGMENT' : '\r',
                'FIELD' :  '@',
                'COMPONENT' : '$',
                'SUBCOMPONENT' : '%',
                'REPETITION' : '*',
                'ESCAPE' : '\\'}

    def test_parse_message_ignoring_groups(self):
        msh = 'MSH|^~\&|SENDING APP|SENDING FAC|REC APP|REC FAC|20080115153000||ADT^A01^ADT_A01|0123456789|P|2.5||||AL\r'
        evn = 'EVN||20080115153000||AAA|AAA|20080114003000\r'
        pid = 'PID|1||123-456-789^^^HOSPITAL^MR||SURNAME^NAME^A|||M|||1111 SOMEWHERE STREET^^SOMEWHERE^^^USA||555-555-2004~444-333-222|||M\r'
        nk1 = 'NK1|1|WOMAN^WIFE|SPO|1111 SOMEWHERE STREET^^SOMEWHERE^^^USA\r'
        pv1 = 'PV1|1|I|PATIENT WARD|U||||^REFERRING^DOCTOR^^MD|^CONSULTING^DOCTOR|CAR||||2|A0|||||||||||||||||||||||||||||2013\r'
        in1 = 'IN1|1|INSURANCE PLAN ID^PLAN DESC|COMPANY ID|INSURANCE COMPANY, INC.|5555 INSURERS STREET^^SOMEWHERE^^^USA||||||||||||||||||||||||||||||||||||||||||||555-44-3333'

        str_message = msh+evn+pid+nk1+pv1+in1
        message = parse_message(str_message, find_groups=False)

        self.assertEqual(message.children[0].name, 'MSH')
        self.assertEqual(message.children[1].name, 'EVN')
        self.assertEqual(message.children[2].name, 'PID')
        self.assertEqual(message.children[3].name, 'NK1')
        self.assertEqual(message.children[4].name, 'PV1')
        self.assertEqual(message.children[5].name, 'IN1')
        self.assertEqual(message.pid.pid_5.pid_5_1.fn_1.to_er7(), 'SURNAME')
        self.assertEqual(message.evn.evn_5.xcn_1.to_er7(), message.evn.evn_5.evn_5_1.to_er7())
        m_string = message.to_er7()
        self.assertEqual(m_string, str_message)

    def test_parse_message_create_groups(self):
        msg = self._get_multiple_segments_groups_message()
        message = parse_message(msg)
        self.assertEqual(message.children[0].name, 'MSH')
        self.assertEqual(message.children[1].name, 'OML_O33_PATIENT')
        self.assertEqual(message.children[2].name, 'OML_O33_SPECIMEN')
        self.assertEqual(message.children[3].name, 'OML_O33_SPECIMEN')
        #the first specimen has only one order
        specimen_1 = message.children[2]
        self.assertEqual(specimen_1.children[0].name, 'SPM')
        self.assertEqual(specimen_1.children[1].name, 'OML_O33_ORDER')
        #the second specimen has three different orders, and the second and third are inside the ORDER PRIOR group
        specimen_2 = message.children[3]
        self.assertEqual(specimen_2.children[1].name, 'OML_O33_ORDER')
        spm_2_order =  specimen_2.children[1]
        self.assertEqual(spm_2_order.children[0].name, 'ORC')
        self.assertEqual(spm_2_order.children[1].name, 'OML_O33_TIMING')
        spm_2_obs_req = spm_2_order.oml_o33_observation_request
        self.assertEqual(spm_2_obs_req.children[0].name, 'OBR')
        self.assertEqual(spm_2_obs_req.children[1].name, 'OML_O33_PRIOR_RESULT')

    def test_message_inspection_by_group_parsing(self):
        msg = self._get_multiple_segments_groups_message()
        message = parse_message(msg)
        #access first spm_27_1: P2_S1
        self.assertEqual(message.oml_o33_specimen[0].spm.spm_27.spm_27_1.to_er7(), 'CONTAINER')
        #by datatype name instead that by position it is the same than previous one
        self.assertEqual(message.oml_o33_specimen[0].spm.spm_27.cwe_1.to_er7(), 'CONTAINER')
        #access to the second order test belonging to the second specimen
        self.assertEqual(message.oml_o33_specimen[
                             1].oml_o33_order.oml_o33_observation_request.oml_o33_prior_result.oml_o33_order_prior[
                             1].obr.obr_4.obr_4_1.to_er7(), 'HDL')
        #try to access to non-existent field
        # with self.assertRaises(IndexError): # IndexError cannot be raised here to maintain lazy instantiation of children during traversal
        #     message.oml_o33_specimen[1].oml_o33_order.oml_o33_observation_request.oml_o33_prior_result.oml_o33_order_prior[2].obr.obr_4.obr_4_1.to_er7()
        #self.assertEqual(message.to_er7(), msg)


    def test_parse_message_with_repetition_segments_and_groups(self):
        msg = self._get_multiple_segments_groups_message()
        parse_message(msg)

    def test_parse_invalid_message(self):
        msh = 'PID|^~\&|SENDING APP|SENDING FAC|REC APP|REC FAC|20080115153000||ADT^A01^ADT_A01|0123456789|P|2.6||||AL\r'
        pid = 'PID|1||123-456-789^^^HOSPITAL^MR||SURNAME^NAME^A|||M|||1111 SOMEWHERE STREET^^SOMEWHERE^^^USA||555-555-2004~444-333-222|||M'
        msg = msh  + pid
        self.assertRaises(ParserError, parse_message, msg)

    def test_parse_message_missing_encoding_chars_zero(self):
        a = 'MSH|||||||||||||||||||'
        self.assertRaises(InvalidEncodingChars, parse_message, a)
        self.assertRaises(InvalidEncodingChars, parse_message, a, validation_level=VALIDATION_LEVEL.STRICT)

    def test_parse_message_missing_encoding_chars(self):
        a = 'MSH|@%\|||||||||'
        self.assertRaises(InvalidEncodingChars, parse_message, a)
        self.assertRaises(InvalidEncodingChars, parse_message, a, validation_level=VALIDATION_LEVEL.STRICT)

    def test_parse_message_too_many_encoding_chars(self):
        a = 'MSH|@%\&$?!|||||||||'
        self.assertRaises(InvalidEncodingChars, parse_message, a)
        self.assertRaises(InvalidEncodingChars, parse_message, a, validation_level=VALIDATION_LEVEL.STRICT)

    def test_parse_unknown_message_strict(self):
        message = 'MSH|^~\&|SENDING APP|SENDING FAC|REC APP|REC FAC|20080115153000||ADT^A01^ADT_A01|0123456789|P|2.6||||AL\r'
        parse_message(message, validation_level=VALIDATION_LEVEL.STRICT)
        message = 'MSH|^~\&|SENDING APP|SENDING FAC|REC APP|REC FAC|20080115153000|||0123456789|P|2.6||||AL\r'
        self.assertRaises(OperationNotAllowed, parse_message, message, validation_level=VALIDATION_LEVEL.STRICT)

    def test_parse_message_duplicate_encoding_chars(self):
        message = 'MSH|^&&^|SENDING APP|SENDING FAC|REC APP|REC FAC|20080115153000||ADT^A01^ADT_A01|0123456789|P|2.6||||AL\r'
        self.assertRaises(InvalidEncodingChars, parse_message, message)
        self.assertRaises(InvalidEncodingChars, parse_message, message, validation_level=VALIDATION_LEVEL.STRICT)

    def test_parse_message_missing_structure(self):
        msh = 'MSH|^~\&|SENDING APP|SENDING FAC|REC APP|REC FAC|20080115153000|||0123456789|P|2.6||||AL\r'
        pid = 'PID|1||123-456-789^^^HOSPITAL^MR||SURNAME^NAME^A|||M|||1111 SOMEWHERE STREET^^SOMEWHERE^^^USA||555-555-2004~444-333-222|||M\r'
        msg = msh+pid
        parse_message(msg)

    def test_parse_message_missing_structure_strict(self):
        msh = 'MSH|^~\&|SENDING APP|SENDING FAC|REC APP|REC FAC|20080115153000|||0123456789|P|2.6||||AL\r'
        pid = 'PID|1||123-456-789^^^HOSPITAL^MR||SURNAME^NAME^A|||M|||1111 SOMEWHERE STREET^^SOMEWHERE^^^USA||555-555-2004~444-333-222|||M\r'
        msg = msh+pid
        self.assertRaises(OperationNotAllowed, parse_message, msg, validation_level=VALIDATION_LEVEL.STRICT)

    def test_parse_message_incomplete_structure(self):
        m = parse_message('MSH|^~\&|SENDING APP|SENDING FAC|REC APP|REC FAC|20080115153000||ADT^|')

    def test_parse_message_missing_version(self):
        m = parse_message('MSH|^~\&|SENDING APP|SENDING FAC|REC APP|REC FAC|20080115153000||ADT^A01^ADT_A01||')


    def test_parse_segments(self):
        msh = 'MSH|^~\&|SENDING APP|SENDING FAC|REC APP|REC FAC|20080115153000||ADT^A01^ADT_A01|0123456789|P|2.5||||AL\r'
        pid = 'PID|1||123-456-789^^^HOSPITAL^MR||SURNAME^NAME^A|||M|||1111 SOMEWHERE STREET^^SOMEWHERE^^^USA||555-555-2004~444-333-222|||M'

        segments_str = msh+pid
        segments = parse_segments(segments_str)
        self.assertEqual(msh.replace('\r',''), segments[0].to_er7())
        self.assertEqual(pid, segments[1].to_er7())

    def test_parse_segment(self):
        segment = 'PV1|1|I|PATIENT WARD|U||||^REFERRING^DOCTOR|^CONSULTING^DOCTOR|CAR||||2|A0|||||||||||||||||||||||||||||2008'
        pv1 = parse_segment(segment)
        self.assertEqual(pv1.name, 'PV1')
        self.assertEqual(pv1.pv1_2.to_er7(), 'I')

    def test_parse_segment_invalid_encoding_chars(self):
        segment = 'EVN@@20080115153000@@@@20080114003000\r'
        self.assertRaises(InvalidEncodingChars, parse_segment, segment, encoding_chars=self._get_invalid_encoding_chars())
        self.assertRaises(InvalidEncodingChars, parse_segment, segment, encoding_chars=self._get_invalid_encoding_chars(),
                          validation_level=VALIDATION_LEVEL.STRICT)

    def test_parse_segment_custom_encoding_chars(self):
        segment = 'PV1@1@I@PATIENT WARD@U@@@@$REFERRING$DOCTOR$$MD@$CONSULTING$DOCTOR$P@CAR@@@@2@A0@@@@@@@@'
        s = parse_segment(segment, encoding_chars=self._get_custom_encoding_chars())
        self.assertEqual(s.pv1_3.to_er7(), 'PATIENT WARD')
        self.assertEqual(s.pv1_8.pv1_8_2.to_er7(), 'REFERRING')

    def test_parse_segment_all_values_null(self):
        segment = 'PID|||||||||||'
        s = parse_segment(segment)
        self.assertEqual(len(s.children), 0)
        s.pid_2.to_er7()
        s.pid_23.to_er7()
        self.assertEqual(len(s.children), 0)
        s.pid_23 = ''
        self.assertEqual(s.to_er7(), 'PID|||||||||||||||||||||||')

    def test_parse_segment_containing_multiple_instances_field(self):
        segment = 'QPD|||@PID.3.1^aaaa~@PID.8^F'
        s = parse_segment(segment)
        self.assertEqual(len(s.qpd_3), 2)
        #check single PID_3 instances
        self.assertEqual(s.qpd_3[0].qpd_3_1.to_er7(), '@PID.3.1' )
        self.assertEqual(s.qpd_3[0].qpd_3_2.to_er7(), 'aaaa')
        self.assertEqual(s.qpd_3[1].qpd_3_1.to_er7(), '@PID.8' )
        self.assertEqual(s.qpd_3[1].qpd_3_2.to_er7(), 'F')

    def test_parse_fields(self):
        #note: this method seems not to work without segment definition, and also for MSH segment
        field = 'PID|xxx|yyy^zz'
        fields = parse_fields(field)
        for field in fields:
            self.assertEqual(field.classname, 'Field')
        self.assertEqual(fields[0].to_er7(), 'PID')
        self.assertEqual(fields[1].to_er7(), 'xxx')

    def test_parse_fields_multiple_instances(self):
        field = '||@PID.3.1^aaaa^~@PID.8^F'
        f = parse_fields(field, name_prefix='PID')
        self.assertEqual(len(f), 2) #only the valued field is recognized
        self.assertEqual(f[0].cx_1.to_er7(), '@PID.3.1')

    def test_parse_null_fields(self):
        fields = 'PID|||'
        f = parse_fields(fields)
        self.assertEqual(len(f), 4)

    def test_parse_fields_invalid_encoding_chars(self):
        fields = 'PID|xxx|yyy^zz'
        self.assertRaises(InvalidEncodingChars, parse_fields, fields, encoding_chars=self._get_invalid_encoding_chars())
        self.assertRaises(InvalidEncodingChars, parse_fields, fields, encoding_chars=self._get_invalid_encoding_chars(),
                          validation_level=VALIDATION_LEVEL.STRICT)

    def test_parse_fields_custom_encoding_chars(self):
        fields = 'xxx@yyy$zz'
        f = parse_fields(fields, encoding_chars=self._get_custom_encoding_chars())
        self.assertEqual(f[0].to_er7(encoding_chars=self._get_custom_encoding_chars()), 'xxx')
        self.assertEqual(f[1].children[0].to_er7(), 'yyy')

    def test_parse_field(self):
        field = 'xxx^yyy^zzz'
        f = parse_field(field) #exception thrown here

    def test_parse_field_invalid_encoding_chars(self):
        field = 'xxx^yyy^zzz'
        self.assertRaises(InvalidEncodingChars, parse_field, field, encoding_chars=self._get_invalid_encoding_chars())
        self.assertRaises(InvalidEncodingChars, parse_field, field, encoding_chars=self._get_invalid_encoding_chars(),
                          validation_level=VALIDATION_LEVEL.STRICT)

    def test_parse_field_custom_encoding_chars(self):
        field = 'aaa$bbb$ccc'
        f = parse_field(field, encoding_chars=self._get_custom_encoding_chars())
        self.assertEqual(len(f.children), 3)
        self.assertEqual(f.children[0].to_er7(), 'aaa')
        self.assertEqual(f.children[1].to_er7(), 'bbb')
        self.assertEqual(f.children[2].to_er7(), 'ccc')

        field = 'aaa^bbb^ccc'
        to_string_field = 'aaa\\S\\bbb\\S\\ccc'
        f =  parse_field(field, encoding_chars=self._get_custom_encoding_chars())
        self.assertEqual(len(f.children), 1)
        self.assertEqual(f.children[0].to_er7(), to_string_field)
        self.assertEqual(f.children[0].to_er7(encoding_chars=self._get_custom_encoding_chars()), field)

    def test_parse_invalid_name_field(self):
        f = parse_field('xxx',name='yyy')
        self.assertIsNone(f.name)

    def test_parse_components(self):
        components = 'aaa^bbb'
        c = parse_components(components)
        self.assertEqual(c[0].to_er7(), 'aaa')
        self.assertEqual(c[1].to_er7(), 'bbb')
        components = '^comp^'
        c = parse_components(components)
        self.assertEqual(len(c), 3)
        self.assertEqual(c[0].to_er7(), '')
        self.assertEqual(c[1].to_er7(), 'comp')
        self.assertEqual(c[2].to_er7(), '')

    def test_parse_components_invalid_encoding_chars(self):
        components = 'aaa^bbb'
        self.assertRaises(InvalidEncodingChars, parse_components, components, encoding_chars=self._get_invalid_encoding_chars())
        self.assertRaises(InvalidEncodingChars, parse_components, components, encoding_chars=self._get_invalid_encoding_chars(),
                          validation_level=VALIDATION_LEVEL.STRICT)

    def test_parse_component(self):
        component = 'comp'
        c = parse_component(component)
        self.assertEqual(c.to_er7(), 'comp')
        component = '^comp^'
        c = parse_component(component)
        self.assertEqual(c.to_er7(), '\\S\\comp\\S\\')
        component = 'comp1&comp2'
        c = parse_component(component)
        self.assertEqual(c.to_er7(), 'comp1&comp2')
        self.assertEqual(c.children[0].to_er7(), 'comp1')
        self.assertEqual(c.children[1].to_er7(), 'comp2')

    def test_parse_component_invalid_encoding_chars(self):
        component = 'comp'
        self.assertRaises(InvalidEncodingChars, parse_component, component, encoding_chars=self._get_invalid_encoding_chars())
        self.assertRaises(InvalidEncodingChars, parse_component, component, encoding_chars=self._get_invalid_encoding_chars(),
                          validation_level=VALIDATION_LEVEL.STRICT)

    def test_parse_invalid_name_component_strict(self):
        self.assertRaises(InvalidName, parse_component, 'xxx', 'XXX', validation_level=VALIDATION_LEVEL.STRICT)

    def test_parse_subcomponents(self):
        subcomponent = 'subcomp'
        s = parse_subcomponents(subcomponent)
        self.assertEqual(s[0].to_er7(), 'subcomp')
        subcomponent = '&subcomp&'
        s = parse_subcomponents(subcomponent)
        self.assertEqual(s[0].to_er7(), '')
        self.assertEqual(s[1].to_er7(), 'subcomp')
        self.assertEqual(s[2].to_er7(), '')

    def test_parse_subcomponents_invalid_encoding_chars(self):
        subcomponents = 'sub1&subcomp&sub2'
        self.assertRaises(InvalidEncodingChars, parse_subcomponents, subcomponents,
                          encoding_chars=self._get_invalid_encoding_chars())
        self.assertRaises(InvalidEncodingChars, parse_subcomponents, subcomponents,
                          encoding_chars=self._get_invalid_encoding_chars(), validation_level=VALIDATION_LEVEL.STRICT)


if __name__ == '__main__':
    unittest.main()



