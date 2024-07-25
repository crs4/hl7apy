from hl7apy.utils import iteritems

from .segments import SEGMENTS

GROUPS = {
    'ADT_A01_INSURANCE': (
        'sequence',
        (
            ['IN1', SEGMENTS['IN1'], (1, 1), 'SEG'],
            ['IN2', SEGMENTS['IN2'], (0, 1), 'SEG'],
            ['IN3', SEGMENTS['IN3'], (0, 1), 'SEG'],
        ),
    ),
    'ADT_A01_PROCEDURE': (
        'sequence',
        (
            ['PR1', SEGMENTS['PR1'], (1, 1), 'SEG'],
            ['ROL', SEGMENTS['ROL'], (0, -1), 'SEG'],
        ),
    ),
    'ADT_A03_PROCEDURE': (
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
            ['IN3', SEGMENTS['IN3'], (0, 1), 'SEG'],
        ),
    ),
    'ADT_A06_PROCEDURE': (
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
    'ADT_A45_MERGE_INFO': (
        'sequence',
        (
            ['MRG', SEGMENTS['MRG'], (1, 1), 'SEG'],
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
        ),
    ),
    'ARD_A19_INSURANCE': (
        'sequence',
        (
            ['IN1', SEGMENTS['IN1'], (1, 1), 'SEG'],
            ['IN2', SEGMENTS['IN2'], (0, 1), 'SEG'],
            ['IN3', SEGMENTS['IN3'], (0, 1), 'SEG'],
        ),
    ),
    'ARD_A19_PROCEDURE': (
        'sequence',
        (
            ['PR1', SEGMENTS['PR1'], (1, 1), 'SEG'],
            ['ROL', SEGMENTS['ROL'], (0, -1), 'SEG'],
        ),
    ),
    'ARD_A19_QUERY_RESPONSE': (
        'sequence',
        (
            ['EVN', SEGMENTS['EVN'], (0, 1), 'SEG'],
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['NK1', SEGMENTS['NK1'], (0, -1), 'SEG'],
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['DB1', SEGMENTS['DB1'], (0, -1), 'SEG'],
            ['OBX', SEGMENTS['OBX'], (0, -1), 'SEG'],
            ['AL1', SEGMENTS['AL1'], (0, -1), 'SEG'],
            ['DG1', SEGMENTS['DG1'], (0, -1), 'SEG'],
            ['DRG', SEGMENTS['DRG'], (0, 1), 'SEG'],
            ['ARD_A19_PROCEDURE', None, (0, -1), 'GRP'],
            ['GT1', SEGMENTS['GT1'], (0, -1), 'SEG'],
            ['ARD_A19_INSURANCE', None, (0, -1), 'GRP'],
            ['ACC', SEGMENTS['ACC'], (0, 1), 'SEG'],
            ['UB1', SEGMENTS['UB1'], (0, 1), 'SEG'],
            ['UB2', SEGMENTS['UB2'], (0, 1), 'SEG'],
        ),
    ),
    'BAR_P01_INSURANCE': (
        'sequence',
        (
            ['IN1', SEGMENTS['IN1'], (1, 1), 'SEG'],
            ['IN2', SEGMENTS['IN2'], (0, 1), 'SEG'],
            ['IN3', SEGMENTS['IN3'], (0, 1), 'SEG'],
        ),
    ),
    'BAR_P01_PROCEDURE': (
        'sequence',
        (
            ['PR1', SEGMENTS['PR1'], (1, 1), 'SEG'],
            ['ROL', SEGMENTS['ROL'], (0, -1), 'SEG'],
        ),
    ),
    'BAR_P01_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (0, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
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
    'BAR_P06_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PV1', SEGMENTS['PV1'], (0, 1), 'SEG'],
        ),
    ),
    'CRM_C01_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PV1', SEGMENTS['PV1'], (0, 1), 'SEG'],
            ['CSR', SEGMENTS['CSR'], (1, 1), 'SEG'],
            ['CSP', SEGMENTS['CSP'], (0, -1), 'SEG'],
        ),
    ),
    'CSU_C09_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
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
        ),
    ),
    'CSU_C09_STUDY_OBSERVATION': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (0, 1), 'SEG'],
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['OBX', SEGMENTS['OBX'], (1, -1), 'SEG'],
        ),
    ),
    'CSU_C09_STUDY_PHARM': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (0, 1), 'SEG'],
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
            ['CSU_C09_STUDY_OBSERVATION', None, (0, -1), 'GRP'],
            ['CSU_C09_STUDY_PHARM', None, (1, -1), 'GRP'],
        ),
    ),
    'CSU_C09_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
        ),
    ),
    'DFT_P03_FINANCIAL': (
        'sequence',
        (
            ['FT1', SEGMENTS['FT1'], (1, 1), 'SEG'],
            ['DFT_P03_FINANCIAL_PROCEDURE', None, (0, -1), 'GRP'],
        ),
    ),
    'DFT_P03_FINANCIAL_PROCEDURE': (
        'sequence',
        (
            ['PR1', SEGMENTS['PR1'], (1, 1), 'SEG'],
            ['ROL', SEGMENTS['ROL'], (0, -1), 'SEG'],
        ),
    ),
    'DFT_P03_INSURANCE': (
        'sequence',
        (
            ['IN1', SEGMENTS['IN1'], (1, 1), 'SEG'],
            ['IN2', SEGMENTS['IN2'], (0, 1), 'SEG'],
            ['IN3', SEGMENTS['IN3'], (0, 1), 'SEG'],
        ),
    ),
    'DOC_T12_RESULT': (
        'sequence',
        (
            ['EVN', SEGMENTS['EVN'], (0, 1), 'SEG'],
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['TXA', SEGMENTS['TXA'], (1, 1), 'SEG'],
            ['OBX', SEGMENTS['OBX'], (0, -1), 'SEG'],
        ),
    ),
    'MFN_M01_MF': ('sequence', (['MFE', SEGMENTS['MFE'], (1, 1), 'SEG'],)),
    'MFN_M02_MF_STAFF': (
        'sequence',
        (
            ['MFE', SEGMENTS['MFE'], (1, 1), 'SEG'],
            ['STF', SEGMENTS['STF'], (1, 1), 'SEG'],
            ['PRA', SEGMENTS['PRA'], (0, 1), 'SEG'],
        ),
    ),
    'MFN_M03_MF_TEST': (
        'sequence',
        (
            ['MFE', SEGMENTS['MFE'], (1, 1), 'SEG'],
            ['OM1', SEGMENTS['OM1'], (1, 1), 'SEG'],
            ['ANYHL7SEGMENT', SEGMENTS['ANYHL7SEGMENT'], (1, 1), 'SEG'],
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
    'MFN_M06_MF_CDM': (
        'sequence',
        (
            ['MFE', SEGMENTS['MFE'], (1, 1), 'SEG'],
            ['CDM', SEGMENTS['CDM'], (1, 1), 'SEG'],
            ['PRC', SEGMENTS['PRC'], (0, -1), 'SEG'],
        ),
    ),
    'MFN_M07_MF_CLIN_STUDY': (
        'sequence',
        (
            ['MFE', SEGMENTS['MFE'], (1, 1), 'SEG'],
            ['CM0', SEGMENTS['CM0'], (1, 1), 'SEG'],
            ['MFN_M07_MF_PHASE_SCHED_DETAIL', None, (0, -1), 'GRP'],
        ),
    ),
    'MFN_M07_MF_PHASE_SCHED_DETAIL': (
        'sequence',
        (
            ['CM1', SEGMENTS['CM1'], (1, 1), 'SEG'],
            ['CM2', SEGMENTS['CM2'], (0, -1), 'SEG'],
        ),
    ),
    'MFN_M08_MF_NUMERIC_OBSERVATION': (
        'sequence',
        (
            ['OM2', SEGMENTS['OM2'], (0, 1), 'SEG'],
            ['OM3', SEGMENTS['OM3'], (0, 1), 'SEG'],
            ['OM4', SEGMENTS['OM4'], (0, 1), 'SEG'],
        ),
    ),
    'MFN_M08_MF_TEST_NUMERIC': (
        'sequence',
        (
            ['MFE', SEGMENTS['MFE'], (1, 1), 'SEG'],
            ['OM1', SEGMENTS['OM1'], (1, 1), 'SEG'],
            ['MFN_M08_MF_NUMERIC_OBSERVATION', None, (0, 1), 'GRP'],
        ),
    ),
    'MFN_M09_MF_TEST_CATEGORICAL': (
        'sequence',
        (
            ['MFE', SEGMENTS['MFE'], (1, 1), 'SEG'],
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
        (['MFN_M10_MF_TEST_BATT_DETAIL', None, (0, 1), 'GRP'],),
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
    'OMD_O01_DIET': (
        'sequence',
        (
            ['ODS', SEGMENTS['ODS'], (1, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['OMD_O01_OBSERVATION', None, (1, -1), 'GRP'],
        ),
    ),
    'OMD_O01_INSURANCE': (
        'sequence',
        (
            ['IN1', SEGMENTS['IN1'], (1, 1), 'SEG'],
            ['IN2', SEGMENTS['IN2'], (0, 1), 'SEG'],
            ['IN3', SEGMENTS['IN3'], (0, 1), 'SEG'],
        ),
    ),
    'OMD_O01_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'OMD_O01_ORDER_DIET': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['OMD_O01_DIET', None, (0, 1), 'GRP'],
        ),
    ),
    'OMD_O01_ORDER_TRAY': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['ODT', SEGMENTS['ODT'], (1, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'OMD_O01_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['OMD_O01_PATIENT_VISIT', None, (0, 1), 'GRP'],
            ['OMD_O01_INSURANCE', None, (0, -1), 'GRP'],
            ['GT1', SEGMENTS['GT1'], (0, 1), 'SEG'],
            ['AL1', SEGMENTS['AL1'], (0, -1), 'SEG'],
        ),
    ),
    'OMD_O01_PATIENT_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
        ),
    ),
    'OMN_O01_INSURANCE': (
        'sequence',
        (
            ['IN1', SEGMENTS['IN1'], (1, 1), 'SEG'],
            ['IN2', SEGMENTS['IN2'], (0, 1), 'SEG'],
            ['IN3', SEGMENTS['IN3'], (0, 1), 'SEG'],
        ),
    ),
    'OMN_O01_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'OMN_O01_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['OMN_O01_ORDER_DETAIL', None, (0, 1), 'GRP'],
            ['BLG', SEGMENTS['BLG'], (0, 1), 'SEG'],
        ),
    ),
    'OMN_O01_ORDER_DETAIL': (
        'sequence',
        (
            ['RQD', SEGMENTS['RQD'], (1, 1), 'SEG'],
            ['RQ1', SEGMENTS['RQ1'], (0, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['OMN_O01_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'OMN_O01_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['OMN_O01_PATIENT_VISIT', None, (0, 1), 'GRP'],
            ['OMN_O01_INSURANCE', None, (0, -1), 'GRP'],
            ['GT1', SEGMENTS['GT1'], (0, 1), 'SEG'],
            ['AL1', SEGMENTS['AL1'], (0, -1), 'SEG'],
        ),
    ),
    'OMN_O01_PATIENT_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
        ),
    ),
    'OMS_O01_INSURANCE': (
        'sequence',
        (
            ['IN1', SEGMENTS['IN1'], (1, 1), 'SEG'],
            ['IN2', SEGMENTS['IN2'], (0, 1), 'SEG'],
            ['IN3', SEGMENTS['IN3'], (0, 1), 'SEG'],
        ),
    ),
    'OMS_O01_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'OMS_O01_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['OMS_O01_ORDER_DETAIL', None, (0, 1), 'GRP'],
            ['BLG', SEGMENTS['BLG'], (0, 1), 'SEG'],
        ),
    ),
    'OMS_O01_ORDER_DETAIL': (
        'sequence',
        (
            ['RQD', SEGMENTS['RQD'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['OMS_O01_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'OMS_O01_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['OMS_O01_PATIENT_VISIT', None, (0, 1), 'GRP'],
            ['OMS_O01_INSURANCE', None, (0, -1), 'GRP'],
            ['GT1', SEGMENTS['GT1'], (0, 1), 'SEG'],
            ['AL1', SEGMENTS['AL1'], (0, -1), 'SEG'],
        ),
    ),
    'OMS_O01_PATIENT_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
        ),
    ),
    'ORD_O02_ORDER_DIET': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['ODS', SEGMENTS['ODS'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'ORD_O02_ORDER_TRAY': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['ODT', SEGMENTS['ODT'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'ORD_O02_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'ORD_O02_RESPONSE': (
        'sequence',
        (
            ['ORD_O02_PATIENT', None, (0, 1), 'GRP'],
            ['ORD_O02_ORDER_DIET', None, (1, -1), 'GRP'],
            ['ORD_O02_ORDER_TRAY', None, (0, -1), 'GRP'],
        ),
    ),
    'ORF_R04_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (0, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'ORF_R04_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (0, 1), 'SEG'],
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['ORF_R04_OBSERVATION', None, (1, -1), 'GRP'],
            ['CTI', SEGMENTS['CTI'], (0, -1), 'SEG'],
        ),
    ),
    'ORF_R04_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'ORF_R04_QUERY_RESPONSE': (
        'sequence',
        (
            ['ORF_R04_PATIENT', None, (0, 1), 'GRP'],
            ['ORF_R04_ORDER', None, (1, -1), 'GRP'],
        ),
    ),
    'ORM_O01_CHOICE': (
        'choice',
        (
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['RQD', SEGMENTS['RQD'], (1, 1), 'SEG'],
            ['RQ1', SEGMENTS['RQ1'], (1, 1), 'SEG'],
            ['RXO', SEGMENTS['RXO'], (1, 1), 'SEG'],
            ['ODS', SEGMENTS['ODS'], (1, 1), 'SEG'],
            ['ODT', SEGMENTS['ODT'], (1, 1), 'SEG'],
        ),
    ),
    'ORM_O01_INSURANCE': (
        'sequence',
        (
            ['IN1', SEGMENTS['IN1'], (1, 1), 'SEG'],
            ['IN2', SEGMENTS['IN2'], (0, 1), 'SEG'],
            ['IN3', SEGMENTS['IN3'], (0, 1), 'SEG'],
        ),
    ),
    'ORM_O01_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'ORM_O01_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['ORM_O01_ORDER_DETAIL', None, (0, 1), 'GRP'],
            ['CTI', SEGMENTS['CTI'], (0, 1), 'SEG'],
            ['BLG', SEGMENTS['BLG'], (0, 1), 'SEG'],
        ),
    ),
    'ORM_O01_ORDER_DETAIL': (
        'sequence',
        (
            ['ORM_O01_CHOICE', None, (1, 1), 'GRP'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['DG1', SEGMENTS['DG1'], (0, -1), 'SEG'],
            ['ORM_O01_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'ORM_O01_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['ORM_O01_PATIENT_VISIT', None, (0, 1), 'GRP'],
            ['ORM_O01_INSURANCE', None, (0, -1), 'GRP'],
            ['GT1', SEGMENTS['GT1'], (0, 1), 'SEG'],
            ['AL1', SEGMENTS['AL1'], (0, -1), 'SEG'],
        ),
    ),
    'ORM_O01_PATIENT_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
        ),
    ),
    'ORN_O02_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['RQD', SEGMENTS['RQD'], (1, 1), 'SEG'],
            ['RQ1', SEGMENTS['RQ1'], (0, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'ORN_O02_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'ORN_O02_RESPONSE': (
        'sequence',
        (
            ['ORN_O02_PATIENT', None, (0, 1), 'GRP'],
            ['ORN_O02_ORDER', None, (1, -1), 'GRP'],
        ),
    ),
    'ORR_O02_CHOICE': (
        'choice',
        (
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['RQD', SEGMENTS['RQD'], (1, 1), 'SEG'],
            ['RQ1', SEGMENTS['RQ1'], (1, 1), 'SEG'],
            ['RXO', SEGMENTS['RXO'], (1, 1), 'SEG'],
            ['ODS', SEGMENTS['ODS'], (1, 1), 'SEG'],
            ['ODT', SEGMENTS['ODT'], (1, 1), 'SEG'],
        ),
    ),
    'ORR_O02_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['ORR_O02_CHOICE', None, (1, 1), 'GRP'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['CTI', SEGMENTS['CTI'], (0, -1), 'SEG'],
        ),
    ),
    'ORR_O02_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'ORR_O02_RESPONSE': (
        'sequence',
        (
            ['ORR_O02_PATIENT', None, (0, 1), 'GRP'],
            ['ORR_O02_ORDER', None, (1, -1), 'GRP'],
        ),
    ),
    'ORU_R01_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (0, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'ORU_R01_ORDER_OBSERVATION': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (0, 1), 'SEG'],
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['ORU_R01_OBSERVATION', None, (1, -1), 'GRP'],
            ['CTI', SEGMENTS['CTI'], (0, -1), 'SEG'],
        ),
    ),
    'ORU_R01_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['ORU_R01_VISIT', None, (0, 1), 'GRP'],
        ),
    ),
    'ORU_R01_RESPONSE': (
        'sequence',
        (
            ['ORU_R01_PATIENT', None, (0, 1), 'GRP'],
            ['ORU_R01_ORDER_OBSERVATION', None, (1, -1), 'GRP'],
        ),
    ),
    'ORU_R01_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
        ),
    ),
    'OSR_Q06_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['OBR', SEGMENTS['OBR'], (0, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['CTI', SEGMENTS['CTI'], (0, -1), 'SEG'],
        ),
    ),
    'OSR_Q06_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'OSR_Q06_RESPONSE': (
        'sequence',
        (
            ['OSR_Q06_PATIENT', None, (0, 1), 'GRP'],
            ['OSR_Q06_ORDER', None, (1, -1), 'GRP'],
        ),
    ),
    'PEX_P07_ASSOCIATED_PERSON': (
        'sequence',
        (
            ['NK1', SEGMENTS['NK1'], (1, 1), 'SEG'],
            ['PEX_P07_ASSOCIATED_RX_ORDER', None, (0, 1), 'GRP'],
            ['PEX_P07_ASSOCIATED_RX_ADMIN', None, (0, -1), 'GRP'],
            ['PRB', SEGMENTS['PRB'], (0, -1), 'SEG'],
            ['OBX', SEGMENTS['OBX'], (0, -1), 'SEG'],
        ),
    ),
    'PEX_P07_ASSOCIATED_RX_ADMIN': (
        'sequence',
        (
            ['RXA', SEGMENTS['RXA'], (1, 1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (0, 1), 'SEG'],
        ),
    ),
    'PEX_P07_ASSOCIATED_RX_ORDER': (
        'sequence',
        (
            ['RXE', SEGMENTS['RXE'], (1, 1), 'SEG'],
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
    'PEX_P07_PEX_CAUSE': (
        'sequence',
        (
            ['PCR', SEGMENTS['PCR'], (1, 1), 'SEG'],
            ['PEX_P07_RX_ORDER', None, (0, 1), 'GRP'],
            ['PEX_P07_RX_ADMINISTRATION', None, (0, -1), 'GRP'],
            ['PRB', SEGMENTS['PRB'], (0, -1), 'SEG'],
            ['OBX', SEGMENTS['OBX'], (0, -1), 'SEG'],
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
        ),
    ),
    'PEX_P07_RX_ORDER': (
        'sequence',
        (
            ['RXE', SEGMENTS['RXE'], (1, 1), 'SEG'],
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
    'PEX_P07_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
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
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
            ['PGL_PC6_ORDER_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'PGL_PC6_ORDER_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
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
    'PIN_I07_GUARANTOR_INSURANCE': (
        'sequence',
        (
            ['GT1', SEGMENTS['GT1'], (0, -1), 'SEG'],
            ['PIN_I07_INSURANCE', None, (1, -1), 'GRP'],
        ),
    ),
    'PIN_I07_INSURANCE': (
        'sequence',
        (
            ['IN1', SEGMENTS['IN1'], (1, 1), 'SEG'],
            ['IN2', SEGMENTS['IN2'], (0, 1), 'SEG'],
            ['IN3', SEGMENTS['IN3'], (0, 1), 'SEG'],
        ),
    ),
    'PIN_I07_PROVIDER': (
        'sequence',
        (
            ['PRD', SEGMENTS['PRD'], (1, 1), 'SEG'],
            ['CTD', SEGMENTS['CTD'], (0, -1), 'SEG'],
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
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
            ['PPG_PCG_ORDER_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'PPG_PCG_ORDER_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
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
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
            ['PPP_PCB_ORDER_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'PPP_PCB_ORDER_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
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
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
            ['PPR_PC1_ORDER_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'PPR_PC1_ORDER_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
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
    'PPT_PCL_GOAL': (
        'sequence',
        (
            ['GOL', SEGMENTS['GOL'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
            ['PPT_PCL_GOAL_ROLE', None, (0, -1), 'GRP'],
            ['PPT_PCL_GOAL_OBSERVATION', None, (0, -1), 'GRP'],
            ['PPT_PCL_PROBLEM', None, (0, -1), 'GRP'],
            ['PPT_PCL_ORDER', None, (0, -1), 'GRP'],
        ),
    ),
    'PPT_PCL_GOAL_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'PPT_PCL_GOAL_ROLE': (
        'sequence',
        (
            ['ROL', SEGMENTS['ROL'], (1, 1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
        ),
    ),
    'PPT_PCL_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PPT_PCL_ORDER_DETAIL', None, (0, 1), 'GRP'],
        ),
    ),
    'PPT_PCL_ORDER_DETAIL': (
        'sequence',
        (
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
            ['PPT_PCL_ORDER_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'PPT_PCL_ORDER_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
        ),
    ),
    'PPT_PCL_PATHWAY': (
        'sequence',
        (
            ['PTH', SEGMENTS['PTH'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
            ['PPT_PCL_PATHWAY_ROLE', None, (0, -1), 'GRP'],
            ['PPT_PCL_GOAL', None, (0, -1), 'GRP'],
        ),
    ),
    'PPT_PCL_PATHWAY_ROLE': (
        'sequence',
        (
            ['ROL', SEGMENTS['ROL'], (1, 1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
        ),
    ),
    'PPT_PCL_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PPT_PCL_PATIENT_VISIT', None, (0, 1), 'GRP'],
            ['PPT_PCL_PATHWAY', None, (1, -1), 'GRP'],
        ),
    ),
    'PPT_PCL_PATIENT_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
        ),
    ),
    'PPT_PCL_PROBLEM': (
        'sequence',
        (
            ['PRB', SEGMENTS['PRB'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
            ['PPT_PCL_PROBLEM_ROLE', None, (0, -1), 'GRP'],
            ['PPT_PCL_PROBLEM_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'PPT_PCL_PROBLEM_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'PPT_PCL_PROBLEM_ROLE': (
        'sequence',
        (
            ['ROL', SEGMENTS['ROL'], (1, 1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
        ),
    ),
    'PPV_PCA_GOAL': (
        'sequence',
        (
            ['GOL', SEGMENTS['GOL'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
            ['PPV_PCA_GOAL_ROLE', None, (0, -1), 'GRP'],
            ['PPV_PCA_GOAL_PATHWAY', None, (0, -1), 'GRP'],
            ['PPV_PCA_GOAL_OBSERVATION', None, (0, -1), 'GRP'],
            ['PPV_PCA_PROBLEM', None, (0, -1), 'GRP'],
            ['PPV_PCA_ORDER', None, (0, -1), 'GRP'],
        ),
    ),
    'PPV_PCA_GOAL_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'PPV_PCA_GOAL_PATHWAY': (
        'sequence',
        (
            ['PTH', SEGMENTS['PTH'], (1, 1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
        ),
    ),
    'PPV_PCA_GOAL_ROLE': (
        'sequence',
        (
            ['ROL', SEGMENTS['ROL'], (1, 1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
        ),
    ),
    'PPV_PCA_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PPV_PCA_ORDER_DETAIL', None, (0, 1), 'GRP'],
        ),
    ),
    'PPV_PCA_ORDER_DETAIL': (
        'sequence',
        (
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
            ['PPV_PCA_ORDER_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'PPV_PCA_ORDER_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
        ),
    ),
    'PPV_PCA_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PPV_PCA_PATIENT_VISIT', None, (0, 1), 'GRP'],
            ['PPV_PCA_GOAL', None, (1, -1), 'GRP'],
        ),
    ),
    'PPV_PCA_PATIENT_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
        ),
    ),
    'PPV_PCA_PROBLEM': (
        'sequence',
        (
            ['PRB', SEGMENTS['PRB'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
            ['PPV_PCA_PROBLEM_ROLE', None, (0, -1), 'GRP'],
            ['PPV_PCA_PROBLEM_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'PPV_PCA_PROBLEM_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'PPV_PCA_PROBLEM_ROLE': (
        'sequence',
        (
            ['ROL', SEGMENTS['ROL'], (1, 1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
        ),
    ),
    'PRR_PC5_GOAL': (
        'sequence',
        (
            ['GOL', SEGMENTS['GOL'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
            ['PRR_PC5_GOAL_ROLE', None, (0, -1), 'GRP'],
            ['PRR_PC5_GOAL_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'PRR_PC5_GOAL_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'PRR_PC5_GOAL_ROLE': (
        'sequence',
        (
            ['ROL', SEGMENTS['ROL'], (1, 1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
        ),
    ),
    'PRR_PC5_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PRR_PC5_ORDER_DETAIL', None, (0, 1), 'GRP'],
        ),
    ),
    'PRR_PC5_ORDER_DETAIL': (
        'sequence',
        (
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
            ['PRR_PC5_ORDER_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'PRR_PC5_ORDER_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
        ),
    ),
    'PRR_PC5_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PRR_PC5_PATIENT_VISIT', None, (0, 1), 'GRP'],
            ['PRR_PC5_PROBLEM', None, (1, -1), 'GRP'],
        ),
    ),
    'PRR_PC5_PATIENT_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
        ),
    ),
    'PRR_PC5_PROBLEM': (
        'sequence',
        (
            ['PRB', SEGMENTS['PRB'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
            ['PRR_PC5_PROBLEM_ROLE', None, (0, -1), 'GRP'],
            ['PRR_PC5_PROBLEM_PATHWAY', None, (0, -1), 'GRP'],
            ['PRR_PC5_PROBLEM_OBSERVATION', None, (0, -1), 'GRP'],
            ['PRR_PC5_GOAL', None, (0, -1), 'GRP'],
            ['PRR_PC5_ORDER', None, (0, -1), 'GRP'],
        ),
    ),
    'PRR_PC5_PROBLEM_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'PRR_PC5_PROBLEM_PATHWAY': (
        'sequence',
        (
            ['PTH', SEGMENTS['PTH'], (1, 1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
        ),
    ),
    'PRR_PC5_PROBLEM_ROLE': (
        'sequence',
        (
            ['ROL', SEGMENTS['ROL'], (1, 1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
        ),
    ),
    'PTR_PCF_GOAL': (
        'sequence',
        (
            ['GOL', SEGMENTS['GOL'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
            ['PTR_PCF_GOAL_ROLE', None, (0, -1), 'GRP'],
            ['PTR_PCF_GOAL_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'PTR_PCF_GOAL_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'PTR_PCF_GOAL_ROLE': (
        'sequence',
        (
            ['ROL', SEGMENTS['ROL'], (1, 1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
        ),
    ),
    'PTR_PCF_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['PTR_PCF_ORDER_DETAIL', None, (0, 1), 'GRP'],
        ),
    ),
    'PTR_PCF_ORDER_DETAIL': (
        'sequence',
        (
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
            ['PTR_PCF_ORDER_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'PTR_PCF_ORDER_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
        ),
    ),
    'PTR_PCF_PATHWAY': (
        'sequence',
        (
            ['PTH', SEGMENTS['PTH'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
            ['PTR_PCF_PATHWAY_ROLE', None, (0, -1), 'GRP'],
            ['PTR_PCF_PROBLEM', None, (0, -1), 'GRP'],
        ),
    ),
    'PTR_PCF_PATHWAY_ROLE': (
        'sequence',
        (
            ['ROL', SEGMENTS['ROL'], (1, 1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
        ),
    ),
    'PTR_PCF_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PTR_PCF_PATIENT_VISIT', None, (0, 1), 'GRP'],
            ['PTR_PCF_PATHWAY', None, (1, -1), 'GRP'],
        ),
    ),
    'PTR_PCF_PATIENT_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
        ),
    ),
    'PTR_PCF_PROBLEM': (
        'sequence',
        (
            ['PRB', SEGMENTS['PRB'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
            ['PTR_PCF_PROBLEM_ROLE', None, (0, -1), 'GRP'],
            ['PTR_PCF_PROBLEM_OBSERVATION', None, (0, -1), 'GRP'],
            ['PTR_PCF_GOAL', None, (0, -1), 'GRP'],
            ['PTR_PCF_ORDER', None, (0, -1), 'GRP'],
        ),
    ),
    'PTR_PCF_PROBLEM_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'PTR_PCF_PROBLEM_ROLE': (
        'sequence',
        (
            ['ROL', SEGMENTS['ROL'], (1, 1), 'SEG'],
            ['VAR', SEGMENTS['VAR'], (0, -1), 'SEG'],
        ),
    ),
    'RAR_RAR_DEFINITION': (
        'sequence',
        (
            ['QRD', SEGMENTS['QRD'], (1, 1), 'SEG'],
            ['QRF', SEGMENTS['QRF'], (0, 1), 'SEG'],
            ['RAR_RAR_PATIENT', None, (0, 1), 'GRP'],
            ['RAR_RAR_ORDER', None, (1, -1), 'GRP'],
        ),
    ),
    'RAR_RAR_ENCODING': (
        'sequence',
        (
            ['RXE', SEGMENTS['RXE'], (1, 1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (1, -1), 'SEG'],
            ['RXC', SEGMENTS['RXC'], (0, -1), 'SEG'],
        ),
    ),
    'RAR_RAR_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['RAR_RAR_ENCODING', None, (0, 1), 'GRP'],
            ['RXA', SEGMENTS['RXA'], (1, -1), 'SEG'],
        ),
    ),
    'RAR_RAR_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'RAS_O01_COMPONENTS': (
        'sequence',
        (
            ['RXC', SEGMENTS['RXC'], (1, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'RAS_O01_ENCODING': (
        'sequence',
        (
            ['RXE', SEGMENTS['RXE'], (1, 1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (1, -1), 'SEG'],
            ['RXC', SEGMENTS['RXC'], (0, -1), 'SEG'],
        ),
    ),
    'RAS_O01_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'RAS_O01_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['RAS_O01_ORDER_DETAIL', None, (0, 1), 'GRP'],
            ['RAS_O01_ENCODING', None, (0, 1), 'GRP'],
            ['RXA', SEGMENTS['RXA'], (1, -1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (1, 1), 'SEG'],
            ['RAS_O01_OBSERVATION', None, (0, -1), 'GRP'],
            ['CTI', SEGMENTS['CTI'], (0, -1), 'SEG'],
        ),
    ),
    'RAS_O01_ORDER_DETAIL': (
        'sequence',
        (
            ['RXO', SEGMENTS['RXO'], (1, 1), 'SEG'],
            ['RAS_O01_ORDER_DETAIL_SUPPLEMENT', None, (0, 1), 'GRP'],
        ),
    ),
    'RAS_O01_ORDER_DETAIL_SUPPLEMENT': (
        'sequence',
        (
            ['NTE', SEGMENTS['NTE'], (1, -1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (1, -1), 'SEG'],
            ['RAS_O01_COMPONENTS', None, (0, 1), 'GRP'],
        ),
    ),
    'RAS_O01_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['AL1', SEGMENTS['AL1'], (0, -1), 'SEG'],
            ['RAS_O01_PATIENT_VISIT', None, (0, 1), 'GRP'],
        ),
    ),
    'RAS_O01_PATIENT_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
        ),
    ),
    'RCI_I05_OBSERVATION': (
        'sequence',
        (
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['RCI_I05_RESULTS', None, (0, -1), 'GRP'],
        ),
    ),
    'RCI_I05_PROVIDER': (
        'sequence',
        (
            ['PRD', SEGMENTS['PRD'], (1, 1), 'SEG'],
            ['CTD', SEGMENTS['CTD'], (0, -1), 'SEG'],
        ),
    ),
    'RCI_I05_RESULTS': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'RCL_I06_PROVIDER': (
        'sequence',
        (
            ['PRD', SEGMENTS['PRD'], (1, 1), 'SEG'],
            ['CTD', SEGMENTS['CTD'], (0, -1), 'SEG'],
        ),
    ),
    'RDE_O01_COMPONENT': (
        'sequence',
        (
            ['RXC', SEGMENTS['RXC'], (1, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'RDE_O01_INSURANCE': (
        'sequence',
        (
            ['IN1', SEGMENTS['IN1'], (1, 1), 'SEG'],
            ['IN2', SEGMENTS['IN2'], (0, 1), 'SEG'],
            ['IN3', SEGMENTS['IN3'], (0, 1), 'SEG'],
        ),
    ),
    'RDE_O01_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (0, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'RDE_O01_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['RDE_O01_ORDER_DETAIL', None, (0, 1), 'GRP'],
            ['RXE', SEGMENTS['RXE'], (1, 1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (1, -1), 'SEG'],
            ['RXC', SEGMENTS['RXC'], (0, -1), 'SEG'],
            ['RDE_O01_OBSERVATION', None, (1, -1), 'GRP'],
            ['CTI', SEGMENTS['CTI'], (0, 1), 'SEG'],
        ),
    ),
    'RDE_O01_ORDER_DETAIL': (
        'sequence',
        (
            ['RXO', SEGMENTS['RXO'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (1, -1), 'SEG'],
            ['RDE_O01_COMPONENT', None, (0, 1), 'GRP'],
        ),
    ),
    'RDE_O01_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['RDE_O01_PATIENT_VISIT', None, (0, 1), 'GRP'],
            ['RDE_O01_INSURANCE', None, (0, -1), 'GRP'],
            ['GT1', SEGMENTS['GT1'], (0, 1), 'SEG'],
            ['AL1', SEGMENTS['AL1'], (0, -1), 'SEG'],
        ),
    ),
    'RDE_O01_PATIENT_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
        ),
    ),
    'RDO_O01_COMPONENT': (
        'sequence',
        (
            ['RXC', SEGMENTS['RXC'], (1, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'RDO_O01_INSURANCE': (
        'sequence',
        (
            ['IN1', SEGMENTS['IN1'], (1, 1), 'SEG'],
            ['IN2', SEGMENTS['IN2'], (0, 1), 'SEG'],
            ['IN3', SEGMENTS['IN3'], (0, 1), 'SEG'],
        ),
    ),
    'RDO_O01_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'RDO_O01_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['RDO_O01_ORDER_DETAIL', None, (0, 1), 'GRP'],
            ['BLG', SEGMENTS['BLG'], (0, 1), 'SEG'],
        ),
    ),
    'RDO_O01_ORDER_DETAIL': (
        'sequence',
        (
            ['RXO', SEGMENTS['RXO'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (1, -1), 'SEG'],
            ['RDO_O01_COMPONENT', None, (0, 1), 'GRP'],
            ['RDO_O01_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'RDO_O01_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['RDO_O01_PATIENT_VISIT', None, (0, 1), 'GRP'],
            ['RDO_O01_INSURANCE', None, (0, -1), 'GRP'],
            ['GT1', SEGMENTS['GT1'], (0, 1), 'SEG'],
            ['AL1', SEGMENTS['AL1'], (0, -1), 'SEG'],
        ),
    ),
    'RDO_O01_PATIENT_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
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
            ['RXR', SEGMENTS['RXR'], (1, 1), 'SEG'],
            ['RXC', SEGMENTS['RXC'], (0, -1), 'SEG'],
        ),
    ),
    'RDR_RDR_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
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
    'RDS_O01_COMPONENT': (
        'sequence',
        (
            ['RXC', SEGMENTS['RXC'], (1, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'RDS_O01_ENCODING': (
        'sequence',
        (
            ['RXE', SEGMENTS['RXE'], (1, 1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (1, -1), 'SEG'],
            ['RXC', SEGMENTS['RXC'], (0, -1), 'SEG'],
        ),
    ),
    'RDS_O01_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'RDS_O01_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['RDS_O01_ORDER_DETAIL', None, (0, 1), 'GRP'],
            ['RDS_O01_ENCODING', None, (0, 1), 'GRP'],
            ['RXD', SEGMENTS['RXD'], (1, 1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (1, -1), 'SEG'],
            ['RXC', SEGMENTS['RXC'], (0, -1), 'SEG'],
            ['RDS_O01_OBSERVATION', None, (1, -1), 'GRP'],
        ),
    ),
    'RDS_O01_ORDER_DETAIL': (
        'sequence',
        (
            ['RXO', SEGMENTS['RXO'], (1, 1), 'SEG'],
            ['RDS_O01_ORDER_DETAIL_SUPPLEMENT', None, (0, 1), 'GRP'],
        ),
    ),
    'RDS_O01_ORDER_DETAIL_SUPPLEMENT': (
        'sequence',
        (
            ['NTE', SEGMENTS['NTE'], (1, -1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (1, -1), 'SEG'],
            ['RDS_O01_COMPONENT', None, (0, 1), 'GRP'],
        ),
    ),
    'RDS_O01_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PD1', SEGMENTS['PD1'], (0, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['AL1', SEGMENTS['AL1'], (0, -1), 'SEG'],
            ['RDS_O01_PATIENT_VISIT', None, (0, 1), 'GRP'],
        ),
    ),
    'RDS_O01_PATIENT_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
        ),
    ),
    'REF_I12_AUTCTD_SUPPGRP2': (
        'sequence',
        (
            ['AUT', SEGMENTS['AUT'], (1, 1), 'SEG'],
            ['CTD', SEGMENTS['CTD'], (0, 1), 'SEG'],
        ),
    ),
    'REF_I12_AUTHORIZATION': (
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
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'REF_I12_PROCEDURE': (
        'sequence',
        (
            ['PR1', SEGMENTS['PR1'], (1, 1), 'SEG'],
            ['REF_I12_AUTCTD_SUPPGRP2', None, (0, 1), 'GRP'],
        ),
    ),
    'REF_I12_PROVIDER': (
        'sequence',
        (
            ['PRD', SEGMENTS['PRD'], (1, 1), 'SEG'],
            ['CTD', SEGMENTS['CTD'], (0, -1), 'SEG'],
        ),
    ),
    'REF_I12_RESULTS': (
        'sequence',
        (
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['REF_I12_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'REF_I12_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
        ),
    ),
    'RER_RER_DEFINITION': (
        'sequence',
        (
            ['QRD', SEGMENTS['QRD'], (1, 1), 'SEG'],
            ['QRF', SEGMENTS['QRF'], (0, 1), 'SEG'],
            ['RER_RER_PATIENT', None, (0, 1), 'GRP'],
            ['RER_RER_ORDER', None, (1, -1), 'GRP'],
        ),
    ),
    'RER_RER_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['RXE', SEGMENTS['RXE'], (1, 1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (1, -1), 'SEG'],
            ['RXC', SEGMENTS['RXC'], (0, -1), 'SEG'],
        ),
    ),
    'RER_RER_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'RGR_RGR_DEFINITION': (
        'sequence',
        (
            ['QRD', SEGMENTS['QRD'], (1, 1), 'SEG'],
            ['QRF', SEGMENTS['QRF'], (0, 1), 'SEG'],
            ['RGR_RGR_PATIENT', None, (0, 1), 'GRP'],
            ['RGR_RGR_ORDER', None, (1, -1), 'GRP'],
        ),
    ),
    'RGR_RGR_ENCODING': (
        'sequence',
        (
            ['RXE', SEGMENTS['RXE'], (1, 1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (1, -1), 'SEG'],
            ['RXC', SEGMENTS['RXC'], (0, -1), 'SEG'],
        ),
    ),
    'RGR_RGR_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['RGR_RGR_ENCODING', None, (0, 1), 'GRP'],
            ['RXG', SEGMENTS['RXG'], (1, -1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (1, -1), 'SEG'],
            ['RXC', SEGMENTS['RXC'], (0, -1), 'SEG'],
        ),
    ),
    'RGR_RGR_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'RGV_O01_COMPONENTS': (
        'sequence',
        (
            ['RXC', SEGMENTS['RXC'], (1, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'RGV_O01_ENCODING': (
        'sequence',
        (
            ['RXE', SEGMENTS['RXE'], (1, 1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (1, -1), 'SEG'],
            ['RXC', SEGMENTS['RXC'], (0, -1), 'SEG'],
        ),
    ),
    'RGV_O01_GIVE': (
        'sequence',
        (
            ['RXG', SEGMENTS['RXG'], (1, 1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (1, -1), 'SEG'],
            ['RXC', SEGMENTS['RXC'], (0, -1), 'SEG'],
            ['RGV_O01_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'RGV_O01_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'RGV_O01_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['RGV_O01_ORDER_DETAIL', None, (0, 1), 'GRP'],
            ['RGV_O01_ENCODING', None, (0, 1), 'GRP'],
            ['RGV_O01_GIVE', None, (1, -1), 'GRP'],
        ),
    ),
    'RGV_O01_ORDER_DETAIL': (
        'sequence',
        (
            ['RXO', SEGMENTS['RXO'], (1, 1), 'SEG'],
            ['RGV_O01_ORDER_DETAIL_SUPPLEMENT', None, (0, 1), 'GRP'],
        ),
    ),
    'RGV_O01_ORDER_DETAIL_SUPPLEMENT': (
        'sequence',
        (
            ['NTE', SEGMENTS['NTE'], (1, -1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (1, -1), 'SEG'],
            ['RGV_O01_COMPONENTS', None, (0, 1), 'GRP'],
        ),
    ),
    'RGV_O01_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['AL1', SEGMENTS['AL1'], (0, -1), 'SEG'],
            ['RGV_O01_PATIENT_VISIT', None, (0, 1), 'GRP'],
        ),
    ),
    'RGV_O01_PATIENT_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
        ),
    ),
    'ROR_ROR_DEFINITION': (
        'sequence',
        (
            ['QRD', SEGMENTS['QRD'], (1, 1), 'SEG'],
            ['QRF', SEGMENTS['QRF'], (0, 1), 'SEG'],
            ['ROR_ROR_PATIENT', None, (0, 1), 'GRP'],
            ['ROR_ROR_ORDER', None, (1, -1), 'GRP'],
        ),
    ),
    'ROR_ROR_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['RXO', SEGMENTS['RXO'], (1, 1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (1, -1), 'SEG'],
            ['RXC', SEGMENTS['RXC'], (0, -1), 'SEG'],
        ),
    ),
    'ROR_ROR_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'RPA_I08_AUTCTD_SUPPGRP2': (
        'sequence',
        (
            ['AUT', SEGMENTS['AUT'], (1, 1), 'SEG'],
            ['CTD', SEGMENTS['CTD'], (0, 1), 'SEG'],
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
            ['RPA_I08_AUTCTD_SUPPGRP2', None, (0, 1), 'GRP'],
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
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'RPA_I08_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
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
    'RPL_I02_PROVIDER': (
        'sequence',
        (
            ['PRD', SEGMENTS['PRD'], (1, 1), 'SEG'],
            ['CTD', SEGMENTS['CTD'], (0, -1), 'SEG'],
        ),
    ),
    'RQA_I08_AUTCTD_SUPPGRP2': (
        'sequence',
        (
            ['AUT', SEGMENTS['AUT'], (1, 1), 'SEG'],
            ['CTD', SEGMENTS['CTD'], (0, 1), 'SEG'],
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
            ['RQA_I08_AUTCTD_SUPPGRP2', None, (0, 1), 'GRP'],
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
    'RQC_I05_PROVIDER': (
        'sequence',
        (
            ['PRD', SEGMENTS['PRD'], (1, 1), 'SEG'],
            ['CTD', SEGMENTS['CTD'], (0, -1), 'SEG'],
        ),
    ),
    'RQC_I06_PROVIDER': (
        'sequence',
        (
            ['PRD', SEGMENTS['PRD'], (1, 1), 'SEG'],
            ['CTD', SEGMENTS['CTD'], (0, -1), 'SEG'],
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
    'RRA_O02_ADMINISTRATION': (
        'sequence',
        (
            ['RXA', SEGMENTS['RXA'], (1, 1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (1, 1), 'SEG'],
        ),
    ),
    'RRA_O02_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['RRA_O02_ADMINISTRATION', None, (0, -1), 'GRP'],
        ),
    ),
    'RRA_O02_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'RRA_O02_RESPONSE': (
        'sequence',
        (
            ['RRA_O02_PATIENT', None, (0, 1), 'GRP'],
            ['RRA_O02_ORDER', None, (1, -1), 'GRP'],
        ),
    ),
    'RRD_O02_DISPENSE': (
        'sequence',
        (
            ['RXD', SEGMENTS['RXD'], (1, 1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (1, -1), 'SEG'],
            ['RXC', SEGMENTS['RXC'], (0, -1), 'SEG'],
        ),
    ),
    'RRD_O02_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['RRD_O02_DISPENSE', None, (0, 1), 'GRP'],
        ),
    ),
    'RRD_O02_PATIENT': (
        'sequence',
        (
            ['RRD_O02_RESPONSE', None, (0, 1), 'GRP'],
            ['RRD_O02_ORDER', None, (1, -1), 'GRP'],
        ),
    ),
    'RRD_O02_RESPONSE': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'RRG_O02_GIVE': (
        'sequence',
        (
            ['RXG', SEGMENTS['RXG'], (1, 1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (1, -1), 'SEG'],
            ['RXC', SEGMENTS['RXC'], (0, -1), 'SEG'],
        ),
    ),
    'RRG_O02_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['RRG_O02_GIVE', None, (0, 1), 'GRP'],
        ),
    ),
    'RRG_O02_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'RRG_O02_RESPONSE': (
        'sequence',
        (
            ['RRG_O02_PATIENT', None, (0, 1), 'GRP'],
            ['RRG_O02_ORDER', None, (1, -1), 'GRP'],
        ),
    ),
    'RRI_I12_AUTCTD_SUPPGRP2': (
        'sequence',
        (
            ['AUT', SEGMENTS['AUT'], (1, 1), 'SEG'],
            ['CTD', SEGMENTS['CTD'], (0, 1), 'SEG'],
        ),
    ),
    'RRI_I12_AUTHORIZATION': (
        'sequence',
        (
            ['AUT', SEGMENTS['AUT'], (1, 1), 'SEG'],
            ['CTD', SEGMENTS['CTD'], (0, 1), 'SEG'],
        ),
    ),
    'RRI_I12_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'RRI_I12_PROCEDURE': (
        'sequence',
        (
            ['PR1', SEGMENTS['PR1'], (1, 1), 'SEG'],
            ['RRI_I12_AUTCTD_SUPPGRP2', None, (0, 1), 'GRP'],
        ),
    ),
    'RRI_I12_PROVIDER': (
        'sequence',
        (
            ['PRD', SEGMENTS['PRD'], (1, 1), 'SEG'],
            ['CTD', SEGMENTS['CTD'], (0, -1), 'SEG'],
        ),
    ),
    'RRI_I12_RESULTS': (
        'sequence',
        (
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['RRI_I12_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'RRI_I12_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
        ),
    ),
    'RRO_O02_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['RRO_O02_ORDER_DETAIL', None, (0, 1), 'GRP'],
        ),
    ),
    'RRO_O02_ORDER_DETAIL': (
        'sequence',
        (
            ['RXO', SEGMENTS['RXO'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (1, -1), 'SEG'],
            ['RXC', SEGMENTS['RXC'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'RRO_O02_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'RRO_O02_RESPONSE': (
        'sequence',
        (
            ['RRO_O02_PATIENT', None, (0, 1), 'GRP'],
            ['RRO_O02_ORDER', None, (1, -1), 'GRP'],
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
    'SQM_S25_GENERAL_RESOURCE': (
        'sequence',
        (
            ['AIG', SEGMENTS['AIG'], (1, 1), 'SEG'],
            ['APR', SEGMENTS['APR'], (0, 1), 'SEG'],
        ),
    ),
    'SQM_S25_LOCATION_RESOURCE': (
        'sequence',
        (
            ['AIL', SEGMENTS['AIL'], (1, 1), 'SEG'],
            ['APR', SEGMENTS['APR'], (0, 1), 'SEG'],
        ),
    ),
    'SQM_S25_PERSONNEL_RESOURCE': (
        'sequence',
        (
            ['AIP', SEGMENTS['AIP'], (1, 1), 'SEG'],
            ['APR', SEGMENTS['APR'], (0, 1), 'SEG'],
        ),
    ),
    'SQM_S25_REQUEST': (
        'sequence',
        (
            ['ARQ', SEGMENTS['ARQ'], (1, 1), 'SEG'],
            ['APR', SEGMENTS['APR'], (0, 1), 'SEG'],
            ['PID', SEGMENTS['PID'], (0, 1), 'SEG'],
            ['SQM_S25_RESOURCES', None, (1, -1), 'GRP'],
        ),
    ),
    'SQM_S25_RESOURCES': (
        'sequence',
        (
            ['RGS', SEGMENTS['RGS'], (1, 1), 'SEG'],
            ['SQM_S25_SERVICE', None, (0, -1), 'GRP'],
            ['SQM_S25_GENERAL_RESOURCE', None, (0, -1), 'GRP'],
            ['SQM_S25_PERSONNEL_RESOURCE', None, (0, -1), 'GRP'],
            ['SQM_S25_LOCATION_RESOURCE', None, (0, -1), 'GRP'],
        ),
    ),
    'SQM_S25_SERVICE': (
        'sequence',
        (
            ['AIS', SEGMENTS['AIS'], (1, 1), 'SEG'],
            ['APR', SEGMENTS['APR'], (0, 1), 'SEG'],
        ),
    ),
    'SQR_S25_GENERAL_RESOURCE': (
        'sequence',
        (
            ['AIG', SEGMENTS['AIG'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SQR_S25_LOCATION_RESOURCE': (
        'sequence',
        (
            ['AIL', SEGMENTS['AIL'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SQR_S25_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PV1', SEGMENTS['PV1'], (0, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['DG1', SEGMENTS['DG1'], (0, 1), 'SEG'],
        ),
    ),
    'SQR_S25_PERSONNEL_RESOURCE': (
        'sequence',
        (
            ['AIP', SEGMENTS['AIP'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'SQR_S25_RESOURCES': (
        'sequence',
        (
            ['RGS', SEGMENTS['RGS'], (1, 1), 'SEG'],
            ['SQR_S25_SERVICE', None, (0, -1), 'GRP'],
            ['SQR_S25_GENERAL_RESOURCE', None, (0, -1), 'GRP'],
            ['SQR_S25_PERSONNEL_RESOURCE', None, (0, -1), 'GRP'],
            ['SQR_S25_LOCATION_RESOURCE', None, (0, -1), 'GRP'],
        ),
    ),
    'SQR_S25_SCHEDULE': (
        'sequence',
        (
            ['SCH', SEGMENTS['SCH'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['SQR_S25_PATIENT', None, (0, 1), 'GRP'],
            ['SQR_S25_RESOURCES', None, (1, -1), 'GRP'],
        ),
    ),
    'SQR_S25_SERVICE': (
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
    'SRM_S01_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PV1', SEGMENTS['PV1'], (0, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['OBX', SEGMENTS['OBX'], (0, -1), 'SEG'],
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
    'SUR_P09_FACILITY': (
        'sequence',
        (
            ['FAC', SEGMENTS['FAC'], (1, 1), 'SEG'],
            ['SUR_P09_PRODUCT', None, (1, -1), 'GRP'],
            ['PSH', SEGMENTS['PSH'], (1, 1), 'SEG'],
            ['SUR_P09_FACILITY_DETAIL', None, (1, -1), 'GRP'],
        ),
    ),
    'SUR_P09_FACILITY_DETAIL': (
        'sequence',
        (
            ['FAC', SEGMENTS['FAC'], (1, 1), 'SEG'],
            ['PDC', SEGMENTS['PDC'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (1, 1), 'SEG'],
        ),
    ),
    'SUR_P09_PRODUCT': (
        'sequence',
        (
            ['PSH', SEGMENTS['PSH'], (1, 1), 'SEG'],
            ['PDC', SEGMENTS['PDC'], (1, 1), 'SEG'],
        ),
    ),
    'VXR_V03_INSURANCE': (
        'sequence',
        (
            ['IN1', SEGMENTS['IN1'], (1, 1), 'SEG'],
            ['IN2', SEGMENTS['IN2'], (0, 1), 'SEG'],
            ['IN3', SEGMENTS['IN3'], (0, 1), 'SEG'],
        ),
    ),
    'VXR_V03_OBSERVATION': (
        'sequence',
        (
            ['OBX', SEGMENTS['OBX'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'VXR_V03_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (0, 1), 'SEG'],
            ['RXA', SEGMENTS['RXA'], (1, 1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (0, 1), 'SEG'],
            ['VXR_V03_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'VXR_V03_PATIENT_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
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
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'VXU_V04_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (0, 1), 'SEG'],
            ['RXA', SEGMENTS['RXA'], (1, 1), 'SEG'],
            ['RXR', SEGMENTS['RXR'], (0, 1), 'SEG'],
            ['VXU_V04_OBSERVATION', None, (0, -1), 'GRP'],
        ),
    ),
    'VXU_V04_PATIENT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
        ),
    ),
    'VXX_V02_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['NK1', SEGMENTS['NK1'], (0, -1), 'SEG'],
        ),
    ),
}
for k, v in iteritems(GROUPS):
    for item in v[1]:
        if item[3] == 'GRP':
            item[1] = GROUPS[item[0]]
