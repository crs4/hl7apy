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
import re
import sys
import tempfile
import unittest

import hl7apy
from hl7apy.core import Group, Field, Component, SubComponent
from hl7apy.exceptions import ValidationError
from hl7apy.parser import parse_message, parse_segments, parse_segment, parse_field
from hl7apy.validation import VALIDATION_LEVEL


class TestValidation(unittest.TestCase):

    def setUp(self):
        hl7apy.set_default_validation_level(VALIDATION_LEVEL.TOLERANT)
        self.adt_a01 = \
            'MSH|^~\\&|SENDING APP|SENDING FAC|REC APP|REC FAC|20130101101500||ADT^A01^ADT_A01|0123456789|P|2.6||||AL\r' \
            'EVN||20130101101500||01|AAA|20130101082500\r' \
            'PID|1||123-456-789^^^HOSPITAL^MR||SURNAME^NAME^A|||M|||1111 SOMEWHERE STREET^^SOMEWHERE^^^USA|||||M\r' \
            'NK1|1|WOMAN^WIFE|SPO|1111 SOMEWHERE STREET^^SOMEWHERE^^^USA\r' \
            'PV1|1|I|PATIENT WARD|U||||^REFERRING^DOCTOR^^MD|^CONSULTING^DOCTOR|CAR||||2|A0|||||||||||||||||||||||||||||2013\r' \
            'IN1|1|INSURANCE PLAN ID^PLAN DESC|COMPANY ID|INSURANCE COMPANY, INC.|5555 INSURERS STREET^^SOMEWHERE^^^USA||||||||||||||||||||||||||||||||||||||||||||555-44-3333\r'

        self.zdt_z01 = \
            'MSH|^~\\&|SENDING APP|SENDING FAC|REC APP|REC FAC|20130101101500||ZDT^Z01^ZDT_Z01|0123456789|P|2.5||||AL\r' \
            'EVN||20130101101500||AAA|AAA|20130101082500\r' \
            'PID|1||123-456-789^^^HOSPITAL^MR||SURNAME^NAME^A|||M|||1111 SOMEWHERE STREET^^SOMEWHERE^^^USA||555-555-2004~444-333-222|||M\r' \
            'NK1|1|WOMAN^WIFE|SPO|1111 SOMEWHERE STREET^^SOMEWHERE^^^USA\r' \
            'PV1|1|I|PATIENT WARD|U||||^REFERRING^DOCTOR^^MD|^CONSULTING^DOCTOR|CAR||||2|A0|||||||||||||||||||||||||||||2013\r' \
            'IN1|1|INSURANCE PLAN ID^PLAN DESC|COMPANY ID|INSURANCE COMPANY, INC.|5555 INSURERS STREET^^SOMEWHERE^^^USA||||||||||||||||||||||||||||||||||||||||||||555-44-3333\r'

        self.oml_o33 = \
            'MSH|^~\\&|SENDING APP|SENDING FAC|REC APP|REC FAC|20110708162817||OML^O33^OML_O33|978226056138290600|D|2.5|||||USA||EN\r' \
            'PID|||1010110909194822^^^GATEWAY_IL&1.3.6.1.4.1.21367.2011.2.5.17&ISO^PK||PIPPO^PLUTO^^^^^L||19790515|M|||VIA DI TOPOLINO^CAGLIARI^CAGLIARI^^09100^100^H^^092009^^~^^^^^^L^^^|||||||PPPPPP79E15B354I^^^CF|||||CAGLIARI|||100|||||||||||\r' \
            'PV1||O|||||||||||||||||1107080001^^^LIS\r' \
            'SPM|1|100187400201^||BLDV|||||||B||||||20110708162817||20110708162817|||||||1|CONTAINER^CONTAINER DESC\r' \
            'ORC|NW|83428|83428|18740|SC||||20110708162817||||||||^\r' \
            'TQ1|||||||||R\r' \
            'OBR||83428|83428|TPO^ANTI THYROPEROXIDASE ANTIBODIES(TPO)^^TPO||||||||||||ND^UNKNOWN^UNKNOWN\r'

        self.oml_o33_2 = \
            'MSH|^~\\&|SENDING APP|SENDING FAC|REC APP|REC FAC|20110708162817||OML^O33^OML_O33|978226056138290600|D|2.5|||||USA||EN\r' \
            'PID|||1010110909194822^^^GATEWAY_IL&1.3.6.1.4.1.21367.2011.2.5.17&ISO^PK||PIPPO^PLUTO^^^^^L||19790515|M|||VIA DI TOPOLINO^CAGLIARI^CAGLIARI^^09100^100^H^^092009^^~^^^^^^L^^^|||||||PPPPPP79E15B354I^^^CF|||||CAGLIARI|||100|||||||||||\r' \
            'PV1||O|||||||||||||||||1107080001^^^LIS\r' \
            'SPM|1|100187400201^||BLDV|||||||PSN^Human Patient||||||20110708162817||20110708162817|||||||1|CONTAINER^CONTAINER DESC\r' \
            'ORC|NW|83428|83428|18740|SC||||20110708162817||||||||^\r' \
            'TQ1|||||||||R\r' \
            'OBR||83428|83428|TPO^ANTI THYROPEROXIDASE ANTIBODIES(TPO)^^TPO||||||||||||ND^UNKNOWN^UNKNOWN\r' \
            'SPM|2|100187400101^||BLDV|||||||PSN^Human Patient||||||20110708162817||20110708162817|||||||1|CONTAINER^CONTAINER DESC\r' \
            'ORC|NW|83425|83425|18740|SC||||20110708162817||||||||^\r' \
            'TQ1|||||||||R\r' \
            'OBR||83425|83425|CA^S-CALCIUM^^CA||||||||||||ND^UNKNOWN^UNKNOWN\r' \
            'ORC|NW|83426|83426|18740|SC||||20110708162817||||||||^\r' \
            'TQ1|||||||||R\r' \
            'OBR||83426|83426|HDL^HDL CHOLESTEROL^^HDL||||||||||||ND^UNKNOWN^UNKNOWN\r' \
            'ORC|NW|83427|83427|18740|SC||||20110708162817||||||||^\r' \
            'TQ1|||||||||R\r' \
            'OBR||83427|83427|LDL^LDL CHOLESTEROL^^LDL||||||||||||ND^UNKNOWN^UNKNOWN\r'

        report_file = tempfile.NamedTemporaryFile()
        self.report_file = report_file.name

    def _create_message(self, msg_str):
        return parse_message(msg_str)

    def _test_report_file(self, error_type):

        with open(self.report_file, 'r') as f:
            s = f.read()
        if error_type == 'ERROR':
            regex = r'Error:.*'
        elif error_type == 'WARNING':
            regex = r'Warning:.*'

        self.assertTrue(re.search(regex, s))

        os.remove(self.report_file)

    def test_well_structured_message(self):
        """
        Tests that a valid message is validated
        """
        for msg_str in (self.adt_a01, self.oml_o33):
            msg = self._create_message(msg_str)
            self.assertTrue(msg.validate())

    # def test_oml_o33_2_message(self):
    #     # This test is failing because the oml_o33_2 parsing creates a
    #     # OML_O33_ORDER_PRIOR which expect a OBR segment, but the parser's
    #     # implementation puts the OBR segment in the group OML_O33_OBSERVATION_REQUEST
    #     # This behaviour HL7 fault
    #     msg = self._create_message(self.oml_o33_2)
    #     self.assertTrue(msg.validate())

    def test_unknown_message(self):
        msg = self._create_message(self.adt_a01)
        msg.name = None
        self.assertRaises(ValidationError, msg.validate, report_file=self.report_file)
        self._test_report_file('ERROR')

    def test_missing_required_group(self):
        """
        Test that if a required group is not present the messase in not validated
        The message misses the oml_o33_specimen group
        """
        msg = self._create_message(self.oml_o33)
        del msg.oml_o33_specimen
        self.assertRaises(ValidationError, msg.validate, report_file=self.report_file)
        self._test_report_file('ERROR')

    def test_missing_required_segment(self):
        """
        Tests that when a required segment is missing the message is not validated
        The message used misses the EVN segment
        """
        msg = self._create_message(self.adt_a01)
        del msg.evn
        self.assertRaises(ValidationError, msg.validate, report_file=self.report_file)
        self._test_report_file('ERROR')

    def test_missing_required_field(self):
        """
        Tests that when a required field is missing the message is not validated
        The message used misses the msh_9 segment
        """
        msg = self._create_message(self.adt_a01)
        del msg.msh.msh_9
        self.assertRaises(ValidationError, msg.validate, report_file=self.report_file)
        self._test_report_file('ERROR')

    def test_missing_required_component(self):
        """
        Tests that when a required component is missing the message is not validated
        The message used misses the msg_1 component in the msh_9 field
        """
        msg = self._create_message(self.adt_a01)
        del msg.msh.msh_9.msg_1
        self.assertRaises(ValidationError, msg.validate, report_file=self.report_file)
        self._test_report_file('ERROR')

    def test_missing_required_subcomponent(self):
        """
        Tests that when a required subcomponent is missing the message is not validated
        The message used misses the cwe_1 subcomponent in the cx_10 component
        """
        msg = self._create_message(self.oml_o33)
        msg.pid.pid_3.cx_10 = 'xxx&yyy&zzz&&&&&&&'
        del msg.pid.pid_3.cx_10.cwe_1
        self.assertRaises(ValidationError, msg.validate, report_file=self.report_file)
        self._test_report_file('ERROR')

    def test_having_more_groups(self):
        """
        Tests that when a group occurs more than the allowed times the message is not validated
        The message used has 2 occurrence of oml_o33_group
        """
        msg = self._create_message(self.oml_o33)
        oml_o33_patient = Group('OML_O33_PATIENT')
        segments = parse_segments(
            'PID|||1010110909194822^^^GATEWAY_IL&1.3.6.1.4.1.21367.2011.2.5.17&ISO^PK||PIPPO^PLUTO^^^^^L||19790515|M|||VIA DI TOPOLINO^CAGLIARI^CAGLIARI^^09100^100^H^^092009~^^^^^^L|||||||PPPPPP79E15B354I^^^CF|||||CAGLIARI|||100\rPV1||O|||||||||||||||||1107080001^^^LIS')
        oml_o33_patient.children = segments
        msg.add(oml_o33_patient)
        self.assertRaises(ValidationError, msg.validate, report_file=self.report_file)
        self._test_report_file('ERROR')

    def test_having_more_segments(self):
        """
        Tests that when a segment occurs more than the allowed times the message is not validated
        The message used has 2 occurrence of the segment evn
        """
        msg = self._create_message(self.adt_a01)
        evn = parse_segment('EVN||20080115153000||AAA|AAA|20080114003000', version='2.6')
        msg.add(evn)
        self.assertRaises(ValidationError, msg.validate, report_file=self.report_file)
        self._test_report_file('ERROR')

    def test_having_more_fields(self):
        """
        Tests that when a field occurs more than the allowed times the message is not validated
        The message used has 2 occurrence of msh_9
        """
        msg = self._create_message(self.adt_a01)
        msh_9 = parse_field('RSP^SLI^RSP_K11', 'MSH_9', version="2.6")
        msg.msh.add(msh_9)
        self.assertRaises(ValidationError, msg.validate, report_file=self.report_file)
        self._test_report_file('ERROR')

    def test_wrong_datatype_field(self):
        """
        Tests that if a field is not of the correct datatype the message is not validate
        The message used has the MSH_9 of type ST
        """
        msg = self._create_message(self.adt_a01)
        msh_9 = Field('MSH_9', datatype='ST', version='2.6')
        msh_9.msh_9_1 = 'ADT_A01'
        msg.msh.msh_9 = msh_9
        self.assertRaises(ValidationError, msg.validate, report_file=self.report_file)
        self._test_report_file('ERROR')

    def test_wrong_datatype_component(self):
        """
        Tests that if a component is not of the correct datatype the message is not validate
        The message used has the MSG_1 of type ST
        """
        msg = self._create_message(self.adt_a01)
        msg_1 = Component('MSG_1', datatype='ST', version='2.6')
        msg_1.add(SubComponent(datatype='ST', value='ADT_A01', version='2.6'))
        msg.msh.msh_9.msg_1 = msg_1
        self.assertRaises(ValidationError, msg.validate, report_file=self.report_file)
        self._test_report_file('ERROR')

    def test_wrong_datatype_subcomponent(self):
        """
        Tests that if a component is not of the correct datatype the message is not validated
        The message used has the CWE_1 of type NM
        """
        msg = self._create_message(self.adt_a01)
        cwe_1 = SubComponent('CWE_1', datatype='NM', value='1', version='2.6')
        msg.pid.pid_3.cx_10.cwe_1 = cwe_1
        self.assertRaises(ValidationError, msg.validate, report_file=self.report_file)
        self._test_report_file('ERROR')

    def test_wrong_segment(self):
        """
        Tests that if there is an unexpected segment the message in not validated
        The message used has an unexpected SPM
        """
        msg = self._create_message(self.adt_a01)
        spm = parse_segment('SPM|1|100187400201^||SPECIMEN^Blood|||||||PSN^Human Patient||||||20110708162817||'
                            '20110708162817|||||||1|CONTAINER^CONTAINER DESC\r', version='2.6')
        msg.add(spm)
        self.assertRaises(ValidationError, msg.validate, report_file=self.report_file)
        self._test_report_file('ERROR')

    def test_wrong_group(self):
        """
        Tests that if there is an unexpected segment the message in not validated
        The message used has an unexpected OML_O33_PATIENT
        """
        msg = self._create_message(self.adt_a01)
        oml_o33_patient = Group('OML_O33_PATIENT', version='2.6')
        segments = parse_segments('PID|||1010110909194822^^^GATEWAY_IL&1.3.6.1.4.1.21367.2011.2.5.17&ISO^PK||'
                                  'PIPPO^PLUTO^^^^^L||19790515|M|||VIA DI TOPOLINO^CAGLIARI^CAGLIARI^^09100^100^'
                                  'H^^092009~^^^^^^L|||||||PPPPPP79E15B354I^^^CF|||||CAGLIARI|||100\rPV1||O|||||||||'
                                  '||||||||1107080001^^^LIS', version='2.6')
        oml_o33_patient.children = segments
        msg.add(oml_o33_patient)
        self.assertRaises(ValidationError, msg.validate, report_file=self.report_file)
        self._test_report_file('ERROR')

    def test_wrong_field(self):
        """
        Tests that if there is an unexpected field the message in not validated
        The message used has an unexpected unknown field in the pid
        """
        msg = self._create_message(self.adt_a01)
        unkn_field = Field(version='2.6')
        msg.pid.add(unkn_field)
        self.assertRaises(ValidationError, msg.validate, report_file=self.report_file)
        self._test_report_file('ERROR')

    def test_wrong_component(self):
        """
        Tests that if there is an unexpected component the message in not validated
        The message used has an unexpected unknown component in the msh_9
        """
        msg = self._create_message(self.adt_a01)
        unkn_component = Component(version='2.6')
        msg.msh.msh_9.add(unkn_component)
        self.assertRaises(ValidationError, msg.validate, report_file=self.report_file)
        self._test_report_file('ERROR')

    def test_wrong_subcomponent(self):
        """
        Tests that if there is an unexpected subcomponent the message in not validated
        The message used has an unexpected unknown subcomponent in the cx_10
        """
        msg = self._create_message(self.adt_a01)
        unkn_subcomponent = SubComponent(datatype='ST', version='2.6')
        msg.pid.pid_3.cx_10 = Component('CX_10', version='2.6')
        msg.pid.pid_3.cx_10.add(unkn_subcomponent)
        self.assertRaises(ValidationError, msg.validate, report_file=self.report_file)
        self._test_report_file('ERROR')

    def test_wrong_value_table(self):
        """
        Tests that if a value doesn't belong to the table specified in HL7 structures, it writes a warning in
        the report file
        """
        msg = self._create_message(self.adt_a01)
        msg.msh.msh_15 = 'AB'  # AB is not one of the value in the msh_15 table (HL70155)
        self.assertTrue(msg.validate(report_file=self.report_file))
        self._test_report_file('WARNING')

    # def test_too_long_value(self):
    # TODO: reinsert this test after adding the length control of base datatype
    #     """
    #     Tests that if a value exceeds the maximum length, it writes a warning in the report file
    #     """
    #     msg = self._create_message(self.adt_a01)
    #     msg.pid.pid_1 = '12345'  # PID 1 is an SI field, which has maximum length of 4
    #     self.assertTrue(msg.validate(report_file=self.report_file))
    #     self._test_report_file('WARNING')

    def test_z_message(self):
        """
        Tests that a Z Message is validated, no matter what segments it has
        """
        msg = self._create_message(self.zdt_z01)
        self.assertTrue(msg.validate())

    def test_z_segment(self):
        """
        Tests that, after adding a Z segment to a valid message, the message is still valid
        """
        msg = self._create_message(self.adt_a01)
        msg.add_segment('zin')
        msg.zin = 'ZIN|aa|bb|cc|'
        zin_4 = Field('ZIN_4', datatype='CWE', version='2.6')
        zin_4.value = 'dd'
        msg.zin.zin_4 = zin_4
        self.assertTrue(msg.validate())

    def test_wrong_z_segment(self):
        """
        Tests that, if the Z segment doesn't follow HL7 rules, the message is not validated
        """
        msg = self._create_message(self.adt_a01)
        msg.add_segment('zin')
        msg.zin = 'ZIN|aa|bb|cc|'
        # CX_1 is mandatory
        zin_4 = Field('ZIN_4', datatype='CX', version='2.6')
        zin_4.value = '^12'
        msg.zin.add(zin_4)
        self.assertRaises(ValidationError, msg.validate, report_file=self.report_file)

        del msg.zin.zin_4

        # Z segment with unknown fields are not validated
        msg.zin.add(Field(version="2.6"))
        self.assertRaises(ValidationError, msg.validate, report_file=self.report_file)
        self._test_report_file('ERROR')

    def test_z_field(self):
        f = Field('zin_1')
        self.assertTrue(f.validate())

    def test_wrong_z_field(self):
        """
        Tests that Fields of None datatype are not validated
        """
        f = Field('zin_1')
        f.value = 'aa^bb'
        self.assertRaises(ValidationError, f.validate, report_file=self.report_file)
        self._test_report_file('ERROR')

    def test_wd_type_field(self):
        """
        Tests that, in strict mode, a wd field is not present
        """
        # The EV1 message is of type WD
        s = 'EVN|EV1|20080115153000||AAA|AAA|20080114003000'
        parsed_s = parse_segment(s, version='2.7')
        self.assertRaises(ValidationError, parsed_s.validate)


