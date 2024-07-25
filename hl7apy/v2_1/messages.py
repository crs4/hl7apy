from .groups import GROUPS
from .segments import SEGMENTS

MESSAGES = {
    'ACK': (
        'sequence',
        (
            ('MSH', SEGMENTS['MSH'], (1, 1), 'SEG'),
            ('MSA', SEGMENTS['MSA'], (1, 1), 'SEG'),
            ('ERR', SEGMENTS['ERR'], (0, 1), 'SEG'),
        ),
    ),
    'ADR_A19': (
        'sequence',
        (
            ('MSH', SEGMENTS['MSH'], (1, 1), 'SEG'),
            ('MSA', SEGMENTS['MSA'], (1, 1), 'SEG'),
            ('QRD', SEGMENTS['QRD'], (1, 1), 'SEG'),
            (
                'ADR_A19_QUERY_RESPONSE',
                GROUPS['ADR_A19_QUERY_RESPONSE'],
                (1, -1),
                'GRP',
            ),
            ('DSC', SEGMENTS['DSC'], (0, 1), 'SEG'),
        ),
    ),
    'ADT_A01': (
        'sequence',
        (
            ('MSH', SEGMENTS['MSH'], (1, 1), 'SEG'),
            ('EVN', SEGMENTS['EVN'], (1, 1), 'SEG'),
            ('PID', SEGMENTS['PID'], (1, 1), 'SEG'),
            ('NK1', SEGMENTS['NK1'], (1, 1), 'SEG'),
            ('PV1', SEGMENTS['PV1'], (1, 1), 'SEG'),
            ('DG1', SEGMENTS['DG1'], (0, 1), 'SEG'),
        ),
    ),
    'ADT_A02': (
        'sequence',
        (
            ('MSH', SEGMENTS['MSH'], (1, 1), 'SEG'),
            ('EVN', SEGMENTS['EVN'], (1, 1), 'SEG'),
            ('PID', SEGMENTS['PID'], (1, 1), 'SEG'),
            ('PV1', SEGMENTS['PV1'], (1, 1), 'SEG'),
        ),
    ),
    'ADT_A03': (
        'sequence',
        (
            ('MSH', SEGMENTS['MSH'], (1, 1), 'SEG'),
            ('EVN', SEGMENTS['EVN'], (1, 1), 'SEG'),
            ('PID', SEGMENTS['PID'], (1, 1), 'SEG'),
        ),
    ),
    'ADT_A04': (
        'sequence',
        (
            ('MSH', SEGMENTS['MSH'], (1, 1), 'SEG'),
            ('EVN', SEGMENTS['EVN'], (1, 1), 'SEG'),
            ('PID', SEGMENTS['PID'], (1, 1), 'SEG'),
            ('NK1', SEGMENTS['NK1'], (1, 1), 'SEG'),
            ('PV1', SEGMENTS['PV1'], (1, 1), 'SEG'),
            ('DG1', SEGMENTS['DG1'], (0, 1), 'SEG'),
        ),
    ),
    'ADT_A05': (
        'sequence',
        (
            ('MSH', SEGMENTS['MSH'], (1, 1), 'SEG'),
            ('EVN', SEGMENTS['EVN'], (1, 1), 'SEG'),
            ('PID', SEGMENTS['PID'], (1, 1), 'SEG'),
            ('NK1', SEGMENTS['NK1'], (1, 1), 'SEG'),
            ('PV1', SEGMENTS['PV1'], (1, 1), 'SEG'),
            ('DG1', SEGMENTS['DG1'], (0, 1), 'SEG'),
        ),
    ),
    'ADT_A06': (
        'sequence',
        (
            ('MSH', SEGMENTS['MSH'], (1, 1), 'SEG'),
            ('EVN', SEGMENTS['EVN'], (1, 1), 'SEG'),
            ('PID', SEGMENTS['PID'], (1, 1), 'SEG'),
            ('PV1', SEGMENTS['PV1'], (1, 1), 'SEG'),
        ),
    ),
    'ADT_A07': (
        'sequence',
        (
            ('MSH', SEGMENTS['MSH'], (1, 1), 'SEG'),
            ('EVN', SEGMENTS['EVN'], (1, 1), 'SEG'),
            ('PID', SEGMENTS['PID'], (1, 1), 'SEG'),
            ('PV1', SEGMENTS['PV1'], (1, 1), 'SEG'),
        ),
    ),
    'ADT_A08': (
        'sequence',
        (
            ('MSH', SEGMENTS['MSH'], (1, 1), 'SEG'),
            ('EVN', SEGMENTS['EVN'], (1, 1), 'SEG'),
            ('PID', SEGMENTS['PID'], (1, 1), 'SEG'),
            ('NK1', SEGMENTS['NK1'], (1, 1), 'SEG'),
            ('PV1', SEGMENTS['PV1'], (1, 1), 'SEG'),
            ('DG1', SEGMENTS['DG1'], (0, 1), 'SEG'),
        ),
    ),
    'ADT_A09': (
        'sequence',
        (
            ('MSH', SEGMENTS['MSH'], (1, 1), 'SEG'),
            ('EVN', SEGMENTS['EVN'], (1, 1), 'SEG'),
            ('PID', SEGMENTS['PID'], (1, 1), 'SEG'),
            ('PV1', SEGMENTS['PV1'], (1, 1), 'SEG'),
            ('DG1', SEGMENTS['DG1'], (0, 1), 'SEG'),
        ),
    ),
    'ADT_A10': (
        'sequence',
        (
            ('MSH', SEGMENTS['MSH'], (1, 1), 'SEG'),
            ('EVN', SEGMENTS['EVN'], (1, 1), 'SEG'),
            ('PID', SEGMENTS['PID'], (1, 1), 'SEG'),
            ('PV1', SEGMENTS['PV1'], (1, 1), 'SEG'),
            ('DG1', SEGMENTS['DG1'], (0, 1), 'SEG'),
        ),
    ),
    'ADT_A11': (
        'sequence',
        (
            ('MSH', SEGMENTS['MSH'], (1, 1), 'SEG'),
            ('EVN', SEGMENTS['EVN'], (1, 1), 'SEG'),
            ('PID', SEGMENTS['PID'], (1, 1), 'SEG'),
            ('PV1', SEGMENTS['PV1'], (1, 1), 'SEG'),
            ('DG1', SEGMENTS['DG1'], (0, 1), 'SEG'),
        ),
    ),
    'ADT_A12': (
        'sequence',
        (
            ('MSH', SEGMENTS['MSH'], (1, 1), 'SEG'),
            ('EVN', SEGMENTS['EVN'], (1, 1), 'SEG'),
            ('PID', SEGMENTS['PID'], (1, 1), 'SEG'),
            ('PV1', SEGMENTS['PV1'], (1, 1), 'SEG'),
            ('DG1', SEGMENTS['DG1'], (0, 1), 'SEG'),
        ),
    ),
    'ADT_A13': (
        'sequence',
        (
            ('MSH', SEGMENTS['MSH'], (1, 1), 'SEG'),
            ('EVN', SEGMENTS['EVN'], (1, 1), 'SEG'),
            ('PID', SEGMENTS['PID'], (1, 1), 'SEG'),
            ('PV1', SEGMENTS['PV1'], (1, 1), 'SEG'),
            ('DG1', SEGMENTS['DG1'], (0, 1), 'SEG'),
        ),
    ),
    'ADT_A14': (
        'sequence',
        (
            ('MSH', SEGMENTS['MSH'], (1, 1), 'SEG'),
            ('EVN', SEGMENTS['EVN'], (1, 1), 'SEG'),
            ('PID', SEGMENTS['PID'], (1, 1), 'SEG'),
            ('PD1', SEGMENTS['PD1'], (1, 1), 'SEG'),
            ('NK1', SEGMENTS['NK1'], (1, 1), 'SEG'),
            ('PV1', SEGMENTS['PV1'], (1, 1), 'SEG'),
            ('DG1', SEGMENTS['DG1'], (0, 1), 'SEG'),
        ),
    ),
    'ADT_A15': (
        'sequence',
        (
            ('MSH', SEGMENTS['MSH'], (1, 1), 'SEG'),
            ('EVN', SEGMENTS['EVN'], (1, 1), 'SEG'),
            ('PID', SEGMENTS['PID'], (1, 1), 'SEG'),
            ('PV1', SEGMENTS['PV1'], (1, 1), 'SEG'),
            ('DG1', SEGMENTS['DG1'], (0, 1), 'SEG'),
        ),
    ),
    'ADT_A16': (
        'sequence',
        (
            ('MSH', SEGMENTS['MSH'], (1, 1), 'SEG'),
            ('EVN', SEGMENTS['EVN'], (1, 1), 'SEG'),
            ('PID', SEGMENTS['PID'], (1, 1), 'SEG'),
            ('PV1', SEGMENTS['PV1'], (1, 1), 'SEG'),
            ('DG1', SEGMENTS['DG1'], (0, 1), 'SEG'),
        ),
    ),
    'ADT_A17': (
        'sequence',
        (
            ('MSH', SEGMENTS['MSH'], (1, 1), 'SEG'),
            ('EVN', SEGMENTS['EVN'], (1, 1), 'SEG'),
            ('ADT_A17_PATIENT', GROUPS['ADT_A17_PATIENT'], (1, -1), 'GRP'),
        ),
    ),
    'ADT_A18': (
        'sequence',
        (
            ('MSH', SEGMENTS['MSH'], (1, 1), 'SEG'),
            ('EVN', SEGMENTS['EVN'], (1, 1), 'SEG'),
            ('PID', SEGMENTS['PID'], (1, 1), 'SEG'),
            ('MRG', SEGMENTS['MRG'], (1, 1), 'SEG'),
            ('PV1', SEGMENTS['PV1'], (0, 1), 'SEG'),
        ),
    ),
    'ADT_A20': (
        'sequence',
        (
            ('MSH', SEGMENTS['MSH'], (1, 1), 'SEG'),
            ('EVN', SEGMENTS['EVN'], (1, 1), 'SEG'),
            ('NPU', SEGMENTS['NPU'], (1, 1), 'SEG'),
        ),
    ),
    'ADT_A21': (
        'sequence',
        (
            ('MSH', SEGMENTS['MSH'], (1, 1), 'SEG'),
            ('EVN', SEGMENTS['EVN'], (1, 1), 'SEG'),
            ('PID', SEGMENTS['PID'], (1, 1), 'SEG'),
            ('PV1', SEGMENTS['PV1'], (1, 1), 'SEG'),
        ),
    ),
    'ADT_A22': (
        'sequence',
        (
            ('MSH', SEGMENTS['MSH'], (1, 1), 'SEG'),
            ('EVN', SEGMENTS['EVN'], (1, 1), 'SEG'),
            ('PID', SEGMENTS['PID'], (1, 1), 'SEG'),
            ('PV1', SEGMENTS['PV1'], (1, 1), 'SEG'),
        ),
    ),
    'ADT_A23': (
        'sequence',
        (
            ('MSH', SEGMENTS['MSH'], (1, 1), 'SEG'),
            ('EVN', SEGMENTS['EVN'], (1, 1), 'SEG'),
            ('PID', SEGMENTS['PID'], (1, 1), 'SEG'),
            ('PV1', SEGMENTS['PV1'], (1, 1), 'SEG'),
        ),
    ),
    'ADT_A24': (
        'sequence',
        (
            ('MSH', SEGMENTS['MSH'], (1, 1), 'SEG'),
            ('EVN', SEGMENTS['EVN'], (1, 1), 'SEG'),
            ('PID', SEGMENTS['PID'], (1, 1), 'SEG'),
            ('PV1', SEGMENTS['PV1'], (1, 1), 'SEG'),
            ('PID', SEGMENTS['PID'], (1, 1), 'SEG'),
        ),
    ),
    'BAR_P01': (
        'sequence',
        (
            ('MSH', SEGMENTS['MSH'], (1, 1), 'SEG'),
            ('EVN', SEGMENTS['EVN'], (1, 1), 'SEG'),
            ('PID', SEGMENTS['PID'], (1, 1), 'SEG'),
            ('BAR_P01_VISIT', GROUPS['BAR_P01_VISIT'], (1, -1), 'GRP'),
        ),
    ),
    'BAR_P02': (
        'sequence',
        (
            ('MSH', SEGMENTS['MSH'], (1, 1), 'SEG'),
            ('EVN', SEGMENTS['EVN'], (1, 1), 'SEG'),
            ('BAR_P02_PATIENT', GROUPS['BAR_P02_PATIENT'], (1, -1), 'GRP'),
        ),
    ),
    'DFT_P03': (
        'sequence',
        (
            ('MSH', SEGMENTS['MSH'], (1, 1), 'SEG'),
            ('EVN', SEGMENTS['EVN'], (1, 1), 'SEG'),
            ('PID', SEGMENTS['PID'], (1, 1), 'SEG'),
            ('PV1', SEGMENTS['PV1'], (0, 1), 'SEG'),
            ('FT1', SEGMENTS['FT1'], (0, -1), 'SEG'),
        ),
    ),
    'DSR_Q01': (
        'sequence',
        (
            ('MSH', SEGMENTS['MSH'], (1, 1), 'SEG'),
            ('MSA', SEGMENTS['MSA'], (1, 1), 'SEG'),
            ('QRD', SEGMENTS['QRD'], (1, 1), 'SEG'),
            ('QRF', SEGMENTS['QRF'], (0, 1), 'SEG'),
            ('DSP', SEGMENTS['DSP'], (1, -1), 'SEG'),
            ('DSC', SEGMENTS['DSC'], (1, 1), 'SEG'),
        ),
    ),
    'DSR_Q03': (
        'sequence',
        (
            ('MSH', SEGMENTS['MSH'], (1, 1), 'SEG'),
            ('QRD', SEGMENTS['QRD'], (1, 1), 'SEG'),
            ('QRF', SEGMENTS['QRF'], (0, 1), 'SEG'),
            ('DSP', SEGMENTS['DSP'], (1, -1), 'SEG'),
            ('DSC', SEGMENTS['DSC'], (0, 1), 'SEG'),
        ),
    ),
    'MCF_Q02': (
        'sequence',
        (
            ('MSH', SEGMENTS['MSH'], (1, 1), 'SEG'),
            ('MSA', SEGMENTS['MSA'], (1, 1), 'SEG'),
        ),
    ),
    'ORM_O01': (
        'sequence',
        (
            ('MSH', SEGMENTS['MSH'], (1, 1), 'SEG'),
            ('NTE', SEGMENTS['NTE'], (0, -1), 'SEG'),
            ('ORM_O01_PATIENT', GROUPS['ORM_O01_PATIENT'], (0, 1), 'GRP'),
            ('ORM_O01_ORDER', GROUPS['ORM_O01_ORDER'], (1, -1), 'GRP'),
        ),
    ),
    'ORR_O02': (
        'sequence',
        (
            ('MSH', SEGMENTS['MSH'], (1, 1), 'SEG'),
            ('MSA', SEGMENTS['MSA'], (1, 1), 'SEG'),
            ('NTE', SEGMENTS['NTE'], (0, -1), 'SEG'),
            ('ORR_O02_PATIENT', GROUPS['ORR_O02_PATIENT'], (0, 1), 'GRP'),
        ),
    ),
    'ORU_R01': (
        'sequence',
        (
            ('MSH', SEGMENTS['MSH'], (1, 1), 'SEG'),
            (
                'ORU_R01_PATIENT_RESULT',
                GROUPS['ORU_R01_PATIENT_RESULT'],
                (1, -1),
                'GRP',
            ),
            ('DSC', SEGMENTS['DSC'], (0, 1), 'SEG'),
        ),
    ),
    'ORU_R03': (
        'sequence',
        (
            ('MSH', SEGMENTS['MSH'], (1, 1), 'SEG'),
            (
                'ORU_R03_PATIENT_RESULT',
                GROUPS['ORU_R03_PATIENT_RESULT'],
                (1, -1),
                'GRP',
            ),
            ('DSC', SEGMENTS['DSC'], (0, 1), 'SEG'),
        ),
    ),
    'QRY_A19': (
        'sequence',
        (
            ('MSH', SEGMENTS['MSH'], (1, 1), 'SEG'),
            ('QRD', SEGMENTS['QRD'], (1, 1), 'SEG'),
        ),
    ),
    'QRY_Q01': (
        'sequence',
        (
            ('MSH', SEGMENTS['MSH'], (1, 1), 'SEG'),
            ('QRD', SEGMENTS['QRD'], (1, 1), 'SEG'),
            ('QRF', SEGMENTS['QRF'], (0, 1), 'SEG'),
            ('DSC', SEGMENTS['DSC'], (1, 1), 'SEG'),
        ),
    ),
    'QRY_Q02': (
        'sequence',
        (
            ('MSH', SEGMENTS['MSH'], (1, 1), 'SEG'),
            ('QRD', SEGMENTS['QRD'], (1, 1), 'SEG'),
            ('QRF', SEGMENTS['QRF'], (0, 1), 'SEG'),
            ('DSC', SEGMENTS['DSC'], (1, 1), 'SEG'),
        ),
    ),
    'UDM_Q05': (
        'sequence',
        (
            ('MSH', SEGMENTS['MSH'], (1, 1), 'SEG'),
            ('URD', SEGMENTS['URD'], (1, 1), 'SEG'),
            ('URS', SEGMENTS['URS'], (0, 1), 'SEG'),
            ('DSP', SEGMENTS['DSP'], (1, -1), 'SEG'),
            ('DSC', SEGMENTS['DSC'], (1, 1), 'SEG'),
        ),
    ),
}
