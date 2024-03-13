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
import os
import unittest

import hl7apy
from hl7apy.parser import parse_message, parse_segments, parse_segment, parse_fields, parse_field, \
    parse_components, parse_component, parse_subcomponents, get_message_type
from hl7apy.validation import VALIDATION_LEVEL
from hl7apy.exceptions import ParserError, OperationNotAllowed, InvalidEncodingChars, InvalidName, \
    ValidationError, MaxChildLimitReached


class TestParser(unittest.TestCase):

    def setUp(self):
        self.rsp_k21 = \
            'MSH|^~\\&|SEND APP|SEND FAC|REC APP|REC FAC|20110708163514||RSP^K22^RSP_K21|1234|D|2.5|||||ITA||EN\r' \
            'MSA|AA|26775702551812240|\r' \
            'QAK|111069|OK||1|1|0\r' \
            'QPD|IHE PDQ Query|111069|@PID.3.1^1010110909194822~@PID.5.1^SMITH||||\r' \
            'PID|1||10101^^^GATEWAY&1.3.6.1.4.1.21367.2011.2.5.17&ISO||JOHN^SMITH^^^^^A||19690113|M|||VIA DELLE VIE^^CAGLIARI^^^100^H^^092009||||||||||||CAGLIARI|||||\r'

        # it misses some PID.3 components
        self.invalid_rsp_k21 = \
            'MSH|^~\\&|SEND APP|SEND FAC|REC APP|REC FAC|20110708163514||RSP^K22^RSP_K21|1234|D|2.5|||||ITA||EN\r' \
            'MSA|AA|26775702551812240|\r' \
            'QAK|111069|OK||1|1|0\r' \
            'QPD|IHE PDQ Query|111069|@PID.3.1^1010110909194822~@PID.5.1^SMITH||||\r' \
            'PID|1||10101^^^||JOHN^SMITH^^^^^A||19690113|M|||VIA DELLE VIE^^CAGLIARI^^^100^H^^092009|||||||||||||||||\r'

        self.rsp_k21_27 = \
            'MSH|^~\\&#|SEND APP|SEND FAC|REC APP|REC FAC|20110708163514||RSP^K22^RSP_K21|1234|D|2.7|||||ITA||EN\r' \
            'MSA|AA|26775702551812240\r' \
            'QAK|111069|OK||1|1|0\r' \
            'QPD|IHE PDQ Query|111069|@PID.3.1^1010110909194822~@PID.5.1^SMITH\r' \
            'PID|1||10101^^^GATEWAY&1.3.6.1.4.1.21367.2011.2.5.17&ISO||JOHN^SMITH^^^^^A||19690113|M|||VIA DELLE VIE^^CAGLIARI^^^100^H^^092009||||||||||||CAGLIARI'

        self.rsp_k21_27_no_truncation = \
            'MSH|^~\\&|SEND APP|SEND FAC|REC APP|REC FAC|20110708163514||RSP^K22^RSP_K21|1234|D|2.7|||||ITA||EN\r' \
            'MSA|AA|26775702551812240\r' \
            'QAK|111069|OK||1|1|0\r' \
            'QPD|IHE PDQ Query|111069|@PID.3.1^1010110909194822~@PID.5.1^SMITH\r' \
            'PID|1||10101^^^GATEWAY&1.3.6.1.4.1.21367.2011.2.5.17&ISO||JOHN^SMITH^^^^^A||19690113|M|||VIA DELLE VIE^^CAGLIARI^^^100^H^^092009||||||||||||CAGLIARI'

        base_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(base_path, 'profiles/iti_21')
        self.rsp_k21_mp = hl7apy.load_message_profile(path)

    def _get_multiple_segments_groups_message(self):

        msg_o33 = \
            'MSH|^~\\&|SEND APP|SEND FAC|REC APP|REC FAC|20110708162817||OML^O33^OML_O33|978226056138290600|D|2.5|||||USA||EN\r' \
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
        return {'COMPONENT': '$',
                'SUBCOMPONENT': '@',
                'REPETITION': 'r',
                'ESCAPE': '@'}

    def _get_custom_encoding_chars(self):
        return {'SEGMENT': '\r',
                'FIELD': '@',
                'COMPONENT': '$',
                'SUBCOMPONENT': '%',
                'REPETITION': '*',
                'ESCAPE': '\\'}

    def test_parse_message_ignoring_groups(self):
        msh = 'MSH|^~\\&|SEND APP|SEND FAC|REC APP|REC FAC|20080115153000||ADT^A01^ADT_A01|0123456789|P|2.5||||AL\r'
        evn = 'EVN||20080115153000||AAA|AAA|20080114003000\r'
        pid = 'PID|1||123-456-789^^^HOSPITAL^MR||SURNAME^NAME^A|||M|||1111 SOMEWHERE^^SOMEWHERE^^^USA||555~444|||M\r'
        nk1 = 'NK1|1|WOMAN^WIFE|SPO|1111 SOMEWHERE^^SOMEWHERE^^^USA\r'
        pv1 = 'PV1|1|I|PATIENT WARD|U||||^REFER^DOCTOR^^MD|^CONSUL^DOC|CAR||||2|A0|||||||||||||||||||||||||||||2013\r'
        in1 = 'IN1|1|INSURANCE PLAN ID^PLAN DESC|COMPANY ID|INS CNY, INC.|5555 INSURERS STREET^^SOMEWHERE^^^USA'

        str_message = msh + evn + pid + nk1 + pv1 + in1
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
        # the first specimen has only one order
        specimen_1 = message.children[2]
        self.assertEqual(specimen_1.children[0].name, 'SPM')
        self.assertEqual(specimen_1.children[1].name, 'OML_O33_ORDER')
        # the second specimen has three different orders, and the second and third are inside the ORDER PRIOR group
        specimen_2 = message.children[3]
        self.assertEqual(specimen_2.children[1].name, 'OML_O33_ORDER')
        spm_2_order = specimen_2.children[1]
        self.assertEqual(spm_2_order.children[0].name, 'ORC')
        self.assertEqual(spm_2_order.children[1].name, 'OML_O33_TIMING')
        spm_2_obs_req = spm_2_order.oml_o33_observation_request
        self.assertEqual(spm_2_obs_req.children[0].name, 'OBR')
        self.assertEqual(spm_2_obs_req.children[1].name, 'OML_O33_PRIOR_RESULT')

    def test_message_inspection_by_group_parsing(self):
        msg = self._get_multiple_segments_groups_message()
        message = parse_message(msg)
        # access first spm_27_1: P2_S1
        self.assertEqual(message.oml_o33_specimen[0].spm.spm_27.spm_27_1.to_er7(), 'CONTAINER')
        # by datatype name instead that by position it is the same than previous one
        self.assertEqual(message.oml_o33_specimen[0].spm.spm_27.cwe_1.to_er7(), 'CONTAINER')
        # access to the second order test belonging to the second specimen
        self.assertEqual(message.oml_o33_specimen[1].oml_o33_order.
                         oml_o33_observation_request.oml_o33_prior_result.
                         oml_o33_order_prior.obr.obr_4.obr_4_1.to_er7(), 'HDL')
        self.assertEqual(message.oml_o33_specimen[1].oml_o33_order.
                         oml_o33_observation_request.oml_o33_prior_result.
                         oml_o33_order_prior[1].obr.obr_4.obr_4_1.to_er7(), 'LDL')
        # try to access to non-existent field
        # IndexError cannot be raised here to maintain lazy instantiation of children during traversal
        # with self.assertRaises(IndexError):
        #     message.oml_o33_specimen[1].oml_o33_order.oml_o33_observation_request.\
        #         oml_o33_prior_result.oml_o33_order_prior[2].obr.obr_4.obr_4_1.to_er7()
        # self.assertEqual(message.to_er7(), msg)

    def test_parse_message_with_repetition_segments_and_groups(self):
        msg = self._get_multiple_segments_groups_message()
        parse_message(msg)

    def test_parse_invalid_message(self):
        msh = 'PID|^~\\&|SEND APP|SEND FAC|REC APP|REC FAC|20080115153000||ADT^A01^ADT_A01|0123456789|P|2.6||||AL\r'
        pid = 'PID|1||123-456-789^^^HOSPITAL^MR||SURNAME^NAME^A|||M|||1111 SOMEWHERE^^SOMEWHERE^^^USA||555~444|||M'
        msg = msh + pid
        self.assertRaises(ParserError, parse_message, msg)

    def test_parse_message_missing_encoding_chars_zero(self):
        m = 'MSH|||||||||||||||||||'
        self.assertRaises(InvalidEncodingChars, parse_message, m)
        self.assertRaises(InvalidEncodingChars, parse_message, m, validation_level=VALIDATION_LEVEL.STRICT)
        m = 'MSH|^~\\||||||||||2.7'
        self.assertRaises(InvalidEncodingChars, parse_message, m)
        self.assertRaises(InvalidEncodingChars, parse_message, m, validation_level=VALIDATION_LEVEL.STRICT)

    def test_parse_message_missing_encoding_chars(self):
        m = 'MSH|@%\\|||||||||'
        self.assertRaises(InvalidEncodingChars, parse_message, m)
        self.assertRaises(InvalidEncodingChars, parse_message, m, validation_level=VALIDATION_LEVEL.STRICT)
        m = 'MSH|^~\\||||||||||2.7'
        self.assertRaises(InvalidEncodingChars, parse_message, m)
        self.assertRaises(InvalidEncodingChars, parse_message, m, validation_level=VALIDATION_LEVEL.STRICT)

    def test_parse_message_too_many_encoding_chars(self):
        m = 'MSH|@%\\&$?!|||||||||'
        self.assertRaises(InvalidEncodingChars, parse_message, m)
        self.assertRaises(InvalidEncodingChars, parse_message, m, validation_level=VALIDATION_LEVEL.STRICT)
        m = 'MSH|^~\\&#$||||||||||2.7'
        self.assertRaises(InvalidEncodingChars, parse_message, m)
        self.assertRaises(InvalidEncodingChars, parse_message, m, validation_level=VALIDATION_LEVEL.STRICT)

    def test_parse_unknown_message_strict(self):
        m = 'MSH|^~\\&|SEND APP|SEND FAC|REC APP|REC FAC|20080115153000||ADT^A01^ADT_A01|0123456789|P|2.6||||AL\r'
        self.assertRaises(ValidationError, parse_message, m,
                          validation_level=VALIDATION_LEVEL.STRICT, force_validation=True)
        m = 'MSH|^~\\&|SEND APP|SEND FAC|REC APP|REC FAC|20080115153000|||0123456789|P|2.6||||AL\r'
        self.assertRaises(OperationNotAllowed, parse_message, m, validation_level=VALIDATION_LEVEL.STRICT)

    def test_parse_message_duplicate_encoding_chars(self):
        m = 'MSH|^&&^|SEND APP|SEND FAC|REC APP|REC FAC|20080115153000||ADT^A01^ADT_A01|0123456789|P|2.6||||AL\r'
        self.assertRaises(InvalidEncodingChars, parse_message, m)
        self.assertRaises(InvalidEncodingChars, parse_message, m, validation_level=VALIDATION_LEVEL.STRICT)
        m = 'MSH|^&&^##|SEND APP|SEND FAC|REC APP|REC FAC|20080115153000||ADT^A01^ADT_A01|0123456789|P|2.7||||AL\r'
        self.assertRaises(InvalidEncodingChars, parse_message, m)
        self.assertRaises(InvalidEncodingChars, parse_message, m, validation_level=VALIDATION_LEVEL.STRICT)

    def test_parse_message_missing_structure(self):
        msh = 'MSH|^~\\&|SEND APP|SEND FAC|REC APP|REC FAC|20080115153000|||0123456789|P|2.6||||AL\r'
        pid = 'PID|1||123-456-789^^^HOSPITAL^MR||SURNAME^NAME^A|||M|||1111 SOMEWHERE^^SOMEWHERE^^^USA||555~444|||M\r'
        msg = msh + pid
        parse_message(msg)

    def test_parse_message_missing_structure_strict(self):
        msh = 'MSH|^~\\&|SEND APP|SEND FAC|REC APP|REC FAC|20080115153000|||0123456789|P|2.6||||AL\r'
        pid = 'PID|1||123-456-789^^^HOSPITAL^MR||SURNAME^NAME^A|||M|||1111 SOMEWHERE^^SOMEWHERE^^^USA||555~444|||M\r'
        msg = msh + pid
        self.assertRaises(OperationNotAllowed, parse_message, msg, validation_level=VALIDATION_LEVEL.STRICT)

    def test_parse_message_incomplete_structure(self):
        m = parse_message('MSH|^~\\&|SEND APP|SEND FAC|REC APP|REC FAC|20080115153000||ADT^|')

    def test_parse_message_missing_version(self):
        m = parse_message('MSH|^~\\&|SEND APP|SEND FAC|REC APP|REC FAC|20080115153000||ADT^A01^ADT_A01||')

    def test_parse_segments(self):
        msh = 'MSH|^~\\&|SEND APP|SEND FAC|REC APP|REC FAC|20080115153000||ADT^A01^ADT_A01|0123456789|P|2.5||||AL\r'
        pid = 'PID|1||123-456-789^^^HOSPITAL^MR||SURNAME^NAME^A|||M|||1111 SOMEWHERE^^SOMEWHERE^^^USA||555~444|||M'

        segments_str = msh + pid
        segments = parse_segments(segments_str)
        self.assertEqual(msh.replace('\r', ''), segments[0].to_er7())
        self.assertEqual(pid, segments[1].to_er7())

    def test_parse_segment(self):
        segment = 'PV1|1|I|PATIENT WARD|U||||^REFERRING^DOCTOR|^CONSULTING^DOCTOR|CAR||||2|A0|||||||||||||||||||||||||||||2008'
        pv1 = parse_segment(segment)
        self.assertEqual(pv1.name, 'PV1')
        self.assertEqual(pv1.pv1_2.to_er7(), 'I')

    def test_parse_segment_invalid_encoding_chars(self):
        segment = 'EVN@@20080115153000@@@@20080114003000\r'
        self.assertRaises(InvalidEncodingChars, parse_segment, segment,
                          encoding_chars=self._get_invalid_encoding_chars())
        self.assertRaises(InvalidEncodingChars, parse_segment, segment,
                          encoding_chars=self._get_invalid_encoding_chars(),
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
        # check single PID_3 instances
        self.assertEqual(s.qpd_3[0].qpd_3_1.to_er7(), '@PID.3.1')
        self.assertEqual(s.qpd_3[0].qpd_3_2.to_er7(), 'aaaa')
        self.assertEqual(s.qpd_3[1].qpd_3_1.to_er7(), '@PID.8')
        self.assertEqual(s.qpd_3[1].qpd_3_2.to_er7(), 'F')

    def test_parse_segment_ending_with_varies_field(self):
        segment = 'QPD|IHE PDQ Query|622e3df468654c2fb3e0ac35bfe3369e|xxxx|yyyyy||||zzzzz'
        s = parse_segment(segment)
        self.assertEqual(s.qpd_1.datatype, 'CE')
        self.assertEqual(s.qpd_2.datatype, 'ST')
        self.assertEqual(s.qpd_3.datatype, 'varies')
        self.assertEqual(s.qpd_4.datatype, 'varies')
        self.assertEqual(s.qpd_8.datatype, 'varies')

    def test_parse_segment_containing_varies_field(self):
        segment = 'OBX|1|ST|1^YYY||ABCDEFG|HJKLMN|||||O'
        s = parse_segment(segment)
        self.assertEqual(s.obx_5.datatype, 'varies')
        self.assertNotEqual(s.obx_6.datatype, 'varies')

    def test_parse_fields(self):
        # note: this method seems not to work without segment definition, and also for MSH segment
        field = 'PID|xxx|yyy^zz'
        fields = parse_fields(field)
        for field in fields:
            self.assertEqual(field.classname, 'Field')
        self.assertEqual(fields[0].to_er7(), 'PID')
        self.assertEqual(fields[1].to_er7(), 'xxx')

    def test_parse_fields_multiple_instances(self):
        field = '||@PID.3.1^aaaa^~@PID.8^F'
        f = parse_fields(field, name_prefix='PID')
        self.assertEqual(len(f), 2)  # only the valued field is recognized
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
        f = parse_field(field)  # exception thrown here

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
        f = parse_field(field, encoding_chars=self._get_custom_encoding_chars())
        self.assertEqual(len(f.children), 1)
        self.assertEqual(f.children[0].to_er7(), to_string_field)
        self.assertEqual(f.children[0].to_er7(encoding_chars=self._get_custom_encoding_chars()), field)

    def test_parse_invalid_name_field(self):
        f = parse_field('xxx', name='yyy')
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
        self.assertRaises(InvalidEncodingChars, parse_components, components,
                          encoding_chars=self._get_invalid_encoding_chars())
        self.assertRaises(InvalidEncodingChars, parse_components, components,
                          encoding_chars=self._get_invalid_encoding_chars(),
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

    def test_parse_component_with_datatype(self):
        c = parse_component('555-55-5555&PRIMARY&PATRICIA&6&&MD', datatype='CE', version='2.5.1')
        self.assertEqual(c.value, '555-55-5555&PRIMARY&PATRICIA&6&&MD')

    def test_parse_component_with_datatype_and_unknown_subcomponent(self):
        c = parse_component('555-55-5555&PRIMARY&PATRICIA P&6&&MD&UNKN', datatype='CE', version='2.5.1')
        self.assertEqual(c.value, '555-55-5555&PRIMARY&PATRICIA P&6&&MD&UNKN')

    def test_parse_component_invalid_encoding_chars(self):
        component = 'comp'
        self.assertRaises(InvalidEncodingChars, parse_component, component,
                          encoding_chars=self._get_invalid_encoding_chars())
        self.assertRaises(InvalidEncodingChars, parse_component, component,
                          encoding_chars=self._get_invalid_encoding_chars(),
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

    def test_message_profile(self):
        m = parse_message(self.rsp_k21, message_profile=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.TOLERANT)
        self.assertEqual(m.qpd.qpd_3.datatype, 'QIP')
        self.assertFalse(m.qpd.allow_infinite_children)

        m = parse_message(self.rsp_k21, message_profile=self.rsp_k21_mp, validation_level=VALIDATION_LEVEL.STRICT)
        self.assertEqual(m.qpd.qpd_3.datatype, 'QIP')
        self.assertFalse(m.qpd.allow_infinite_children)

    def test_message_profile_invalid_message(self):
        self.assertRaises(ValidationError, parse_message, self.invalid_rsp_k21, message_profile=self.rsp_k21_mp,
                          validation_level=VALIDATION_LEVEL.STRICT, force_validation=True)

    def test_get_message_type(self):
        msh = 'MSH|^~\\&|SEND APP|SEND FAC|REC APP|REC FAC|20080115153000||{}|0123456789|P|2.5||||AL\r'

        for mt in ('ADT^A01^ADT_A01', 'ADT^A01', '^^^', '^^ADT_A01'):
            self.assertEqual(get_message_type(msh.format(mt)), mt)

    def test_parse_version_27_message(self):
        m = parse_message(self.rsp_k21_27)
        self.assertEqual(m.msh.msh_2.to_er7(), '^~\\&#')
        self.assertEqual(m.encoding_chars['TRUNCATION'], '#')
        self.assertEqual(m.to_er7(), self.rsp_k21_27)

    def test_parse_version_27_message_no_truncation(self):
        m = parse_message(self.rsp_k21_27_no_truncation)
        self.assertEqual(m.msh.msh_2.to_er7(), '^~\\&')
        self.assertNotIn('TRUNCATION', m.encoding_chars)
        self.assertEqual(m.to_er7(), self.rsp_k21_27_no_truncation)

    def test_parse_wd_field(self):
        """
        Tests that, in strict mode, a wd field is not present
        """
        # The EV1 message is of type WD
        s = 'EVN|EV1|20080115153000||AAA|AAA|20080114003000'
        self.assertRaises(MaxChildLimitReached, parse_segment, s, version='2.7',
                          validation_level=VALIDATION_LEVEL.STRICT)
        parsed_s = parse_segment(s, version='2.7')
        self.assertEqual(parsed_s.to_er7(), s)

    def test_complex_datatype_depth(self):
        """
        Related to issue 56 in github, checks that the complex datatype chain has at most a depth of two.
        :return:
        """

        for version in hl7apy.SUPPORTED_LIBRARIES.values():
            module = importlib.import_module(version)
            for dts, strct in module.DATATYPES_STRUCTS.items():
                for dts_cmp in strct:
                    cmp_type, cmp_dts = dts_cmp[1][0], dts_cmp[1][1]
                    if cmp_type == 'sequence':
                        for sub_cmp in cmp_dts:
                            sub_cmp_type = sub_cmp[1][0]
                            self.assertEqual(sub_cmp_type, 'leaf')


if __name__ == '__main__':
    unittest.main()