class TestMessageProfile(unittest.TestCase):

    def setUp(self):
        self.rsp_k21 = \
            'MSH|^~\\&|SENDING APP|SENDING FAC|RECEIVING APP|RECEIVING FAC|20140410170011||RSP^K22^RSP_K21|11111111|P|2.5\r' \
            'MSA|AA|20140410170015\r' \
            'QAK|222222222|OK\r' \
            'QPD|IHE PDQ Query|222222222|@PID.3.1.1^3333333|||||^^^IHEFACILITY&1.3.6.1.4.1.21367.3000.1.6&ISO^|\r' \
            'PID|1||10101109091948^^^GATEWAY&1.3.6.1.4.1.21367.2011.2.5.17&ISO||JOHN^SMITH^^^^^A||19690113|M|||VIA DELLE VIE^^CAGLIARI^^^ITA^H^^092009||||||||||||CAGLIARI|||\r'

        base_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(base_path, 'profiles/iti_21')
        self.rsp_k21_mp = hl7apy.load_message_profile(path)

        report_file = tempfile.NamedTemporaryFile()
        self.report_file = report_file.name

    def _create_message(self, msg_str):
        return parse_message(msg_str, message_profile=self.rsp_k21_mp)

    def _test_report_file(self, error_type, present=True):

        with open(self.report_file, 'r') as f:
            s = f.read()
        if error_type == 'ERROR':
            regex = r'Error:.*'
        elif error_type == 'WARNING':
            regex = r'Warning:.*'
        else:
            return

        if sys.version_info == '2':
            if present:
                self.assertTrue(re.search(regex, s))
            else:
                self.assertFalse(re.search(regex, s))

        os.remove(self.report_file)

    def test_well_structured_message(self):
        """
        Tests that a valid message is validated
        """
        m = self._create_message(self.rsp_k21)
        self.assertTrue(m.validate())

    # def test_oml_o33_2_message(self):
    #     # This test is failing because the oml_o33_2 parsing creates a
    #     # OML_O33_ORDER_PRIOR which expect a OBR segment, but the parser's
    #     # implementation puts the OBR segment in the group OML_O33_OBSERVATION_REQUEST
    #     # This behaviour HL7 fault
    #     msg = self._create_message(self.oml_o33_2)
    #     self.assertTrue(msg.validate())

    # def test_missing_required_group(self):
    #     """
    #     Test that if a required group is not present the messase in not validated
    #     The message misses the oml_o33_specimen group
    #     """
    #     msg = self._create_message(self.rsp_k21)
    #     del msg.oml_o33_specimen
    #     self.assertRaises(ValidationError, msg.validate, report_file=self.report_file)
    #     self._test_report_file('ERROR')

    def test_missing_required_segment(self):
        """
        Tests that when a required segment is missing the message is not validated
        The message used misses the EVN segment
        """
        msg = self._create_message(self.rsp_k21)
        del msg.qak
        self.assertRaises(ValidationError, msg.validate, report_file=self.report_file)
        self._test_report_file('ERROR')

    def test_missing_required_field(self):
        """
        Tests that when a required field is missing the message is not validated
        The message used misses the msh_9 segment
        """
        msg = self._create_message(self.rsp_k21)
        del msg.qak.qak_1
        self.assertRaises(ValidationError, msg.validate, report_file=self.report_file)
        self._test_report_file('ERROR')

    def test_missing_required_component(self):
        """
        Tests that when a required component is missing the message is not validated
        The message used misses the msg_1 component in the msh_9 field
        """
        msg = self._create_message(self.rsp_k21)
        del msg.qpd.qpd_8.cx_4
        self.assertRaises(ValidationError, msg.validate, report_file=self.report_file)
        self._test_report_file('ERROR')

    def test_missing_required_subcomponent(self):
        """
        Tests that when a required subcomponent is missing the message is not validated
        The message used misses the cwe_1 subcomponent in the cx_10 component
        """
        msg = self._create_message(self.rsp_k21)
        msg.pid.pid_2.cx_4 = '&yyy&zzz'  # it misses the required cwe_1
        # del msg.pid.pid_3.cx_10.cwe_1
        self.assertRaises(ValidationError, msg.validate, report_file=self.report_file)
        self._test_report_file('ERROR')

    # def test_having_more_groups(self):
    #     """
    #     Tests that when a group occurs more than the allowed times the message is not validated
    #     The message used has 2 occurrence of oml_o33_group
    #     """
    #     msg = self._create_message(self.oml_o33)
    #     oml_o33_patient = Group('OML_O33_PATIENT')
    #     segments = parse_segments('PID|||1010110909194822^^^GATEWAY_IL&1.3.6.1.4.1.21367.2011.2.5.17&ISO^PK||PIPPO^PLUTO^^^^^L||19790515|M|||VIA DI TOPOLINO^CAGLIARI^CAGLIARI^^09100^100^H^^092009~^^^^^^L|||||||PPPPPP79E15B354I^^^CF|||||CAGLIARI|||100\rPV1||O|||||||||||||||||1107080001^^^LIS')
    #     oml_o33_patient.children = segments
    #     msg.add(oml_o33_patient)
    #     self.assertRaises(ValidationError, msg.validate, report_file=self.report_file)
    #     self._test_report_file('ERROR')

    def test_having_more_segments(self):
        """
        Tests that when a segment occurs more than the allowed times the message is not validated
        The message used has 2 occurrence of the segment evn
        """
        msg = self._create_message(self.rsp_k21)
        msg.add_segment('qak')
        msg.qak[1] = 'QAK|222222222|OK'
        self.assertRaises(ValidationError, msg.validate, report_file=self.report_file)
        self._test_report_file('ERROR')

    def test_having_more_fields(self):
        """
        Tests that when a field occurs more than the allowed times the message is not validated
        The message used has 2 occurrence of msh_9
        """
        msg = self._create_message(self.rsp_k21)
        msg.msh.add_field('msh_9')
        self.assertRaises(ValidationError, msg.validate, report_file=self.report_file)
        self._test_report_file('ERROR')

    def test_wrong_datatype_field(self):
        """
        Tests that if a field is not of the correct datatype the message is not validate
        The message used has the MSH_9 of type ST
        """
        msg = self._create_message(self.rsp_k21)
        msh_9 = Field('MSH_9', datatype='ST')
        msh_9.msh_9_1 = 'RSP_K21'
        msg.msh.msh_9 = msh_9
        self.assertRaises(ValidationError, msg.validate, report_file=self.report_file)
        self._test_report_file('ERROR')

    def test_wrong_datatype_component(self):
        """
        Tests that if a component is not of the correct datatype the message is not validate
        The message used has the MSG_1 of type ST
        """
        msg = self._create_message(self.rsp_k21)
        msg_1 = Component('MSG_1', datatype='ST')
        msg_1.add(SubComponent(datatype='ST', value='ADT_A01'))
        msg.msh.msh_9.msg_1 = msg_1
        self.assertRaises(ValidationError, msg.validate, report_file=self.report_file)
        self._test_report_file('ERROR')

    def test_wrong_datatype_subcomponent(self):
        """
        Tests that if a component is not of the correct datatype the message is not validated
        The message used has the CWE_1 of type NM
        """
        msg = self._create_message(self.rsp_k21)
        cwe_1 = SubComponent('CWE_1', datatype='NM', value='1')
        msg.pid.pid_3.cx_10.cwe_1 = cwe_1
        self.assertRaises(ValidationError, msg.validate, report_file=self.report_file)
        self._test_report_file('ERROR')

    def test_wrong_segment(self):
        """
        Tests that if there is an unexpected segment the message in not validated
        The message used has an unexpected SPM
        """
        msg = self._create_message(self.rsp_k21)
        spm = parse_segment(
            'SPM|1|100187400201^||SPECIMEN^Blood|||||||PSN^Human Patient||||||20110708162817||20110708162817|||||||1|CONTAINER^CONTAINER DESC\r')
        msg.add(spm)
        self.assertRaises(ValidationError, msg.validate, report_file=self.report_file)
        self._test_report_file('ERROR')

    def test_wrong_group(self):
        """
        Tests that if there is an unexpected segment the message in not validated
        The message used has an unexpected OML_O33_PATIENT
        """
        msg = self._create_message(self.rsp_k21)
        oml_o33_patient = Group('OML_O33_PATIENT')
        segments = parse_segments(
            'PID|||1010110909194822^^^GATEWAY_IL&1.3.6.1.4.1.21367.2011.2.5.17&ISO^PK||PIPPO^PLUTO^^^^^L||19790515|M|||VIA DI TOPOLINO^CAGLIARI^CAGLIARI^^09100^100^H^^092009~^^^^^^L|||||||PPPPPP79E15B354I^^^CF|||||CAGLIARI|||100\rPV1||O|||||||||||||||||1107080001^^^LIS')
        oml_o33_patient.children = segments
        msg.add(oml_o33_patient)
        self.assertRaises(ValidationError, msg.validate, report_file=self.report_file)
        self._test_report_file('ERROR')

    def test_wrong_field(self):
        """
        Tests that if there is an unexpected field the message in not validated
        The message used has an unexpected unknown field in the pid
        """
        msg = self._create_message(self.rsp_k21)
        unkn_field = Field()
        msg.rsp_k21_query_response.pid.add(unkn_field)
        self.assertRaises(ValidationError, msg.validate, report_file=self.report_file)
        self._test_report_file('ERROR')

    def test_wrong_component(self):
        """
        Tests that if there is an unexpected component the message in not validated
        The message used has an unexpected unknown component in the msh_9
        """
        msg = self._create_message(self.rsp_k21)
        unkn_component = Component()
        msg.msh.msh_9.add(unkn_component)
        self.assertRaises(ValidationError, msg.validate, report_file=self.report_file)
        self._test_report_file('ERROR')

    def test_wrong_subcomponent(self):
        """
        Tests that if there is an unexpected subcomponent the message in not validated
        The message used has an unexpected unknown subcomponent in the cx_10
        """
        msg = self._create_message(self.rsp_k21)
        unkn_subcomponent = SubComponent(datatype='ST')
        msg.rsp_k21_query_response.pid.pid_3.cx_10 = Component('CX_10')
        msg.rsp_k21_query_response.pid.pid_3.cx_10.add(unkn_subcomponent)
        self.assertRaises(ValidationError, msg.validate, report_file=self.report_file)
        self._test_report_file('ERROR')

    def test_wrong_value_table(self):
        """
        Tests that if a value doesn't belong to the table specified in HL7 structures, it writes a warning in
        the report file
        """
        msg = self._create_message(self.rsp_k21)
        msg.msh.msh_15 = 'AB'  # AB is not one of the value in the msh_15 table (HL70155)
        self.assertTrue(msg.validate(report_file=self.report_file))
        self._test_report_file('WARNING')

    def test_too_long_value(self):
        """
        Tests that if a value exceeds the maximum length, it writes a warning in the report file
        """
        msg = self._create_message(self.rsp_k21)
        msg.rsp_k21_query_response.pid.pid_1 = '12345'  # PID 1 is an SI field, which has maximum length of 4
        self.assertTrue(msg.validate(report_file=self.report_file))
        self._test_report_file('WARNING')

    def test_z_segment(self):
        """
        Tests that, after adding a Z segment to a valid message, the message is still valid
        """
        msg = self._create_message(self.rsp_k21)
        msg.add_segment('zin')
        msg.zin = 'ZIN|aa|bb|cc|'
        zin_4 = Field('ZIN_4', datatype='CWE')
        zin_4.value = 'dd'
        msg.zin.zin_4 = zin_4
        self.assertTrue(msg.validate())


if __name__ == '__main__':
    unittest.main()
