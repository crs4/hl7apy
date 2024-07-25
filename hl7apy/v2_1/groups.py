from hl7apy.utils import iteritems

from .segments import SEGMENTS

GROUPS = {
    'ADR_A19_QUERY_RESPONSE': (
        'sequence',
        (
            ['EVN', SEGMENTS['EVN'], (0, 1), 'SEG'],
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
        ),
    ),
    'ADT_A17_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PV1', SEGMENTS['PV1'], (1, 1), 'SEG'],
        ),
    ),
    'BAR_P01_VISIT': (
        'sequence',
        (
            ['PV1', SEGMENTS['PV1'], (0, 1), 'SEG'],
            ['DG1', SEGMENTS['DG1'], (0, -1), 'SEG'],
            ['PR1', SEGMENTS['PR1'], (0, -1), 'SEG'],
            ['GT1', SEGMENTS['GT1'], (0, -1), 'SEG'],
            ['NK1', SEGMENTS['NK1'], (0, -1), 'SEG'],
            ['IN1', SEGMENTS['IN1'], (0, -1), 'SEG'],
            ['ACC', SEGMENTS['ACC'], (0, 1), 'SEG'],
            ['UB1', SEGMENTS['UB1'], (0, 1), 'SEG'],
        ),
    ),
    'BAR_P02_PATIENT': (
        'sequence',
        (
            ['PID', SEGMENTS['PID'], (1, 1), 'SEG'],
            ['PV1', SEGMENTS['PV1'], (0, 1), 'SEG'],
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
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['ORO', SEGMENTS['ORO'], (1, 1), 'SEG'],
            ['RX1', SEGMENTS['RX1'], (1, 1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
            ['OBX', SEGMENTS['OBX'], (0, -1), 'SEG'],
            ['NTE', SEGMENTS['NTE'], (0, -1), 'SEG'],
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
    'ORR_O02_ORDER_DETAIL': (
        'sequence',
        (
            ['OBR', SEGMENTS['OBR'], (1, 1), 'SEG'],
            ['ORO', SEGMENTS['ORO'], (1, 1), 'SEG'],
            ['RX1', SEGMENTS['RX1'], (1, 1), 'SEG'],
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
    'ORU_R03_OBSERVATION': (
        'sequence',
        (
            ['OBX', None, (0, 1), 'SEG'],
            ['NTE', None, (0, -1), 'SEG'],
        ),
    ),
    'ORU_R03_ORDER_OBSERVATION': (
        'sequence',
        (
            ['ORC', None, (0, 1), 'SEG'],
            ['OBR', None, (1, 1), 'SEG'],
            ['NTE', None, (0, -1), 'SEG'],
            ['ORU_R03_OBSERVATION', None, (1, -1), 'GRP'],
        ),
    ),
    'ORU_R03_PATIENT': (
        'sequence',
        (
            ['PID', None, (1, 1), 'SEG'],
            ['NTE', None, (0, -1), 'SEG'],
            ['PV1', None, (0, 1), 'SEG'],
        ),
    ),
    'ORU_R03_PATIENT_RESULT': (
        'sequence',
        (
            ['ORU_R03_PATIENT', None, (0, 1), 'GRP'],
            ['ORU_R03_ORDER_OBSERVATION', None, (1, -1), 'GRP'],
        ),
    ),
}

for k, v in iteritems(GROUPS):
    for item in v[1]:
        if item[3] == 'GRP':
            item[1] = GROUPS[item[0]]
