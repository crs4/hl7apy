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


from hl7apy.utils import iteritems
from .segments import SEGMENTS

GROUPS = {
    'ADT_A01_INSURANCE': (
        'sequence',
        (
            ['IN1', SEGMENTS['IN1'], (1, 1), 'SEG'],
            ['IN2', SEGMENTS['IN2'], (0, 1), 'SEG'],
            ['IN3', SEGMENTS['IN3'], (0, -1), 'SEG'],
            ['ROL', SEGMENTS['ROL'], (0, -1), 'SEG'],
            ['AUT', SEGMENTS['AUT'], (0, -1), 'SEG'],
            ['RF1', SEGMENTS['RF1'], (0, -1), 'SEG'],
        ),
    ),
    'ADT_A01_PROCEDURE': (
        'sequence',
        (
            ['PR1', SEGMENTS['PR1'], (1, 1), 'SEG'],
            ['ROL', SEGMENTS['ROL'], (0, -1), 'SEG'],
        ),
    ),
    'ADT_A03_INSURANCE': (
        'sequence',
        (
            ['IN1', SEGMENTS['IN1'], (1, 1), 'SEG'],
            ['IN2', SEGMENTS['IN2'], (0, 1), 'SEG'],
            ['IN3', SEGMENTS['IN3'], (0, -1), 'SEG'],
            ['ROL', SEGMENTS['ROL'], (0, -1), 'SEG'],
            ['AUT', SEGMENTS['AUT'], (0, -1), 'SEG'],
            ['RF1', SEGMENTS['RF1'], (0, -1), 'SEG'],
        ),
    ),
    'ADT_A03_PROCEDURE': (
        'sequence',
        (
            ['PR1', SEGMENTS['PR1'], (1, 1), 'SEG'],
            ['ROL', SEGMENTS['ROL'], (0, -1), 'SEG'],
        ),
    ),
    'ADT_A05_INSURANCE': (
        'sequence',
        (
            ['IN1', SEGMENTS['IN1'], (1, 1), 'SEG'],
            ['IN2', SEGMENTS['IN2'], (0, 1), 'SEG'],
            ['IN3', SEGMENTS['IN3'], (0, -1), 'SEG'],
            ['ROL', SEGMENTS['ROL'], (0, -1), 'SEG'],
            ['AUT', SEGMENTS['AUT'], (0, -1), 'SEG'],
            ['RF1', SEGMENTS['RF1'], (0, -1), 'SEG'],
        ),
    ),
    'ADT_A05_PROCEDURE': (
        'sequence',
        (
            ['PR1', SEGMENTS['PR1'], (1, 1), 'SEG'],
            ['ROL', SEGMENTS['ROL'], (0, -1), 'SEG'],
        ),
    ),
    'ADT_A06_INSURANCE': (
        'sequence',
        (
            ['IN1', SEGMENTS['IN1'], (1, 1), 'SEG'],
            ['IN2', SEGMENTS['IN2'], (0, 1), 'SEG'],
            ['IN3', SEGMENTS['IN3'], (0, -1), 'SEG'],
            ['ROL', SEGMENTS['ROL'], (0, -1), 'SEG'],
        ),
    ),
    'ADT_A06_PROCEDURE': (
        'sequence',
        (
            ['PR1', SEGMENTS['PR1'], (1, 1), 'SEG'],
            ['ROL', SEGMENTS['ROL'], (0, -1), 'SEG'],
        ),
    ),
    'ADT_A16_INSURANCE': (
        'sequence',
        (
            ['IN1', SEGMENTS['IN1'], (1, 1), 'SEG'],
            ['IN2', SEGMENTS['IN2'], (0, 1), 'SEG'],
            ['IN3', SEGMENTS['IN3'], (0, -1), 'SEG'],
            ['ROL', SEGMENTS['ROL'], (0, -1), 'SEG'],
            ['AUT', SEGMENTS['AUT'], (0, -1), 'SEG'],
            ['RF1', SEGMENTS['RF1'], (0, -1), 'SEG'],
        ),
    ),
    'ADT_A16_PROCEDURE': (
        'sequence',
        (
            ['PR1', SEGMENTS['PR1'], (1, 1), 'SEG'],
            ['ROL', SEGMENTS['ROL'], (0, -1), 'SEG'],
        ),
    ),
    'ADT_A39_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['MRG', SEGMENTS['MRG'], (1, 1), 'SEG'],
            ['PV1', SEGMENTS['PV1'], (0, 1), 'SEG'],
        ),
    ),
    'ADT_A43_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['MRG', SEGMENTS['MRG'], (1, 1), 'SEG'],
        ),
    ),
    'ADT_A44_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
            ['MRG', SEGMENTS['MRG'], (1, 1), 'SEG'],
        ),
    ),
    'ADT_A45_MERGE_INFO': (
        'sequence',
        (
            ['MRG', SEGMENTS['MRG'], (1, 1), 'SEG'],
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
        ),
    ),
    'ADT_A60_ADVERSE_REACTION_GROUP': (
        'sequence',
        (
            ['IAM', SEGMENTS['IAM'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['IAR', SEGMENTS['IAR'], (0, -1), 'SEG'],
        ),
    ),
    'ADT_A60_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
        ),
    ),
    'BAR_P01_INSURANCE': (
        'sequence',
        (
            ['IN1', SEGMENTS['IN1'], (1, 1), 'SEG'],
            ['IN2', SEGMENTS['IN2'], (0, 1), 'SEG'],
            ['IN3', SEGMENTS['IN3'], (0, -1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ROL', SEGMENTS['ROL'], (0, -1), 'SEG'],
        ),
    ),
    'BAR_P01_PROCEDURE': (
        'sequence',
        (
            ['PR1', SEGMENTS['PR1'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ROL', SEGMENTS['ROL'], (0, -1), 'SEG'],
        ),
    ),
    'BAR_P01_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (0, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ROL', SEGMENTS['ROL'], (0, -1), 'SEG'],
            ['DB1', SEGMENTS['DB1'], (0, -1), 'SEG'],
            ['OBX', SEGMENTS['OBX'], (0, -1), 'SEG'],
            ['AL1', SEGMENTS['AL1'], (0, -1), 'SEG'],
            ['DG1', SEGMENTS['DG1'], (0, -1), 'SEG'],
            ['DRG', SEGMENTS['DRG'], (0, 1), 'SEG'],
            ['BAR_P01_PROCEDURE', None, (0, -1), 'GRP'],
            ['GT1', SEGMENTS['GT1'], (0, -1), 'SEG'],
            ['NK1', SEGMENTS['NK1'], (0, -1), 'SEG'],
            ['BAR_P01_INSURANCE', None, (0, -1), 'GRP'],
            ['ACC', SEGMENTS['ACC'], (0, 1), 'SEG'],
            ['UB1', SEGMENTS['UB1'], (0, 1), 'SEG'],
            ['UB2', SEGMENTS['UB2'], (0, 1), 'SEG'],
        ),
    ),
    'BAR_P02_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['PV1', SEGMENTS['PV1'], (0, 1), 'SEG'],
            ['DB1', SEGMENTS['DB1'], (0, -1), 'SEG'],
        ),
    ),
    'BAR_P05_INSURANCE': (
        'sequence',
        (
            ['IN1', SEGMENTS['IN1'], (1, 1), 'SEG'],
            ['IN2', SEGMENTS['IN2'], (0, 1), 'SEG'],
            ['IN3', SEGMENTS['IN3'], (0, -1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ROL', SEGMENTS['ROL'], (0, -1), 'SEG'],
        ),
    ),
    'BAR_P05_PROCEDURE': (
        'sequence',
        (
            ['PR1', SEGMENTS['PR1'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ROL', SEGMENTS['ROL'], (0, -1), 'SEG'],
        ),
    ),
    'BAR_P05_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (0, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ROL', SEGMENTS['ROL'], (0, -1), 'SEG'],
            ['DB1', SEGMENTS['DB1'], (0, -1), 'SEG'],
            ['OBX', SEGMENTS['OBX'], (0, -1), 'SEG'],
            ['AL1', SEGMENTS['AL1'], (0, -1), 'SEG'],
            ['DG1', SEGMENTS['DG1'], (0, -1), 'SEG'],
            ['DRG', SEGMENTS['DRG'], (0, 1), 'SEG'],
            ['BAR_P05_PROCEDURE', None, (0, -1), 'GRP'],
            ['GT1', SEGMENTS['GT1'], (0, -1), 'SEG'],
            ['NK1', SEGMENTS['NK1'], (0, -1), 'SEG'],
            ['BAR_P05_INSURANCE', None, (0, -1), 'GRP'],
            ['ACC', SEGMENTS['ACC'], (0, 1), 'SEG'],
            ['UB1', SEGMENTS['UB1'], (0, 1), 'SEG'],
            ['UB2', SEGMENTS['UB2'], (0, 1), 'SEG'],
            ['ABS', SEGMENTS['ABS'], (0, 1), 'SEG'],
            ['BLC', SEGMENTS['BLC'], (0, -1), 'SEG'],
            ['RMI', SEGMENTS['RMI'], (0, 1), 'SEG'],
        ),
    ),
    'BAR_P06_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PV1', SEGMENTS['PV1'], (0, 1), 'SEG'],
        ),
    ),
    'BAR_P10_PROCEDURE': (
        'sequence',
        (
            ['PR1', SEGMENTS['PR1'], (1, 1), 'SEG'],
            ['GP2', SEGMENTS['GP2'], (0, 1), 'SEG'],
        ),
    ),
    'BAR_P12_PROCEDURE': (
        'sequence',
        (
            ['PR1', SEGMENTS['PR1'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ROL', SEGMENTS['ROL'], (0, -1), 'SEG'],
        ),
    ),
    'BPS_O29_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['BPS_O29_TIMING', None, (0, -1), 'GRP'],
            ['BPO', SEGMENTS['BPO'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['BPS_O29_PRODUCT', None, (0, -1), 'GRP'],
        ),
    ),
    'BPS_O29_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['BPS_O29_PATIENT_VISIT', None, (0, 1), 'GRP'],
        ),
    ),
    'BPS_O29_PATIENT_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'BPS_O29_PRODUCT': (
        'sequence',
        (
            ['BPX', SEGMENTS['BPX'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'BPS_O29_TIMING': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'BRP_O30_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['BRP_O30_TIMING', None, (0, -1), 'GRP'],
            ['BPO', SEGMENTS['BPO'], (0, 1), 'SEG'],
            ['BPX', SEGMENTS['BPX'], (0, -1), 'SEG'],
        ),
    ),
    'BRP_O30_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
            ['BRP_O30_ORDER', None, (0, -1), 'GRP'],
        ),
    ),
    'BRP_O30_RESPONSE': ('sequence', (['BRP_O30_PATIENT', None, (0, 1), 'GRP'],)),
    'BRP_O30_TIMING': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'BRT_O32_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['BRT_O32_TIMING', None, (0, -1), 'GRP'],
            ['BPO', SEGMENTS['BPO'], (0, 1), 'SEG'],
            ['BTX', SEGMENTS['BTX'], (0, -1), 'SEG'],
        ),
    ),
    'BRT_O32_RESPONSE': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (0, 1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
            ['BRT_O32_ORDER', None, (0, -1), 'GRP'],
        ),
    ),
    'BRT_O32_TIMING': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'BTS_O31_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['BTS_O31_TIMING', None, (0, -1), 'GRP'],
            ['BPO', SEGMENTS['BPO'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['BTS_O31_PRODUCT_STATUS', None, (0, -1), 'GRP'],
        ),
    ),
    'BTS_O31_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['BTS_O31_PATIENT_VISIT', None, (0, 1), 'GRP'],
        ),
    ),
    'BTS_O31_PATIENT_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'BTS_O31_PRODUCT_STATUS': (
        'sequence',
        (
            ['BTX', SEGMENTS['BTX'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'BTS_O31_TIMING': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'CCI_I22_APPOINTMENT_HISTORY': (
        'sequence',
        (
            ['SCH', SEGMENTS['SCH'], (1, 1), 'SEG'],
            ['CCI_I22_RESOURCES', None, (0, -1), 'GRP'],
        ),
    ),
    'CCI_I22_CLINICAL_HISTORY': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['CCI_I22_CLINICAL_HISTORY_DETAIL', None, (0, -1), 'GRP'],
            ['CCI_I22_ROLE_CLINICAL_HISTORY', None, (0, -1), 'GRP'],
            ['CTI', SEGMENTS['CTI'], (0, -1), 'SEG'],
        ),
    ),
    'CCI_I22_CLINICAL_HISTORY_DETAIL': (
        'sequence',
        (
            ['CCI_I22_CLINICAL_HISTORY_OBJECT', None, (1, 1), 'GRP'],
            ['CCI_I22_CLINICAL_HISTORY_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'CCI_I22_CLINICAL_HISTORY_OBJECT': (
        'choice',
        (
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['ODS', SEGMENTS['ODS'], (1, 1), 'SEG'],
            ['PR1', SEGMENTS['PR1'], (1, 1), 'SEG'],
            ['RF1', SEGMENTS['RF1'], (1, 1), 'SEG'],
            ['AL1', SEGMENTS['AL1'], (1, 1), 'SEG'],
            ['IAM', SEGMENTS['IAM'], (1, 1), 'SEG'],
            ['ACC', SEGMENTS['ACC'], (1, 1), 'SEG'],
            ['RMI', SEGMENTS['RMI'], (1, 1), 'SEG'],
            ['DB1', SEGMENTS['DB1'], (1, 1), 'SEG'],
            ['DG1', SEGMENTS['DG1'], (1, 1), 'SEG'],
            ['DRG', SEGMENTS['DRG'], (1, 1), 'SEG'],
            ['PDA', SEGMENTS['PDA'], (1, 1), 'SEG'],
        ),
    ),
    'CCI_I22_CLINICAL_HISTORY_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'CCI_I22_GOAL': (
        'sequence',
        (
            ['GOL', SEGMENTS['GOL'], (1, 1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
            ['CCI_I22_ROLE_GOAL', None, (0, -1), 'GRP'],
            ['CCI_I22_GOAL_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'CCI_I22_GOAL_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'CCI_I22_INSURANCE': (
        'sequence',
        (
            ['IN1', SEGMENTS['IN1'], (1, 1), 'SEG'],
            ['IN2', SEGMENTS['IN2'], (0, 1), 'SEG'],
            ['IN3', SEGMENTS['IN3'], (0, 1), 'SEG'],
        ),
    ),
    'CCI_I22_MEDICATION_ADMINISTRATION_DETAIL': (
        'sequence',
        (
            ['RXA', SEGMENTS['RXA'], (1, -1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (1, 1), 'SEG'],
            ['CCI_I22_MEDICATION_ADMINISTRATION_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'CCI_I22_MEDICATION_ADMINISTRATION_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'CCI_I22_MEDICATION_ENCODING_DETAIL': (
        'sequence',
        (
            ['RXE', SEGMENTS['RXE'], (1, 1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (1, -1), 'SEG'],
            ['RXC', SEGMENTS['RXC'], (0, -1), 'SEG'],
            ['CCI_I22_MEDICATION_ENCODING_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'CCI_I22_MEDICATION_ENCODING_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'CCI_I22_MEDICATION_HISTORY': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['CCI_I22_MEDICATION_ORDER_DETAIL', None, (0, 1), 'GRP'],
            ['CCI_I22_MEDICATION_ENCODING_DETAIL', None, (0, 1), 'GRP'],
            ['CCI_I22_MEDICATION_ADMINISTRATION_DETAIL', None, (0, -1), 'GRP'],
            ['CTI', SEGMENTS['CTI'], (0, -1), 'SEG'],
        ),
    ),
    'CCI_I22_MEDICATION_ORDER_DETAIL': (
        'sequence',
        (
            ['RXO', SEGMENTS['RXO'], (1, 1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (1, -1), 'SEG'],
            ['RXC', SEGMENTS['RXC'], (0, -1), 'SEG'],
            ['CCI_I22_MEDICATION_ORDER_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'CCI_I22_MEDICATION_ORDER_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'CCI_I22_PATHWAY': (
        'sequence',
        (
            ['PTH', SEGMENTS['PTH'], (1, 1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
            ['CCI_I22_ROLE_PATHWAY', None, (0, -1), 'GRP'],
            ['CCI_I22_PATHWAY_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'CCI_I22_PATHWAY_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'CCI_I22_PATIENT_VISITS': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
        ),
    ),
    'CCI_I22_PROBLEM': (
        'sequence',
        (
            ['PRB', SEGMENTS['PRB'], (1, 1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
            ['CCI_I22_ROLE_PROBLEM', None, (0, -1), 'GRP'],
            ['CCI_I22_PROBLEM_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'CCI_I22_PROBLEM_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'CCI_I22_RESOURCES': (
        'sequence',
        (
            ['RGS', SEGMENTS['RGS'], (1, 1), 'SEG'],
            ['CCI_I22_RESOURCE_DETAIL', None, (0, -1), 'GRP'],
        ),
    ),
    'CCI_I22_RESOURCE_DETAIL': (
        'sequence',
        (
            ['CCI_I22_RESOURCE_OBJECT', None, (1, 1), 'GRP'],
            ['CCI_I22_RESOURCE_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'CCI_I22_RESOURCE_OBJECT': (
        'choice',
        (
            ['AIS', SEGMENTS['AIS'], (1, 1), 'SEG'],
            ['AIG', SEGMENTS['AIG'], (1, 1), 'SEG'],
            ['AIL', SEGMENTS['AIL'], (1, 1), 'SEG'],
            ['AIP', SEGMENTS['AIP'], (1, 1), 'SEG'],
        ),
    ),
    'CCI_I22_RESOURCE_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'CCI_I22_ROLE_CLINICAL_HISTORY': (
        'sequence',
        (
            ['CCI_I22_ROLE_CLINICAL_HISTORY_OBJECT', None, (1, 1), 'GRP'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
        ),
    ),
    'CCI_I22_ROLE_CLINICAL_HISTORY_OBJECT': (
        'choice',
        (
            ['ROL', SEGMENTS['ROL'], (1, 1), 'SEG'],
            ['PRD', SEGMENTS['PRD'], (1, 1), 'SEG'],
        ),
    ),
    'CCI_I22_ROLE_GOAL': (
        'sequence',
        (
            ['CCI_I22_ROLE_GOAL_OBJECT', None, (1, 1), 'GRP'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
        ),
    ),
    'CCI_I22_ROLE_GOAL_OBJECT': (
        'choice',
        (
            ['ROL', SEGMENTS['ROL'], (1, 1), 'SEG'],
            ['PRD', SEGMENTS['PRD'], (1, 1), 'SEG'],
        ),
    ),
    'CCI_I22_ROLE_PATHWAY': (
        'sequence',
        (
            ['CCI_I22_ROLE_PATHWAY_OBJECT', None, (1, 1), 'GRP'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
        ),
    ),
    'CCI_I22_ROLE_PATHWAY_OBJECT': (
        'choice',
        (
            ['ROL', SEGMENTS['ROL'], (1, 1), 'SEG'],
            ['PRD', SEGMENTS['PRD'], (1, 1), 'SEG'],
        ),
    ),
    'CCI_I22_ROLE_PROBLEM': (
        'sequence',
        (
            ['CCI_I22_ROLE_PROBLEM_OBJECT', None, (1, 1), 'GRP'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
        ),
    ),
    'CCI_I22_ROLE_PROBLEM_OBJECT': (
        'choice',
        (
            ['ROL', SEGMENTS['ROL'], (1, 1), 'SEG'],
            ['PRD', SEGMENTS['PRD'], (1, 1), 'SEG'],
        ),
    ),
    'CCM_I21_APPOINTMENT_HISTORY': (
        'sequence',
        (
            ['SCH', SEGMENTS['SCH'], (1, 1), 'SEG'],
            ['CCM_I21_RESOURCES', None, (0, -1), 'GRP'],
        ),
    ),
    'CCM_I21_CLINICAL_HISTORY': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['CCM_I21_CLINICAL_HISTORY_DETAIL', None, (0, -1), 'GRP'],
            ['CCM_I21_ROLE_CLINICAL_HISTORY', None, (0, -1), 'GRP'],
            ['CTI', SEGMENTS['CTI'], (0, -1), 'SEG'],
        ),
    ),
    'CCM_I21_CLINICAL_HISTORY_DETAIL': (
        'sequence',
        (
            ['CCM_I21_CLINICAL_HISTORY_OBJECT', None, (1, 1), 'GRP'],
            ['CCM_I21_CLINICAL_HISTORY_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'CCM_I21_CLINICAL_HISTORY_OBJECT': (
        'choice',
        (
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['ODS', SEGMENTS['ODS'], (1, 1), 'SEG'],
            ['PR1', SEGMENTS['PR1'], (1, 1), 'SEG'],
            ['RF1', SEGMENTS['RF1'], (1, 1), 'SEG'],
            ['AL1', SEGMENTS['AL1'], (1, 1), 'SEG'],
            ['IAM', SEGMENTS['IAM'], (1, 1), 'SEG'],
            ['ACC', SEGMENTS['ACC'], (1, 1), 'SEG'],
            ['RMI', SEGMENTS['RMI'], (1, 1), 'SEG'],
            ['DB1', SEGMENTS['DB1'], (1, 1), 'SEG'],
            ['DG1', SEGMENTS['DG1'], (1, 1), 'SEG'],
            ['DRG', SEGMENTS['DRG'], (1, 1), 'SEG'],
            ['PDA', SEGMENTS['PDA'], (1, 1), 'SEG'],
        ),
    ),
    'CCM_I21_CLINICAL_HISTORY_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'CCM_I21_GOAL': (
        'sequence',
        (
            ['GOL', SEGMENTS['GOL'], (1, 1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
            ['CCM_I21_ROLE_GOAL', None, (0, -1), 'GRP'],
            ['CCM_I21_GOAL_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'CCM_I21_GOAL_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'CCM_I21_INSURANCE': (
        'sequence',
        (
            ['IN1', SEGMENTS['IN1'], (1, 1), 'SEG'],
            ['IN2', SEGMENTS['IN2'], (0, 1), 'SEG'],
            ['IN3', SEGMENTS['IN3'], (0, 1), 'SEG'],
        ),
    ),
    'CCM_I21_MEDICATION_ADMINISTRATION_DETAIL': (
        'sequence',
        (
            ['RXA', SEGMENTS['RXA'], (1, -1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (1, 1), 'SEG'],
            ['CCM_I21_MEDICATION_ADMINISTRATION_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'CCM_I21_MEDICATION_ADMINISTRATION_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'CCM_I21_MEDICATION_ENCODING_DETAIL': (
        'sequence',
        (
            ['RXE', SEGMENTS['RXE'], (1, 1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (1, -1), 'SEG'],
            ['RXC', SEGMENTS['RXC'], (0, -1), 'SEG'],
            ['CCM_I21_MEDICATION_ENCODING_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'CCM_I21_MEDICATION_ENCODING_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'CCM_I21_MEDICATION_HISTORY': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['CCM_I21_MEDICATION_ORDER_DETAIL', None, (0, 1), 'GRP'],
            ['CCM_I21_MEDICATION_ENCODING_DETAIL', None, (0, 1), 'GRP'],
            ['CCM_I21_MEDICATION_ADMINISTRATION_DETAIL', None, (0, -1), 'GRP'],
            ['CTI', SEGMENTS['CTI'], (0, -1), 'SEG'],
        ),
    ),
    'CCM_I21_MEDICATION_ORDER_DETAIL': (
        'sequence',
        (
            ['RXO', SEGMENTS['RXO'], (1, 1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (1, -1), 'SEG'],
            ['RXC', SEGMENTS['RXC'], (0, -1), 'SEG'],
            ['CCM_I21_MEDICATION_ORDER_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'CCM_I21_MEDICATION_ORDER_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'CCM_I21_PATHWAY': (
        'sequence',
        (
            ['PTH', SEGMENTS['PTH'], (1, 1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
            ['CCM_I21_ROLE_PATHWAY', None, (0, -1), 'GRP'],
            ['CCM_I21_PATHWAY_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'CCM_I21_PATHWAY_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'CCM_I21_PATIENT_VISITS': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
        ),
    ),
    'CCM_I21_PROBLEM': (
        'sequence',
        (
            ['PRB', SEGMENTS['PRB'], (1, 1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
            ['CCM_I21_ROLE_PROBLEM', None, (0, -1), 'GRP'],
            ['CCM_I21_PROBLEM_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'CCM_I21_PROBLEM_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'CCM_I21_RESOURCES': (
        'sequence',
        (
            ['RGS', SEGMENTS['RGS'], (1, 1), 'SEG'],
            ['CCM_I21_RESOURCE_DETAIL', None, (0, -1), 'GRP'],
        ),
    ),
    'CCM_I21_RESOURCE_DETAIL': (
        'sequence',
        (
            ['CCM_I21_RESOURCE_OBJECT', None, (1, 1), 'GRP'],
            ['CCM_I21_RESOURCE_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'CCM_I21_RESOURCE_OBJECT': (
        'choice',
        (
            ['AIS', SEGMENTS['AIS'], (1, 1), 'SEG'],
            ['AIG', SEGMENTS['AIG'], (1, 1), 'SEG'],
            ['AIL', SEGMENTS['AIL'], (1, 1), 'SEG'],
            ['AIP', SEGMENTS['AIP'], (1, 1), 'SEG'],
        ),
    ),
    'CCM_I21_RESOURCE_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'CCM_I21_ROLE_CLINICAL_HISTORY': (
        'sequence',
        (
            ['CCM_I21_ROLE_CLINICAL_HISTORY_OBJECT', None, (1, 1), 'GRP'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
        ),
    ),
    'CCM_I21_ROLE_CLINICAL_HISTORY_OBJECT': (
        'choice',
        (
            ['ROL', SEGMENTS['ROL'], (1, 1), 'SEG'],
            ['PRD', SEGMENTS['PRD'], (1, 1), 'SEG'],
        ),
    ),
    'CCM_I21_ROLE_GOAL': (
        'sequence',
        (
            ['CCM_I21_ROLE_GOAL_OBJECT', None, (1, 1), 'GRP'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
        ),
    ),
    'CCM_I21_ROLE_GOAL_OBJECT': (
        'choice',
        (
            ['ROL', SEGMENTS['ROL'], (1, 1), 'SEG'],
            ['PRD', SEGMENTS['PRD'], (1, 1), 'SEG'],
        ),
    ),
    'CCM_I21_ROLE_PATHWAY': (
        'sequence',
        (
            ['CCM_I21_ROLE_PATHWAY_OBJECT', None, (1, 1), 'GRP'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
        ),
    ),
    'CCM_I21_ROLE_PATHWAY_OBJECT': (
        'choice',
        (
            ['ROL', SEGMENTS['ROL'], (1, 1), 'SEG'],
            ['PRD', SEGMENTS['PRD'], (1, 1), 'SEG'],
        ),
    ),
    'CCM_I21_ROLE_PROBLEM': (
        'sequence',
        (
            ['CCM_I21_ROLE_PROBLEM_OBJECT', None, (1, 1), 'GRP'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
        ),
    ),
    'CCM_I21_ROLE_PROBLEM_OBJECT': (
        'choice',
        (
            ['ROL', SEGMENTS['ROL'], (1, 1), 'SEG'],
            ['PRD', SEGMENTS['PRD'], (1, 1), 'SEG'],
        ),
    ),
    'CCQ_I19_PROVIDER_CONTACT': (
        'sequence',
        (
            ['PRD', SEGMENTS['PRD'], (1, 1), 'SEG'],
            ['CTD', SEGMENTS['CTD'], (0, -1), 'SEG'],
        ),
    ),
    'CCR_I16_APPOINTMENT_HISTORY': (
        'sequence',
        (
            ['SCH', SEGMENTS['SCH'], (1, 1), 'SEG'],
            ['CCR_I16_RESOURCES', None, (0, -1), 'GRP'],
        ),
    ),
    'CCR_I16_CLINICAL_HISTORY': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['CCR_I16_CLINICAL_HISTORY_DETAIL', None, (0, -1), 'GRP'],
            ['CCR_I16_ROLE_CLINICAL_HISTORY', None, (0, -1), 'GRP'],
            ['CTI', SEGMENTS['CTI'], (0, -1), 'SEG'],
        ),
    ),
    'CCR_I16_CLINICAL_HISTORY_DETAIL': (
        'sequence',
        (
            ['CCR_I16_CLINICAL_HISTORY_OBJECT', None, (1, 1), 'GRP'],
            ['CCR_I16_CLINICAL_HISTORY_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'CCR_I16_CLINICAL_HISTORY_OBJECT': (
        'choice',
        (
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['ODS', SEGMENTS['ODS'], (1, 1), 'SEG'],
            ['PR1', SEGMENTS['PR1'], (1, 1), 'SEG'],
            ['RF1', SEGMENTS['RF1'], (1, 1), 'SEG'],
            ['AL1', SEGMENTS['AL1'], (1, 1), 'SEG'],
            ['IAM', SEGMENTS['IAM'], (1, 1), 'SEG'],
            ['ACC', SEGMENTS['ACC'], (1, 1), 'SEG'],
            ['RMI', SEGMENTS['RMI'], (1, 1), 'SEG'],
            ['DB1', SEGMENTS['DB1'], (1, 1), 'SEG'],
            ['DG1', SEGMENTS['DG1'], (1, 1), 'SEG'],
            ['DRG', SEGMENTS['DRG'], (1, 1), 'SEG'],
        ),
    ),
    'CCR_I16_CLINICAL_HISTORY_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'CCR_I16_CLINICAL_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['CCR_I16_CLINICAL_ORDER_TIMING', None, (0, -1), 'GRP'],
            ['CCR_I16_CLINICAL_ORDER_DETAIL', None, (1, -1), 'GRP'],
            ['CTI', SEGMENTS['CTI'], (0, -1), 'SEG'],
        ),
    ),
    'CCR_I16_CLINICAL_ORDER_DETAIL': (
        'sequence',
        (
            ['CCR_I16_CLINICAL_ORDER_OBJECT', None, (1, 1), 'GRP'],
            ['CCR_I16_CLINICAL_ORDER_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'CCR_I16_CLINICAL_ORDER_OBJECT': (
        'choice',
        (
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['RXO', SEGMENTS['RXO'], (1, 1), 'SEG'],
            ['ODS', SEGMENTS['ODS'], (1, 1), 'SEG'],
            ['PR1', SEGMENTS['PR1'], (1, 1), 'SEG'],
        ),
    ),
    'CCR_I16_CLINICAL_ORDER_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'CCR_I16_CLINICAL_ORDER_TIMING': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'CCR_I16_GOAL': (
        'sequence',
        (
            ['GOL', SEGMENTS['GOL'], (1, 1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
            ['CCR_I16_ROLE_GOAL', None, (0, -1), 'GRP'],
            ['CCR_I16_GOAL_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'CCR_I16_GOAL_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'CCR_I16_INSURANCE': (
        'sequence',
        (
            ['IN1', SEGMENTS['IN1'], (1, 1), 'SEG'],
            ['IN2', SEGMENTS['IN2'], (0, 1), 'SEG'],
            ['IN3', SEGMENTS['IN3'], (0, 1), 'SEG'],
        ),
    ),
    'CCR_I16_MEDICATION_ADMINISTRATION_DETAIL': (
        'sequence',
        (
            ['RXA', SEGMENTS['RXA'], (1, -1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (1, 1), 'SEG'],
            ['CCR_I16_MEDICATION_ADMINISTRATION_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'CCR_I16_MEDICATION_ADMINISTRATION_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'CCR_I16_MEDICATION_ENCODING_DETAIL': (
        'sequence',
        (
            ['RXE', SEGMENTS['RXE'], (1, 1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (1, -1), 'SEG'],
            ['RXC', SEGMENTS['RXC'], (0, -1), 'SEG'],
            ['CCR_I16_MEDICATION_ENCODING_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'CCR_I16_MEDICATION_ENCODING_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'CCR_I16_MEDICATION_HISTORY': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['CCR_I16_MEDICATION_ORDER_DETAIL', None, (0, 1), 'GRP'],
            ['CCR_I16_MEDICATION_ENCODING_DETAIL', None, (0, 1), 'GRP'],
            ['CCR_I16_MEDICATION_ADMINISTRATION_DETAIL', None, (0, -1), 'GRP'],
            ['CTI', SEGMENTS['CTI'], (0, -1), 'SEG'],
        ),
    ),
    'CCR_I16_MEDICATION_ORDER_DETAIL': (
        'sequence',
        (
            ['RXO', SEGMENTS['RXO'], (1, 1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (1, -1), 'SEG'],
            ['RXC', SEGMENTS['RXC'], (0, -1), 'SEG'],
            ['CCR_I16_MEDICATION_ORDER_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'CCR_I16_MEDICATION_ORDER_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'CCR_I16_PATHWAY': (
        'sequence',
        (
            ['PTH', SEGMENTS['PTH'], (1, 1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
            ['CCR_I16_ROLE_PATHWAY', None, (0, -1), 'GRP'],
            ['CCR_I16_PATHWAY_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'CCR_I16_PATHWAY_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'CCR_I16_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
        ),
    ),
    'CCR_I16_PATIENT_VISITS': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
        ),
    ),
    'CCR_I16_PROBLEM': (
        'sequence',
        (
            ['PRB', SEGMENTS['PRB'], (1, 1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
            ['CCR_I16_ROLE_PROBLEM', None, (0, -1), 'GRP'],
            ['CCR_I16_ROLE_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'CCR_I16_PROVIDER_CONTACT': (
        'sequence',
        (
            ['PRD', SEGMENTS['PRD'], (1, 1), 'SEG'],
            ['CTD', SEGMENTS['CTD'], (0, -1), 'SEG'],
        ),
    ),
    'CCR_I16_RESOURCES': (
        'sequence',
        (
            ['RGS', SEGMENTS['RGS'], (1, 1), 'SEG'],
            ['CCR_I16_RESOURCE_DETAIL', None, (0, -1), 'GRP'],
        ),
    ),
    'CCR_I16_RESOURCE_DETAIL': (
        'sequence',
        (
            ['CCR_I16_RESOURCE_OBJECT', None, (1, 1), 'GRP'],
            ['CCR_I16_RESOURCE_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'CCR_I16_RESOURCE_OBJECT': (
        'choice',
        (
            ['AIS', SEGMENTS['AIS'], (1, 1), 'SEG'],
            ['AIG', SEGMENTS['AIG'], (1, 1), 'SEG'],
            ['AIL', SEGMENTS['AIL'], (1, 1), 'SEG'],
            ['AIP', SEGMENTS['AIP'], (1, 1), 'SEG'],
        ),
    ),
    'CCR_I16_RESOURCE_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'CCR_I16_ROLE_CLINICAL_HISTORY': (
        'sequence',
        (
            ['CCR_I16_ROLE_CLINICAL_HISTORY_OBJECT', None, (1, 1), 'GRP'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
        ),
    ),
    'CCR_I16_ROLE_CLINICAL_HISTORY_OBJECT': (
        'choice',
        (
            ['ROL', SEGMENTS['ROL'], (1, 1), 'SEG'],
            ['PRD', SEGMENTS['PRD'], (1, 1), 'SEG'],
        ),
    ),
    'CCR_I16_ROLE_GOAL': (
        'sequence',
        (
            ['CCR_I16_ROLE_GOAL_OBJECT', None, (1, 1), 'GRP'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
        ),
    ),
    'CCR_I16_ROLE_GOAL_OBJECT': (
        'choice',
        (
            ['ROL', SEGMENTS['ROL'], (1, 1), 'SEG'],
            ['PRD', SEGMENTS['PRD'], (1, 1), 'SEG'],
        ),
    ),
    'CCR_I16_ROLE_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'CCR_I16_ROLE_PATHWAY': (
        'sequence',
        (
            ['CCR_I16_ROLE_PATHWAY_OBJECT', None, (1, 1), 'GRP'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
        ),
    ),
    'CCR_I16_ROLE_PATHWAY_OBJECT': (
        'choice',
        (
            ['ROL', SEGMENTS['ROL'], (1, 1), 'SEG'],
            ['PRD', SEGMENTS['PRD'], (1, 1), 'SEG'],
        ),
    ),
    'CCR_I16_ROLE_PROBLEM': (
        'sequence',
        (
            ['CCR_I16_ROLE_PROBLEM_OBJECT', None, (1, 1), 'GRP'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
        ),
    ),
    'CCR_I16_ROLE_PROBLEM_OBJECT': (
        'choice',
        (
            ['ROL', SEGMENTS['ROL'], (1, 1), 'SEG'],
            ['PRD', SEGMENTS['PRD'], (1, 1), 'SEG'],
        ),
    ),
    'CCU_I20_APPOINTMENT_HISTORY': (
        'sequence',
        (
            ['SCH', SEGMENTS['SCH'], (1, 1), 'SEG'],
            ['CCU_I20_RESOURCES', None, (0, -1), 'GRP'],
        ),
    ),
    'CCU_I20_CLINICAL_HISTORY': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['CCU_I20_CLINICAL_HISTORY_DETAIL', None, (0, -1), 'GRP'],
            ['CCU_I20_ROLE_CLINICAL_HISTORY', None, (0, -1), 'GRP'],
            ['CTI', SEGMENTS['CTI'], (0, -1), 'SEG'],
        ),
    ),
    'CCU_I20_CLINICAL_HISTORY_DETAIL': (
        'sequence',
        (
            ['CCU_I20_CLINICAL_HISTORY_OBJECT', None, (1, 1), 'GRP'],
            ['CCU_I20_CLINICAL_HISTORY_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'CCU_I20_CLINICAL_HISTORY_OBJECT': (
        'choice',
        (
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['ODS', SEGMENTS['ODS'], (1, 1), 'SEG'],
            ['PR1', SEGMENTS['PR1'], (1, 1), 'SEG'],
            ['RF1', SEGMENTS['RF1'], (1, 1), 'SEG'],
            ['AL1', SEGMENTS['AL1'], (1, 1), 'SEG'],
            ['IAM', SEGMENTS['IAM'], (1, 1), 'SEG'],
            ['ACC', SEGMENTS['ACC'], (1, 1), 'SEG'],
            ['RMI', SEGMENTS['RMI'], (1, 1), 'SEG'],
            ['DB1', SEGMENTS['DB1'], (1, 1), 'SEG'],
            ['DG1', SEGMENTS['DG1'], (1, 1), 'SEG'],
            ['DRG', SEGMENTS['DRG'], (1, 1), 'SEG'],
            ['PDA', SEGMENTS['PDA'], (1, 1), 'SEG'],
        ),
    ),
    'CCU_I20_CLINICAL_HISTORY_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'CCU_I20_GOAL': (
        'sequence',
        (
            ['GOL', SEGMENTS['GOL'], (1, 1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
            ['CCU_I20_ROLE_GOAL', None, (0, -1), 'GRP'],
            ['CCU_I20_GOAL_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'CCU_I20_GOAL_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'CCU_I20_INSURANCE': (
        'sequence',
        (
            ['IN1', SEGMENTS['IN1'], (1, 1), 'SEG'],
            ['IN2', SEGMENTS['IN2'], (0, 1), 'SEG'],
            ['IN3', SEGMENTS['IN3'], (0, 1), 'SEG'],
        ),
    ),
    'CCU_I20_MEDICATION_ADMINISTRATION_DETAIL': (
        'sequence',
        (
            ['RXA', SEGMENTS['RXA'], (1, -1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (1, 1), 'SEG'],
            ['CCU_I20_MEDICATION_ADMINISTRATION_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'CCU_I20_MEDICATION_ADMINISTRATION_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'CCU_I20_MEDICATION_ENCODING_DETAIL': (
        'sequence',
        (
            ['RXE', SEGMENTS['RXE'], (1, 1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (1, -1), 'SEG'],
            ['RXC', SEGMENTS['RXC'], (0, -1), 'SEG'],
            ['CCU_I20_MEDICATION_ENCODING_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'CCU_I20_MEDICATION_ENCODING_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'CCU_I20_MEDICATION_HISTORY': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['CCU_I20_MEDICATION_ORDER_DETAIL', None, (0, 1), 'GRP'],
            ['CCU_I20_MEDICATION_ENCODING_DETAIL', None, (0, 1), 'GRP'],
            ['CCU_I20_MEDICATION_ADMINISTRATION_DETAIL', None, (0, -1), 'GRP'],
            ['CTI', SEGMENTS['CTI'], (0, -1), 'SEG'],
        ),
    ),
    'CCU_I20_MEDICATION_ORDER_DETAIL': (
        'sequence',
        (
            ['RXO', SEGMENTS['RXO'], (1, 1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (1, -1), 'SEG'],
            ['RXC', SEGMENTS['RXC'], (0, -1), 'SEG'],
            ['CCU_I20_MEDICATION_ORDER_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'CCU_I20_MEDICATION_ORDER_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'CCU_I20_PATHWAY': (
        'sequence',
        (
            ['PTH', SEGMENTS['PTH'], (1, 1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
            ['CCU_I20_ROLE_PATHWAY', None, (0, -1), 'GRP'],
            ['CCU_I20_PATHWAY_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'CCU_I20_PATHWAY_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'CCU_I20_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
        ),
    ),
    'CCU_I20_PATIENT_VISITS': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
        ),
    ),
    'CCU_I20_PROBLEM': (
        'sequence',
        (
            ['PRB', SEGMENTS['PRB'], (1, 1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
            ['CCU_I20_ROLE_PROBLEM', None, (0, -1), 'GRP'],
            ['CCU_I20_PROBLEM_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'CCU_I20_PROBLEM_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'CCU_I20_PROVIDER_CONTACT': (
        'sequence',
        (
            ['PRD', SEGMENTS['PRD'], (1, 1), 'SEG'],
            ['CTD', SEGMENTS['CTD'], (0, -1), 'SEG'],
        ),
    ),
    'CCU_I20_RESOURCES': (
        'sequence',
        (
            ['RGS', SEGMENTS['RGS'], (1, 1), 'SEG'],
            ['CCU_I20_RESOURCE_DETAIL', None, (0, -1), 'GRP'],
        ),
    ),
    'CCU_I20_RESOURCE_DETAIL': (
        'sequence',
        (
            ['CCU_I20_RESOURCE_OBJECT', None, (1, 1), 'GRP'],
            ['CCU_I20_RESOURCE_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'CCU_I20_RESOURCE_OBJECT': (
        'choice',
        (
            ['AIS', SEGMENTS['AIS'], (1, 1), 'SEG'],
            ['AIG', SEGMENTS['AIG'], (1, 1), 'SEG'],
            ['AIL', SEGMENTS['AIL'], (1, 1), 'SEG'],
            ['AIP', SEGMENTS['AIP'], (1, 1), 'SEG'],
        ),
    ),
    'CCU_I20_RESOURCE_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'CCU_I20_ROLE_CLINICAL_HISTORY': (
        'sequence',
        (
            ['CCU_I20_ROLE_CLINICAL_HISTORY_OBJECT', None, (1, 1), 'GRP'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
        ),
    ),
    'CCU_I20_ROLE_CLINICAL_HISTORY_OBJECT': (
        'choice',
        (
            ['ROL', SEGMENTS['ROL'], (1, 1), 'SEG'],
            ['PRD', SEGMENTS['PRD'], (1, 1), 'SEG'],
        ),
    ),
    'CCU_I20_ROLE_GOAL': (
        'sequence',
        (
            ['CCU_I20_ROLE_GOAL_OBJECT', None, (1, 1), 'GRP'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
        ),
    ),
    'CCU_I20_ROLE_GOAL_OBJECT': (
        'choice',
        (
            ['ROL', SEGMENTS['ROL'], (1, 1), 'SEG'],
            ['PRD', SEGMENTS['PRD'], (1, 1), 'SEG'],
        ),
    ),
    'CCU_I20_ROLE_PATHWAY': (
        'sequence',
        (
            ['CCU_I20_ROLE_PATHWAY_OBJECT', None, (1, 1), 'GRP'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
        ),
    ),
    'CCU_I20_ROLE_PATHWAY_OBJECT': (
        'choice',
        (
            ['ROL', SEGMENTS['ROL'], (1, 1), 'SEG'],
            ['PRD', SEGMENTS['PRD'], (1, 1), 'SEG'],
        ),
    ),
    'CCU_I20_ROLE_PROBLEM': (
        'sequence',
        (
            ['CCU_I20_ROLE_PROBLEM_OBJECT', None, (1, 1), 'GRP'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
        ),
    ),
    'CCU_I20_ROLE_PROBLEM_OBJECT': (
        'choice',
        (
            ['ROL', SEGMENTS['ROL'], (1, 1), 'SEG'],
            ['PRD', SEGMENTS['PRD'], (1, 1), 'SEG'],
        ),
    ),
    'CQU_I19_APPOINTMENT_HISTORY': (
        'sequence',
        (
            ['SCH', SEGMENTS['SCH'], (1, 1), 'SEG'],
            ['CQU_I19_RESOURCES', None, (0, -1), 'GRP'],
        ),
    ),
    'CQU_I19_CLINICAL_HISTORY': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['CQU_I19_CLINICAL_HISTORY_DETAIL', None, (0, -1), 'GRP'],
            ['CQU_I19_ROLE_CLINICAL_HISTORY', None, (0, -1), 'GRP'],
            ['CTI', SEGMENTS['CTI'], (0, -1), 'SEG'],
        ),
    ),
    'CQU_I19_CLINICAL_HISTORY_DETAIL': (
        'sequence',
        (
            ['CQU_I19_CLINICAL_HISTORY_OBJECT', None, (1, 1), 'GRP'],
            ['CQU_I19_CLINICAL_HISTORY_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'CQU_I19_CLINICAL_HISTORY_OBJECT': (
        'choice',
        (
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['ODS', SEGMENTS['ODS'], (1, 1), 'SEG'],
            ['PR1', SEGMENTS['PR1'], (1, 1), 'SEG'],
            ['RF1', SEGMENTS['RF1'], (1, 1), 'SEG'],
            ['AL1', SEGMENTS['AL1'], (1, 1), 'SEG'],
            ['IAM', SEGMENTS['IAM'], (1, 1), 'SEG'],
            ['ACC', SEGMENTS['ACC'], (1, 1), 'SEG'],
            ['RMI', SEGMENTS['RMI'], (1, 1), 'SEG'],
            ['DB1', SEGMENTS['DB1'], (1, 1), 'SEG'],
            ['DG1', SEGMENTS['DG1'], (1, 1), 'SEG'],
            ['DRG', SEGMENTS['DRG'], (1, 1), 'SEG'],
            ['PDA', SEGMENTS['PDA'], (1, 1), 'SEG'],
        ),
    ),
    'CQU_I19_CLINICAL_HISTORY_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'CQU_I19_GOAL': (
        'sequence',
        (
            ['GOL', SEGMENTS['GOL'], (1, 1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
            ['CQU_I19_ROLE_GOAL', None, (0, -1), 'GRP'],
            ['CQU_I19_GOAL_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'CQU_I19_GOAL_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'CQU_I19_INSURANCE': (
        'sequence',
        (
            ['IN1', SEGMENTS['IN1'], (1, 1), 'SEG'],
            ['IN2', SEGMENTS['IN2'], (0, 1), 'SEG'],
            ['IN3', SEGMENTS['IN3'], (0, 1), 'SEG'],
        ),
    ),
    'CQU_I19_MEDICATION_ADMINISTRATION_DETAIL': (
        'sequence',
        (
            ['RXA', SEGMENTS['RXA'], (1, -1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (1, 1), 'SEG'],
            ['CQU_I19_MEDICATION_ADMINISTRATION_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'CQU_I19_MEDICATION_ADMINISTRATION_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'CQU_I19_MEDICATION_ENCODING_DETAIL': (
        'sequence',
        (
            ['RXE', SEGMENTS['RXE'], (1, 1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (1, -1), 'SEG'],
            ['RXC', SEGMENTS['RXC'], (0, -1), 'SEG'],
            ['CQU_I19_MEDICATION_ENCODING_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'CQU_I19_MEDICATION_ENCODING_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'CQU_I19_MEDICATION_HISTORY': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['CQU_I19_MEDICATION_ORDER_DETAIL', None, (0, 1), 'GRP'],
            ['CQU_I19_MEDICATION_ENCODING_DETAIL', None, (0, 1), 'GRP'],
            ['CQU_I19_MEDICATION_ADMINISTRATION_DETAIL', None, (0, -1), 'GRP'],
            ['CTI', SEGMENTS['CTI'], (0, -1), 'SEG'],
        ),
    ),
    'CQU_I19_MEDICATION_ORDER_DETAIL': (
        'sequence',
        (
            ['RXO', SEGMENTS['RXO'], (1, 1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (1, -1), 'SEG'],
            ['RXC', SEGMENTS['RXC'], (0, -1), 'SEG'],
            ['CQU_I19_MEDICATION_ORDER_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'CQU_I19_MEDICATION_ORDER_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'CQU_I19_PATHWAY': (
        'sequence',
        (
            ['PTH', SEGMENTS['PTH'], (1, 1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
            ['CQU_I19_ROLE_PATHWAY', None, (0, -1), 'GRP'],
            ['CQU_I19_PATHWAY_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'CQU_I19_PATHWAY_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'CQU_I19_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
        ),
    ),
    'CQU_I19_PATIENT_VISITS': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
        ),
    ),
    'CQU_I19_PROBLEM': (
        'sequence',
        (
            ['PRB', SEGMENTS['PRB'], (1, 1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
            ['CQU_I19_ROLE_PROBLEM', None, (0, -1), 'GRP'],
            ['CQU_I19_PROBLEM_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'CQU_I19_PROBLEM_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'CQU_I19_PROVIDER_CONTACT': (
        'sequence',
        (
            ['PRD', SEGMENTS['PRD'], (1, 1), 'SEG'],
            ['CTD', SEGMENTS['CTD'], (0, -1), 'SEG'],
        ),
    ),
    'CQU_I19_RESOURCES': (
        'sequence',
        (
            ['RGS', SEGMENTS['RGS'], (1, 1), 'SEG'],
            ['CQU_I19_RESOURCE_DETAIL', None, (0, -1), 'GRP'],
        ),
    ),
    'CQU_I19_RESOURCE_DETAIL': (
        'sequence',
        (
            ['CQU_I19_RESOURCE_OBJECT', None, (1, 1), 'GRP'],
            ['CQU_I19_RESOURCE_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'CQU_I19_RESOURCE_OBJECT': (
        'choice',
        (
            ['AIS', SEGMENTS['AIS'], (1, 1), 'SEG'],
            ['AIG', SEGMENTS['AIG'], (1, 1), 'SEG'],
            ['AIL', SEGMENTS['AIL'], (1, 1), 'SEG'],
            ['AIP', SEGMENTS['AIP'], (1, 1), 'SEG'],
        ),
    ),
    'CQU_I19_RESOURCE_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'CQU_I19_ROLE_CLINICAL_HISTORY': (
        'sequence',
        (
            ['CQU_I19_ROLE_CLINICAL_HISTORY_OBJECT', None, (1, 1), 'GRP'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
        ),
    ),
    'CQU_I19_ROLE_CLINICAL_HISTORY_OBJECT': (
        'choice',
        (
            ['ROL', SEGMENTS['ROL'], (1, 1), 'SEG'],
            ['PRD', SEGMENTS['PRD'], (1, 1), 'SEG'],
        ),
    ),
    'CQU_I19_ROLE_GOAL': (
        'sequence',
        (
            ['CQU_I19_ROLE_GOAL_OBJECT', None, (1, 1), 'GRP'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
        ),
    ),
    'CQU_I19_ROLE_GOAL_OBJECT': (
        'choice',
        (
            ['ROL', SEGMENTS['ROL'], (1, 1), 'SEG'],
            ['PRD', SEGMENTS['PRD'], (1, 1), 'SEG'],
        ),
    ),
    'CQU_I19_ROLE_PATHWAY': (
        'sequence',
        (
            ['CQU_I19_ROLE_PATHWAY_OBJECT', None, (1, 1), 'GRP'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
        ),
    ),
    'CQU_I19_ROLE_PATHWAY_OBJECT': (
        'choice',
        (
            ['ROL', SEGMENTS['ROL'], (1, 1), 'SEG'],
            ['PRD', SEGMENTS['PRD'], (1, 1), 'SEG'],
        ),
    ),
    'CQU_I19_ROLE_PROBLEM': (
        'sequence',
        (
            ['CQU_I19_ROLE_PROBLEM_OBJECT', None, (1, 1), 'GRP'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
        ),
    ),
    'CQU_I19_ROLE_PROBLEM_OBJECT': (
        'choice',
        (
            ['ROL', SEGMENTS['ROL'], (1, 1), 'SEG'],
            ['PRD', SEGMENTS['PRD'], (1, 1), 'SEG'],
        ),
    ),
    'CRM_C01_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
            ['CRM_C01_PATIENT_VISIT', None, (0, 1), 'GRP'],
            ['CSR', SEGMENTS['CSR'], (1, 1), 'SEG'],
            ['CSP', SEGMENTS['CSP'], (0, -1), 'SEG'],
        ),
    ),
    'CRM_C01_PATIENT_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'CSU_C09_COMMON_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'CSU_C09_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['CSU_C09_VISIT', None, (0, 1), 'GRP'],
            ['CSR', SEGMENTS['CSR'], (1, 1), 'SEG'],
            ['CSU_C09_STUDY_PHASE', None, (1, -1), 'GRP'],
        ),
    ),
    'CSU_C09_RX_ADMIN': (
        'sequence',
        (
            ['RXA', SEGMENTS['RXA'], (1, 1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'CSU_C09_STUDY_OBSERVATION': (
        'sequence',
        (
            ['CSU_C09_STUDY_OBSERVATION_ORDER', None, (0, 1), 'GRP'],
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['CSU_C09_TIMING_QTY', None, (0, -1), 'GRP'],
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'CSU_C09_STUDY_OBSERVATION_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'CSU_C09_STUDY_PHARM': (
        'sequence',
        (
            ['CSU_C09_COMMON_ORDER', None, (0, 1), 'GRP'],
            ['CSU_C09_RX_ADMIN', None, (1, -1), 'GRP'],
        ),
    ),
    'CSU_C09_STUDY_PHASE': (
        'sequence',
        (
            ['CSP', SEGMENTS['CSP'], (0, 1), 'SEG'],
            ['CSU_C09_STUDY_SCHEDULE', None, (1, -1), 'GRP'],
        ),
    ),
    'CSU_C09_STUDY_SCHEDULE': (
        'sequence',
        (
            ['CSS', SEGMENTS['CSS'], (0, 1), 'SEG'],
            ['CSU_C09_STUDY_OBSERVATION', None, (1, -1), 'GRP'],
            ['CSU_C09_STUDY_PHARM', None, (1, -1), 'GRP'],
        ),
    ),
    'CSU_C09_TIMING_QTY': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'CSU_C09_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'DBC_O41_DONOR': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['OBX', SEGMENTS['OBX'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
            ['AL1', SEGMENTS['AL1'], (0, -1), 'SEG'],
        ),
    ),
    'DBC_O42_DONOR': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['OBX', SEGMENTS['OBX'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['AL1', SEGMENTS['AL1'], (0, -1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
        ),
    ),
    'DEL_O46_DONOR': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['OBX', SEGMENTS['OBX'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['AL1', SEGMENTS['AL1'], (0, -1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
            ['DEL_O46_DONOR_REGISTRATION', None, (0, 1), 'GRP'],
        ),
    ),
    'DEL_O46_DONOR_REGISTRATION': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (0, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'DEO_O45_DONOR': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['OBX', SEGMENTS['OBX'], (0, -1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['DEO_O45_DONOR_REGISTRATION', None, (0, 1), 'GRP'],
        ),
    ),
    'DEO_O45_DONOR_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'DEO_O45_DONOR_ORDER': (
        'sequence',
        (
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['DEO_O45_DONOR_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'DEO_O45_DONOR_REGISTRATION': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (0, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'DER_O44_DONOR': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['OBX', SEGMENTS['OBX'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['AL1', SEGMENTS['AL1'], (0, -1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
            ['DER_O44_DONOR_REGISTRATION', None, (0, 1), 'GRP'],
        ),
    ),
    'DER_O44_DONOR_ORDER': (
        'sequence',
        (
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'DER_O44_DONOR_REGISTRATION': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (0, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'DFT_P03_COMMON_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (0, 1), 'SEG'],
            ['DFT_P03_TIMING_QUANTITY', None, (0, -1), 'GRP'],
            ['DFT_P03_ORDER', None, (0, 1), 'GRP'],
            ['DFT_P03_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'DFT_P03_FINANCIAL': (
        'sequence',
        (
            ['FT1', SEGMENTS['FT1'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ROL', SEGMENTS['ROL'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, 1), 'SEG'],
            ['DFT_P03_FINANCIAL_PROCEDURE', None, (0, -1), 'GRP'],
            ['DFT_P03_FINANCIAL_COMMON_ORDER', None, (0, -1), 'GRP'],
        ),
    ),
    'DFT_P03_FINANCIAL_COMMON_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (0, 1), 'SEG'],
            ['DFT_P03_FINANCIAL_TIMING_QUANTITY', None, (0, -1), 'GRP'],
            ['DFT_P03_FINANCIAL_ORDER', None, (0, 1), 'GRP'],
            ['DFT_P03_FINANCIAL_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'DFT_P03_FINANCIAL_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'DFT_P03_FINANCIAL_ORDER': (
        'sequence',
        (
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'DFT_P03_FINANCIAL_PROCEDURE': (
        'sequence',
        (
            ['PR1', SEGMENTS['PR1'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ROL', SEGMENTS['ROL'], (0, -1), 'SEG'],
        ),
    ),
    'DFT_P03_FINANCIAL_TIMING_QUANTITY': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'DFT_P03_INSURANCE': (
        'sequence',
        (
            ['IN1', SEGMENTS['IN1'], (1, 1), 'SEG'],
            ['IN2', SEGMENTS['IN2'], (0, 1), 'SEG'],
            ['IN3', SEGMENTS['IN3'], (0, -1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ROL', SEGMENTS['ROL'], (0, -1), 'SEG'],
        ),
    ),
    'DFT_P03_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'DFT_P03_ORDER': (
        'sequence',
        (
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'DFT_P03_TIMING_QUANTITY': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'DFT_P03_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ROL', SEGMENTS['ROL'], (0, -1), 'SEG'],
        ),
    ),
    'DFT_P11_COMMON_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (0, 1), 'SEG'],
            ['DFT_P11_TIMING_QUANTITY', None, (0, -1), 'GRP'],
            ['DFT_P11_ORDER', None, (0, 1), 'GRP'],
            ['DFT_P11_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'DFT_P11_FINANCIAL': (
        'sequence',
        (
            ['FT1', SEGMENTS['FT1'], (1, 1), 'SEG'],
            ['DFT_P11_FINANCIAL_PROCEDURE', None, (0, -1), 'GRP'],
            ['DFT_P11_FINANCIAL_COMMON_ORDER', None, (0, -1), 'GRP'],
            ['DG1', SEGMENTS['DG1'], (0, -1), 'SEG'],
            ['DRG', SEGMENTS['DRG'], (0, 1), 'SEG'],
            ['GT1', SEGMENTS['GT1'], (0, -1), 'SEG'],
            ['DFT_P11_FINANCIAL_INSURANCE', None, (0, -1), 'GRP'],
        ),
    ),
    'DFT_P11_FINANCIAL_COMMON_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (0, 1), 'SEG'],
            ['DFT_P11_FINANCIAL_TIMING_QUANTITY', None, (0, -1), 'GRP'],
            ['DFT_P11_FINANCIAL_ORDER', None, (0, 1), 'GRP'],
            ['DFT_P11_FINANCIAL_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'DFT_P11_FINANCIAL_INSURANCE': (
        'sequence',
        (
            ['IN1', SEGMENTS['IN1'], (1, 1), 'SEG'],
            ['IN2', SEGMENTS['IN2'], (0, 1), 'SEG'],
            ['IN3', SEGMENTS['IN3'], (0, -1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ROL', SEGMENTS['ROL'], (0, -1), 'SEG'],
        ),
    ),
    'DFT_P11_FINANCIAL_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'DFT_P11_FINANCIAL_ORDER': (
        'sequence',
        (
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'DFT_P11_FINANCIAL_PROCEDURE': (
        'sequence',
        (
            ['PR1', SEGMENTS['PR1'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ROL', SEGMENTS['ROL'], (0, -1), 'SEG'],
        ),
    ),
    'DFT_P11_FINANCIAL_TIMING_QUANTITY': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'DFT_P11_INSURANCE': (
        'sequence',
        (
            ['IN1', SEGMENTS['IN1'], (1, 1), 'SEG'],
            ['IN2', SEGMENTS['IN2'], (0, 1), 'SEG'],
            ['IN3', SEGMENTS['IN3'], (0, -1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ROL', SEGMENTS['ROL'], (0, -1), 'SEG'],
        ),
    ),
    'DFT_P11_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'DFT_P11_ORDER': (
        'sequence',
        (
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'DFT_P11_TIMING_QUANTITY': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'DFT_P11_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ROL', SEGMENTS['ROL'], (0, -1), 'SEG'],
        ),
    ),
    'DPR_O48_BLOOD_UNIT': (
        'sequence',
        (
            ['BUI', SEGMENTS['BUI'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'DPR_O48_DONATION': (
        'sequence',
        (
            ['DON', SEGMENTS['DON'], (1, 1), 'SEG'],
            ['OBX', SEGMENTS['OBX'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['DPR_O48_BLOOD_UNIT', None, (0, 1), 'GRP'],
        ),
    ),
    'DPR_O48_DONATION_ORDER': (
        'sequence',
        (
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'DPR_O48_DONOR': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['OBX', SEGMENTS['OBX'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['AL1', SEGMENTS['AL1'], (0, -1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
            ['DPR_O48_DONOR_REGISTRATION', None, (0, 1), 'GRP'],
        ),
    ),
    'DPR_O48_DONOR_REGISTRATION': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (0, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'DRC_O47_DONATION_ORDER': (
        'sequence',
        (
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'DRC_O47_DONOR': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['OBX', SEGMENTS['OBX'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['AL1', SEGMENTS['AL1'], (0, -1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
            ['DRC_O47_DONOR_REGISTRATION', None, (0, 1), 'GRP'],
        ),
    ),
    'DRC_O47_DONOR_REGISTRATION': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (0, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'DRG_O43_DONOR': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['OBX', SEGMENTS['OBX'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['AL1', SEGMENTS['AL1'], (0, -1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
            ['DRG_O43_DONOR_REGISTRATION', None, (0, 1), 'GRP'],
        ),
    ),
    'DRG_O43_DONOR_REGISTRATION': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (0, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'EAC_U07_COMMAND': (
        'sequence',
        (
            ['ECD', SEGMENTS['ECD'], (1, 1), 'SEG'],
            ['TQ1', SEGMENTS['TQ1'], (0, 1), 'SEG'],
            ['EAC_U07_SPECIMEN_CONTAINER', None, (0, 1), 'GRP'],
            ['CNS', SEGMENTS['CNS'], (0, 1), 'SEG'],
        ),
    ),
    'EAC_U07_SPECIMEN_CONTAINER': (
        'sequence',
        (
            ['SAC', SEGMENTS['SAC'], (1, 1), 'SEG'],
            ['OBR', SEGMENTS['OBR'], (0, -1), 'SEG'],
            ['SPM', SEGMENTS['SPM'], (0, -1), 'SEG'],
        ),
    ),
    'EAN_U09_NOTIFICATION': (
        'sequence',
        (
            ['NDS', SEGMENTS['NDS'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, 1), 'SEG'],
        ),
    ),
    'EAR_U08_COMMAND_RESPONSE': (
        'sequence',
        (
            ['ECD', SEGMENTS['ECD'], (1, 1), 'SEG'],
            ['EAR_U08_SPECIMEN_CONTAINER', None, (0, 1), 'GRP'],
            ['ECR', SEGMENTS['ECR'], (1, 1), 'SEG'],
        ),
    ),
    'EAR_U08_SPECIMEN_CONTAINER': (
        'sequence',
        (
            ['SAC', SEGMENTS['SAC'], (1, 1), 'SEG'],
            ['SPM', SEGMENTS['SPM'], (0, -1), 'SEG'],
        ),
    ),
    'EHC_E01_DIAGNOSIS': (
        'sequence',
        (
            ['DG1', SEGMENTS['DG1'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'EHC_E01_INSURANCE': (
        'sequence',
        (
            ['IN1', SEGMENTS['IN1'], (1, 1), 'SEG'],
            ['IN2', SEGMENTS['IN2'], (0, 1), 'SEG'],
        ),
    ),
    'EHC_E01_INVOICE_INFORMATION_SUBMIT': (
        'choice',
        (
            ['IVC', SEGMENTS['IVC'], (1, 1), 'SEG'],
            ['PYE', SEGMENTS['PYE'], (0, 1), 'SEG'],
            ['CTD', SEGMENTS['CTD'], (0, -1), 'SEG'],
            ['AUT', SEGMENTS['AUT'], (0, 1), 'SEG'],
            ['LOC', SEGMENTS['LOC'], (0, -1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ROL', SEGMENTS['ROL'], (0, -1), 'SEG'],
            ['EHC_E01_PRODUCT_SERVICE_SECTION', None, (1, -1), 'GRP'],
        ),
    ),
    'EHC_E01_PATIENT_INFO': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PV1', SEGMENTS['PV1'], (0, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['ACC', SEGMENTS['ACC'], (0, -1), 'SEG'],
            ['EHC_E01_INSURANCE', None, (1, -1), 'GRP'],
            ['EHC_E01_DIAGNOSIS', None, (0, -1), 'GRP'],
            ['OBX', SEGMENTS['OBX'], (0, -1), 'SEG'],
        ),
    ),
    'EHC_E01_PROCEDURE': (
        'sequence',
        (
            ['PR1', SEGMENTS['PR1'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ROL', SEGMENTS['ROL'], (0, -1), 'SEG'],
        ),
    ),
    'EHC_E01_PRODUCT_SERVICE_GROUP': (
        'sequence',
        (
            ['PSG', SEGMENTS['PSG'], (1, 1), 'SEG'],
            ['LOC', SEGMENTS['LOC'], (0, -1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ROL', SEGMENTS['ROL'], (0, -1), 'SEG'],
            ['EHC_E01_PATIENT_INFO', None, (0, -1), 'GRP'],
            ['EHC_E01_PRODUCT_SERVICE_LINE_ITEM', None, (1, -1), 'GRP'],
            ['EHC_E01_PROCEDURE', None, (0, -1), 'GRP'],
            ['IPR', SEGMENTS['IPR'], (0, -1), 'SEG'],
        ),
    ),
    'EHC_E01_PRODUCT_SERVICE_LINE_ITEM': (
        'sequence',
        (
            ['PSL', SEGMENTS['PSL'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['ADJ', SEGMENTS['ADJ'], (0, -1), 'SEG'],
            ['AUT', SEGMENTS['AUT'], (0, 1), 'SEG'],
            ['LOC', SEGMENTS['LOC'], (0, -1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ROL', SEGMENTS['ROL'], (0, -1), 'SEG'],
        ),
    ),
    'EHC_E01_PRODUCT_SERVICE_SECTION': (
        'sequence',
        (
            ['PSS', SEGMENTS['PSS'], (1, 1), 'SEG'],
            ['EHC_E01_PRODUCT_SERVICE_GROUP', None, (1, -1), 'GRP'],
        ),
    ),
    'EHC_E02_INVOICE_INFORMATION_CANCEL': (
        'choice',
        (
            ['IVC', SEGMENTS['IVC'], (1, 1), 'SEG'],
            ['PYE', SEGMENTS['PYE'], (1, 1), 'SEG'],
            ['CTD', SEGMENTS['CTD'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['EHC_E02_PRODUCT_SERVICE_SECTION', None, (0, -1), 'GRP'],
        ),
    ),
    'EHC_E02_PRODUCT_SERVICE_SECTION': (
        'sequence',
        (
            ['PSS', SEGMENTS['PSS'], (1, 1), 'SEG'],
            ['EHC_E02_PSG', None, (0, -1), 'GRP'],
        ),
    ),
    'EHC_E02_PSG': (
        'sequence',
        (
            ['PSG', SEGMENTS['PSG'], (1, 1), 'SEG'],
            ['PSL', SEGMENTS['PSL'], (0, -1), 'SEG'],
        ),
    ),
    'EHC_E04_PRODUCT_SERVICE_GROUP': (
        'sequence',
        (
            ['PSG', SEGMENTS['PSG'], (1, 1), 'SEG'],
            ['PSL', SEGMENTS['PSL'], (0, -1), 'SEG'],
        ),
    ),
    'EHC_E04_PRODUCT_SERVICE_SECTION': (
        'sequence',
        (
            ['PSS', SEGMENTS['PSS'], (1, 1), 'SEG'],
            ['EHC_E04_PRODUCT_SERVICE_GROUP', None, (0, -1), 'GRP'],
        ),
    ),
    'EHC_E04_REASSESSMENT_REQUEST_INFO': (
        'choice',
        (
            ['IVC', SEGMENTS['IVC'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['EHC_E04_PRODUCT_SERVICE_SECTION', None, (0, -1), 'GRP'],
        ),
    ),
    'EHC_E10_INVOICE_PROCESSING_RESULTS_INFO': (
        'sequence',
        (
            ['IPR', SEGMENTS['IPR'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['PYE', SEGMENTS['PYE'], (1, 1), 'SEG'],
            ['IN1', SEGMENTS['IN1'], (1, 1), 'SEG'],
            ['IN2', SEGMENTS['IN2'], (0, 1), 'SEG'],
            ['IVC', SEGMENTS['IVC'], (1, 1), 'SEG'],
            ['EHC_E10_PRODUCT_SERVICE_SECTION', None, (1, -1), 'GRP'],
        ),
    ),
    'EHC_E10_PRODUCT_SERVICE_GROUP': (
        'sequence',
        (
            ['PSG', SEGMENTS['PSG'], (1, 1), 'SEG'],
            ['EHC_E10_PRODUCT_SERVICE_LINE_INFO', None, (1, -1), 'GRP'],
        ),
    ),
    'EHC_E10_PRODUCT_SERVICE_LINE_INFO': (
        'sequence',
        (
            ['PSL', SEGMENTS['PSL'], (1, 1), 'SEG'],
            ['ADJ', SEGMENTS['ADJ'], (0, -1), 'SEG'],
        ),
    ),
    'EHC_E10_PRODUCT_SERVICE_SECTION': (
        'sequence',
        (
            ['PSS', SEGMENTS['PSS'], (1, 1), 'SEG'],
            ['EHC_E10_PRODUCT_SERVICE_GROUP', None, (1, -1), 'GRP'],
        ),
    ),
    'EHC_E12_REQUEST': (
        'sequence',
        (
            ['CTD', SEGMENTS['CTD'], (0, 1), 'SEG'],
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, 1), 'SEG'],
            ['OBX', SEGMENTS['OBX'], (0, -1), 'SEG'],
        ),
    ),
    'EHC_E13_REQUEST': (
        'sequence',
        (
            ['CTD', SEGMENTS['CTD'], (0, 1), 'SEG'],
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, 1), 'SEG'],
            ['EHC_E13_RESPONSE', None, (1, -1), 'GRP'],
        ),
    ),
    'EHC_E13_RESPONSE': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, 1), 'SEG'],
            ['TXA', SEGMENTS['TXA'], (0, 1), 'SEG'],
        ),
    ),
    'EHC_E15_ADJUSTMENT_PAYEE': (
        'sequence',
        (
            ['ADJ', SEGMENTS['ADJ'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, 1), 'SEG'],
            ['ROL', SEGMENTS['ROL'], (0, 1), 'SEG'],
        ),
    ),
    'EHC_E15_PAYMENT_REMITTANCE_DETAIL_INFO': (
        'sequence',
        (
            ['IPR', SEGMENTS['IPR'], (1, 1), 'SEG'],
            ['IVC', SEGMENTS['IVC'], (1, 1), 'SEG'],
            ['EHC_E15_PRODUCT_SERVICE_SECTION', None, (1, -1), 'GRP'],
        ),
    ),
    'EHC_E15_PAYMENT_REMITTANCE_HEADER_INFO': (
        'choice',
        (
            ['PMT', SEGMENTS['PMT'], (1, 1), 'SEG'],
            ['PYE', SEGMENTS['PYE'], (1, 1), 'SEG'],
        ),
    ),
    'EHC_E15_PRODUCT_SERVICE_GROUP': (
        'sequence',
        (
            ['PSG', SEGMENTS['PSG'], (1, 1), 'SEG'],
            ['EHC_E15_PSL_ITEM_INFO', None, (1, -1), 'GRP'],
        ),
    ),
    'EHC_E15_PRODUCT_SERVICE_SECTION': (
        'sequence',
        (
            ['PSS', SEGMENTS['PSS'], (1, 1), 'SEG'],
            ['EHC_E15_PRODUCT_SERVICE_GROUP', None, (1, -1), 'GRP'],
        ),
    ),
    'EHC_E15_PSL_ITEM_INFO': (
        'sequence',
        (
            ['PSL', SEGMENTS['PSL'], (1, 1), 'SEG'],
            ['ADJ', SEGMENTS['ADJ'], (0, -1), 'SEG'],
        ),
    ),
    'EHC_E20_AUTHORIZATION_REQUEST': (
        'choice',
        (
            ['IVC', SEGMENTS['IVC'], (1, 1), 'SEG'],
            ['CTD', SEGMENTS['CTD'], (1, -1), 'SEG'],
            ['LOC', SEGMENTS['LOC'], (0, -1), 'SEG'],
            ['ROL', SEGMENTS['ROL'], (0, -1), 'SEG'],
            ['EHC_E20_PAT_INFO', None, (1, -1), 'GRP'],
            ['EHC_E20_PSL_ITEM_INFO', None, (1, -1), 'GRP'],
        ),
    ),
    'EHC_E20_DIAGNOSIS': (
        'sequence',
        (
            ['DG1', SEGMENTS['DG1'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'EHC_E20_INSURANCE': (
        'sequence',
        (
            ['IN1', SEGMENTS['IN1'], (1, 1), 'SEG'],
            ['IN2', SEGMENTS['IN2'], (0, 1), 'SEG'],
        ),
    ),
    'EHC_E20_PAT_INFO': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['ACC', SEGMENTS['ACC'], (0, -1), 'SEG'],
            ['EHC_E20_INSURANCE', None, (1, -1), 'GRP'],
            ['EHC_E20_DIAGNOSIS', None, (0, -1), 'GRP'],
            ['OBX', SEGMENTS['OBX'], (0, -1), 'SEG'],
        ),
    ),
    'EHC_E20_PSL_ITEM_INFO': (
        'sequence',
        (
            ['PSL', SEGMENTS['PSL'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['ADJ', SEGMENTS['ADJ'], (0, -1), 'SEG'],
            ['LOC', SEGMENTS['LOC'], (0, -1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ROL', SEGMENTS['ROL'], (0, -1), 'SEG'],
        ),
    ),
    'EHC_E21_AUTHORIZATION_REQUEST': (
        'choice',
        (
            ['IVC', SEGMENTS['IVC'], (1, 1), 'SEG'],
            ['EHC_E21_PSL_ITEM_INFO', None, (1, -1), 'GRP'],
        ),
    ),
    'EHC_E21_PSL_ITEM_INFO': (
        'sequence',
        (
            ['PSL', SEGMENTS['PSL'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['AUT', SEGMENTS['AUT'], (0, 1), 'SEG'],
        ),
    ),
    'EHC_E24_AUTHORIZATION_RESPONSE_INFO': (
        'choice',
        (
            ['IVC', SEGMENTS['IVC'], (1, 1), 'SEG'],
            ['EHC_E24_PSL_ITEM_INFO', None, (1, -1), 'GRP'],
        ),
    ),
    'EHC_E24_PSL_ITEM_INFO': (
        'sequence',
        (
            ['PSL', SEGMENTS['PSL'], (1, 1), 'SEG'],
            ['AUT', SEGMENTS['AUT'], (0, 1), 'SEG'],
            ['ADJ', SEGMENTS['ADJ'], (0, -1), 'SEG'],
        ),
    ),
    'MDM_T01_COMMON_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['MDM_T01_TIMING', None, (0, -1), 'GRP'],
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'MDM_T01_TIMING': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'MDM_T02_COMMON_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['MDM_T02_TIMING', None, (0, -1), 'GRP'],
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'MDM_T02_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'MDM_T02_TIMING': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'MFN_M02_MF_STAFF': (
        'sequence',
        (
            ['MFE', SEGMENTS['MFE'], (1, 1), 'SEG'],
            ['STF', SEGMENTS['STF'], (1, 1), 'SEG'],
            ['PRA', SEGMENTS['PRA'], (0, -1), 'SEG'],
            ['ORG', SEGMENTS['ORG'], (0, -1), 'SEG'],
            ['AFF', SEGMENTS['AFF'], (0, -1), 'SEG'],
            ['LAN', SEGMENTS['LAN'], (0, -1), 'SEG'],
            ['EDU', SEGMENTS['EDU'], (0, -1), 'SEG'],
            ['CER', SEGMENTS['CER'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'MFN_M04_MF_CDM': (
        'sequence',
        (
            ['MFE', SEGMENTS['MFE'], (1, 1), 'SEG'],
            ['CDM', SEGMENTS['CDM'], (1, 1), 'SEG'],
            ['PRC', SEGMENTS['PRC'], (0, -1), 'SEG'],
        ),
    ),
    'MFN_M05_MF_LOCATION': (
        'sequence',
        (
            ['MFE', SEGMENTS['MFE'], (1, 1), 'SEG'],
            ['LOC', SEGMENTS['LOC'], (1, 1), 'SEG'],
            ['LCH', SEGMENTS['LCH'], (0, -1), 'SEG'],
            ['LRL', SEGMENTS['LRL'], (0, -1), 'SEG'],
            ['MFN_M05_MF_LOC_DEPT', None, (1, -1), 'GRP'],
        ),
    ),
    'MFN_M05_MF_LOC_DEPT': (
        'sequence',
        (
            ['LDP', SEGMENTS['LDP'], (1, 1), 'SEG'],
            ['LCH', SEGMENTS['LCH'], (0, -1), 'SEG'],
            ['LCC', SEGMENTS['LCC'], (0, -1), 'SEG'],
        ),
    ),
    'MFN_M06_MF_CLIN_STUDY': (
        'sequence',
        (
            ['MFE', SEGMENTS['MFE'], (1, 1), 'SEG'],
            ['CM0', SEGMENTS['CM0'], (1, 1), 'SEG'],
            ['MFN_M06_MF_PHASE_SCHED_DETAIL', None, (0, -1), 'GRP'],
        ),
    ),
    'MFN_M06_MF_PHASE_SCHED_DETAIL': (
        'sequence',
        (
            ['CM1', SEGMENTS['CM1'], (1, 1), 'SEG'],
            ['CM2', SEGMENTS['CM2'], (0, -1), 'SEG'],
        ),
    ),
    'MFN_M07_MF_CLIN_STUDY_SCHED': (
        'sequence',
        (
            ['MFE', SEGMENTS['MFE'], (1, 1), 'SEG'],
            ['CM0', SEGMENTS['CM0'], (1, 1), 'SEG'],
            ['CM2', SEGMENTS['CM2'], (0, -1), 'SEG'],
        ),
    ),
    'MFN_M08_MF_TEST_NUMERIC': (
        'sequence',
        (
            ['MFE', SEGMENTS['MFE'], (1, 1), 'SEG'],
            ['OM1', SEGMENTS['OM1'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['OM2', SEGMENTS['OM2'], (0, 1), 'SEG'],
            ['OM3', SEGMENTS['OM3'], (0, 1), 'SEG'],
            ['OM4', SEGMENTS['OM4'], (0, -1), 'SEG'],
        ),
    ),
    'MFN_M09_MF_TEST_CATEGORICAL': (
        'sequence',
        (
            ['MFE', SEGMENTS['MFE'], (1, 1), 'SEG'],
            ['OM1', SEGMENTS['OM1'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['MFN_M09_MF_TEST_CAT_DETAIL', None, (0, 1), 'GRP'],
        ),
    ),
    'MFN_M09_MF_TEST_CAT_DETAIL': (
        'sequence',
        (
            ['OM3', SEGMENTS['OM3'], (1, 1), 'SEG'],
            ['OM4', SEGMENTS['OM4'], (0, -1), 'SEG'],
        ),
    ),
    'MFN_M10_MF_TEST_BATTERIES': (
        'sequence',
        (
            ['MFE', SEGMENTS['MFE'], (1, 1), 'SEG'],
            ['OM1', SEGMENTS['OM1'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['MFN_M10_MF_TEST_BATT_DETAIL', None, (0, 1), 'GRP'],
        ),
    ),
    'MFN_M10_MF_TEST_BATT_DETAIL': (
        'sequence',
        (
            ['OM5', SEGMENTS['OM5'], (1, 1), 'SEG'],
            ['OM4', SEGMENTS['OM4'], (0, -1), 'SEG'],
        ),
    ),
    'MFN_M11_MF_TEST_CALCULATED': (
        'sequence',
        (
            ['MFE', SEGMENTS['MFE'], (1, 1), 'SEG'],
            ['OM1', SEGMENTS['OM1'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['MFN_M11_MF_TEST_CALC_DETAIL', None, (0, 1), 'GRP'],
        ),
    ),
    'MFN_M11_MF_TEST_CALC_DETAIL': (
        'sequence',
        (
            ['OM6', SEGMENTS['OM6'], (1, 1), 'SEG'],
            ['OM2', SEGMENTS['OM2'], (1, 1), 'SEG'],
        ),
    ),
    'MFN_M12_MF_OBS_ATTRIBUTES': (
        'sequence',
        (
            ['MFE', SEGMENTS['MFE'], (1, 1), 'SEG'],
            ['OM1', SEGMENTS['OM1'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['MFN_M12_MF_OBS_OTHER_ATTRIBUTES', None, (0, 1), 'GRP'],
        ),
    ),
    'MFN_M12_MF_OBS_OTHER_ATTRIBUTES': (
        'sequence',
        (
            ['OM7', SEGMENTS['OM7'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'MFN_M15_MF_INV_ITEM': (
        'sequence',
        (
            ['MFE', SEGMENTS['MFE'], (1, 1), 'SEG'],
            ['IIM', SEGMENTS['IIM'], (1, 1), 'SEG'],
        ),
    ),
    'MFN_M16_MATERIAL_ITEM_RECORD': (
        'sequence',
        (
            ['MFE', SEGMENTS['MFE'], (1, 1), 'SEG'],
            ['ITM', SEGMENTS['ITM'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['MFN_M16_STERILIZATION', None, (0, -1), 'GRP'],
            ['MFN_M16_PURCHASING_VENDOR', None, (0, -1), 'GRP'],
            ['MFN_M16_MATERIAL_LOCATION', None, (0, -1), 'GRP'],
        ),
    ),
    'MFN_M16_MATERIAL_LOCATION': (
        'sequence',
        (
            ['IVT', SEGMENTS['IVT'], (1, 1), 'SEG'],
            ['ILT', SEGMENTS['ILT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'MFN_M16_PACKAGING': (
        'sequence',
        (
            ['PKG', SEGMENTS['PKG'], (1, 1), 'SEG'],
            ['PCE', SEGMENTS['PCE'], (0, -1), 'SEG'],
        ),
    ),
    'MFN_M16_PURCHASING_VENDOR': (
        'sequence',
        (
            ['VND', SEGMENTS['VND'], (1, 1), 'SEG'],
            ['MFN_M16_PACKAGING', None, (0, -1), 'GRP'],
        ),
    ),
    'MFN_M16_STERILIZATION': (
        'sequence',
        (
            ['STZ', SEGMENTS['STZ'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'MFN_M17_MF_DRG': (
        'sequence',
        (
            ['MFE', SEGMENTS['MFE'], (1, 1), 'SEG'],
            ['DMI', SEGMENTS['DMI'], (1, 1), 'SEG'],
        ),
    ),
    'MFN_ZNN': (
        'sequence',
        (
            ['MSH', SEGMENTS['MSH'], (1, 1), 'SEG'],
            ['SFT', SEGMENTS['SFT'], (0, -1), 'SEG'],
            ['UAC', SEGMENTS['UAC'], (0, 1), 'SEG'],
            ['MFI', SEGMENTS['MFI'], (1, 1), 'SEG'],
            ['MFN_ZNN_MF_SITE_DEFINED', None, (1, -1), 'GRP'],
        ),
    ),
    'MFN_ZNN_MF_SITE_DEFINED': (
        'sequence',
        (
            ['MFE', SEGMENTS['MFE'], (1, 1), 'SEG'],
            ['ANYHL7SEGMENT', SEGMENTS['ANYHL7SEGMENT'], (1, 1), 'SEG'],
        ),
    ),
    'NMD_N02_APP_STATS': (
        'sequence',
        (
            ['NST', SEGMENTS['NST'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'NMD_N02_APP_STATUS': (
        'sequence',
        (
            ['NSC', SEGMENTS['NSC'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'NMD_N02_CLOCK': (
        'sequence',
        (
            ['NCK', SEGMENTS['NCK'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'NMD_N02_CLOCK_AND_STATS_WITH_NOTES': (
        'sequence',
        (
            ['NMD_N02_CLOCK', None, (0, 1), 'GRP'],
            ['NMD_N02_APP_STATS', None, (0, 1), 'GRP'],
            ['NMD_N02_APP_STATUS', None, (0, 1), 'GRP'],
        ),
    ),
    'OMB_O27_INSURANCE': (
        'sequence',
        (
            ['IN1', SEGMENTS['IN1'], (1, 1), 'SEG'],
            ['IN2', SEGMENTS['IN2'], (0, 1), 'SEG'],
            ['IN3', SEGMENTS['IN3'], (0, 1), 'SEG'],
        ),
    ),
    'OMB_O27_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'OMB_O27_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['OMB_O27_TIMING', None, (0, -1), 'GRP'],
            ['BPO', SEGMENTS['BPO'], (1, 1), 'SEG'],
            ['SPM', SEGMENTS['SPM'], (0, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['DG1', SEGMENTS['DG1'], (0, -1), 'SEG'],
            ['OMB_O27_OBSERVATION', None, (0, -1), 'GRP'],
            ['FT1', SEGMENTS['FT1'], (0, -1), 'SEG'],
            ['BLG', SEGMENTS['BLG'], (0, 1), 'SEG'],
        ),
    ),
    'OMB_O27_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['OMB_O27_PATIENT_VISIT', None, (0, 1), 'GRP'],
            ['OMB_O27_INSURANCE', None, (0, -1), 'GRP'],
            ['GT1', SEGMENTS['GT1'], (0, 1), 'SEG'],
            ['AL1', SEGMENTS['AL1'], (0, -1), 'SEG'],
        ),
    ),
    'OMB_O27_PATIENT_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'OMB_O27_TIMING': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'OMD_O03_DIET': (
        'sequence',
        (
            ['ODS', SEGMENTS['ODS'], (1, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['OMD_O03_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'OMD_O03_INSURANCE': (
        'sequence',
        (
            ['IN1', SEGMENTS['IN1'], (1, 1), 'SEG'],
            ['IN2', SEGMENTS['IN2'], (0, 1), 'SEG'],
            ['IN3', SEGMENTS['IN3'], (0, 1), 'SEG'],
        ),
    ),
    'OMD_O03_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'OMD_O03_ORDER_DIET': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['OMD_O03_TIMING_DIET', None, (0, -1), 'GRP'],
            ['OMD_O03_DIET', None, (0, 1), 'GRP'],
        ),
    ),
    'OMD_O03_ORDER_TRAY': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['OMD_O03_TIMING_TRAY', None, (0, -1), 'GRP'],
            ['ODT', SEGMENTS['ODT'], (1, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'OMD_O03_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['OMD_O03_PATIENT_VISIT', None, (0, 1), 'GRP'],
            ['OMD_O03_INSURANCE', None, (0, -1), 'GRP'],
            ['GT1', SEGMENTS['GT1'], (0, 1), 'SEG'],
            ['AL1', SEGMENTS['AL1'], (0, -1), 'SEG'],
        ),
    ),
    'OMD_O03_PATIENT_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'OMD_O03_TIMING_DIET': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'OMD_O03_TIMING_TRAY': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'OMG_O19_CONTAINER': (
        'sequence',
        (
            ['SAC', SEGMENTS['SAC'], (1, 1), 'SEG'],
            ['OMG_O19_CONTAINER_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'OMG_O19_CONTAINER_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'OMG_O19_INSURANCE': (
        'sequence',
        (
            ['IN1', SEGMENTS['IN1'], (1, 1), 'SEG'],
            ['IN2', SEGMENTS['IN2'], (0, 1), 'SEG'],
            ['IN3', SEGMENTS['IN3'], (0, 1), 'SEG'],
        ),
    ),
    'OMG_O19_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'OMG_O19_OBSERVATION_PRIOR': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'OMG_O19_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['OMG_O19_TIMING', None, (0, -1), 'GRP'],
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['CTD', SEGMENTS['CTD'], (0, 1), 'SEG'],
            ['DG1', SEGMENTS['DG1'], (0, -1), 'SEG'],
            ['OMG_O19_OBSERVATION', None, (0, -1), 'GRP'],
            ['OMG_O19_SPECIMEN', None, (0, -1), 'GRP'],
            ['OMG_O19_PRIOR_RESULT', None, (0, -1), 'GRP'],
            ['FT1', SEGMENTS['FT1'], (0, -1), 'SEG'],
            ['CTI', SEGMENTS['CTI'], (0, -1), 'SEG'],
            ['BLG', SEGMENTS['BLG'], (0, 1), 'SEG'],
        ),
    ),
    'OMG_O19_ORDER_PRIOR': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['OMG_O19_TIMING_PRIOR', None, (0, -1), 'GRP'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['CTD', SEGMENTS['CTD'], (0, 1), 'SEG'],
            ['OMG_O19_OBSERVATION_PRIOR', None, (1, -1), 'GRP'],
        ),
    ),
    'OMG_O19_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['NK1', SEGMENTS['NK1'], (0, -1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
            ['OMG_O19_PATIENT_VISIT', None, (0, 1), 'GRP'],
            ['OMG_O19_INSURANCE', None, (0, -1), 'GRP'],
            ['GT1', SEGMENTS['GT1'], (0, 1), 'SEG'],
            ['AL1', SEGMENTS['AL1'], (0, -1), 'SEG'],
        ),
    ),
    'OMG_O19_PATIENT_PRIOR': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'OMG_O19_PATIENT_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'OMG_O19_PATIENT_VISIT_PRIOR': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'OMG_O19_PRIOR_RESULT': (
        'sequence',
        (
            ['OMG_O19_PATIENT_PRIOR', None, (0, 1), 'GRP'],
            ['OMG_O19_PATIENT_VISIT_PRIOR', None, (0, 1), 'GRP'],
            ['AL1', SEGMENTS['AL1'], (0, -1), 'SEG'],
            ['OMG_O19_ORDER_PRIOR', None, (1, -1), 'GRP'],
        ),
    ),
    'OMG_O19_SPECIMEN': (
        'sequence',
        (
            ['SPM', SEGMENTS['SPM'], (1, 1), 'SEG'],
            ['OMG_O19_SPECIMEN_OBSERVATION', None, (0, -1), 'GRP'],
            ['OMG_O19_CONTAINER', None, (0, -1), 'GRP'],
        ),
    ),
    'OMG_O19_SPECIMEN_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'OMG_O19_TIMING': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'OMG_O19_TIMING_PRIOR': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'OMI_O23_INSURANCE': (
        'sequence',
        (
            ['IN1', SEGMENTS['IN1'], (1, 1), 'SEG'],
            ['IN2', SEGMENTS['IN2'], (0, 1), 'SEG'],
            ['IN3', SEGMENTS['IN3'], (0, 1), 'SEG'],
        ),
    ),
    'OMI_O23_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'OMI_O23_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['OMI_O23_TIMING', None, (0, -1), 'GRP'],
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['CTD', SEGMENTS['CTD'], (0, 1), 'SEG'],
            ['DG1', SEGMENTS['DG1'], (0, -1), 'SEG'],
            ['OMI_O23_OBSERVATION', None, (0, -1), 'GRP'],
            ['IPC', SEGMENTS['IPC'], (1, -1), 'SEG'],
        ),
    ),
    'OMI_O23_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['OMI_O23_PATIENT_VISIT', None, (0, 1), 'GRP'],
            ['OMI_O23_INSURANCE', None, (0, -1), 'GRP'],
            ['GT1', SEGMENTS['GT1'], (0, 1), 'SEG'],
            ['AL1', SEGMENTS['AL1'], (0, -1), 'SEG'],
        ),
    ),
    'OMI_O23_PATIENT_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'OMI_O23_TIMING': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'OML_O21_CONTAINER': (
        'sequence',
        (
            ['SAC', SEGMENTS['SAC'], (1, 1), 'SEG'],
            ['OML_O21_CONTAINER_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'OML_O21_CONTAINER_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'OML_O21_INSURANCE': (
        'sequence',
        (
            ['IN1', SEGMENTS['IN1'], (1, 1), 'SEG'],
            ['IN2', SEGMENTS['IN2'], (0, 1), 'SEG'],
            ['IN3', SEGMENTS['IN3'], (0, 1), 'SEG'],
        ),
    ),
    'OML_O21_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['TCD', SEGMENTS['TCD'], (0, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'OML_O21_OBSERVATION_PRIOR': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'OML_O21_OBSERVATION_REQUEST': (
        'sequence',
        (
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['TCD', SEGMENTS['TCD'], (0, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['CTD', SEGMENTS['CTD'], (0, 1), 'SEG'],
            ['DG1', SEGMENTS['DG1'], (0, -1), 'SEG'],
            ['OML_O21_OBSERVATION', None, (0, -1), 'GRP'],
            ['OML_O21_SPECIMEN', None, (0, -1), 'GRP'],
            ['OML_O21_PRIOR_RESULT', None, (0, -1), 'GRP'],
        ),
    ),
    'OML_O21_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['OML_O21_TIMING', None, (0, -1), 'GRP'],
            ['OML_O21_OBSERVATION_REQUEST', None, (0, 1), 'GRP'],
            ['FT1', SEGMENTS['FT1'], (0, -1), 'SEG'],
            ['CTI', SEGMENTS['CTI'], (0, -1), 'SEG'],
            ['BLG', SEGMENTS['BLG'], (0, 1), 'SEG'],
        ),
    ),
    'OML_O21_ORDER_PRIOR': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['OML_O21_TIMING_PRIOR', None, (0, -1), 'GRP'],
            ['OML_O21_OBSERVATION_PRIOR', None, (1, -1), 'GRP'],
        ),
    ),
    'OML_O21_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['NK1', SEGMENTS['NK1'], (0, -1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
            ['OML_O21_PATIENT_VISIT', None, (0, 1), 'GRP'],
            ['OML_O21_INSURANCE', None, (0, -1), 'GRP'],
            ['GT1', SEGMENTS['GT1'], (0, 1), 'SEG'],
            ['AL1', SEGMENTS['AL1'], (0, -1), 'SEG'],
        ),
    ),
    'OML_O21_PATIENT_PRIOR': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
        ),
    ),
    'OML_O21_PATIENT_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'OML_O21_PATIENT_VISIT_PRIOR': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'OML_O21_PRIOR_RESULT': (
        'sequence',
        (
            ['OML_O21_PATIENT_PRIOR', None, (0, 1), 'GRP'],
            ['OML_O21_PATIENT_VISIT_PRIOR', None, (0, 1), 'GRP'],
            ['AL1', SEGMENTS['AL1'], (0, -1), 'SEG'],
            ['OML_O21_ORDER_PRIOR', None, (1, -1), 'GRP'],
        ),
    ),
    'OML_O21_SPECIMEN': (
        'sequence',
        (
            ['SPM', SEGMENTS['SPM'], (1, 1), 'SEG'],
            ['OML_O21_SPECIMEN_OBSERVATION', None, (0, -1), 'GRP'],
            ['OML_O21_CONTAINER', None, (0, -1), 'GRP'],
        ),
    ),
    'OML_O21_SPECIMEN_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'OML_O21_TIMING': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'OML_O21_TIMING_PRIOR': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'OML_O33_INSURANCE': (
        'sequence',
        (
            ['IN1', SEGMENTS['IN1'], (1, 1), 'SEG'],
            ['IN2', SEGMENTS['IN2'], (0, 1), 'SEG'],
            ['IN3', SEGMENTS['IN3'], (0, 1), 'SEG'],
        ),
    ),
    'OML_O33_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['TCD', SEGMENTS['TCD'], (0, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'OML_O33_OBSERVATION_PRIOR': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'OML_O33_OBSERVATION_REQUEST': (
        'sequence',
        (
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['TCD', SEGMENTS['TCD'], (0, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['DG1', SEGMENTS['DG1'], (0, -1), 'SEG'],
            ['OML_O33_OBSERVATION', None, (0, -1), 'GRP'],
            ['OML_O33_PRIOR_RESULT', None, (0, -1), 'GRP'],
        ),
    ),
    'OML_O33_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['OML_O33_TIMING', None, (0, -1), 'GRP'],
            ['OML_O33_OBSERVATION_REQUEST', None, (0, 1), 'GRP'],
            ['FT1', SEGMENTS['FT1'], (0, -1), 'SEG'],
            ['CTI', SEGMENTS['CTI'], (0, -1), 'SEG'],
            ['BLG', SEGMENTS['BLG'], (0, 1), 'SEG'],
        ),
    ),
    'OML_O33_ORDER_PRIOR': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['OML_O33_TIMING_PRIOR', None, (0, -1), 'GRP'],
            ['OML_O33_OBSERVATION_PRIOR', None, (1, -1), 'GRP'],
        ),
    ),
    'OML_O33_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['NK1', SEGMENTS['NK1'], (0, -1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
            ['OML_O33_PATIENT_VISIT', None, (0, 1), 'GRP'],
            ['OML_O33_INSURANCE', None, (0, -1), 'GRP'],
            ['GT1', SEGMENTS['GT1'], (0, 1), 'SEG'],
            ['AL1', SEGMENTS['AL1'], (0, -1), 'SEG'],
        ),
    ),
    'OML_O33_PATIENT_PRIOR': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
        ),
    ),
    'OML_O33_PATIENT_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'OML_O33_PATIENT_VISIT_PRIOR': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'OML_O33_PRIOR_RESULT': (
        'sequence',
        (
            ['OML_O33_PATIENT_PRIOR', None, (0, 1), 'GRP'],
            ['OML_O33_PATIENT_VISIT_PRIOR', None, (0, 1), 'GRP'],
            ['AL1', SEGMENTS['AL1'], (0, -1), 'SEG'],
            ['OML_O33_ORDER_PRIOR', None, (1, -1), 'GRP'],
        ),
    ),
    'OML_O33_SPECIMEN': (
        'sequence',
        (
            ['SPM', SEGMENTS['SPM'], (1, 1), 'SEG'],
            ['OML_O33_SPECIMEN_OBSERVATION', None, (0, -1), 'GRP'],
            ['SAC', SEGMENTS['SAC'], (0, -1), 'SEG'],
            ['OML_O33_ORDER', None, (1, -1), 'GRP'],
        ),
    ),
    'OML_O33_SPECIMEN_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'OML_O33_TIMING': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'OML_O33_TIMING_PRIOR': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'OML_O35_INSURANCE': (
        'sequence',
        (
            ['IN1', SEGMENTS['IN1'], (1, 1), 'SEG'],
            ['IN2', SEGMENTS['IN2'], (0, 1), 'SEG'],
            ['IN3', SEGMENTS['IN3'], (0, 1), 'SEG'],
        ),
    ),
    'OML_O35_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['TCD', SEGMENTS['TCD'], (0, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'OML_O35_OBSERVATION_PRIOR': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'OML_O35_OBSERVATION_REQUEST': (
        'sequence',
        (
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['TCD', SEGMENTS['TCD'], (0, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['DG1', SEGMENTS['DG1'], (0, -1), 'SEG'],
            ['OML_O35_OBSERVATION', None, (0, -1), 'GRP'],
            ['OML_O35_PRIOR_RESULT', None, (0, -1), 'GRP'],
        ),
    ),
    'OML_O35_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['OML_O35_TIMING', None, (0, -1), 'GRP'],
            ['OML_O35_OBSERVATION_REQUEST', None, (0, 1), 'GRP'],
            ['FT1', SEGMENTS['FT1'], (0, -1), 'SEG'],
            ['CTI', SEGMENTS['CTI'], (0, -1), 'SEG'],
            ['BLG', SEGMENTS['BLG'], (0, 1), 'SEG'],
        ),
    ),
    'OML_O35_ORDER_PRIOR': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['OML_O35_TIMING_PRIOR', None, (0, -1), 'GRP'],
            ['OML_O35_OBSERVATION_PRIOR', None, (1, -1), 'GRP'],
        ),
    ),
    'OML_O35_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['NK1', SEGMENTS['NK1'], (0, -1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
            ['OML_O35_PATIENT_VISIT', None, (0, 1), 'GRP'],
            ['OML_O35_INSURANCE', None, (0, -1), 'GRP'],
            ['GT1', SEGMENTS['GT1'], (0, 1), 'SEG'],
            ['AL1', SEGMENTS['AL1'], (0, -1), 'SEG'],
        ),
    ),
    'OML_O35_PATIENT_PRIOR': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
        ),
    ),
    'OML_O35_PATIENT_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'OML_O35_PATIENT_VISIT_PRIOR': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'OML_O35_PRIOR_RESULT': (
        'sequence',
        (
            ['OML_O35_PATIENT_PRIOR', None, (0, 1), 'GRP'],
            ['OML_O35_PATIENT_VISIT_PRIOR', None, (0, 1), 'GRP'],
            ['AL1', SEGMENTS['AL1'], (0, -1), 'SEG'],
            ['OML_O35_ORDER_PRIOR', None, (1, -1), 'GRP'],
        ),
    ),
    'OML_O35_SPECIMEN': (
        'sequence',
        (
            ['SPM', SEGMENTS['SPM'], (1, 1), 'SEG'],
            ['OML_O35_SPECIMEN_OBSERVATION', None, (0, -1), 'GRP'],
            ['OML_O35_SPECIMEN_CONTAINER', None, (1, -1), 'GRP'],
        ),
    ),
    'OML_O35_SPECIMEN_CONTAINER': (
        'sequence',
        (
            ['SAC', SEGMENTS['SAC'], (1, 1), 'SEG'],
            ['OML_O35_ORDER', None, (1, -1), 'GRP'],
        ),
    ),
    'OML_O35_SPECIMEN_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'OML_O35_TIMING': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'OML_O35_TIMING_PRIOR': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'OML_O39_CONTAINER_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'OML_O39_INSURANCE': (
        'sequence',
        (
            ['IN1', SEGMENTS['IN1'], (1, 1), 'SEG'],
            ['IN2', SEGMENTS['IN2'], (0, 1), 'SEG'],
            ['IN3', SEGMENTS['IN3'], (0, 1), 'SEG'],
        ),
    ),
    'OML_O39_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['TCD', SEGMENTS['TCD'], (0, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'OML_O39_OBSERVATION_REQUEST': (
        'sequence',
        (
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['TCD', SEGMENTS['TCD'], (0, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['CTD', SEGMENTS['CTD'], (0, 1), 'SEG'],
            ['DG1', SEGMENTS['DG1'], (0, -1), 'SEG'],
            ['OML_O39_OBSERVATION', None, (0, -1), 'GRP'],
            ['OML_O39_SPECIMEN_SHIPMENT', None, (0, -1), 'GRP'],
        ),
    ),
    'OML_O39_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['OML_O39_TIMING', None, (0, -1), 'GRP'],
            ['OML_O39_OBSERVATION_REQUEST', None, (0, 1), 'GRP'],
            ['FT1', SEGMENTS['FT1'], (0, -1), 'SEG'],
            ['CTI', SEGMENTS['CTI'], (0, -1), 'SEG'],
            ['BLG', SEGMENTS['BLG'], (0, 1), 'SEG'],
        ),
    ),
    'OML_O39_PACKAGE': (
        'sequence',
        (
            ['PAC', SEGMENTS['PAC'], (1, 1), 'SEG'],
            ['OML_O39_SPECIMEN_IN_PACKAGE', None, (0, -1), 'GRP'],
        ),
    ),
    'OML_O39_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['NK1', SEGMENTS['NK1'], (0, -1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
            ['OML_O39_PATIENT_VISIT', None, (0, 1), 'GRP'],
            ['OML_O39_INSURANCE', None, (0, -1), 'GRP'],
            ['GT1', SEGMENTS['GT1'], (0, 1), 'SEG'],
            ['AL1', SEGMENTS['AL1'], (0, -1), 'SEG'],
        ),
    ),
    'OML_O39_PATIENT_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'OML_O39_SHIPMENT_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'OML_O39_SPECIMEN_CONTAINER_IN_PACKAGE': (
        'sequence',
        (
            ['SAC', SEGMENTS['SAC'], (1, 1), 'SEG'],
            ['OML_O39_CONTAINER_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'OML_O39_SPECIMEN_IN_PACKAGE': (
        'sequence',
        (
            ['SPM', SEGMENTS['SPM'], (1, 1), 'SEG'],
            ['OML_O39_SPECIMEN_OBSERVATION', None, (0, -1), 'GRP'],
            ['OML_O39_SPECIMEN_CONTAINER_IN_PACKAGE', None, (0, -1), 'GRP'],
        ),
    ),
    'OML_O39_SPECIMEN_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'OML_O39_SPECIMEN_SHIPMENT': (
        'sequence',
        (
            ['SHP', SEGMENTS['SHP'], (1, 1), 'SEG'],
            ['OML_O39_SHIPMENT_OBSERVATION', None, (0, -1), 'GRP'],
            ['OML_O39_PACKAGE', None, (1, -1), 'GRP'],
        ),
    ),
    'OML_O39_TIMING': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'OMN_O07_INSURANCE': (
        'sequence',
        (
            ['IN1', SEGMENTS['IN1'], (1, 1), 'SEG'],
            ['IN2', SEGMENTS['IN2'], (0, 1), 'SEG'],
            ['IN3', SEGMENTS['IN3'], (0, 1), 'SEG'],
        ),
    ),
    'OMN_O07_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'OMN_O07_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['OMN_O07_TIMING', None, (0, -1), 'GRP'],
            ['RQD', SEGMENTS['RQD'], (1, 1), 'SEG'],
            ['RQ1', SEGMENTS['RQ1'], (0, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['OMN_O07_OBSERVATION', None, (0, -1), 'GRP'],
            ['BLG', SEGMENTS['BLG'], (0, 1), 'SEG'],
        ),
    ),
    'OMN_O07_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['OMN_O07_PATIENT_VISIT', None, (0, 1), 'GRP'],
            ['OMN_O07_INSURANCE', None, (0, -1), 'GRP'],
            ['GT1', SEGMENTS['GT1'], (0, 1), 'SEG'],
            ['AL1', SEGMENTS['AL1'], (0, -1), 'SEG'],
        ),
    ),
    'OMN_O07_PATIENT_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'OMN_O07_TIMING': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'OMP_O09_ADDITIONAL_DEMOGRAPHICS': (
        'sequence',
        (
            ['PD1', SEGMENTS['PD1'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'OMP_O09_COMPONENT': (
        'sequence',
        (
            ['RXC', SEGMENTS['RXC'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'OMP_O09_INSURANCE': (
        'sequence',
        (
            ['IN1', SEGMENTS['IN1'], (1, 1), 'SEG'],
            ['IN2', SEGMENTS['IN2'], (0, 1), 'SEG'],
            ['IN3', SEGMENTS['IN3'], (0, 1), 'SEG'],
        ),
    ),
    'OMP_O09_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'OMP_O09_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['OMP_O09_TIMING', None, (0, -1), 'GRP'],
            ['RXO', SEGMENTS['RXO'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (1, -1), 'SEG'],
            ['OMP_O09_COMPONENT', None, (0, -1), 'GRP'],
            ['CDO', SEGMENTS['CDO'], (0, -1), 'SEG'],
            ['OMP_O09_OBSERVATION', None, (0, -1), 'GRP'],
            ['FT1', SEGMENTS['FT1'], (0, -1), 'SEG'],
            ['BLG', SEGMENTS['BLG'], (0, 1), 'SEG'],
        ),
    ),
    'OMP_O09_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['OMP_O09_ADDITIONAL_DEMOGRAPHICS', None, (0, 1), 'GRP'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
            ['OMP_O09_PATIENT_VISIT', None, (0, 1), 'GRP'],
            ['OMP_O09_INSURANCE', None, (0, -1), 'GRP'],
            ['GT1', SEGMENTS['GT1'], (0, 1), 'SEG'],
            ['AL1', SEGMENTS['AL1'], (0, -1), 'SEG'],
        ),
    ),
    'OMP_O09_PATIENT_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
        ),
    ),
    'OMP_O09_TIMING': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'OMQ_O42_INSURANCE': (
        'sequence',
        (
            ['IN1', SEGMENTS['IN1'], (1, 1), 'SEG'],
            ['IN2', SEGMENTS['IN2'], (0, 1), 'SEG'],
            ['IN3', SEGMENTS['IN3'], (0, 1), 'SEG'],
        ),
    ),
    'OMQ_O42_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'OMQ_O42_OBSERVATION_PRIOR': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'OMQ_O42_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['TXA', SEGMENTS['TXA'], (1, 1), 'SEG'],
            ['CTD', SEGMENTS['CTD'], (0, 1), 'SEG'],
            ['DG1', SEGMENTS['DG1'], (0, -1), 'SEG'],
            ['OMQ_O42_OBSERVATION', None, (0, -1), 'GRP'],
            ['OMQ_O42_PRIOR_RESULT', None, (0, -1), 'GRP'],
            ['FT1', SEGMENTS['FT1'], (0, -1), 'SEG'],
            ['CTI', SEGMENTS['CTI'], (0, -1), 'SEG'],
            ['BLG', SEGMENTS['BLG'], (0, 1), 'SEG'],
        ),
    ),
    'OMQ_O42_ORDER_PRIOR': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['OMQ_O42_TIMING_PRIOR', None, (0, -1), 'GRP'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['CTD', SEGMENTS['CTD'], (0, 1), 'SEG'],
            ['OMQ_O42_OBSERVATION_PRIOR', None, (1, -1), 'GRP'],
        ),
    ),
    'OMQ_O42_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['NK1', SEGMENTS['NK1'], (0, -1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
            ['OMQ_O42_PATIENT_VISIT', None, (0, 1), 'GRP'],
            ['OMQ_O42_INSURANCE', None, (0, -1), 'GRP'],
            ['GT1', SEGMENTS['GT1'], (0, 1), 'SEG'],
            ['AL1', SEGMENTS['AL1'], (0, -1), 'SEG'],
        ),
    ),
    'OMQ_O42_PATIENT_PRIOR': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
        ),
    ),
    'OMQ_O42_PATIENT_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'OMQ_O42_PATIENT_VISIT_PRIOR': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'OMQ_O42_PRIOR_RESULT': (
        'sequence',
        (
            ['OMQ_O42_PATIENT_PRIOR', None, (0, 1), 'GRP'],
            ['OMQ_O42_PATIENT_VISIT_PRIOR', None, (0, 1), 'GRP'],
            ['AL1', SEGMENTS['AL1'], (0, -1), 'SEG'],
            ['OMQ_O42_ORDER_PRIOR', None, (1, -1), 'GRP'],
        ),
    ),
    'OMQ_O42_TIMING_PRIOR': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'OMS_O05_INSURANCE': (
        'sequence',
        (
            ['IN1', SEGMENTS['IN1'], (1, 1), 'SEG'],
            ['IN2', SEGMENTS['IN2'], (0, 1), 'SEG'],
            ['IN3', SEGMENTS['IN3'], (0, 1), 'SEG'],
        ),
    ),
    'OMS_O05_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'OMS_O05_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['OMS_O05_TIMING', None, (0, -1), 'GRP'],
            ['RQD', SEGMENTS['RQD'], (1, 1), 'SEG'],
            ['RQ1', SEGMENTS['RQ1'], (0, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['OMS_O05_OBSERVATION', None, (0, -1), 'GRP'],
            ['BLG', SEGMENTS['BLG'], (0, 1), 'SEG'],
        ),
    ),
    'OMS_O05_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['OMS_O05_PATIENT_VISIT', None, (0, 1), 'GRP'],
            ['OMS_O05_INSURANCE', None, (0, -1), 'GRP'],
            ['GT1', SEGMENTS['GT1'], (0, 1), 'SEG'],
            ['AL1', SEGMENTS['AL1'], (0, -1), 'SEG'],
        ),
    ),
    'OMS_O05_PATIENT_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'OMS_O05_TIMING': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'OPL_O37_CONTAINER': (
        'sequence',
        (
            ['SAC', SEGMENTS['SAC'], (1, 1), 'SEG'],
            ['OPL_O37_CONTAINER_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'OPL_O37_CONTAINER_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'OPL_O37_GUARANTOR': (
        'sequence',
        (
            ['GT1', SEGMENTS['GT1'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'OPL_O37_INSURANCE': (
        'sequence',
        (
            ['IN1', SEGMENTS['IN1'], (1, 1), 'SEG'],
            ['IN2', SEGMENTS['IN2'], (0, 1), 'SEG'],
            ['IN3', SEGMENTS['IN3'], (0, 1), 'SEG'],
        ),
    ),
    'OPL_O37_OBSERVATIONS_ON_PATIENT': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'OPL_O37_OBSERVATION_REQUEST': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['OPL_O37_TIMING', None, (0, -1), 'GRP'],
            ['TCD', SEGMENTS['TCD'], (0, 1), 'SEG'],
            ['DG1', SEGMENTS['DG1'], (0, -1), 'SEG'],
            ['OPL_O37_ORDER_RELATED_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'OPL_O37_OBSERVATION_RESULT_GROUP': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'OPL_O37_ORDER': (
        'sequence',
        (
            ['NK1', SEGMENTS['NK1'], (1, -1), 'SEG'],
            ['OPL_O37_PATIENT', None, (0, 1), 'GRP'],
            ['OPL_O37_SPECIMEN', None, (1, -1), 'GRP'],
            ['OPL_O37_PRIOR_RESULT', None, (0, 1), 'GRP'],
            ['FT1', SEGMENTS['FT1'], (0, -1), 'SEG'],
            ['CTI', SEGMENTS['CTI'], (0, -1), 'SEG'],
            ['BLG', SEGMENTS['BLG'], (0, 1), 'SEG'],
        ),
    ),
    'OPL_O37_ORDER_PRIOR': (
        'sequence',
        (
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['ORC', SEGMENTS['ORC'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['OPL_O37_TIMING', None, (0, 1), 'GRP'],
            ['OPL_O37_OBSERVATION_RESULT_GROUP', None, (1, -1), 'GRP'],
        ),
    ),
    'OPL_O37_ORDER_RELATED_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'OPL_O37_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
            ['OPL_O37_OBSERVATIONS_ON_PATIENT', None, (0, -1), 'GRP'],
            ['OPL_O37_INSURANCE', None, (0, -1), 'GRP'],
            ['AL1', SEGMENTS['AL1'], (0, -1), 'SEG'],
        ),
    ),
    'OPL_O37_PATIENT_PRIOR': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
        ),
    ),
    'OPL_O37_PATIENT_VISIT_PRIOR': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'OPL_O37_PRIOR_RESULT': (
        'sequence',
        (
            ['NK1', SEGMENTS['NK1'], (1, -1), 'SEG'],
            ['OPL_O37_PATIENT_PRIOR', None, (0, 1), 'GRP'],
            ['OPL_O37_PATIENT_VISIT_PRIOR', None, (0, 1), 'GRP'],
            ['AL1', SEGMENTS['AL1'], (0, 1), 'SEG'],
            ['OPL_O37_ORDER_PRIOR', None, (1, -1), 'GRP'],
        ),
    ),
    'OPL_O37_SPECIMEN': (
        'sequence',
        (
            ['SPM', SEGMENTS['SPM'], (1, 1), 'SEG'],
            ['OPL_O37_SPECIMEN_OBSERVATION', None, (0, -1), 'GRP'],
            ['OPL_O37_CONTAINER', None, (0, -1), 'GRP'],
            ['OPL_O37_OBSERVATION_REQUEST', None, (1, -1), 'GRP'],
        ),
    ),
    'OPL_O37_SPECIMEN_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'OPL_O37_TIMING': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'OPR_O38_OBSERVATION_REQUEST': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'OPR_O38_ORDER': (
        'sequence',
        (
            ['NK1', SEGMENTS['NK1'], (1, -1), 'SEG'],
            ['PID', SEGMENTS['PID'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
            ['OPR_O38_SPECIMEN', None, (0, -1), 'GRP'],
        ),
    ),
    'OPR_O38_RESPONSE': ('sequence', (['OPR_O38_ORDER', None, (1, -1), 'GRP'],)),
    'OPR_O38_SPECIMEN': (
        'sequence',
        (
            ['SPM', SEGMENTS['SPM'], (1, 1), 'SEG'],
            ['OPR_O38_SPECIMEN_OBSERVATION', None, (0, -1), 'GRP'],
            ['SAC', SEGMENTS['SAC'], (0, -1), 'SEG'],
            ['OPR_O38_OBSERVATION_REQUEST', None, (0, -1), 'GRP'],
            ['OPR_O38_TIMING', None, (0, -1), 'GRP'],
        ),
    ),
    'OPR_O38_SPECIMEN_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'OPR_O38_TIMING': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'OPU_R25_ACCESSION_DETAIL': (
        'sequence',
        (
            ['NK1', SEGMENTS['NK1'], (1, -1), 'SEG'],
            ['OPU_R25_PATIENT', None, (0, 1), 'GRP'],
            ['OPU_R25_SPECIMEN', None, (1, -1), 'GRP'],
        ),
    ),
    'OPU_R25_COMMON_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'OPU_R25_CONTAINER': (
        'sequence',
        (
            ['SAC', SEGMENTS['SAC'], (1, 1), 'SEG'],
            ['INV', SEGMENTS['INV'], (0, 1), 'SEG'],
        ),
    ),
    'OPU_R25_ORDER': (
        'sequence',
        (
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['OPU_R25_COMMON_ORDER', None, (0, 1), 'GRP'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['OPU_R25_TIMING_QTY', None, (0, -1), 'GRP'],
            ['OPU_R25_RESULT', None, (1, -1), 'GRP'],
        ),
    ),
    'OPU_R25_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
            ['OPU_R25_PATIENT_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'OPU_R25_PATIENT_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'OPU_R25_PATIENT_VISIT_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'OPU_R25_RESULT': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'OPU_R25_SPECIMEN': (
        'sequence',
        (
            ['SPM', SEGMENTS['SPM'], (1, 1), 'SEG'],
            ['OPU_R25_SPECIMEN_OBSERVATION', None, (0, -1), 'GRP'],
            ['OPU_R25_CONTAINER', None, (0, -1), 'GRP'],
            ['OPU_R25_ORDER', None, (1, -1), 'GRP'],
        ),
    ),
    'OPU_R25_SPECIMEN_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'OPU_R25_TIMING_QTY': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'ORB_O28_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ORB_O28_TIMING', None, (0, -1), 'GRP'],
            ['BPO', SEGMENTS['BPO'], (0, 1), 'SEG'],
        ),
    ),
    'ORB_O28_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
            ['ORB_O28_ORDER', None, (0, -1), 'GRP'],
        ),
    ),
    'ORB_O28_RESPONSE': ('sequence', (['ORB_O28_PATIENT', None, (0, 1), 'GRP'],)),
    'ORB_O28_TIMING': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'ORD_O04_ORDER_DIET': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ORD_O04_TIMING_DIET', None, (0, -1), 'GRP'],
            ['ODS', SEGMENTS['ODS'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'ORD_O04_ORDER_TRAY': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ORD_O04_TIMING_TRAY', None, (0, -1), 'GRP'],
            ['ODT', SEGMENTS['ODT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'ORD_O04_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'ORD_O04_RESPONSE': (
        'sequence',
        (
            ['ORD_O04_PATIENT', None, (0, 1), 'GRP'],
            ['ORD_O04_ORDER_DIET', None, (1, -1), 'GRP'],
            ['ORD_O04_ORDER_TRAY', None, (0, -1), 'GRP'],
        ),
    ),
    'ORD_O04_TIMING_DIET': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'ORD_O04_TIMING_TRAY': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'ORG_O20_OBSERVATION_GROUP': (
        'sequence',
        (
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'ORG_O20_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ORG_O20_TIMING', None, (0, -1), 'GRP'],
            ['ORG_O20_OBSERVATION_GROUP', None, (0, 1), 'GRP'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['CTI', SEGMENTS['CTI'], (0, -1), 'SEG'],
            ['ORG_O20_SPECIMEN', None, (0, -1), 'GRP'],
        ),
    ),
    'ORG_O20_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
        ),
    ),
    'ORG_O20_RESPONSE': (
        'sequence',
        (
            ['ORG_O20_PATIENT', None, (0, 1), 'GRP'],
            ['ORG_O20_ORDER', None, (1, -1), 'GRP'],
        ),
    ),
    'ORG_O20_SPECIMEN': (
        'sequence',
        (
            ['SPM', SEGMENTS['SPM'], (1, 1), 'SEG'],
            ['SAC', SEGMENTS['SAC'], (0, -1), 'SEG'],
        ),
    ),
    'ORG_O20_TIMING': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'ORI_O24_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ORI_O24_TIMING', None, (0, -1), 'GRP'],
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['IPC', SEGMENTS['IPC'], (1, -1), 'SEG'],
        ),
    ),
    'ORI_O24_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'ORI_O24_RESPONSE': (
        'sequence',
        (
            ['ORI_O24_PATIENT', None, (0, 1), 'GRP'],
            ['ORI_O24_ORDER', None, (1, -1), 'GRP'],
        ),
    ),
    'ORI_O24_TIMING': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'ORL_O22_OBSERVATION_REQUEST': (
        'sequence',
        (
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ORL_O22_SPECIMEN', None, (0, -1), 'GRP'],
        ),
    ),
    'ORL_O22_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ORL_O22_TIMING', None, (0, -1), 'GRP'],
            ['ORL_O22_OBSERVATION_REQUEST', None, (0, 1), 'GRP'],
        ),
    ),
    'ORL_O22_RESPONSE': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
            ['ORL_O22_ORDER', None, (0, -1), 'GRP'],
        ),
    ),
    'ORL_O22_SPECIMEN': (
        'sequence',
        (
            ['SPM', SEGMENTS['SPM'], (1, 1), 'SEG'],
            ['SAC', SEGMENTS['SAC'], (0, -1), 'SEG'],
        ),
    ),
    'ORL_O22_TIMING': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'ORL_O34_OBSERVATION_REQUEST': (
        'sequence',
        (
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'ORL_O34_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ORL_O34_TIMING', None, (0, -1), 'GRP'],
            ['ORL_O34_OBSERVATION_REQUEST', None, (0, 1), 'GRP'],
        ),
    ),
    'ORL_O34_RESPONSE': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
            ['ORL_O34_SPECIMEN', None, (1, -1), 'GRP'],
        ),
    ),
    'ORL_O34_SPECIMEN': (
        'sequence',
        (
            ['SPM', SEGMENTS['SPM'], (1, 1), 'SEG'],
            ['ORL_O34_SPECIMEN_OBSERVATION', None, (0, -1), 'GRP'],
            ['SAC', SEGMENTS['SAC'], (0, -1), 'SEG'],
            ['ORL_O34_ORDER', None, (0, -1), 'GRP'],
        ),
    ),
    'ORL_O34_SPECIMEN_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'ORL_O34_TIMING': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'ORL_O36_OBSERVATION_REQUEST': (
        'sequence',
        (
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'ORL_O36_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ORL_O36_TIMING', None, (0, -1), 'GRP'],
            ['ORL_O36_OBSERVATION_REQUEST', None, (0, 1), 'GRP'],
        ),
    ),
    'ORL_O36_RESPONSE': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
            ['ORL_O36_SPECIMEN', None, (1, -1), 'GRP'],
        ),
    ),
    'ORL_O36_SPECIMEN': (
        'sequence',
        (
            ['SPM', SEGMENTS['SPM'], (1, 1), 'SEG'],
            ['ORL_O36_SPECIMEN_OBSERVATION', None, (0, -1), 'GRP'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['ORL_O36_SPECIMEN_CONTAINER', None, (1, -1), 'GRP'],
        ),
    ),
    'ORL_O36_SPECIMEN_CONTAINER': (
        'sequence',
        (
            ['SAC', SEGMENTS['SAC'], (1, 1), 'SEG'],
            ['ORL_O36_ORDER', None, (0, -1), 'GRP'],
        ),
    ),
    'ORL_O36_SPECIMEN_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'ORL_O36_TIMING': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'ORL_O40_OBSERVATION_REQUEST': (
        'sequence',
        (
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ORL_O40_SPECIMEN_SHIPMENT', None, (0, -1), 'GRP'],
        ),
    ),
    'ORL_O40_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ORL_O40_TIMING', None, (0, -1), 'GRP'],
            ['ORL_O40_OBSERVATION_REQUEST', None, (0, 1), 'GRP'],
        ),
    ),
    'ORL_O40_PACKAGE': (
        'sequence',
        (
            ['PAC', SEGMENTS['PAC'], (1, 1), 'SEG'],
            ['ORL_O40_SPECIMEN_IN_PACKAGE', None, (0, -1), 'GRP'],
        ),
    ),
    'ORL_O40_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
            ['ORL_O40_ORDER', None, (0, -1), 'GRP'],
        ),
    ),
    'ORL_O40_RESPONSE': ('sequence', (['ORL_O40_PATIENT', None, (0, 1), 'GRP'],)),
    'ORL_O40_SPECIMEN_CONTAINER_IN_PACKAGE': (
        'sequence',
        (['SAC', SEGMENTS['SAC'], (1, 1), 'SEG'],),
    ),
    'ORL_O40_SPECIMEN_IN_PACKAGE': (
        'sequence',
        (
            ['SPM', SEGMENTS['SPM'], (1, 1), 'SEG'],
            ['ORL_O40_SPECIMEN_CONTAINER_IN_PACKAGE', None, (0, -1), 'GRP'],
        ),
    ),
    'ORL_O40_SPECIMEN_SHIPMENT': (
        'sequence',
        (
            ['SHP', SEGMENTS['SHP'], (1, 1), 'SEG'],
            ['ORL_O40_PACKAGE', None, (1, -1), 'GRP'],
        ),
    ),
    'ORL_O40_TIMING': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'ORN_O08_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ORN_O08_TIMING', None, (0, -1), 'GRP'],
            ['RQD', SEGMENTS['RQD'], (1, 1), 'SEG'],
            ['RQ1', SEGMENTS['RQ1'], (0, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'ORN_O08_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'ORN_O08_RESPONSE': (
        'sequence',
        (
            ['ORN_O08_PATIENT', None, (0, 1), 'GRP'],
            ['ORN_O08_ORDER', None, (1, -1), 'GRP'],
        ),
    ),
    'ORN_O08_TIMING': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'ORP_O10_COMPONENT': (
        'sequence',
        (
            ['RXC', SEGMENTS['RXC'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'ORP_O10_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ORP_O10_TIMING', None, (0, -1), 'GRP'],
            ['ORP_O10_ORDER_DETAIL', None, (0, 1), 'GRP'],
        ),
    ),
    'ORP_O10_ORDER_DETAIL': (
        'sequence',
        (
            ['RXO', SEGMENTS['RXO'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (1, -1), 'SEG'],
            ['ORP_O10_COMPONENT', None, (0, -1), 'GRP'],
        ),
    ),
    'ORP_O10_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'ORP_O10_RESPONSE': (
        'sequence',
        (
            ['ORP_O10_PATIENT', None, (0, 1), 'GRP'],
            ['ORP_O10_ORDER', None, (1, -1), 'GRP'],
        ),
    ),
    'ORP_O10_TIMING': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'ORS_O06_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ORS_O06_TIMING', None, (0, -1), 'GRP'],
            ['RQD', SEGMENTS['RQD'], (1, 1), 'SEG'],
            ['RQ1', SEGMENTS['RQ1'], (0, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'ORS_O06_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'ORS_O06_RESPONSE': (
        'sequence',
        (
            ['ORS_O06_PATIENT', None, (0, 1), 'GRP'],
            ['ORS_O06_ORDER', None, (1, -1), 'GRP'],
        ),
    ),
    'ORS_O06_TIMING': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'ORU_R01_COMMON_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ORU_R01_ORDER_DOCUMENT', None, (0, 1), 'GRP'],
        ),
    ),
    'ORU_R01_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'ORU_R01_ORDER_DOCUMENT': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['TXA', SEGMENTS['TXA'], (1, 1), 'SEG'],
        ),
    ),
    'ORU_R01_ORDER_OBSERVATION': (
        'sequence',
        (
            ['ORU_R01_COMMON_ORDER', None, (0, 1), 'GRP'],
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ORU_R01_TIMING_QTY', None, (0, -1), 'GRP'],
            ['CTD', SEGMENTS['CTD'], (0, 1), 'SEG'],
            ['ORU_R01_OBSERVATION', None, (0, -1), 'GRP'],
            ['FT1', SEGMENTS['FT1'], (0, -1), 'SEG'],
            ['CTI', SEGMENTS['CTI'], (0, -1), 'SEG'],
            ['ORU_R01_SPECIMEN', None, (0, -1), 'GRP'],
        ),
    ),
    'ORU_R01_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['NK1', SEGMENTS['NK1'], (0, -1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
            ['ORU_R01_PATIENT_OBSERVATION', None, (0, -1), 'GRP'],
            ['ORU_R01_VISIT', None, (0, 1), 'GRP'],
        ),
    ),
    'ORU_R01_PATIENT_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'ORU_R01_PATIENT_RESULT': (
        'sequence',
        (
            ['ORU_R01_PATIENT', None, (0, 1), 'GRP'],
            ['ORU_R01_ORDER_OBSERVATION', None, (1, -1), 'GRP'],
        ),
    ),
    'ORU_R01_SPECIMEN': (
        'sequence',
        (
            ['SPM', SEGMENTS['SPM'], (1, 1), 'SEG'],
            ['ORU_R01_SPECIMEN_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'ORU_R01_SPECIMEN_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'ORU_R01_TIMING_QTY': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'ORU_R01_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'ORU_R30_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'ORU_R30_PATIENT_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'ORU_R30_TIMING_QTY': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'ORU_R30_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'ORX_O43_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['TXA', SEGMENTS['TXA'], (1, 1), 'SEG'],
            ['CTI', SEGMENTS['CTI'], (0, -1), 'SEG'],
        ),
    ),
    'ORX_O43_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
        ),
    ),
    'ORX_O43_RESPONSE': (
        'sequence',
        (
            ['ORX_O43_PATIENT', None, (0, 1), 'GRP'],
            ['ORX_O43_ORDER', None, (1, -1), 'GRP'],
        ),
    ),
    'OSM_R26_CONTAINER': (
        'sequence',
        (
            ['SAC', SEGMENTS['SAC'], (1, 1), 'SEG'],
            ['OSM_R26_CONTAINER_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'OSM_R26_CONTAINER_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'OSM_R26_PACKAGE': (
        'sequence',
        (
            ['PAC', SEGMENTS['PAC'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['OSM_R26_SPECIMEN', None, (0, -1), 'GRP'],
        ),
    ),
    'OSM_R26_PATIENT_INFORMATION': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'OSM_R26_PATIENT_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'OSM_R26_PATIENT_VISIT_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'OSM_R26_SHIPMENT': (
        'sequence',
        (
            ['SHP', SEGMENTS['SHP'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (1, -1), 'SEG'],
            ['OSM_R26_SHIPPING_OBSERVATION', None, (0, -1), 'GRP'],
            ['OSM_R26_PACKAGE', None, (1, -1), 'GRP'],
        ),
    ),
    'OSM_R26_SHIPPING_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'OSM_R26_SPECIMEN': (
        'sequence',
        (
            ['SPM', SEGMENTS['SPM'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['OSM_R26_SPECIMEN_OBSERVATION', None, (0, -1), 'GRP'],
            ['OSM_R26_CONTAINER', None, (0, -1), 'GRP'],
            ['OSM_R26_SUBJECT_PERSON_OR_ANIMAL_IDENTIFICATION', None, (0, 1), 'GRP'],
            [
                'OSM_R26_SUBJECT_POPULATION_OR_LOCATION_IDENTIFICATION',
                None,
                (0, 1),
                'GRP',
            ],
        ),
    ),
    'OSM_R26_SPECIMEN_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'OSM_R26_SUBJECT_PERSON_OR_ANIMAL_IDENTIFICATION': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
            ['OSM_R26_PATIENT_OBSERVATION', None, (0, -1), 'GRP'],
            ['NK1', SEGMENTS['NK1'], (0, -1), 'SEG'],
        ),
    ),
    'OSM_R26_SUBJECT_POPULATION_OR_LOCATION_IDENTIFICATION': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['OSM_R26_PATIENT_VISIT_OBSERVATION', None, (0, -1), 'GRP'],
            ['OSM_R26_PATIENT_INFORMATION', None, (0, 1), 'GRP'],
            ['NK1', SEGMENTS['NK1'], (0, -1), 'SEG'],
        ),
    ),
    'OSU_O41_ORDER_STATUS': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'OUL_R22_COMMON_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['OUL_R22_ORDER_DOCUMENT', None, (0, 1), 'GRP'],
        ),
    ),
    'OUL_R22_CONTAINER': (
        'sequence',
        (
            ['SAC', SEGMENTS['SAC'], (1, 1), 'SEG'],
            ['INV', SEGMENTS['INV'], (0, 1), 'SEG'],
        ),
    ),
    'OUL_R22_ORDER': (
        'sequence',
        (
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['OUL_R22_COMMON_ORDER', None, (0, 1), 'GRP'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['OUL_R22_TIMING_QTY', None, (0, -1), 'GRP'],
            ['OUL_R22_RESULT', None, (0, -1), 'GRP'],
            ['CTI', SEGMENTS['CTI'], (0, -1), 'SEG'],
        ),
    ),
    'OUL_R22_ORDER_DOCUMENT': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['TXA', SEGMENTS['TXA'], (1, 1), 'SEG'],
        ),
    ),
    'OUL_R22_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['OUL_R22_PATIENT_OBSERVATION', None, (0, -1), 'GRP'],
            ['OUL_R22_VISIT', None, (0, 1), 'GRP'],
        ),
    ),
    'OUL_R22_PATIENT_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'OUL_R22_RESULT': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['TCD', SEGMENTS['TCD'], (0, 1), 'SEG'],
            ['SID', SEGMENTS['SID'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'OUL_R22_SPECIMEN': (
        'sequence',
        (
            ['SPM', SEGMENTS['SPM'], (1, 1), 'SEG'],
            ['OUL_R22_SPECIMEN_OBSERVATION', None, (0, -1), 'GRP'],
            ['OUL_R22_CONTAINER', None, (0, -1), 'GRP'],
            ['OUL_R22_ORDER', None, (1, -1), 'GRP'],
        ),
    ),
    'OUL_R22_SPECIMEN_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'OUL_R22_TIMING_QTY': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'OUL_R22_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'OUL_R23_COMMON_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['OUL_R23_ORDER_DOCUMENT', None, (0, 1), 'GRP'],
        ),
    ),
    'OUL_R23_CONTAINER': (
        'sequence',
        (
            ['SAC', SEGMENTS['SAC'], (1, 1), 'SEG'],
            ['INV', SEGMENTS['INV'], (0, 1), 'SEG'],
            ['OUL_R23_ORDER', None, (1, -1), 'GRP'],
        ),
    ),
    'OUL_R23_ORDER': (
        'sequence',
        (
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['OUL_R23_COMMON_ORDER', None, (0, 1), 'GRP'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['OUL_R23_TIMING_QTY', None, (0, -1), 'GRP'],
            ['OUL_R23_RESULT', None, (0, -1), 'GRP'],
            ['CTI', SEGMENTS['CTI'], (0, -1), 'SEG'],
        ),
    ),
    'OUL_R23_ORDER_DOCUMENT': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['TXA', SEGMENTS['TXA'], (1, 1), 'SEG'],
        ),
    ),
    'OUL_R23_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['OUL_R23_PATIENT_OBSERVATION', None, (0, -1), 'GRP'],
            ['OUL_R23_VISIT', None, (0, 1), 'GRP'],
        ),
    ),
    'OUL_R23_PATIENT_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'OUL_R23_RESULT': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['TCD', SEGMENTS['TCD'], (0, 1), 'SEG'],
            ['SID', SEGMENTS['SID'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'OUL_R23_SPECIMEN': (
        'sequence',
        (
            ['SPM', SEGMENTS['SPM'], (1, 1), 'SEG'],
            ['OUL_R23_SPECIMEN_OBSERVATION', None, (0, -1), 'GRP'],
            ['OUL_R23_CONTAINER', None, (1, -1), 'GRP'],
        ),
    ),
    'OUL_R23_SPECIMEN_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'OUL_R23_TIMING_QTY': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'OUL_R23_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'OUL_R24_COMMON_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['OUL_R24_ORDER_DOCUMENT', None, (0, 1), 'GRP'],
        ),
    ),
    'OUL_R24_CONTAINER': (
        'sequence',
        (
            ['SAC', SEGMENTS['SAC'], (1, 1), 'SEG'],
            ['INV', SEGMENTS['INV'], (0, 1), 'SEG'],
        ),
    ),
    'OUL_R24_ORDER': (
        'sequence',
        (
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['OUL_R24_COMMON_ORDER', None, (0, 1), 'GRP'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['OUL_R24_TIMING_QTY', None, (0, -1), 'GRP'],
            ['OUL_R24_SPECIMEN', None, (0, -1), 'GRP'],
            ['OUL_R24_RESULT', None, (0, -1), 'GRP'],
            ['CTI', SEGMENTS['CTI'], (0, -1), 'SEG'],
        ),
    ),
    'OUL_R24_ORDER_DOCUMENT': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['TXA', SEGMENTS['TXA'], (1, 1), 'SEG'],
        ),
    ),
    'OUL_R24_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['OUL_R24_PATIENT_OBSERVATION', None, (0, -1), 'GRP'],
            ['OUL_R24_VISIT', None, (0, 1), 'GRP'],
        ),
    ),
    'OUL_R24_PATIENT_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'OUL_R24_RESULT': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['TCD', SEGMENTS['TCD'], (0, 1), 'SEG'],
            ['SID', SEGMENTS['SID'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'OUL_R24_SPECIMEN': (
        'sequence',
        (
            ['SPM', SEGMENTS['SPM'], (1, 1), 'SEG'],
            ['OUL_R24_SPECIMEN_OBSERVATION', None, (0, -1), 'GRP'],
            ['OUL_R24_CONTAINER', None, (0, -1), 'GRP'],
        ),
    ),
    'OUL_R24_SPECIMEN_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'OUL_R24_TIMING_QTY': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'OUL_R24_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'PEX_P07_ASSOCIATED_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'PEX_P07_ASSOCIATED_PERSON': (
        'sequence',
        (
            ['NK1', SEGMENTS['NK1'], (1, 1), 'SEG'],
            ['PEX_P07_ASSOCIATED_RX_ORDER', None, (0, 1), 'GRP'],
            ['PEX_P07_ASSOCIATED_RX_ADMIN', None, (0, -1), 'GRP'],
            ['PRB', SEGMENTS['PRB'], (0, -1), 'SEG'],
            ['PEX_P07_ASSOCIATED_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'PEX_P07_ASSOCIATED_RX_ADMIN': (
        'sequence',
        (
            ['RXA', SEGMENTS['RXA'], (1, 1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'PEX_P07_ASSOCIATED_RX_ORDER': (
        'sequence',
        (
            ['RXE', SEGMENTS['RXE'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['PEX_P07_NK1_TIMING_QTY', None, (1, -1), 'GRP'],
            ['RXR', SEGMENTS['RXR'], (0, -1), 'SEG'],
        ),
    ),
    'PEX_P07_EXPERIENCE': (
        'sequence',
        (
            ['PES', SEGMENTS['PES'], (1, 1), 'SEG'],
            ['PEX_P07_PEX_OBSERVATION', None, (1, -1), 'GRP'],
        ),
    ),
    'PEX_P07_NK1_TIMING_QTY': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'PEX_P07_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'PEX_P07_PEX_CAUSE': (
        'sequence',
        (
            ['PCR', SEGMENTS['PCR'], (1, 1), 'SEG'],
            ['PEX_P07_RX_ORDER', None, (0, 1), 'GRP'],
            ['PEX_P07_RX_ADMINISTRATION', None, (0, -1), 'GRP'],
            ['PRB', SEGMENTS['PRB'], (0, -1), 'SEG'],
            ['PEX_P07_OBSERVATION', None, (0, -1), 'GRP'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['PEX_P07_ASSOCIATED_PERSON', None, (0, 1), 'GRP'],
            ['PEX_P07_STUDY', None, (0, -1), 'GRP'],
        ),
    ),
    'PEX_P07_PEX_OBSERVATION': (
        'sequence',
        (
            ['PEO', SEGMENTS['PEO'], (1, 1), 'SEG'],
            ['PEX_P07_PEX_CAUSE', None, (1, -1), 'GRP'],
        ),
    ),
    'PEX_P07_RX_ADMINISTRATION': (
        'sequence',
        (
            ['RXA', SEGMENTS['RXA'], (1, 1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'PEX_P07_RX_ORDER': (
        'sequence',
        (
            ['RXE', SEGMENTS['RXE'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['PEX_P07_TIMING_QTY', None, (1, -1), 'GRP'],
            ['RXR', SEGMENTS['RXR'], (0, -1), 'SEG'],
        ),
    ),
    'PEX_P07_STUDY': (
        'sequence',
        (
            ['CSR', SEGMENTS['CSR'], (1, 1), 'SEG'],
            ['CSP', SEGMENTS['CSP'], (0, -1), 'SEG'],
        ),
    ),
    'PEX_P07_TIMING_QTY': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'PEX_P07_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'PGL_PC6_CHOICE': (
        'choice',
        (
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['ANYHL7SEGMENT', SEGMENTS['ANYHL7SEGMENT'], (1, 1), 'SEG'],
        ),
    ),
    'PGL_PC6_GOAL': (
        'sequence',
        (
            ['GOL', SEGMENTS['GOL'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
            ['PGL_PC6_GOAL_ROLE', None, (0, -1), 'GRP'],
            ['PGL_PC6_PATHWAY', None, (0, -1), 'GRP'],
            ['PGL_PC6_OBSERVATION', None, (0, -1), 'GRP'],
            ['PGL_PC6_PROBLEM', None, (0, -1), 'GRP'],
            ['PGL_PC6_ORDER', None, (0, -1), 'GRP'],
        ),
    ),
    'PGL_PC6_GOAL_ROLE': (
        'sequence',
        (
            ['ROL', SEGMENTS['ROL'], (1, 1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
        ),
    ),
    'PGL_PC6_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'PGL_PC6_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PGL_PC6_ORDER_DETAIL', None, (0, 1), 'GRP'],
        ),
    ),
    'PGL_PC6_ORDER_DETAIL': (
        'sequence',
        (
            ['PGL_PC6_CHOICE', None, (1, 1), 'GRP'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
            ['PGL_PC6_ORDER_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'PGL_PC6_ORDER_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
        ),
    ),
    'PGL_PC6_PATHWAY': (
        'sequence',
        (
            ['PTH', SEGMENTS['PTH'], (1, 1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
        ),
    ),
    'PGL_PC6_PATIENT_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
        ),
    ),
    'PGL_PC6_PROBLEM': (
        'sequence',
        (
            ['PRB', SEGMENTS['PRB'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
            ['PGL_PC6_PROBLEM_ROLE', None, (0, -1), 'GRP'],
            ['PGL_PC6_PROBLEM_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'PGL_PC6_PROBLEM_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'PGL_PC6_PROBLEM_ROLE': (
        'sequence',
        (
            ['ROL', SEGMENTS['ROL'], (1, 1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
        ),
    ),
    'PMU_B07_CERTIFICATE': (
        'sequence',
        (
            ['CER', SEGMENTS['CER'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ROL', SEGMENTS['ROL'], (0, -1), 'SEG'],
        ),
    ),
    'PPG_PCG_CHOICE': (
        'choice',
        (
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['ANYHL7SEGMENT', SEGMENTS['ANYHL7SEGMENT'], (1, 1), 'SEG'],
        ),
    ),
    'PPG_PCG_GOAL': (
        'sequence',
        (
            ['GOL', SEGMENTS['GOL'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
            ['PPG_PCG_GOAL_ROLE', None, (0, -1), 'GRP'],
            ['PPG_PCG_GOAL_OBSERVATION', None, (0, -1), 'GRP'],
            ['PPG_PCG_PROBLEM', None, (0, -1), 'GRP'],
            ['PPG_PCG_ORDER', None, (0, -1), 'GRP'],
        ),
    ),
    'PPG_PCG_GOAL_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'PPG_PCG_GOAL_ROLE': (
        'sequence',
        (
            ['ROL', SEGMENTS['ROL'], (1, 1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
        ),
    ),
    'PPG_PCG_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PPG_PCG_ORDER_DETAIL', None, (0, 1), 'GRP'],
        ),
    ),
    'PPG_PCG_ORDER_DETAIL': (
        'sequence',
        (
            ['PPG_PCG_CHOICE', None, (1, 1), 'GRP'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
            ['PPG_PCG_ORDER_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'PPG_PCG_ORDER_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
        ),
    ),
    'PPG_PCG_PATHWAY': (
        'sequence',
        (
            ['PTH', SEGMENTS['PTH'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
            ['PPG_PCG_PATHWAY_ROLE', None, (0, -1), 'GRP'],
            ['PPG_PCG_GOAL', None, (0, -1), 'GRP'],
        ),
    ),
    'PPG_PCG_PATHWAY_ROLE': (
        'sequence',
        (
            ['ROL', SEGMENTS['ROL'], (1, 1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
        ),
    ),
    'PPG_PCG_PATIENT_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
        ),
    ),
    'PPG_PCG_PROBLEM': (
        'sequence',
        (
            ['PRB', SEGMENTS['PRB'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
            ['PPG_PCG_PROBLEM_ROLE', None, (0, -1), 'GRP'],
            ['PPG_PCG_PROBLEM_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'PPG_PCG_PROBLEM_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'PPG_PCG_PROBLEM_ROLE': (
        'sequence',
        (
            ['ROL', SEGMENTS['ROL'], (1, 1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
        ),
    ),
    'PPP_PCB_CHOICE': (
        'choice',
        (
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['ANYHL7SEGMENT', SEGMENTS['ANYHL7SEGMENT'], (1, 1), 'SEG'],
        ),
    ),
    'PPP_PCB_GOAL': (
        'sequence',
        (
            ['GOL', SEGMENTS['GOL'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
            ['PPP_PCB_GOAL_ROLE', None, (0, -1), 'GRP'],
            ['PPP_PCB_GOAL_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'PPP_PCB_GOAL_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'PPP_PCB_GOAL_ROLE': (
        'sequence',
        (
            ['ROL', SEGMENTS['ROL'], (1, 1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
        ),
    ),
    'PPP_PCB_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PPP_PCB_ORDER_DETAIL', None, (0, 1), 'GRP'],
        ),
    ),
    'PPP_PCB_ORDER_DETAIL': (
        'sequence',
        (
            ['PPP_PCB_CHOICE', None, (1, 1), 'GRP'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
            ['PPP_PCB_ORDER_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'PPP_PCB_ORDER_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
        ),
    ),
    'PPP_PCB_PATHWAY': (
        'sequence',
        (
            ['PTH', SEGMENTS['PTH'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
            ['PPP_PCB_PATHWAY_ROLE', None, (0, -1), 'GRP'],
            ['PPP_PCB_PROBLEM', None, (0, -1), 'GRP'],
        ),
    ),
    'PPP_PCB_PATHWAY_ROLE': (
        'sequence',
        (
            ['ROL', SEGMENTS['ROL'], (1, 1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
        ),
    ),
    'PPP_PCB_PATIENT_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
        ),
    ),
    'PPP_PCB_PROBLEM': (
        'sequence',
        (
            ['PRB', SEGMENTS['PRB'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
            ['PPP_PCB_PROBLEM_ROLE', None, (0, -1), 'GRP'],
            ['PPP_PCB_PROBLEM_OBSERVATION', None, (0, -1), 'GRP'],
            ['PPP_PCB_GOAL', None, (0, -1), 'GRP'],
            ['PPP_PCB_ORDER', None, (0, -1), 'GRP'],
        ),
    ),
    'PPP_PCB_PROBLEM_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'PPP_PCB_PROBLEM_ROLE': (
        'sequence',
        (
            ['ROL', SEGMENTS['ROL'], (1, 1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
        ),
    ),
    'PPR_PC1_CHOICE': (
        'choice',
        (
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['ANYHL7SEGMENT', SEGMENTS['ANYHL7SEGMENT'], (1, 1), 'SEG'],
        ),
    ),
    'PPR_PC1_GOAL': (
        'sequence',
        (
            ['GOL', SEGMENTS['GOL'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
            ['PPR_PC1_GOAL_ROLE', None, (0, -1), 'GRP'],
            ['PPR_PC1_GOAL_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'PPR_PC1_GOAL_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'PPR_PC1_GOAL_ROLE': (
        'sequence',
        (
            ['ROL', SEGMENTS['ROL'], (1, 1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
        ),
    ),
    'PPR_PC1_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PPR_PC1_ORDER_DETAIL', None, (0, 1), 'GRP'],
        ),
    ),
    'PPR_PC1_ORDER_DETAIL': (
        'sequence',
        (
            ['PPR_PC1_CHOICE', None, (1, 1), 'GRP'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
            ['PPR_PC1_ORDER_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'PPR_PC1_ORDER_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
        ),
    ),
    'PPR_PC1_PATHWAY': (
        'sequence',
        (
            ['PTH', SEGMENTS['PTH'], (1, 1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
        ),
    ),
    'PPR_PC1_PATIENT_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
        ),
    ),
    'PPR_PC1_PROBLEM': (
        'sequence',
        (
            ['PRB', SEGMENTS['PRB'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
            ['PPR_PC1_PROBLEM_ROLE', None, (0, -1), 'GRP'],
            ['PPR_PC1_PATHWAY', None, (0, -1), 'GRP'],
            ['PPR_PC1_PROBLEM_OBSERVATION', None, (0, -1), 'GRP'],
            ['PPR_PC1_GOAL', None, (0, -1), 'GRP'],
            ['PPR_PC1_ORDER', None, (0, -1), 'GRP'],
        ),
    ),
    'PPR_PC1_PROBLEM_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'PPR_PC1_PROBLEM_ROLE': (
        'sequence',
        (
            ['ROL', SEGMENTS['ROL'], (1, 1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
        ),
    ),
    'QBP_E03_QUERY_INFORMATION': (
        'choice',
        (
            ['QPD', SEGMENTS['QPD'], (1, 1), 'SEG'],
            ['RCP', SEGMENTS['RCP'], (1, 1), 'SEG'],
        ),
    ),
    'QBP_E22_QUERY': (
        'choice',
        (
            ['QPD', SEGMENTS['QPD'], (1, 1), 'SEG'],
            ['RCP', SEGMENTS['RCP'], (1, 1), 'SEG'],
        ),
    ),
    'QBP_Q11_QBP': (
        'sequence',
        (['ANYHL7SEGMENT', SEGMENTS['ANYHL7SEGMENT'], (0, 1), 'SEG'],),
    ),
    'QBP_QNN': (
        'sequence',
        (
            ['MSH', SEGMENTS['MSH'], (1, 1), 'SEG'],
            ['SFT', SEGMENTS['SFT'], (0, -1), 'SEG'],
            ['UAC', SEGMENTS['UAC'], (0, 1), 'SEG'],
            ['QPD', SEGMENTS['QPD'], (1, 1), 'SEG'],
            ['RDF', SEGMENTS['RDF'], (0, 1), 'SEG'],
            ['RCP', SEGMENTS['RCP'], (1, 1), 'SEG'],
            ['DSC', SEGMENTS['DSC'], (0, 1), 'SEG'],
        ),
    ),
    'QVR_Q17_QBP': (
        'sequence',
        (['ANYHL7SEGMENT', SEGMENTS['ANYHL7SEGMENT'], (0, 1), 'SEG'],),
    ),
    'RAS_O17_ADDITIONAL_DEMOGRAPHICS': (
        'sequence',
        (
            ['PD1', SEGMENTS['PD1'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'RAS_O17_ADMINISTRATION': (
        'sequence',
        (
            ['RXA', SEGMENTS['RXA'], (1, -1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (1, 1), 'SEG'],
            ['RAS_O17_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'RAS_O17_COMPONENTS': (
        'sequence',
        (
            ['RXC', SEGMENTS['RXC'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'RAS_O17_ENCODING': (
        'sequence',
        (
            ['RXE', SEGMENTS['RXE'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['RAS_O17_TIMING_ENCODED', None, (1, -1), 'GRP'],
            ['RXR', SEGMENTS['RXR'], (1, -1), 'SEG'],
            ['RXC', SEGMENTS['RXC'], (0, -1), 'SEG'],
            ['CDO', SEGMENTS['CDO'], (0, -1), 'SEG'],
        ),
    ),
    'RAS_O17_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'RAS_O17_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['RAS_O17_TIMING', None, (0, -1), 'GRP'],
            ['RAS_O17_ORDER_DETAIL', None, (0, 1), 'GRP'],
            ['RAS_O17_ENCODING', None, (0, 1), 'GRP'],
            ['RAS_O17_ADMINISTRATION', None, (1, -1), 'GRP'],
            ['CTI', SEGMENTS['CTI'], (0, -1), 'SEG'],
        ),
    ),
    'RAS_O17_ORDER_DETAIL': (
        'sequence',
        (
            ['RXO', SEGMENTS['RXO'], (1, 1), 'SEG'],
            ['RAS_O17_ORDER_DETAIL_SUPPLEMENT', None, (0, 1), 'GRP'],
        ),
    ),
    'RAS_O17_ORDER_DETAIL_SUPPLEMENT': (
        'sequence',
        (
            ['NTE', SEGMENTS['NTE'], (1, -1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (1, -1), 'SEG'],
            ['RAS_O17_COMPONENTS', None, (0, -1), 'GRP'],
        ),
    ),
    'RAS_O17_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['RAS_O17_ADDITIONAL_DEMOGRAPHICS', None, (0, 1), 'GRP'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
            ['AL1', SEGMENTS['AL1'], (0, -1), 'SEG'],
            ['RAS_O17_PATIENT_VISIT', None, (0, 1), 'GRP'],
        ),
    ),
    'RAS_O17_PATIENT_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
        ),
    ),
    'RAS_O17_TIMING': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'RAS_O17_TIMING_ENCODED': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'RDE_O11_COMPONENTS': (
        'sequence',
        (
            ['RXC', SEGMENTS['RXC'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'RDE_O11_INSURANCE': (
        'sequence',
        (
            ['IN1', SEGMENTS['IN1'], (1, 1), 'SEG'],
            ['IN2', SEGMENTS['IN2'], (0, 1), 'SEG'],
            ['IN3', SEGMENTS['IN3'], (0, 1), 'SEG'],
        ),
    ),
    'RDE_O11_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'RDE_O11_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['RDE_O11_TIMING', None, (0, -1), 'GRP'],
            ['RDE_O11_ORDER_DETAIL', None, (0, 1), 'GRP'],
            ['RXE', SEGMENTS['RXE'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['RDE_O11_TIMING_ENCODED', None, (1, -1), 'GRP'],
            ['RDE_O11_PHARMACY_TREATMENT_INFUSION_ORDER', None, (0, -1), 'GRP'],
            ['RXR', SEGMENTS['RXR'], (1, -1), 'SEG'],
            ['RXC', SEGMENTS['RXC'], (0, -1), 'SEG'],
            ['CDO', SEGMENTS['CDO'], (0, -1), 'SEG'],
            ['RDE_O11_OBSERVATION', None, (0, -1), 'GRP'],
            ['FT1', SEGMENTS['FT1'], (0, -1), 'SEG'],
            ['BLG', SEGMENTS['BLG'], (0, 1), 'SEG'],
            ['CTI', SEGMENTS['CTI'], (0, -1), 'SEG'],
        ),
    ),
    'RDE_O11_ORDER_DETAIL': (
        'sequence',
        (
            ['RXO', SEGMENTS['RXO'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (1, -1), 'SEG'],
            ['RDE_O11_COMPONENTS', None, (0, -1), 'GRP'],
        ),
    ),
    'RDE_O11_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
            ['RDE_O11_PATIENT_VISIT', None, (0, 1), 'GRP'],
            ['RDE_O11_INSURANCE', None, (0, -1), 'GRP'],
            ['GT1', SEGMENTS['GT1'], (0, 1), 'SEG'],
            ['AL1', SEGMENTS['AL1'], (0, -1), 'SEG'],
        ),
    ),
    'RDE_O11_PATIENT_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
        ),
    ),
    'RDE_O11_PHARMACY_TREATMENT_INFUSION_ORDER': (
        'sequence',
        (
            ['RXV', SEGMENTS['RXV'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['RDE_O11_TIMING_ENCODED', None, (1, -1), 'GRP'],
        ),
    ),
    'RDE_O11_TIMING': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'RDE_O11_TIMING_ENCODED': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'RDR_RDR_DEFINITION': (
        'sequence',
        (
            ['QRD', SEGMENTS['QRD'], (1, 1), 'SEG'],
            ['QRF', SEGMENTS['QRF'], (0, 1), 'SEG'],
            ['RDR_RDR_PATIENT', None, (0, 1), 'GRP'],
            ['RDR_RDR_ORDER', None, (1, -1), 'GRP'],
        ),
    ),
    'RDR_RDR_DISPENSE': (
        'sequence',
        (
            ['RXD', SEGMENTS['RXD'], (1, 1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (1, -1), 'SEG'],
            ['RXC', SEGMENTS['RXC'], (0, -1), 'SEG'],
        ),
    ),
    'RDR_RDR_ENCODING': (
        'sequence',
        (
            ['RXE', SEGMENTS['RXE'], (1, 1), 'SEG'],
            ['RDR_RDR_TIMING_ENCODED', None, (0, -1), 'GRP'],
            ['RXR', SEGMENTS['RXR'], (1, -1), 'SEG'],
            ['RXC', SEGMENTS['RXC'], (0, -1), 'SEG'],
        ),
    ),
    'RDR_RDR_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['RDR_RDR_TIMING', None, (0, -1), 'GRP'],
            ['RDR_RDR_ENCODING', None, (0, 1), 'GRP'],
            ['RDR_RDR_DISPENSE', None, (1, -1), 'GRP'],
        ),
    ),
    'RDR_RDR_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'RDR_RDR_TIMING': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'RDR_RDR_TIMING_ENCODED': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'RDS_O13_ADDITIONAL_DEMOGRAPHICS': (
        'sequence',
        (
            ['PD1', SEGMENTS['PD1'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
        ),
    ),
    'RDS_O13_COMPONENT': (
        'sequence',
        (
            ['RXC', SEGMENTS['RXC'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'RDS_O13_ENCODING': (
        'sequence',
        (
            ['RXE', SEGMENTS['RXE'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['RDS_O13_TIMING_ENCODED', None, (1, -1), 'GRP'],
            ['RXR', SEGMENTS['RXR'], (1, -1), 'SEG'],
            ['RXC', SEGMENTS['RXC'], (0, -1), 'SEG'],
        ),
    ),
    'RDS_O13_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'RDS_O13_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['RDS_O13_TIMING', None, (0, -1), 'GRP'],
            ['RDS_O13_ORDER_DETAIL', None, (0, 1), 'GRP'],
            ['RDS_O13_ENCODING', None, (0, 1), 'GRP'],
            ['RXD', SEGMENTS['RXD'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (1, -1), 'SEG'],
            ['RXC', SEGMENTS['RXC'], (0, -1), 'SEG'],
            ['CDO', SEGMENTS['CDO'], (0, -1), 'SEG'],
            ['RDS_O13_OBSERVATION', None, (0, -1), 'GRP'],
            ['FT1', SEGMENTS['FT1'], (0, -1), 'SEG'],
        ),
    ),
    'RDS_O13_ORDER_DETAIL': (
        'sequence',
        (
            ['RXO', SEGMENTS['RXO'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['RDS_O13_ORDER_DETAIL_SUPPLEMENT', None, (0, 1), 'GRP'],
        ),
    ),
    'RDS_O13_ORDER_DETAIL_SUPPLEMENT': (
        'sequence',
        (
            ['NTE', SEGMENTS['NTE'], (1, -1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (1, -1), 'SEG'],
            ['RDS_O13_COMPONENT', None, (0, -1), 'GRP'],
        ),
    ),
    'RDS_O13_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['RDS_O13_ADDITIONAL_DEMOGRAPHICS', None, (0, 1), 'GRP'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['AL1', SEGMENTS['AL1'], (0, -1), 'SEG'],
            ['RDS_O13_PATIENT_VISIT', None, (0, 1), 'GRP'],
        ),
    ),
    'RDS_O13_PATIENT_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
        ),
    ),
    'RDS_O13_TIMING': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'RDS_O13_TIMING_ENCODED': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'REF_I12_AUTHORIZATION_CONTACT1': (
        'sequence',
        (
            ['AUT', SEGMENTS['AUT'], (1, 1), 'SEG'],
            ['CTD', SEGMENTS['CTD'], (0, 1), 'SEG'],
        ),
    ),
    'REF_I12_AUTHORIZATION_CONTACT2': (
        'sequence',
        (
            ['AUT', SEGMENTS['AUT'], (1, 1), 'SEG'],
            ['CTD', SEGMENTS['CTD'], (0, 1), 'SEG'],
        ),
    ),
    'REF_I12_INSURANCE': (
        'sequence',
        (
            ['IN1', SEGMENTS['IN1'], (1, 1), 'SEG'],
            ['IN2', SEGMENTS['IN2'], (0, 1), 'SEG'],
            ['IN3', SEGMENTS['IN3'], (0, 1), 'SEG'],
        ),
    ),
    'REF_I12_OBSERVATION': (
        'sequence',
        (
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['REF_I12_RESULTS_NOTES', None, (0, -1), 'GRP'],
        ),
    ),
    'REF_I12_PATIENT_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
        ),
    ),
    'REF_I12_PROCEDURE': (
        'sequence',
        (
            ['PR1', SEGMENTS['PR1'], (1, 1), 'SEG'],
            ['REF_I12_AUTHORIZATION_CONTACT2', None, (0, 1), 'GRP'],
        ),
    ),
    'REF_I12_PROVIDER_CONTACT': (
        'sequence',
        (
            ['PRD', SEGMENTS['PRD'], (1, 1), 'SEG'],
            ['CTD', SEGMENTS['CTD'], (0, -1), 'SEG'],
        ),
    ),
    'REF_I12_RESULTS_NOTES': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'RGV_O15_COMPONENTS': (
        'sequence',
        (
            ['RXC', SEGMENTS['RXC'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'RGV_O15_ENCODING': (
        'sequence',
        (
            ['RXE', SEGMENTS['RXE'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['RGV_O15_TIMING_ENCODED', None, (1, -1), 'GRP'],
            ['RXR', SEGMENTS['RXR'], (1, -1), 'SEG'],
            ['RXC', SEGMENTS['RXC'], (0, -1), 'SEG'],
        ),
    ),
    'RGV_O15_GIVE': (
        'sequence',
        (
            ['RXG', SEGMENTS['RXG'], (1, 1), 'SEG'],
            ['RGV_O15_TIMING_GIVE', None, (1, -1), 'GRP'],
            ['RXR', SEGMENTS['RXR'], (1, -1), 'SEG'],
            ['RXC', SEGMENTS['RXC'], (0, -1), 'SEG'],
            ['CDO', SEGMENTS['CDO'], (0, -1), 'SEG'],
            ['RGV_O15_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'RGV_O15_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'RGV_O15_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['RGV_O15_TIMING', None, (0, -1), 'GRP'],
            ['RGV_O15_ORDER_DETAIL', None, (0, 1), 'GRP'],
            ['RGV_O15_ENCODING', None, (0, 1), 'GRP'],
            ['RGV_O15_GIVE', None, (1, -1), 'GRP'],
        ),
    ),
    'RGV_O15_ORDER_DETAIL': (
        'sequence',
        (
            ['RXO', SEGMENTS['RXO'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['RGV_O15_ORDER_DETAIL_SUPPLEMENT', None, (0, 1), 'GRP'],
        ),
    ),
    'RGV_O15_ORDER_DETAIL_SUPPLEMENT': (
        'sequence',
        (
            ['NTE', SEGMENTS['NTE'], (1, -1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (1, -1), 'SEG'],
            ['RGV_O15_COMPONENTS', None, (0, -1), 'GRP'],
        ),
    ),
    'RGV_O15_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['AL1', SEGMENTS['AL1'], (0, -1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
            ['RGV_O15_PATIENT_VISIT', None, (0, 1), 'GRP'],
        ),
    ),
    'RGV_O15_PATIENT_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
        ),
    ),
    'RGV_O15_TIMING': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'RGV_O15_TIMING_ENCODED': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'RGV_O15_TIMING_GIVE': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'RPA_I08_AUTHORIZATION': (
        'sequence',
        (
            ['AUT', SEGMENTS['AUT'], (1, 1), 'SEG'],
            ['CTD', SEGMENTS['CTD'], (0, 1), 'SEG'],
        ),
    ),
    'RPA_I08_INSURANCE': (
        'sequence',
        (
            ['IN1', SEGMENTS['IN1'], (1, 1), 'SEG'],
            ['IN2', SEGMENTS['IN2'], (0, 1), 'SEG'],
            ['IN3', SEGMENTS['IN3'], (0, 1), 'SEG'],
        ),
    ),
    'RPA_I08_OBSERVATION': (
        'sequence',
        (
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['RPA_I08_RESULTS', None, (0, -1), 'GRP'],
        ),
    ),
    'RPA_I08_PROCEDURE': (
        'sequence',
        (
            ['PR1', SEGMENTS['PR1'], (1, 1), 'SEG'],
            ['RPA_I08_AUTHORIZATION', None, (0, 1), 'GRP'],
        ),
    ),
    'RPA_I08_PROVIDER': (
        'sequence',
        (
            ['PRD', SEGMENTS['PRD'], (1, 1), 'SEG'],
            ['CTD', SEGMENTS['CTD'], (0, -1), 'SEG'],
        ),
    ),
    'RPA_I08_RESULTS': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'RPA_I08_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
        ),
    ),
    'RPI_I01_GUARANTOR_INSURANCE': (
        'sequence',
        (
            ['GT1', SEGMENTS['GT1'], (0, -1), 'SEG'],
            ['RPI_I01_INSURANCE', None, (1, -1), 'GRP'],
        ),
    ),
    'RPI_I01_INSURANCE': (
        'sequence',
        (
            ['IN1', SEGMENTS['IN1'], (1, 1), 'SEG'],
            ['IN2', SEGMENTS['IN2'], (0, 1), 'SEG'],
            ['IN3', SEGMENTS['IN3'], (0, 1), 'SEG'],
        ),
    ),
    'RPI_I01_PROVIDER': (
        'sequence',
        (
            ['PRD', SEGMENTS['PRD'], (1, 1), 'SEG'],
            ['CTD', SEGMENTS['CTD'], (0, -1), 'SEG'],
        ),
    ),
    'RPI_I04_GUARANTOR_INSURANCE': (
        'sequence',
        (
            ['GT1', SEGMENTS['GT1'], (0, -1), 'SEG'],
            ['RPI_I04_INSURANCE', None, (1, -1), 'GRP'],
        ),
    ),
    'RPI_I04_INSURANCE': (
        'sequence',
        (
            ['IN1', SEGMENTS['IN1'], (1, 1), 'SEG'],
            ['IN2', SEGMENTS['IN2'], (0, 1), 'SEG'],
            ['IN3', SEGMENTS['IN3'], (0, 1), 'SEG'],
        ),
    ),
    'RPI_I04_PROVIDER': (
        'sequence',
        (
            ['PRD', SEGMENTS['PRD'], (1, 1), 'SEG'],
            ['CTD', SEGMENTS['CTD'], (0, -1), 'SEG'],
        ),
    ),
    'RPL_I02_PROVIDER': (
        'sequence',
        (
            ['PRD', SEGMENTS['PRD'], (1, 1), 'SEG'],
            ['CTD', SEGMENTS['CTD'], (0, -1), 'SEG'],
        ),
    ),
    'RPR_I03_PROVIDER': (
        'sequence',
        (
            ['PRD', SEGMENTS['PRD'], (1, 1), 'SEG'],
            ['CTD', SEGMENTS['CTD'], (0, -1), 'SEG'],
        ),
    ),
    'RQA_I08_AUTHORIZATION': (
        'sequence',
        (
            ['AUT', SEGMENTS['AUT'], (1, 1), 'SEG'],
            ['CTD', SEGMENTS['CTD'], (0, 1), 'SEG'],
        ),
    ),
    'RQA_I08_GUARANTOR_INSURANCE': (
        'sequence',
        (
            ['GT1', SEGMENTS['GT1'], (0, -1), 'SEG'],
            ['RQA_I08_INSURANCE', None, (1, -1), 'GRP'],
        ),
    ),
    'RQA_I08_INSURANCE': (
        'sequence',
        (
            ['IN1', SEGMENTS['IN1'], (1, 1), 'SEG'],
            ['IN2', SEGMENTS['IN2'], (0, 1), 'SEG'],
            ['IN3', SEGMENTS['IN3'], (0, 1), 'SEG'],
        ),
    ),
    'RQA_I08_OBSERVATION': (
        'sequence',
        (
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['RQA_I08_RESULTS', None, (0, -1), 'GRP'],
        ),
    ),
    'RQA_I08_PROCEDURE': (
        'sequence',
        (
            ['PR1', SEGMENTS['PR1'], (1, 1), 'SEG'],
            ['RQA_I08_AUTHORIZATION', None, (0, 1), 'GRP'],
        ),
    ),
    'RQA_I08_PROVIDER': (
        'sequence',
        (
            ['PRD', SEGMENTS['PRD'], (1, 1), 'SEG'],
            ['CTD', SEGMENTS['CTD'], (0, -1), 'SEG'],
        ),
    ),
    'RQA_I08_RESULTS': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'RQA_I08_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
        ),
    ),
    'RQI_I01_GUARANTOR_INSURANCE': (
        'sequence',
        (
            ['GT1', SEGMENTS['GT1'], (0, -1), 'SEG'],
            ['RQI_I01_INSURANCE', None, (1, -1), 'GRP'],
        ),
    ),
    'RQI_I01_INSURANCE': (
        'sequence',
        (
            ['IN1', SEGMENTS['IN1'], (1, 1), 'SEG'],
            ['IN2', SEGMENTS['IN2'], (0, 1), 'SEG'],
            ['IN3', SEGMENTS['IN3'], (0, 1), 'SEG'],
        ),
    ),
    'RQI_I01_PROVIDER': (
        'sequence',
        (
            ['PRD', SEGMENTS['PRD'], (1, 1), 'SEG'],
            ['CTD', SEGMENTS['CTD'], (0, -1), 'SEG'],
        ),
    ),
    'RQP_I04_PROVIDER': (
        'sequence',
        (
            ['PRD', SEGMENTS['PRD'], (1, 1), 'SEG'],
            ['CTD', SEGMENTS['CTD'], (0, -1), 'SEG'],
        ),
    ),
    'RRA_O18_ADMINISTRATION': (
        'sequence',
        (
            ['RRA_O18_TREATMENT', None, (1, -1), 'GRP'],
            ['RXR', SEGMENTS['RXR'], (1, 1), 'SEG'],
        ),
    ),
    'RRA_O18_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['RRA_O18_TIMING', None, (0, -1), 'GRP'],
            ['RRA_O18_ADMINISTRATION', None, (0, 1), 'GRP'],
        ),
    ),
    'RRA_O18_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'RRA_O18_RESPONSE': (
        'sequence',
        (
            ['RRA_O18_PATIENT', None, (0, 1), 'GRP'],
            ['RRA_O18_ORDER', None, (1, -1), 'GRP'],
        ),
    ),
    'RRA_O18_TIMING': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'RRA_O18_TREATMENT': (
        'sequence',
        (
            ['RXA', SEGMENTS['RXA'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'RRD_O14_DISPENSE': (
        'sequence',
        (
            ['RXD', SEGMENTS['RXD'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (1, -1), 'SEG'],
            ['RXC', SEGMENTS['RXC'], (0, -1), 'SEG'],
        ),
    ),
    'RRD_O14_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['RRD_O14_TIMING', None, (0, -1), 'GRP'],
            ['RRD_O14_DISPENSE', None, (0, 1), 'GRP'],
        ),
    ),
    'RRD_O14_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'RRD_O14_RESPONSE': (
        'sequence',
        (
            ['RRD_O14_PATIENT', None, (0, 1), 'GRP'],
            ['RRD_O14_ORDER', None, (1, -1), 'GRP'],
        ),
    ),
    'RRD_O14_TIMING': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'RRE_O12_ENCODING': (
        'sequence',
        (
            ['RXE', SEGMENTS['RXE'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['RRE_O12_TIMING_ENCODED', None, (1, -1), 'GRP'],
            ['RXR', SEGMENTS['RXR'], (1, -1), 'SEG'],
            ['RXC', SEGMENTS['RXC'], (0, -1), 'SEG'],
        ),
    ),
    'RRE_O12_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['RRE_O12_TIMING', None, (0, -1), 'GRP'],
            ['RRE_O12_ENCODING', None, (0, 1), 'GRP'],
        ),
    ),
    'RRE_O12_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'RRE_O12_RESPONSE': (
        'sequence',
        (
            ['RRE_O12_PATIENT', None, (0, 1), 'GRP'],
            ['RRE_O12_ORDER', None, (1, -1), 'GRP'],
        ),
    ),
    'RRE_O12_TIMING': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'RRE_O12_TIMING_ENCODED': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'RRG_O16_GIVE': (
        'sequence',
        (
            ['RXG', SEGMENTS['RXG'], (1, 1), 'SEG'],
            ['RRG_O16_TIMING_GIVE', None, (1, -1), 'GRP'],
            ['RXR', SEGMENTS['RXR'], (1, -1), 'SEG'],
            ['RXC', SEGMENTS['RXC'], (0, -1), 'SEG'],
        ),
    ),
    'RRG_O16_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['RRG_O16_TIMING', None, (0, -1), 'GRP'],
            ['RRG_O16_GIVE', None, (0, 1), 'GRP'],
        ),
    ),
    'RRG_O16_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'RRG_O16_RESPONSE': (
        'sequence',
        (
            ['RRG_O16_PATIENT', None, (0, 1), 'GRP'],
            ['RRG_O16_ORDER', None, (1, -1), 'GRP'],
        ),
    ),
    'RRG_O16_TIMING': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'RRG_O16_TIMING_GIVE': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'RRI_I12_AUTHORIZATION_CONTACT2': (
        'sequence',
        (
            ['AUT', SEGMENTS['AUT'], (1, 1), 'SEG'],
            ['CTD', SEGMENTS['CTD'], (0, 1), 'SEG'],
        ),
    ),
    'RRI_I12_OBSERVATION': (
        'sequence',
        (
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['RRI_I12_RESULTS_NOTES', None, (0, -1), 'GRP'],
        ),
    ),
    'RRI_I12_PATIENT_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
        ),
    ),
    'RRI_I12_PROCEDURE': (
        'sequence',
        (
            ['PR1', SEGMENTS['PR1'], (1, 1), 'SEG'],
            ['RRI_I12_AUTHORIZATION_CONTACT2', None, (0, 1), 'GRP'],
        ),
    ),
    'RRI_I12_PROVIDER_CONTACT': (
        'sequence',
        (
            ['PRD', SEGMENTS['PRD'], (1, 1), 'SEG'],
            ['CTD', SEGMENTS['CTD'], (0, -1), 'SEG'],
        ),
    ),
    'RRI_I12_RESULTS_NOTES': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'RSP_E03_QUERY_ACK_IPR': (
        'choice',
        (
            ['QAK', SEGMENTS['QAK'], (1, 1), 'SEG'],
            ['QPD', SEGMENTS['QPD'], (1, 1), 'SEG'],
            ['IPR', SEGMENTS['IPR'], (0, -1), 'SEG'],
        ),
    ),
    'RSP_E22_AUTHORIZATION_INFO': (
        'sequence',
        (
            ['IVC', SEGMENTS['IVC'], (1, 1), 'SEG'],
            ['PSG', SEGMENTS['PSG'], (1, 1), 'SEG'],
            ['RSP_E22_PSL_ITEM_INFO', None, (1, -1), 'GRP'],
        ),
    ),
    'RSP_E22_PSL_ITEM_INFO': ('sequence', (['PSL', SEGMENTS['PSL'], (1, 1), 'SEG'],)),
    'RSP_E22_QUERY_ACK': (
        'choice',
        (
            ['QAK', SEGMENTS['QAK'], (1, 1), 'SEG'],
            ['QPD', SEGMENTS['QPD'], (1, 1), 'SEG'],
            ['RSP_E22_AUTHORIZATION_INFO', None, (0, 1), 'GRP'],
        ),
    ),
    'RSP_K11_SEGMENT_PATTERN': (
        'sequence',
        (['ANYHL7SEGMENT', SEGMENTS['ANYHL7SEGMENT'], (1, 1), 'SEG'],),
    ),
    'RSP_K21_QUERY_RESPONSE': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
            ['NK1', SEGMENTS['NK1'], (0, -1), 'SEG'],
            ['QRI', SEGMENTS['QRI'], (1, 1), 'SEG'],
        ),
    ),
    'RSP_K22_QUERY_RESPONSE': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['NK1', SEGMENTS['NK1'], (0, -1), 'SEG'],
            ['QRI', SEGMENTS['QRI'], (0, 1), 'SEG'],
        ),
    ),
    'RSP_K23_QUERY_RESPONSE': ('sequence', (['PID', SEGMENTS['PID'], (1, 1), 'SEG'],)),
    'RSP_K25_STAFF': (
        'sequence',
        (
            ['STF', SEGMENTS['STF'], (1, 1), 'SEG'],
            ['PRA', SEGMENTS['PRA'], (0, -1), 'SEG'],
            ['ORG', SEGMENTS['ORG'], (0, -1), 'SEG'],
            ['AFF', SEGMENTS['AFF'], (0, -1), 'SEG'],
            ['LAN', SEGMENTS['LAN'], (0, -1), 'SEG'],
            ['EDU', SEGMENTS['EDU'], (0, -1), 'SEG'],
            ['CER', SEGMENTS['CER'], (0, -1), 'SEG'],
            ['NK1', SEGMENTS['NK1'], (0, -1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ROL', SEGMENTS['ROL'], (0, -1), 'SEG'],
        ),
    ),
    'RSP_K31_ADDITIONAL_DEMOGRAPHICS': (
        'sequence',
        (
            ['PD1', SEGMENTS['PD1'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'RSP_K31_COMPONENTS': (
        'sequence',
        (
            ['RXC', SEGMENTS['RXC'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'RSP_K31_ENCODING': (
        'sequence',
        (
            ['RXE', SEGMENTS['RXE'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['RSP_K31_TIMING_ENCODED', None, (1, -1), 'GRP'],
            ['RXR', SEGMENTS['RXR'], (1, -1), 'SEG'],
            ['RXC', SEGMENTS['RXC'], (0, -1), 'SEG'],
        ),
    ),
    'RSP_K31_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'RSP_K31_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['RSP_K31_TIMING', None, (0, -1), 'GRP'],
            ['RSP_K31_ORDER_DETAIL', None, (0, 1), 'GRP'],
            ['RSP_K31_ENCODING', None, (0, 1), 'GRP'],
            ['RXD', SEGMENTS['RXD'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (1, -1), 'SEG'],
            ['RXC', SEGMENTS['RXC'], (0, -1), 'SEG'],
            ['CDO', SEGMENTS['CDO'], (0, -1), 'SEG'],
            ['RSP_K31_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'RSP_K31_ORDER_DETAIL': (
        'sequence',
        (
            ['RXO', SEGMENTS['RXO'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (1, -1), 'SEG'],
            ['RSP_K31_COMPONENTS', None, (0, -1), 'GRP'],
        ),
    ),
    'RSP_K31_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['RSP_K31_ADDITIONAL_DEMOGRAPHICS', None, (0, 1), 'GRP'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
            ['AL1', SEGMENTS['AL1'], (0, -1), 'SEG'],
            ['RSP_K31_PATIENT_VISIT', None, (0, 1), 'GRP'],
        ),
    ),
    'RSP_K31_PATIENT_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
        ),
    ),
    'RSP_K31_RESPONSE': (
        'sequence',
        (
            ['RSP_K31_PATIENT', None, (0, 1), 'GRP'],
            ['RSP_K31_ORDER', None, (1, -1), 'GRP'],
        ),
    ),
    'RSP_K31_TIMING': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'RSP_K31_TIMING_ENCODED': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'RSP_K32_QUERY_RESPONSE': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['NK1', SEGMENTS['NK1'], (0, -1), 'SEG'],
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['QRI', SEGMENTS['QRI'], (0, 1), 'SEG'],
        ),
    ),
    'RSP_O33_DONOR': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
        ),
    ),
    'RSP_O34_DONATION': (
        'sequence',
        (
            ['DON', SEGMENTS['DON'], (1, 1), 'SEG'],
            ['OBX', SEGMENTS['OBX'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'RSP_O34_DONOR': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['OBX', SEGMENTS['OBX'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['AL1', SEGMENTS['AL1'], (0, -1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
            ['RSP_O34_DONOR_REGISTRATION', None, (0, 1), 'GRP'],
        ),
    ),
    'RSP_O34_DONOR_REGISTRATION': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (0, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'RSP_Z82_COMMON_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['RSP_Z82_TIMING', None, (0, -1), 'GRP'],
            ['RSP_Z82_ORDER_DETAIL', None, (0, 1), 'GRP'],
            ['RSP_Z82_ENCODED_ORDER', None, (0, 1), 'GRP'],
            ['RXD', SEGMENTS['RXD'], (1, 1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (1, -1), 'SEG'],
            ['RXC', SEGMENTS['RXC'], (0, -1), 'SEG'],
            ['RSP_Z82_OBSERVATION', None, (1, -1), 'GRP'],
        ),
    ),
    'RSP_Z82_ENCODED_ORDER': (
        'sequence',
        (
            ['RXE', SEGMENTS['RXE'], (1, 1), 'SEG'],
            ['RSP_Z82_TIMING_ENCODED', None, (0, -1), 'GRP'],
            ['RXR', SEGMENTS['RXR'], (1, -1), 'SEG'],
            ['RXC', SEGMENTS['RXC'], (0, -1), 'SEG'],
        ),
    ),
    'RSP_Z82_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (0, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'RSP_Z82_ORDER_DETAIL': (
        'sequence',
        (
            ['RXO', SEGMENTS['RXO'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (1, -1), 'SEG'],
            ['RSP_Z82_TREATMENT', None, (0, 1), 'GRP'],
        ),
    ),
    'RSP_Z82_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['RSP_Z82_VISIT', None, (0, 1), 'GRP'],
        ),
    ),
    'RSP_Z82_QUERY_RESPONSE': (
        'sequence',
        (
            ['RSP_Z82_PATIENT', None, (0, 1), 'GRP'],
            ['RSP_Z82_COMMON_ORDER', None, (1, -1), 'GRP'],
        ),
    ),
    'RSP_Z82_TIMING': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'RSP_Z82_TIMING_ENCODED': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'RSP_Z82_TREATMENT': (
        'sequence',
        (
            ['RXC', SEGMENTS['RXC'], (1, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'RSP_Z82_VISIT': (
        'sequence',
        (
            ['AL1', SEGMENTS['AL1'], (1, -1), 'SEG'],
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
        ),
    ),
    'RSP_Z84_ROW_DEFINITION': (
        'sequence',
        (
            ['RDF', SEGMENTS['RDF'], (1, 1), 'SEG'],
            ['RDT', SEGMENTS['RDT'], (0, -1), 'SEG'],
        ),
    ),
    'RSP_Z86_ADMINISTRATION': (
        'sequence',
        (
            ['RXA', SEGMENTS['RXA'], (1, 1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (1, -1), 'SEG'],
            ['RXC', SEGMENTS['RXC'], (0, -1), 'SEG'],
        ),
    ),
    'RSP_Z86_COMMON_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['RSP_Z86_TIMING', None, (0, -1), 'GRP'],
            ['RSP_Z86_ORDER_DETAIL', None, (0, 1), 'GRP'],
            ['RSP_Z86_ENCODED_ORDER', None, (0, 1), 'GRP'],
            ['RSP_Z86_DISPENSE', None, (0, 1), 'GRP'],
            ['RSP_Z86_GIVE', None, (0, 1), 'GRP'],
            ['RSP_Z86_ADMINISTRATION', None, (0, 1), 'GRP'],
            ['RSP_Z86_OBSERVATION', None, (1, -1), 'GRP'],
        ),
    ),
    'RSP_Z86_DISPENSE': (
        'sequence',
        (
            ['RXD', SEGMENTS['RXD'], (1, 1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (1, -1), 'SEG'],
            ['RXC', SEGMENTS['RXC'], (0, -1), 'SEG'],
        ),
    ),
    'RSP_Z86_ENCODED_ORDER': (
        'sequence',
        (
            ['RXE', SEGMENTS['RXE'], (1, 1), 'SEG'],
            ['RSP_Z86_TIMING_ENCODED', None, (0, -1), 'GRP'],
            ['RXR', SEGMENTS['RXR'], (1, -1), 'SEG'],
            ['RXC', SEGMENTS['RXC'], (0, -1), 'SEG'],
        ),
    ),
    'RSP_Z86_GIVE': (
        'sequence',
        (
            ['RXG', SEGMENTS['RXG'], (1, 1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (1, -1), 'SEG'],
            ['RXC', SEGMENTS['RXC'], (0, -1), 'SEG'],
        ),
    ),
    'RSP_Z86_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (0, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'RSP_Z86_ORDER_DETAIL': (
        'sequence',
        (
            ['RXO', SEGMENTS['RXO'], (1, 1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (1, -1), 'SEG'],
            ['RXC', SEGMENTS['RXC'], (0, -1), 'SEG'],
        ),
    ),
    'RSP_Z86_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['AL1', SEGMENTS['AL1'], (0, -1), 'SEG'],
        ),
    ),
    'RSP_Z86_QUERY_RESPONSE': (
        'sequence',
        (
            ['RSP_Z86_PATIENT', None, (0, 1), 'GRP'],
            ['RSP_Z86_COMMON_ORDER', None, (1, -1), 'GRP'],
        ),
    ),
    'RSP_Z86_TIMING': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'RSP_Z86_TIMING_ENCODED': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'RSP_Z88_ALLERGY': (
        'sequence',
        (
            ['AL1', SEGMENTS['AL1'], (1, -1), 'SEG'],
            ['RSP_Z88_VISIT', None, (0, 1), 'GRP'],
        ),
    ),
    'RSP_Z88_COMMON_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['RSP_Z88_TIMING', None, (0, -1), 'GRP'],
            ['RSP_Z88_ORDER_DETAIL', None, (0, 1), 'GRP'],
            ['RSP_Z88_ORDER_ENCODED', None, (0, 1), 'GRP'],
            ['RXD', SEGMENTS['RXD'], (1, 1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (1, -1), 'SEG'],
            ['RXC', SEGMENTS['RXC'], (0, -1), 'SEG'],
            ['RSP_Z88_OBSERVATION', None, (1, -1), 'GRP'],
        ),
    ),
    'RSP_Z88_COMPONENT': (
        'sequence',
        (
            ['RXC', SEGMENTS['RXC'], (1, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'RSP_Z88_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (0, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'RSP_Z88_ORDER_DETAIL': (
        'sequence',
        (
            ['RXO', SEGMENTS['RXO'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (1, -1), 'SEG'],
            ['RSP_Z88_COMPONENT', None, (0, 1), 'GRP'],
        ),
    ),
    'RSP_Z88_ORDER_ENCODED': (
        'sequence',
        (
            ['RXE', SEGMENTS['RXE'], (1, 1), 'SEG'],
            ['RSP_Z88_TIMING_ENCODED', None, (0, -1), 'GRP'],
            ['RXR', SEGMENTS['RXR'], (1, -1), 'SEG'],
            ['RXC', SEGMENTS['RXC'], (0, -1), 'SEG'],
        ),
    ),
    'RSP_Z88_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['RSP_Z88_ALLERGY', None, (0, 1), 'GRP'],
        ),
    ),
    'RSP_Z88_QUERY_RESPONSE': (
        'sequence',
        (
            ['RSP_Z88_PATIENT', None, (0, 1), 'GRP'],
            ['RSP_Z88_COMMON_ORDER', None, (1, -1), 'GRP'],
        ),
    ),
    'RSP_Z88_TIMING': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'RSP_Z88_TIMING_ENCODED': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'RSP_Z88_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
        ),
    ),
    'RSP_Z90_COMMON_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['RSP_Z90_TIMING', None, (0, -1), 'GRP'],
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['CTD', SEGMENTS['CTD'], (0, 1), 'SEG'],
            ['RSP_Z90_OBSERVATION', None, (1, -1), 'GRP'],
        ),
    ),
    'RSP_Z90_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (0, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'RSP_Z90_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['NK1', SEGMENTS['NK1'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['RSP_Z90_VISIT', None, (0, 1), 'GRP'],
        ),
    ),
    'RSP_Z90_QUERY_RESPONSE': (
        'sequence',
        (
            ['RSP_Z90_PATIENT', None, (0, 1), 'GRP'],
            ['RSP_Z90_COMMON_ORDER', None, (1, -1), 'GRP'],
            ['RSP_Z90_SPECIMEN', None, (0, -1), 'GRP'],
        ),
    ),
    'RSP_Z90_SPECIMEN': (
        'sequence',
        (
            ['SPM', SEGMENTS['SPM'], (1, 1), 'SEG'],
            ['OBX', SEGMENTS['OBX'], (0, -1), 'SEG'],
        ),
    ),
    'RSP_Z90_TIMING': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
    'RSP_Z90_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
        ),
    ),
    'RSP_ZNN': (
        'sequence',
        (
            ['MSH', SEGMENTS['MSH'], (1, 1), 'SEG'],
            ['SFT', SEGMENTS['SFT'], (0, -1), 'SEG'],
            ['UAC', SEGMENTS['UAC'], (0, 1), 'SEG'],
            ['MSA', SEGMENTS['MSA'], (1, 1), 'SEG'],
            ['ERR', SEGMENTS['ERR'], (0, 1), 'SEG'],
            ['QAK', SEGMENTS['QAK'], (1, 1), 'SEG'],
            ['QPD', SEGMENTS['QPD'], (1, 1), 'SEG'],
            ['ANYHL7SEGMENT', SEGMENTS['ANYHL7SEGMENT'], (0, 1), 'SEG'],
            ['DSC', SEGMENTS['DSC'], (0, 1), 'SEG'],
        ),
    ),
    'RTB_K13_ROW_DEFINITION': (
        'sequence',
        (
            ['RDF', SEGMENTS['RDF'], (1, 1), 'SEG'],
            ['RDT', SEGMENTS['RDT'], (0, -1), 'SEG'],
        ),
    ),
    'RTB_KNN': (
        'sequence',
        (
            ['MSH', SEGMENTS['MSH'], (1, 1), 'SEG'],
            ['SFT', SEGMENTS['SFT'], (0, -1), 'SEG'],
            ['UAC', SEGMENTS['UAC'], (0, 1), 'SEG'],
            ['MSA', SEGMENTS['MSA'], (1, 1), 'SEG'],
            ['ERR', SEGMENTS['ERR'], (0, 1), 'SEG'],
            ['QAK', SEGMENTS['QAK'], (1, 1), 'SEG'],
            ['QPD', SEGMENTS['QPD'], (1, 1), 'SEG'],
            ['ANYHL7SEGMENT', SEGMENTS['ANYHL7SEGMENT'], (1, 1), 'SEG'],
            ['DSC', SEGMENTS['DSC'], (0, 1), 'SEG'],
        ),
    ),
    'RTB_Z74_ROW_DEFINITION': (
        'sequence',
        (
            ['RDF', SEGMENTS['RDF'], (1, 1), 'SEG'],
            ['RDT', SEGMENTS['RDT'], (0, -1), 'SEG'],
        ),
    ),
    'SDR_S31_ANTI_MICROBIAL_DEVICE_DATA': (
        'choice',
        (
            ['SDD', SEGMENTS['SDD'], (1, 1), 'SEG'],
            ['SCD', SEGMENTS['SCD'], (0, -1), 'SEG'],
        ),
    ),
    'SDR_S32_ANTI_MICROBIAL_DEVICE_CYCLE_DATA': (
        'choice',
        (
            ['SDD', SEGMENTS['SDD'], (1, 1), 'SEG'],
            ['SCD', SEGMENTS['SCD'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S12_GENERAL_RESOURCE': (
        'sequence',
        (
            ['AIG', SEGMENTS['AIG'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S12_LOCATION_RESOURCE': (
        'sequence',
        (
            ['AIL', SEGMENTS['AIL'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S12_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['PV1', SEGMENTS['PV1'], (0, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['OBX', SEGMENTS['OBX'], (0, -1), 'SEG'],
            ['DG1', SEGMENTS['DG1'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S12_PERSONNEL_RESOURCE': (
        'sequence',
        (
            ['AIP', SEGMENTS['AIP'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S12_RESOURCES': (
        'sequence',
        (
            ['RGS', SEGMENTS['RGS'], (1, 1), 'SEG'],
            ['SIU_S12_SERVICE', None, (0, -1), 'GRP'],
            ['SIU_S12_GENERAL_RESOURCE', None, (0, -1), 'GRP'],
            ['SIU_S12_LOCATION_RESOURCE', None, (0, -1), 'GRP'],
            ['SIU_S12_PERSONNEL_RESOURCE', None, (0, -1), 'GRP'],
        ),
    ),
    'SIU_S12_SERVICE': (
        'sequence',
        (
            ['AIS', SEGMENTS['AIS'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S13_GENERAL_RESOURCE': (
        'sequence',
        (
            ['AIG', SEGMENTS['AIG'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S13_LOCATION_RESOURCE': (
        'sequence',
        (
            ['AIL', SEGMENTS['AIL'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S13_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['PV1', SEGMENTS['PV1'], (0, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['OBX', SEGMENTS['OBX'], (0, -1), 'SEG'],
            ['DG1', SEGMENTS['DG1'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S13_PERSONNEL_RESOURCE': (
        'sequence',
        (
            ['AIP', SEGMENTS['AIP'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S13_RESOURCES': (
        'sequence',
        (
            ['RGS', SEGMENTS['RGS'], (1, 1), 'SEG'],
            ['SIU_S13_SERVICE', None, (0, -1), 'GRP'],
            ['SIU_S13_GENERAL_RESOURCE', None, (0, -1), 'GRP'],
            ['SIU_S13_LOCATION_RESOURCE', None, (0, -1), 'GRP'],
            ['SIU_S13_PERSONNEL_RESOURCE', None, (0, -1), 'GRP'],
        ),
    ),
    'SIU_S13_SERVICE': (
        'sequence',
        (
            ['AIS', SEGMENTS['AIS'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S14_GENERAL_RESOURCE': (
        'sequence',
        (
            ['AIG', SEGMENTS['AIG'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S14_LOCATION_RESOURCE': (
        'sequence',
        (
            ['AIL', SEGMENTS['AIL'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S14_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['PV1', SEGMENTS['PV1'], (0, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['OBX', SEGMENTS['OBX'], (0, -1), 'SEG'],
            ['DG1', SEGMENTS['DG1'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S14_PERSONNEL_RESOURCE': (
        'sequence',
        (
            ['AIP', SEGMENTS['AIP'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S14_RESOURCES': (
        'sequence',
        (
            ['RGS', SEGMENTS['RGS'], (1, 1), 'SEG'],
            ['SIU_S14_SERVICE', None, (0, -1), 'GRP'],
            ['SIU_S14_GENERAL_RESOURCE', None, (0, -1), 'GRP'],
            ['SIU_S14_LOCATION_RESOURCE', None, (0, -1), 'GRP'],
            ['SIU_S14_PERSONNEL_RESOURCE', None, (0, -1), 'GRP'],
        ),
    ),
    'SIU_S14_SERVICE': (
        'sequence',
        (
            ['AIS', SEGMENTS['AIS'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S15_GENERAL_RESOURCE': (
        'sequence',
        (
            ['AIG', SEGMENTS['AIG'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S15_LOCATION_RESOURCE': (
        'sequence',
        (
            ['AIL', SEGMENTS['AIL'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S15_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['PV1', SEGMENTS['PV1'], (0, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['OBX', SEGMENTS['OBX'], (0, -1), 'SEG'],
            ['DG1', SEGMENTS['DG1'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S15_PERSONNEL_RESOURCE': (
        'sequence',
        (
            ['AIP', SEGMENTS['AIP'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S15_RESOURCES': (
        'sequence',
        (
            ['RGS', SEGMENTS['RGS'], (1, 1), 'SEG'],
            ['SIU_S15_SERVICE', None, (0, -1), 'GRP'],
            ['SIU_S15_GENERAL_RESOURCE', None, (0, -1), 'GRP'],
            ['SIU_S15_LOCATION_RESOURCE', None, (0, -1), 'GRP'],
            ['SIU_S15_PERSONNEL_RESOURCE', None, (0, -1), 'GRP'],
        ),
    ),
    'SIU_S15_SERVICE': (
        'sequence',
        (
            ['AIS', SEGMENTS['AIS'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S16_GENERAL_RESOURCE': (
        'sequence',
        (
            ['AIG', SEGMENTS['AIG'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S16_LOCATION_RESOURCE': (
        'sequence',
        (
            ['AIL', SEGMENTS['AIL'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S16_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['PV1', SEGMENTS['PV1'], (0, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['OBX', SEGMENTS['OBX'], (0, -1), 'SEG'],
            ['DG1', SEGMENTS['DG1'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S16_PERSONNEL_RESOURCE': (
        'sequence',
        (
            ['AIP', SEGMENTS['AIP'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S16_RESOURCES': (
        'sequence',
        (
            ['RGS', SEGMENTS['RGS'], (1, 1), 'SEG'],
            ['SIU_S16_SERVICE', None, (0, -1), 'GRP'],
            ['SIU_S16_GENERAL_RESOURCE', None, (0, -1), 'GRP'],
            ['SIU_S16_LOCATION_RESOURCE', None, (0, -1), 'GRP'],
            ['SIU_S16_PERSONNEL_RESOURCE', None, (0, -1), 'GRP'],
        ),
    ),
    'SIU_S16_SERVICE': (
        'sequence',
        (
            ['AIS', SEGMENTS['AIS'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S17_GENERAL_RESOURCE': (
        'sequence',
        (
            ['AIG', SEGMENTS['AIG'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S17_LOCATION_RESOURCE': (
        'sequence',
        (
            ['AIL', SEGMENTS['AIL'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S17_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['PV1', SEGMENTS['PV1'], (0, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['OBX', SEGMENTS['OBX'], (0, -1), 'SEG'],
            ['DG1', SEGMENTS['DG1'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S17_PERSONNEL_RESOURCE': (
        'sequence',
        (
            ['AIP', SEGMENTS['AIP'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S17_RESOURCES': (
        'sequence',
        (
            ['RGS', SEGMENTS['RGS'], (1, 1), 'SEG'],
            ['SIU_S17_SERVICE', None, (0, -1), 'GRP'],
            ['SIU_S17_GENERAL_RESOURCE', None, (0, -1), 'GRP'],
            ['SIU_S17_LOCATION_RESOURCE', None, (0, -1), 'GRP'],
            ['SIU_S17_PERSONNEL_RESOURCE', None, (0, -1), 'GRP'],
        ),
    ),
    'SIU_S17_SERVICE': (
        'sequence',
        (
            ['AIS', SEGMENTS['AIS'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S18_GENERAL_RESOURCE': (
        'sequence',
        (
            ['AIG', SEGMENTS['AIG'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S18_LOCATION_RESOURCE': (
        'sequence',
        (
            ['AIL', SEGMENTS['AIL'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S18_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['PV1', SEGMENTS['PV1'], (0, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['OBX', SEGMENTS['OBX'], (0, -1), 'SEG'],
            ['DG1', SEGMENTS['DG1'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S18_PERSONNEL_RESOURCE': (
        'sequence',
        (
            ['AIP', SEGMENTS['AIP'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S18_RESOURCES': (
        'sequence',
        (
            ['RGS', SEGMENTS['RGS'], (1, 1), 'SEG'],
            ['SIU_S18_SERVICE', None, (0, -1), 'GRP'],
            ['SIU_S18_GENERAL_RESOURCE', None, (0, -1), 'GRP'],
            ['SIU_S18_LOCATION_RESOURCE', None, (0, -1), 'GRP'],
            ['SIU_S18_PERSONNEL_RESOURCE', None, (0, -1), 'GRP'],
        ),
    ),
    'SIU_S18_SERVICE': (
        'sequence',
        (
            ['AIS', SEGMENTS['AIS'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S19_GENERAL_RESOURCE': (
        'sequence',
        (
            ['AIG', SEGMENTS['AIG'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S19_LOCATION_RESOURCE': (
        'sequence',
        (
            ['AIL', SEGMENTS['AIL'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S19_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['PV1', SEGMENTS['PV1'], (0, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['OBX', SEGMENTS['OBX'], (0, -1), 'SEG'],
            ['DG1', SEGMENTS['DG1'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S19_PERSONNEL_RESOURCE': (
        'sequence',
        (
            ['AIP', SEGMENTS['AIP'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S19_RESOURCES': (
        'sequence',
        (
            ['RGS', SEGMENTS['RGS'], (1, 1), 'SEG'],
            ['SIU_S19_SERVICE', None, (0, -1), 'GRP'],
            ['SIU_S19_GENERAL_RESOURCE', None, (0, -1), 'GRP'],
            ['SIU_S19_LOCATION_RESOURCE', None, (0, -1), 'GRP'],
            ['SIU_S19_PERSONNEL_RESOURCE', None, (0, -1), 'GRP'],
        ),
    ),
    'SIU_S19_SERVICE': (
        'sequence',
        (
            ['AIS', SEGMENTS['AIS'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S20_GENERAL_RESOURCE': (
        'sequence',
        (
            ['AIG', SEGMENTS['AIG'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S20_LOCATION_RESOURCE': (
        'sequence',
        (
            ['AIL', SEGMENTS['AIL'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S20_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['PV1', SEGMENTS['PV1'], (0, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['OBX', SEGMENTS['OBX'], (0, -1), 'SEG'],
            ['DG1', SEGMENTS['DG1'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S20_PERSONNEL_RESOURCE': (
        'sequence',
        (
            ['AIP', SEGMENTS['AIP'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S20_RESOURCES': (
        'sequence',
        (
            ['RGS', SEGMENTS['RGS'], (1, 1), 'SEG'],
            ['SIU_S20_SERVICE', None, (0, -1), 'GRP'],
            ['SIU_S20_GENERAL_RESOURCE', None, (0, -1), 'GRP'],
            ['SIU_S20_LOCATION_RESOURCE', None, (0, -1), 'GRP'],
            ['SIU_S20_PERSONNEL_RESOURCE', None, (0, -1), 'GRP'],
        ),
    ),
    'SIU_S20_SERVICE': (
        'sequence',
        (
            ['AIS', SEGMENTS['AIS'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S21_GENERAL_RESOURCE': (
        'sequence',
        (
            ['AIG', SEGMENTS['AIG'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S21_LOCATION_RESOURCE': (
        'sequence',
        (
            ['AIL', SEGMENTS['AIL'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S21_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['PV1', SEGMENTS['PV1'], (0, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['OBX', SEGMENTS['OBX'], (0, -1), 'SEG'],
            ['DG1', SEGMENTS['DG1'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S21_PERSONNEL_RESOURCE': (
        'sequence',
        (
            ['AIP', SEGMENTS['AIP'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S21_RESOURCES': (
        'sequence',
        (
            ['RGS', SEGMENTS['RGS'], (1, 1), 'SEG'],
            ['SIU_S21_SERVICE', None, (0, -1), 'GRP'],
            ['SIU_S21_GENERAL_RESOURCE', None, (0, -1), 'GRP'],
            ['SIU_S21_LOCATION_RESOURCE', None, (0, -1), 'GRP'],
            ['SIU_S21_PERSONNEL_RESOURCE', None, (0, -1), 'GRP'],
        ),
    ),
    'SIU_S21_SERVICE': (
        'sequence',
        (
            ['AIS', SEGMENTS['AIS'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S22_GENERAL_RESOURCE': (
        'sequence',
        (
            ['AIG', SEGMENTS['AIG'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S22_LOCATION_RESOURCE': (
        'sequence',
        (
            ['AIL', SEGMENTS['AIL'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S22_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['PV1', SEGMENTS['PV1'], (0, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['OBX', SEGMENTS['OBX'], (0, -1), 'SEG'],
            ['DG1', SEGMENTS['DG1'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S22_PERSONNEL_RESOURCE': (
        'sequence',
        (
            ['AIP', SEGMENTS['AIP'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S22_RESOURCES': (
        'sequence',
        (
            ['RGS', SEGMENTS['RGS'], (1, 1), 'SEG'],
            ['SIU_S22_SERVICE', None, (0, -1), 'GRP'],
            ['SIU_S22_GENERAL_RESOURCE', None, (0, -1), 'GRP'],
            ['SIU_S22_LOCATION_RESOURCE', None, (0, -1), 'GRP'],
            ['SIU_S22_PERSONNEL_RESOURCE', None, (0, -1), 'GRP'],
        ),
    ),
    'SIU_S22_SERVICE': (
        'sequence',
        (
            ['AIS', SEGMENTS['AIS'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S23_GENERAL_RESOURCE': (
        'sequence',
        (
            ['AIG', SEGMENTS['AIG'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S23_LOCATION_RESOURCE': (
        'sequence',
        (
            ['AIL', SEGMENTS['AIL'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S23_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['PV1', SEGMENTS['PV1'], (0, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['OBX', SEGMENTS['OBX'], (0, -1), 'SEG'],
            ['DG1', SEGMENTS['DG1'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S23_PERSONNEL_RESOURCE': (
        'sequence',
        (
            ['AIP', SEGMENTS['AIP'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S23_RESOURCES': (
        'sequence',
        (
            ['RGS', SEGMENTS['RGS'], (1, 1), 'SEG'],
            ['SIU_S23_SERVICE', None, (0, -1), 'GRP'],
            ['SIU_S23_GENERAL_RESOURCE', None, (0, -1), 'GRP'],
            ['SIU_S23_LOCATION_RESOURCE', None, (0, -1), 'GRP'],
            ['SIU_S23_PERSONNEL_RESOURCE', None, (0, -1), 'GRP'],
        ),
    ),
    'SIU_S23_SERVICE': (
        'sequence',
        (
            ['AIS', SEGMENTS['AIS'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S24_GENERAL_RESOURCE': (
        'sequence',
        (
            ['AIG', SEGMENTS['AIG'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S24_LOCATION_RESOURCE': (
        'sequence',
        (
            ['AIL', SEGMENTS['AIL'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S24_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['PV1', SEGMENTS['PV1'], (0, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['OBX', SEGMENTS['OBX'], (0, -1), 'SEG'],
            ['DG1', SEGMENTS['DG1'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S24_PERSONNEL_RESOURCE': (
        'sequence',
        (
            ['AIP', SEGMENTS['AIP'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S24_RESOURCES': (
        'sequence',
        (
            ['RGS', SEGMENTS['RGS'], (1, 1), 'SEG'],
            ['SIU_S24_SERVICE', None, (0, -1), 'GRP'],
            ['SIU_S24_GENERAL_RESOURCE', None, (0, -1), 'GRP'],
            ['SIU_S24_LOCATION_RESOURCE', None, (0, -1), 'GRP'],
            ['SIU_S24_PERSONNEL_RESOURCE', None, (0, -1), 'GRP'],
        ),
    ),
    'SIU_S24_SERVICE': (
        'sequence',
        (
            ['AIS', SEGMENTS['AIS'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S26_GENERAL_RESOURCE': (
        'sequence',
        (
            ['AIG', SEGMENTS['AIG'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S26_LOCATION_RESOURCE': (
        'sequence',
        (
            ['AIL', SEGMENTS['AIL'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S26_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['PV1', SEGMENTS['PV1'], (0, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['OBX', SEGMENTS['OBX'], (0, -1), 'SEG'],
            ['DG1', SEGMENTS['DG1'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S26_PERSONNEL_RESOURCE': (
        'sequence',
        (
            ['AIP', SEGMENTS['AIP'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S26_RESOURCES': (
        'sequence',
        (
            ['RGS', SEGMENTS['RGS'], (1, 1), 'SEG'],
            ['SIU_S26_SERVICE', None, (0, -1), 'GRP'],
            ['SIU_S26_GENERAL_RESOURCE', None, (0, -1), 'GRP'],
            ['SIU_S26_LOCATION_RESOURCE', None, (0, -1), 'GRP'],
            ['SIU_S26_PERSONNEL_RESOURCE', None, (0, -1), 'GRP'],
        ),
    ),
    'SIU_S26_SERVICE': (
        'sequence',
        (
            ['AIS', SEGMENTS['AIS'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S27_GENERAL_RESOURCE': (
        'sequence',
        (
            ['AIG', SEGMENTS['AIG'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S27_LOCATION_RESOURCE': (
        'sequence',
        (
            ['AIL', SEGMENTS['AIL'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S27_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['PV1', SEGMENTS['PV1'], (0, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['OBX', SEGMENTS['OBX'], (0, -1), 'SEG'],
            ['DG1', SEGMENTS['DG1'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S27_PERSONNEL_RESOURCE': (
        'sequence',
        (
            ['AIP', SEGMENTS['AIP'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SIU_S27_RESOURCES': (
        'sequence',
        (
            ['RGS', SEGMENTS['RGS'], (1, 1), 'SEG'],
            ['SIU_S27_SERVICE', None, (0, -1), 'GRP'],
            ['SIU_S27_GENERAL_RESOURCE', None, (0, -1), 'GRP'],
            ['SIU_S27_LOCATION_RESOURCE', None, (0, -1), 'GRP'],
            ['SIU_S27_PERSONNEL_RESOURCE', None, (0, -1), 'GRP'],
        ),
    ),
    'SIU_S27_SERVICE': (
        'sequence',
        (
            ['AIS', SEGMENTS['AIS'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SRM_S01_GENERAL_RESOURCE': (
        'sequence',
        (
            ['AIG', SEGMENTS['AIG'], (1, 1), 'SEG'],
            ['APR', SEGMENTS['APR'], (0, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SRM_S01_LOCATION_RESOURCE': (
        'sequence',
        (
            ['AIL', SEGMENTS['AIL'], (1, 1), 'SEG'],
            ['APR', SEGMENTS['APR'], (0, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SRM_S01_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
        ),
    ),
    'SRM_S01_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PV1', SEGMENTS['PV1'], (0, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['SRM_S01_OBSERVATION', None, (0, -1), 'GRP'],
            ['DG1', SEGMENTS['DG1'], (0, -1), 'SEG'],
        ),
    ),
    'SRM_S01_PERSONNEL_RESOURCE': (
        'sequence',
        (
            ['AIP', SEGMENTS['AIP'], (1, 1), 'SEG'],
            ['APR', SEGMENTS['APR'], (0, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SRM_S01_RESOURCES': (
        'sequence',
        (
            ['RGS', SEGMENTS['RGS'], (1, 1), 'SEG'],
            ['SRM_S01_SERVICE', None, (0, -1), 'GRP'],
            ['SRM_S01_GENERAL_RESOURCE', None, (0, -1), 'GRP'],
            ['SRM_S01_LOCATION_RESOURCE', None, (0, -1), 'GRP'],
            ['SRM_S01_PERSONNEL_RESOURCE', None, (0, -1), 'GRP'],
        ),
    ),
    'SRM_S01_SERVICE': (
        'sequence',
        (
            ['AIS', SEGMENTS['AIS'], (1, 1), 'SEG'],
            ['APR', SEGMENTS['APR'], (0, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SRR_S01_GENERAL_RESOURCE': (
        'sequence',
        (
            ['AIG', SEGMENTS['AIG'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SRR_S01_LOCATION_RESOURCE': (
        'sequence',
        (
            ['AIL', SEGMENTS['AIL'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SRR_S01_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PV1', SEGMENTS['PV1'], (0, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['DG1', SEGMENTS['DG1'], (0, -1), 'SEG'],
        ),
    ),
    'SRR_S01_PERSONNEL_RESOURCE': (
        'sequence',
        (
            ['AIP', SEGMENTS['AIP'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SRR_S01_RESOURCES': (
        'sequence',
        (
            ['RGS', SEGMENTS['RGS'], (1, 1), 'SEG'],
            ['SRR_S01_SERVICE', None, (0, -1), 'GRP'],
            ['SRR_S01_GENERAL_RESOURCE', None, (0, -1), 'GRP'],
            ['SRR_S01_LOCATION_RESOURCE', None, (0, -1), 'GRP'],
            ['SRR_S01_PERSONNEL_RESOURCE', None, (0, -1), 'GRP'],
        ),
    ),
    'SRR_S01_SCHEDULE': (
        'sequence',
        (
            ['SCH', SEGMENTS['SCH'], (1, 1), 'SEG'],
            ['TQ1', SEGMENTS['TQ1'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['SRR_S01_PATIENT', None, (0, -1), 'GRP'],
            ['SRR_S01_RESOURCES', None, (1, -1), 'GRP'],
        ),
    ),
    'SRR_S01_SERVICE': (
        'sequence',
        (
            ['AIS', SEGMENTS['AIS'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SSR_U04_SPECIMEN_CONTAINER': (
        'sequence',
        (
            ['SAC', SEGMENTS['SAC'], (1, 1), 'SEG'],
            ['SPM', SEGMENTS['SPM'], (0, -1), 'SEG'],
        ),
    ),
    'SSU_U03_SPECIMEN': (
        'sequence',
        (
            ['SPM', SEGMENTS['SPM'], (1, 1), 'SEG'],
            ['OBX', SEGMENTS['OBX'], (0, -1), 'SEG'],
        ),
    ),
    'SSU_U03_SPECIMEN_CONTAINER': (
        'sequence',
        (
            ['SAC', SEGMENTS['SAC'], (1, 1), 'SEG'],
            ['OBX', SEGMENTS['OBX'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['SSU_U03_SPECIMEN', None, (0, -1), 'GRP'],
        ),
    ),
    'TCU_U10_TEST_CONFIGURATION': (
        'sequence',
        (
            ['SPM', SEGMENTS['SPM'], (0, 1), 'SEG'],
            ['TCC', SEGMENTS['TCC'], (1, -1), 'SEG'],
        ),
    ),
    'VXU_V04_INSURANCE': (
        'sequence',
        (
            ['IN1', SEGMENTS['IN1'], (1, 1), 'SEG'],
            ['IN2', SEGMENTS['IN2'], (0, 1), 'SEG'],
            ['IN3', SEGMENTS['IN3'], (0, 1), 'SEG'],
        ),
    ),
    'VXU_V04_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'VXU_V04_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['VXU_V04_TIMING', None, (0, -1), 'GRP'],
            ['RXA', SEGMENTS['RXA'], (1, 1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (0, 1), 'SEG'],
            ['VXU_V04_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'VXU_V04_PATIENT_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['ARV', SEGMENTS['ARV'], (0, -1), 'SEG'],
        ),
    ),
    'VXU_V04_PERSON_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['PRT', SEGMENTS['PRT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'VXU_V04_TIMING': (
        'sequence',
        (
            ['TQ1', SEGMENTS['TQ1'], (1, 1), 'SEG'],
            ['TQ2', SEGMENTS['TQ2'], (0, -1), 'SEG'],
        ),
    ),
}
for k, v in iteritems(GROUPS):
    for item in v[1]:
        if item[3] == 'GRP':
            item[1] = GROUPS[item[0]]
