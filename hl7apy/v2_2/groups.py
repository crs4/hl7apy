from hl7apy.utils import iteritems

from .segments import SEGMENTS

GROUPS = {
    'ADR_A19_INSURANCE': (
        'sequence',
        (
            ['IN1', SEGMENTS['IN1'], (1, 1), 'SEG'],
            ['IN2', SEGMENTS['IN2'], (0, 1), 'SEG'],
            ['IN3', SEGMENTS['IN3'], (0, 1), 'SEG'],
        ),
    ),
    'ADR_A19_QUERY_RESPONSE': (
        'sequence',
        (
            ['EVN', SEGMENTS['EVN'], (0, 1), 'SEG'],
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['NK1', SEGMENTS['NK1'], (0, -1), 'SEG'],
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['OBX', SEGMENTS['OBX'], (0, -1), 'SEG'],
            ['AL1', SEGMENTS['AL1'], (0, -1), 'SEG'],
            ['DG1', SEGMENTS['DG1'], (0, -1), 'SEG'],
            ['PR1', SEGMENTS['PR1'], (0, -1), 'SEG'],
            ['GT1', SEGMENTS['GT1'], (0, -1), 'SEG'],
            ['ADR_A19_INSURANCE', None, (0, -1), 'GRP'],
            ['ACC', SEGMENTS['ACC'], (0, 1), 'SEG'],
            ['UB1', SEGMENTS['UB1'], (0, 1), 'SEG'],
            ['UB2', SEGMENTS['UB2'], (0, 1), 'SEG'],
        ),
    ),
    'ADT_A01_INSURANCE': (
        'sequence',
        (
            ['IN1', SEGMENTS['IN1'], (1, 1), 'SEG'],
            ['IN2', SEGMENTS['IN2'], (0, 1), 'SEG'],
            ['IN3', SEGMENTS['IN3'], (0, 1), 'SEG'],
        ),
    ),
    'ADT_A04_INSURANCE': (
        'sequence',
        (
            ['IN1', SEGMENTS['IN1'], (1, 1), 'SEG'],
            ['IN2', SEGMENTS['IN2'], (0, 1), 'SEG'],
            ['IN3', SEGMENTS['IN3'], (0, 1), 'SEG'],
        ),
    ),
    'ADT_A05_INSURANCE': (
        'sequence',
        (
            ['IN1', SEGMENTS['IN1'], (1, 1), 'SEG'],
            ['IN2', SEGMENTS['IN2'], (0, 1), 'SEG'],
            ['IN3', SEGMENTS['IN3'], (0, 1), 'SEG'],
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
    'ADT_A07_INSURANCE': (
        'sequence',
        (
            ['IN1', SEGMENTS['IN1'], (1, 1), 'SEG'],
            ['IN2', SEGMENTS['IN2'], (0, 1), 'SEG'],
            ['IN3', SEGMENTS['IN3'], (0, 1), 'SEG'],
        ),
    ),
    'ADT_A08_INSURANCE': (
        'sequence',
        (
            ['IN1', SEGMENTS['IN1'], (1, 1), 'SEG'],
            ['IN2', SEGMENTS['IN2'], (0, 1), 'SEG'],
            ['IN3', SEGMENTS['IN3'], (0, 1), 'SEG'],
        ),
    ),
    'ADT_A13_INSURANCE': (
        'sequence',
        (
            ['IN1', SEGMENTS['IN1'], (1, 1), 'SEG'],
            ['IN2', SEGMENTS['IN2'], (0, 1), 'SEG'],
            ['IN3', SEGMENTS['IN3'], (0, 1), 'SEG'],
        ),
    ),
    'ADT_A14_INSURANCE': (
        'sequence',
        (
            ['IN1', SEGMENTS['IN1'], (1, 1), 'SEG'],
            ['IN2', SEGMENTS['IN2'], (0, 1), 'SEG'],
            ['IN3', SEGMENTS['IN3'], (0, 1), 'SEG'],
        ),
    ),
    'ADT_A28_INSURANCE': (
        'sequence',
        (
            ['IN1', SEGMENTS['IN1'], (1, 1), 'SEG'],
            ['IN2', SEGMENTS['IN2'], (0, 1), 'SEG'],
            ['IN3', SEGMENTS['IN3'], (0, 1), 'SEG'],
        ),
    ),
    'ADT_A31_INSURANCE': (
        'sequence',
        (
            ['IN1', SEGMENTS['IN1'], (1, 1), 'SEG'],
            ['IN2', SEGMENTS['IN2'], (0, 1), 'SEG'],
            ['IN3', SEGMENTS['IN3'], (0, 1), 'SEG'],
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
    'BAR_P01_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (0, 1), 'SEG'],
            ['PV2', SEGMENTS['PV2'], (0, 1), 'SEG'],
            ['OBX', SEGMENTS['OBX'], (0, -1), 'SEG'],
            ['AL1', SEGMENTS['AL1'], (0, -1), 'SEG'],
            ['DG1', SEGMENTS['DG1'], (0, -1), 'SEG'],
            ['PR1', SEGMENTS['PR1'], (0, -1), 'SEG'],
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
            ['PV1', SEGMENTS['PV1'], (0, 1), 'SEG'],
        ),
    ),
    'MFN_M01_MF': ('sequence', (['MFE', SEGMENTS['MFE'], (1, 1), 'SEG'],)),
    'MFN_M02_MF_STAFF': ('sequence', (['MFE', SEGMENTS['MFE'], (1, 1), 'SEG'],)),
    'MFN_M03_MF_TEST': ('sequence', (['MFE', SEGMENTS['MFE'], (1, 1), 'SEG'],)),
    'MFR_M01_MF': ('sequence', (['MFE', SEGMENTS['MFE'], (1, 1), 'SEG'],)),
    'MFR_M02_MF_STAFF': ('sequence', (['MFE', SEGMENTS['MFE'], (1, 1), 'SEG'],)),
    'MFR_M03_MF_TEST': ('sequence', (['MFE', SEGMENTS['MFE'], (1, 1), 'SEG'],)),
    'NMD_N01_APP_STATS': (
        'sequence',
        (
            ['NST', SEGMENTS['NST'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'NMD_N01_APP_STATUS': (
        'sequence',
        (
            ['NSC', SEGMENTS['NSC'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'NMD_N01_CLOCK': (
        'sequence',
        (
            ['NCK', SEGMENTS['NCK'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'NMD_N01_CLOCK_AND_STATS_WITH_NOTES': (
        'sequence',
        (
            ['NMD_N01_CLOCK', None, (0, 1), 'GRP'],
            ['NMD_N01_APP_STATS', None, (0, 1), 'GRP'],
            ['NMD_N01_APP_STATUS', None, (0, 1), 'GRP'],
        ),
    ),
    'NMQ_N02_CLOCK_AND_STATISTICS': (
        'sequence',
        (
            ['NCK', SEGMENTS['NCK'], (0, 1), 'SEG'],
            ['NST', SEGMENTS['NST'], (0, 1), 'SEG'],
            ['NSC', SEGMENTS['NSC'], (0, 1), 'SEG'],
        ),
    ),
    'NMQ_N02_QRY_WITH_DETAIL': (
        'sequence',
        (
            ['QRD', SEGMENTS['QRD'], (1, 1), 'SEG'],
            ['QRF', SEGMENTS['QRF'], (0, 1), 'SEG'],
        ),
    ),
    'NMR_N02_CLOCK_AND_STATS_WITH_NOTES_ALT': (
        'sequence',
        (
            ['NCK', SEGMENTS['NCK'], (0, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['NST', SEGMENTS['NST'], (0, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['NSC', SEGMENTS['NSC'], (0, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
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
        ),
    ),
    'ORF_R04_QUERY_RESPONSE': (
        'sequence',
        (
            ['QRD', SEGMENTS['QRD'], (1, 1), 'SEG'],
            ['QRF', SEGMENTS['QRF'], (0, 1), 'SEG'],
            ['PID', SEGMENTS['PID'], (0, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
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
    'ORM_O01_ORDER': (
        'sequence',
        (
            ['ORC', SEGMENTS['ORC'], (1, 1), 'SEG'],
            ['ORM_O01_ORDER_DETAIL', None, (0, 1), 'GRP'],
            ['BLG', SEGMENTS['BLG'], (0, 1), 'SEG'],
        ),
    ),
    'ORM_O01_ORDER_DETAIL': (
        'sequence',
        (
            ['ORM_O01_CHOICE', None, (1, 1), 'GRP'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['OBX', SEGMENTS['OBX'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (1, -1), 'SEG'],
        ),
    ),
    'ORM_O01_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['PV1', SEGMENTS['PV1'], (0, 1), 'SEG'],
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
            ['ORR_O02_ORDER_DETAIL', None, (0, 1), 'GRP'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
        ),
    ),
    'ORR_O02_ORDER_DETAIL': ('sequence', (['ORR_O02_CHOICE', None, (1, 1), 'GRP'],)),
    'ORR_O02_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (0, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
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
        ),
    ),
    'ORU_R01_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['PV1', SEGMENTS['PV1'], (0, 1), 'SEG'],
        ),
    ),
    'ORU_R01_PATIENT_RESULT': (
        'sequence',
        (
            ['ORU_R01_PATIENT', None, (0, 1), 'GRP'],
            ['ORU_R01_ORDER_OBSERVATION', None, (1, -1), 'GRP'],
        ),
    ),
}
for k, v in iteritems(GROUPS):
    for item in v[1]:
        if item[3] == 'GRP':
            item[1] = GROUPS[item[0]]
