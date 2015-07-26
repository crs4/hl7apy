# -*- coding: utf-8 -*-
#
# Copyright (c) 2012-2015, CRS4
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

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
from builtins import *
SEGMENTS = {'ACC': ('sequence',
                    (('ACC_1', (0, 1)), ('ACC_2', (0, 1)), ('ACC_3', (0, 1)))),
            'ADD': ('sequence', (('ADD_1', (0, 1)),)),
            'AL1': ('sequence',
                    (('AL1_1', (1, 1)),
                     ('AL1_2', (0, 1)),
                     ('AL1_3', (1, 1)),
                     ('AL1_4', (0, 1)),
                     ('AL1_5', (0, 1)),
                     ('AL1_6', (0, 1)))),
            'ANYHL7SEGMENT': ('choice',
                              (('ACC', (0, -1)),
                               ('ADD', (0, -1)),
                               ('AL1', (0, -1)),
                               ('BHS', (0, -1)),
                               ('BLG', (0, -1)),
                               ('BTS', (0, -1)),
                               ('DG1', (0, -1)),
                               ('DSC', (0, -1)),
                               ('DSP', (0, -1)),
                               ('ERR', (0, -1)),
                               ('EVN', (0, -1)),
                               ('FHS', (0, -1)),
                               ('FT1', (0, -1)),
                               ('FTS', (0, -1)),
                               ('GT1', (0, -1)),
                               ('IN1', (0, -1)),
                               ('IN2', (0, -1)),
                               ('IN3', (0, -1)),
                               ('MFA', (0, -1)),
                               ('MFE', (0, -1)),
                               ('MFI', (0, -1)),
                               ('MRG', (0, -1)),
                               ('MSA', (0, -1)),
                               ('MSH', (0, -1)),
                               ('NCK', (0, -1)),
                               ('NK1', (0, -1)),
                               ('NPU', (0, -1)),
                               ('NSC', (0, -1)),
                               ('NST', (0, -1)),
                               ('NTE', (0, -1)),
                               ('OBR', (0, -1)),
                               ('OBX', (0, -1)),
                               ('ODS', (0, -1)),
                               ('ODT', (0, -1)),
                               ('OM1', (0, -1)),
                               ('OM2', (0, -1)),
                               ('OM3', (0, -1)),
                               ('OM4', (0, -1)),
                               ('OM5', (0, -1)),
                               ('OM6', (0, -1)),
                               ('ORC', (0, -1)),
                               ('PID', (0, -1)),
                               ('PR1', (0, -1)),
                               ('PRA', (0, -1)),
                               ('PV1', (0, -1)),
                               ('PV2', (0, -1)),
                               ('QRD', (0, -1)),
                               ('QRF', (0, -1)),
                               ('RQ1', (0, -1)),
                               ('RQD', (0, -1)),
                               ('RXA', (0, -1)),
                               ('RXC', (0, -1)),
                               ('RXD', (0, -1)),
                               ('RXE', (0, -1)),
                               ('RXG', (0, -1)),
                               ('RXO', (0, -1)),
                               ('RXR', (0, -1)),
                               ('STF', (0, -1)),
                               ('UB1', (0, -1)),
                               ('UB2', (0, -1)),
                               ('URD', (0, -1)),
                               ('URS', (0, -1)))),
            'BHS': ('sequence',
                    (('BHS_1', (1, 1)),
                     ('BHS_2', (1, 1)),
                     ('BHS_3', (0, 1)),
                     ('BHS_4', (0, 1)),
                     ('BHS_5', (0, 1)),
                     ('BHS_6', (0, 1)),
                     ('BHS_7', (0, 1)),
                     ('BHS_8', (0, 1)),
                     ('BHS_9', (0, 1)),
                     ('BHS_10', (0, 1)),
                     ('BHS_11', (0, 1)),
                     ('BHS_12', (0, 1)))),
            'BLG': ('sequence',
                    (('BLG_1', (0, 1)), ('BLG_2', (0, 1)), ('BLG_3', (0, 1)))),
            'BTS': ('sequence',
                    (('BTS_1', (0, 1)), ('BTS_2', (0, 1)), ('BTS_3', (0, -1)))),
            'DG1': ('sequence',
                    (('DG1_1', (1, 1)),
                     ('DG1_2', (1, 1)),
                     ('DG1_3', (0, 1)),
                     ('DG1_4', (0, 1)),
                     ('DG1_5', (0, 1)),
                     ('DG1_6', (1, 1)),
                     ('DG1_7', (0, 1)),
                     ('DG1_8', (0, 1)),
                     ('DG1_9', (0, 1)),
                     ('DG1_10', (0, 1)),
                     ('DG1_11', (0, 1)),
                     ('DG1_12', (0, 1)),
                     ('DG1_13', (0, 1)),
                     ('DG1_14', (0, 1)),
                     ('DG1_15', (0, 1)),
                     ('DG1_16', (0, 1)))),
            'DSC': ('sequence', (('DSC_1', (0, 1)),)),
            'DSP': ('sequence',
                    (('DSP_1', (0, 1)),
                     ('DSP_2', (0, 1)),
                     ('DSP_3', (1, 1)),
                     ('DSP_4', (0, 1)),
                     ('DSP_5', (0, 1)))),
            'ERR': ('sequence', (('ERR_1', (1, -1)),)),
            'EVN': ('sequence',
                    (('EVN_1', (1, 1)),
                     ('EVN_2', (1, 1)),
                     ('EVN_3', (0, 1)),
                     ('EVN_4', (0, 1)),
                     ('EVN_5', (0, 1)))),
            'FHS': ('sequence',
                    (('FHS_1', (1, 1)),
                     ('FHS_2', (1, 1)),
                     ('FHS_3', (0, 1)),
                     ('FHS_4', (0, 1)),
                     ('FHS_5', (0, 1)),
                     ('FHS_6', (0, 1)),
                     ('FHS_7', (0, 1)),
                     ('FHS_8', (0, 1)),
                     ('FHS_9', (0, 1)),
                     ('FHS_10', (0, 1)),
                     ('FHS_11', (0, 1)),
                     ('FHS_12', (0, 1)))),
            'FT1': ('sequence',
                    (('FT1_1', (0, 1)),
                     ('FT1_2', (0, 1)),
                     ('FT1_3', (0, 1)),
                     ('FT1_4', (1, 1)),
                     ('FT1_5', (0, 1)),
                     ('FT1_6', (1, 1)),
                     ('FT1_7', (1, 1)),
                     ('FT1_8', (0, 1)),
                     ('FT1_9', (0, 1)),
                     ('FT1_10', (0, 1)),
                     ('FT1_11', (0, 1)),
                     ('FT1_12', (0, 1)),
                     ('FT1_13', (0, 1)),
                     ('FT1_14', (1, 1)),
                     ('FT1_15', (0, 1)),
                     ('FT1_16', (0, 1)),
                     ('FT1_17', (0, 1)),
                     ('FT1_18', (0, 1)),
                     ('FT1_19', (0, -1)),
                     ('FT1_20', (0, 1)),
                     ('FT1_21', (0, 1)),
                     ('FT1_22', (0, 1)),
                     ('FT1_23', (0, 1)))),
            'FTS': ('sequence', (('FTS_1', (0, 1)), ('FTS_2', (0, 1)))),
            'GT1': ('sequence',
                    (('GT1_1', (1, 1)),
                     ('GT1_2', (0, 1)),
                     ('GT1_3', (1, 1)),
                     ('GT1_4', (0, 1)),
                     ('GT1_5', (0, 1)),
                     ('GT1_6', (0, -1)),
                     ('GT1_7', (0, -1)),
                     ('GT1_8', (0, 1)),
                     ('GT1_9', (0, 1)),
                     ('GT1_10', (0, 1)),
                     ('GT1_11', (0, 1)),
                     ('GT1_12', (0, 1)),
                     ('GT1_13', (0, 1)),
                     ('GT1_14', (0, 1)),
                     ('GT1_15', (0, 1)),
                     ('GT1_16', (0, 1)),
                     ('GT1_17', (0, 1)),
                     ('GT1_18', (0, -1)),
                     ('GT1_19', (0, 1)),
                     ('GT1_20', (0, 1)),
                     ('GT1_21', (0, 1)))),
            'IN1': ('sequence',
                    (('IN1_1', (1, 1)),
                     ('IN1_2', (1, 1)),
                     ('IN1_3', (1, 1)),
                     ('IN1_4', (0, 1)),
                     ('IN1_5', (0, 1)),
                     ('IN1_6', (0, 1)),
                     ('IN1_7', (0, -1)),
                     ('IN1_8', (0, 1)),
                     ('IN1_9', (0, 1)),
                     ('IN1_10', (0, 1)),
                     ('IN1_11', (0, 1)),
                     ('IN1_12', (0, 1)),
                     ('IN1_13', (0, 1)),
                     ('IN1_14', (0, 1)),
                     ('IN1_15', (0, 1)),
                     ('IN1_16', (0, 1)),
                     ('IN1_17', (0, 1)),
                     ('IN1_18', (0, 1)),
                     ('IN1_19', (0, 1)),
                     ('IN1_20', (0, 1)),
                     ('IN1_21', (0, 1)),
                     ('IN1_22', (0, 1)),
                     ('IN1_23', (0, 1)),
                     ('IN1_24', (0, 1)),
                     ('IN1_25', (0, 1)),
                     ('IN1_26', (0, 1)),
                     ('IN1_27', (0, 1)),
                     ('IN1_28', (0, 1)),
                     ('IN1_29', (0, 1)),
                     ('IN1_30', (0, 1)),
                     ('IN1_31', (0, 1)),
                     ('IN1_32', (0, 1)),
                     ('IN1_33', (0, 1)),
                     ('IN1_34', (0, 1)),
                     ('IN1_35', (0, 1)),
                     ('IN1_36', (0, 1)),
                     ('IN1_37', (0, 1)),
                     ('IN1_38', (0, 1)),
                     ('IN1_39', (0, 1)),
                     ('IN1_40', (0, 1)),
                     ('IN1_41', (0, 1)),
                     ('IN1_42', (0, 1)),
                     ('IN1_43', (0, 1)),
                     ('IN1_44', (0, 1)),
                     ('IN1_45', (0, 1)),
                     ('IN1_46', (0, 1)))),
            'IN2': ('sequence',
                    (('IN2_1', (0, 1)),
                     ('IN2_2', (0, 1)),
                     ('IN2_3', (0, 1)),
                     ('IN2_4', (0, 1)),
                     ('IN2_5', (0, 1)),
                     ('IN2_6', (0, 1)),
                     ('IN2_7', (0, 1)),
                     ('IN2_8', (0, 1)),
                     ('IN2_9', (0, 1)),
                     ('IN2_10', (0, 1)),
                     ('IN2_11', (0, 1)),
                     ('IN2_12', (0, 1)),
                     ('IN2_13', (0, 1)),
                     ('IN2_14', (0, 1)),
                     ('IN2_15', (0, 1)),
                     ('IN2_16', (0, 1)),
                     ('IN2_17', (0, 1)),
                     ('IN2_18', (0, 1)),
                     ('IN2_19', (0, 1)),
                     ('IN2_20', (0, 1)),
                     ('IN2_21', (0, 1)),
                     ('IN2_22', (0, 1)),
                     ('IN2_23', (0, 1)),
                     ('IN2_24', (0, -1)),
                     ('IN2_25', (0, 1)),
                     ('IN2_26', (0, 1)),
                     ('IN2_27', (0, 1)),
                     ('IN2_28', (0, -1)),
                     ('IN2_29', (0, -1)),
                     ('IN2_30', (0, 1)))),
            'IN3': ('sequence',
                    (('IN3_1', (1, 1)),
                     ('IN3_2', (0, 1)),
                     ('IN3_3', (0, 1)),
                     ('IN3_4', (0, 1)),
                     ('IN3_5', (0, 1)),
                     ('IN3_6', (0, 1)),
                     ('IN3_7', (0, 1)),
                     ('IN3_8', (0, 1)),
                     ('IN3_9', (0, 1)),
                     ('IN3_10', (0, 1)),
                     ('IN3_11', (0, 1)),
                     ('IN3_12', (0, 1)),
                     ('IN3_13', (0, 1)),
                     ('IN3_14', (0, 1)),
                     ('IN3_15', (0, 1)),
                     ('IN3_16', (0, -1)),
                     ('IN3_17', (0, 1)),
                     ('IN3_18', (0, 1)),
                     ('IN3_19', (0, -1)),
                     ('IN3_20', (0, -1)),
                     ('IN3_21', (0, 1)),
                     ('IN3_22', (0, 1)),
                     ('IN3_23', (0, 1)),
                     ('IN3_24', (0, 1)),
                     ('IN3_25', (0, 1)))),
            'MFA': ('sequence',
                    (('MFA_1', (1, 1)),
                     ('MFA_2', (0, 1)),
                     ('MFA_3', (0, 1)),
                     ('MFA_4', (1, 1)),
                     ('MFA_5', (1, -1)))),
            'MFE': ('sequence',
                    (('MFE_1', (1, 1)),
                     ('MFE_2', (0, 1)),
                     ('MFE_3', (0, 1)),
                     ('MFE_4', (1, -1)))),
            'MFI': ('sequence',
                    (('MFI_1', (1, 1)),
                     ('MFI_2', (0, 1)),
                     ('MFI_3', (1, 1)),
                     ('MFI_4', (0, 1)),
                     ('MFI_5', (0, 1)),
                     ('MFI_6', (1, 1)))),
            'MRG': ('sequence',
                    (('MRG_1', (1, 1)),
                     ('MRG_2', (0, 1)),
                     ('MRG_3', (0, 1)),
                     ('MRG_4', (0, 1)))),
            'MSA': ('sequence',
                    (('MSA_1', (1, 1)),
                     ('MSA_2', (1, 1)),
                     ('MSA_3', (0, 1)),
                     ('MSA_4', (0, 1)),
                     ('MSA_5', (0, 1)),
                     ('MSA_6', (0, 1)))),
            'MSH': ('sequence',
                    (('MSH_1', (1, 1)),
                     ('MSH_2', (1, 1)),
                     ('MSH_3', (0, 1)),
                     ('MSH_4', (0, 1)),
                     ('MSH_5', (0, 1)),
                     ('MSH_6', (0, 1)),
                     ('MSH_7', (0, 1)),
                     ('MSH_8', (0, 1)),
                     ('MSH_9', (1, 1)),
                     ('MSH_10', (1, 1)),
                     ('MSH_11', (1, 1)),
                     ('MSH_12', (1, 1)),
                     ('MSH_13', (0, 1)),
                     ('MSH_14', (0, 1)),
                     ('MSH_15', (0, 1)),
                     ('MSH_16', (0, 1)),
                     ('MSH_17', (0, 1)))),
            'NCK': ('sequence', (('NCK_1', (1, 1)),)),
            'NK1': ('sequence',
                    (('NK1_1', (1, 1)),
                     ('NK1_2', (0, 1)),
                     ('NK1_3', (0, 1)),
                     ('NK1_4', (0, 1)),
                     ('NK1_5', (0, -1)),
                     ('NK1_6', (0, 1)),
                     ('NK1_7', (0, 1)),
                     ('NK1_8', (0, 1)),
                     ('NK1_9', (0, 1)),
                     ('NK1_10', (0, 1)),
                     ('NK1_11', (0, 1)),
                     ('NK1_12', (0, 1)),
                     ('NK1_13', (0, 1)))),
            'NPU': ('sequence', (('NPU_1', (1, 1)), ('NPU_2', (0, 1)))),
            'NSC': ('sequence',
                    (('NSC_1', (1, 1)),
                     ('NSC_2', (0, 1)),
                     ('NSC_3', (0, 1)),
                     ('NSC_4', (0, 1)),
                     ('NSC_5', (0, 1)),
                     ('NSC_6', (0, 1)),
                     ('NSC_7', (0, 1)),
                     ('NSC_8', (0, 1)),
                     ('NSC_9', (0, 1)))),
            'NST': ('sequence',
                    (('NST_1', (1, 1)),
                     ('NST_2', (0, 1)),
                     ('NST_3', (0, 1)),
                     ('NST_4', (0, 1)),
                     ('NST_5', (0, 1)),
                     ('NST_6', (0, 1)),
                     ('NST_7', (0, 1)),
                     ('NST_8', (0, 1)),
                     ('NST_9', (0, 1)),
                     ('NST_10', (0, 1)),
                     ('NST_11', (0, 1)),
                     ('NST_12', (0, 1)),
                     ('NST_13', (0, 1)),
                     ('NST_14', (0, 1)),
                     ('NST_15', (0, 1)))),
            'NTE': ('sequence',
                    (('NTE_1', (0, 1)), ('NTE_2', (0, 1)), ('NTE_3', (0, -1)))),
            'OBR': ('sequence',
                    (('OBR_1', (0, 1)),
                     ('OBR_2', (0, 1)),
                     ('OBR_3', (0, 1)),
                     ('OBR_4', (1, 1)),
                     ('OBR_5', (0, 1)),
                     ('OBR_6', (0, 1)),
                     ('OBR_7', (0, 1)),
                     ('OBR_8', (0, 1)),
                     ('OBR_9', (0, 1)),
                     ('OBR_10', (0, -1)),
                     ('OBR_11', (0, 1)),
                     ('OBR_12', (0, 1)),
                     ('OBR_13', (0, 1)),
                     ('OBR_14', (0, 1)),
                     ('OBR_15', (0, 1)),
                     ('OBR_16', (0, 1)),
                     ('OBR_17', (0, -1)),
                     ('OBR_18', (0, 1)),
                     ('OBR_19', (0, 1)),
                     ('OBR_20', (0, 1)),
                     ('OBR_21', (0, 1)),
                     ('OBR_22', (0, 1)),
                     ('OBR_23', (0, 1)),
                     ('OBR_24', (0, 1)),
                     ('OBR_25', (0, 1)),
                     ('OBR_26', (0, 1)),
                     ('OBR_27', (0, -1)),
                     ('OBR_28', (0, -1)),
                     ('OBR_29', (0, 1)),
                     ('OBR_30', (0, 1)),
                     ('OBR_31', (0, -1)),
                     ('OBR_32', (0, 1)),
                     ('OBR_33', (0, -1)),
                     ('OBR_34', (0, -1)),
                     ('OBR_35', (0, -1)),
                     ('OBR_36', (0, 1)))),
            'OBX': ('sequence',
                    (('OBX_1', (0, 1)),
                     ('OBX_2', (1, 1)),
                     ('OBX_3', (1, 1)),
                     ('OBX_4', (0, 1)),
                     ('OBX_5', (0, 1)),
                     ('OBX_6', (0, 1)),
                     ('OBX_7', (0, 1)),
                     ('OBX_8', (0, -1)),
                     ('OBX_9', (0, 1)),
                     ('OBX_10', (0, 1)),
                     ('OBX_11', (1, 1)),
                     ('OBX_12', (0, 1)),
                     ('OBX_13', (0, 1)),
                     ('OBX_14', (0, 1)),
                     ('OBX_15', (0, 1)),
                     ('OBX_16', (0, 1)))),
            'ODS': ('sequence',
                    (('ODS_1', (1, 1)),
                     ('ODS_2', (0, -1)),
                     ('ODS_3', (1, -1)),
                     ('ODS_4', (0, -1)))),
            'ODT': ('sequence',
                    (('ODT_1', (1, 1)), ('ODT_2', (0, -1)), ('ODT_3', (0, -1)))),
            'OM1': ('sequence',
                    (('OM1_1', (0, 1)),
                     ('OM1_2', (0, 1)),
                     ('OM1_3', (1, 1)),
                     ('OM1_4', (0, -1)),
                     ('OM1_5', (1, 1)),
                     ('OM1_6', (1, 1)),
                     ('OM1_7', (0, 1)),
                     ('OM1_8', (0, 1)),
                     ('OM1_9', (1, -1)),
                     ('OM1_10', (0, 1)),
                     ('OM1_11', (0, 1)),
                     ('OM1_12', (0, 1)),
                     ('OM1_13', (0, 1)),
                     ('OM1_14', (0, -1)),
                     ('OM1_15', (0, -1)),
                     ('OM1_16', (0, 1)),
                     ('OM1_17', (0, -1)),
                     ('OM1_18', (0, 1)),
                     ('OM1_19', (1, 1)),
                     ('OM1_20', (0, 1)),
                     ('OM1_21', (0, 1)),
                     ('OM1_22', (1, 1)),
                     ('OM1_23', (0, 1)),
                     ('OM1_24', (0, 1)),
                     ('OM1_25', (0, 1)),
                     ('OM1_26', (0, -1)),
                     ('OM1_27', (0, 1)),
                     ('OM1_28', (0, -1)),
                     ('OM1_29', (0, -1)),
                     ('OM1_30', (0, -1)),
                     ('OM1_31', (0, 1)),
                     ('OM1_32', (0, -1)),
                     ('OM1_33', (0, 1)),
                     ('OM1_34', (0, -1)),
                     ('OM1_35', (0, -1)),
                     ('OM1_36', (0, 1)),
                     ('OM1_37', (0, -1)),
                     ('OM1_38', (0, 1)),
                     ('OM1_39', (0, 1)),
                     ('OM1_40', (0, 1)),
                     ('OM1_41', (0, -1)),
                     ('OM1_42', (0, 1)))),
            'OM2': ('sequence',
                    (('OM2_1', (0, 1)),
                     ('OM2_2', (0, 1)),
                     ('OM2_3', (0, 1)),
                     ('OM2_4', (0, 1)),
                     ('OM2_5', (0, 1)),
                     ('OM2_6', (1, -1)),
                     ('OM2_7', (0, -1)),
                     ('OM2_8', (0, 1)),
                     ('OM2_9', (0, 1)),
                     ('OM2_10', (0, -1)),
                     ('OM2_11', (0, 1)))),
            'OM3': ('sequence',
                    (('OM3_1', (0, 1)),
                     ('OM3_2', (0, 1)),
                     ('OM3_3', (0, 1)),
                     ('OM3_4', (0, -1)),
                     ('OM3_5', (0, -1)),
                     ('OM3_6', (0, 1)),
                     ('OM3_7', (0, 1)),
                     ('OM3_8', (0, 1)))),
            'OM4': ('sequence',
                    (('OM4_1', (0, 1)),
                     ('OM4_2', (0, 1)),
                     ('OM4_3', (0, 1)),
                     ('OM4_4', (0, 1)),
                     ('OM4_5', (0, 1)),
                     ('OM4_6', (0, 1)),
                     ('OM4_7', (0, 1)),
                     ('OM4_8', (0, 1)),
                     ('OM4_9', (0, 1)),
                     ('OM4_10', (0, 1)),
                     ('OM4_11', (0, 1)),
                     ('OM4_12', (0, 1)),
                     ('OM4_13', (0, 1)),
                     ('OM4_14', (0, -1)),
                     ('OM4_15', (0, 1)))),
            'OM5': ('sequence',
                    (('OM5_1', (0, 1)),
                     ('OM5_2', (0, 1)),
                     ('OM5_3', (0, -1)),
                     ('OM5_4', (0, 1)))),
            'OM6': ('sequence',
                    (('OM6_1', (0, 1)), ('OM6_2', (0, 1)), ('OM6_3', (0, 1)))),
            'ORC': ('sequence',
                    (('ORC_1', (1, 1)),
                     ('ORC_2', (0, 1)),
                     ('ORC_3', (0, 1)),
                     ('ORC_4', (0, 1)),
                     ('ORC_5', (0, 1)),
                     ('ORC_6', (0, 1)),
                     ('ORC_7', (0, -1)),
                     ('ORC_8', (0, 1)),
                     ('ORC_9', (0, 1)),
                     ('ORC_10', (0, 1)),
                     ('ORC_11', (0, 1)),
                     ('ORC_12', (0, 1)),
                     ('ORC_13', (0, 1)),
                     ('ORC_14', (0, -1)),
                     ('ORC_15', (0, 1)),
                     ('ORC_16', (0, 1)),
                     ('ORC_17', (0, 1)),
                     ('ORC_18', (0, 1)),
                     ('ORC_19', (0, 1)))),
            'PID': ('sequence',
                    (('PID_1', (0, 1)),
                     ('PID_2', (0, 1)),
                     ('PID_3', (1, -1)),
                     ('PID_4', (0, 1)),
                     ('PID_5', (1, 1)),
                     ('PID_6', (0, 1)),
                     ('PID_7', (0, 1)),
                     ('PID_8', (0, 1)),
                     ('PID_9', (0, -1)),
                     ('PID_10', (0, 1)),
                     ('PID_11', (0, -1)),
                     ('PID_12', (0, 1)),
                     ('PID_13', (0, -1)),
                     ('PID_14', (0, -1)),
                     ('PID_15', (0, 1)),
                     ('PID_16', (0, 1)),
                     ('PID_17', (0, 1)),
                     ('PID_18', (0, 1)),
                     ('PID_19', (0, 1)),
                     ('PID_20', (0, 1)),
                     ('PID_21', (0, 1)),
                     ('PID_22', (0, 1)),
                     ('PID_23', (0, 1)),
                     ('PID_24', (0, 1)),
                     ('PID_25', (0, 1)),
                     ('PID_26', (0, -1)),
                     ('PID_27', (0, 1)))),
            'PR1': ('sequence',
                    (('PR1_1', (1, 1)),
                     ('PR1_2', (1, -1)),
                     ('PR1_3', (1, -1)),
                     ('PR1_4', (0, -1)),
                     ('PR1_5', (1, 1)),
                     ('PR1_6', (1, 1)),
                     ('PR1_7', (0, 1)),
                     ('PR1_8', (0, 1)),
                     ('PR1_9', (0, 1)),
                     ('PR1_10', (0, 1)),
                     ('PR1_11', (0, 1)),
                     ('PR1_12', (0, -1)),
                     ('PR1_13', (0, 1)),
                     ('PR1_14', (0, 1)))),
            'PRA': ('sequence',
                    (('PRA_1', (1, 1)),
                     ('PRA_2', (0, -1)),
                     ('PRA_3', (0, -1)),
                     ('PRA_4', (0, 1)),
                     ('PRA_5', (0, -1)),
                     ('PRA_6', (0, -1)),
                     ('PRA_7', (0, -1)))),
            'PV1': ('sequence',
                    (('PV1_1', (0, 1)),
                     ('PV1_2', (1, 1)),
                     ('PV1_3', (0, 1)),
                     ('PV1_4', (0, 1)),
                     ('PV1_5', (0, 1)),
                     ('PV1_6', (0, 1)),
                     ('PV1_7', (0, 1)),
                     ('PV1_8', (0, 1)),
                     ('PV1_9', (0, -1)),
                     ('PV1_10', (0, 1)),
                     ('PV1_11', (0, 1)),
                     ('PV1_12', (0, 1)),
                     ('PV1_13', (0, 1)),
                     ('PV1_14', (0, 1)),
                     ('PV1_15', (0, -1)),
                     ('PV1_16', (0, 1)),
                     ('PV1_17', (0, 1)),
                     ('PV1_18', (0, 1)),
                     ('PV1_19', (0, 1)),
                     ('PV1_20', (0, -1)),
                     ('PV1_21', (0, 1)),
                     ('PV1_22', (0, 1)),
                     ('PV1_23', (0, 1)),
                     ('PV1_24', (0, -1)),
                     ('PV1_25', (0, -1)),
                     ('PV1_26', (0, -1)),
                     ('PV1_27', (0, -1)),
                     ('PV1_28', (0, 1)),
                     ('PV1_29', (0, 1)),
                     ('PV1_30', (0, 1)),
                     ('PV1_31', (0, 1)),
                     ('PV1_32', (0, 1)),
                     ('PV1_33', (0, 1)),
                     ('PV1_34', (0, 1)),
                     ('PV1_35', (0, 1)),
                     ('PV1_36', (0, 1)),
                     ('PV1_37', (0, 1)),
                     ('PV1_38', (0, 1)),
                     ('PV1_39', (0, 1)),
                     ('PV1_40', (0, 1)),
                     ('PV1_41', (0, 1)),
                     ('PV1_42', (0, 1)),
                     ('PV1_43', (0, 1)),
                     ('PV1_44', (0, 1)),
                     ('PV1_45', (0, 1)),
                     ('PV1_46', (0, 1)),
                     ('PV1_47', (0, 1)),
                     ('PV1_48', (0, 1)),
                     ('PV1_49', (0, 1)),
                     ('PV1_50', (0, 1)))),
            'PV2': ('sequence',
                    (('PV2_1', (0, 1)),
                     ('PV2_2', (0, 1)),
                     ('PV2_3', (0, 1)),
                     ('PV2_4', (0, 1)),
                     ('PV2_5', (0, -1)),
                     ('PV2_6', (0, 1)),
                     ('PV2_7', (0, 1)),
                     ('PV2_8', (0, 1)),
                     ('PV2_9', (0, 1)))),
            'QRD': ('sequence',
                    (('QRD_1', (1, 1)),
                     ('QRD_2', (1, 1)),
                     ('QRD_3', (1, 1)),
                     ('QRD_4', (1, 1)),
                     ('QRD_5', (0, 1)),
                     ('QRD_6', (0, 1)),
                     ('QRD_7', (1, 1)),
                     ('QRD_8', (1, -1)),
                     ('QRD_9', (1, -1)),
                     ('QRD_10', (1, -1)),
                     ('QRD_11', (0, -1)),
                     ('QRD_12', (0, 1)))),
            'QRF': ('sequence',
                    (('QRF_1', (1, -1)),
                     ('QRF_2', (0, 1)),
                     ('QRF_3', (0, 1)),
                     ('QRF_4', (0, -1)),
                     ('QRF_5', (0, -1)),
                     ('QRF_6', (0, -1)),
                     ('QRF_7', (0, -1)),
                     ('QRF_8', (0, -1)))),
            'RQ1': ('sequence',
                    (('RQ1_1', (0, 1)),
                     ('RQ1_2', (0, 1)),
                     ('RQ1_3', (0, 1)),
                     ('RQ1_4', (0, 1)),
                     ('RQ1_5', (0, 1)),
                     ('RQ1_6', (0, 1)),
                     ('RQ1_7', (0, 1)))),
            'RQD': ('sequence',
                    (('RQD_1', (0, 1)),
                     ('RQD_2', (0, 1)),
                     ('RQD_3', (0, 1)),
                     ('RQD_4', (0, 1)),
                     ('RQD_5', (0, 1)),
                     ('RQD_6', (0, 1)),
                     ('RQD_7', (0, 1)),
                     ('RQD_8', (0, 1)),
                     ('RQD_9', (0, 1)),
                     ('RQD_10', (0, 1)))),
            'RXA': ('sequence',
                    (('RXA_1', (1, 1)),
                     ('RXA_2', (1, 1)),
                     ('RXA_3', (1, 1)),
                     ('RXA_4', (1, 1)),
                     ('RXA_5', (1, 1)),
                     ('RXA_6', (1, 1)),
                     ('RXA_7', (0, 1)),
                     ('RXA_8', (0, 1)),
                     ('RXA_9', (0, 1)),
                     ('RXA_10', (0, 1)),
                     ('RXA_11', (0, 1)),
                     ('RXA_12', (0, 1)))),
            'RXC': ('sequence',
                    (('RXC_1', (1, 1)),
                     ('RXC_2', (1, 1)),
                     ('RXC_3', (1, 1)),
                     ('RXC_4', (1, 1)))),
            'RXD': ('sequence',
                    (('RXD_1', (0, 1)),
                     ('RXD_2', (1, 1)),
                     ('RXD_3', (0, 1)),
                     ('RXD_4', (1, 1)),
                     ('RXD_5', (0, 1)),
                     ('RXD_6', (0, 1)),
                     ('RXD_7', (1, 1)),
                     ('RXD_8', (0, 1)),
                     ('RXD_9', (0, -1)),
                     ('RXD_10', (0, 1)),
                     ('RXD_11', (0, 1)),
                     ('RXD_12', (0, 1)),
                     ('RXD_13', (0, 1)),
                     ('RXD_14', (0, 1)),
                     ('RXD_15', (0, 1)))),
            'RXE': ('sequence',
                    (('RXE_1', (0, -1)),
                     ('RXE_2', (1, 1)),
                     ('RXE_3', (1, 1)),
                     ('RXE_4', (0, 1)),
                     ('RXE_5', (1, 1)),
                     ('RXE_6', (0, 1)),
                     ('RXE_7', (0, -1)),
                     ('RXE_8', (0, 1)),
                     ('RXE_9', (0, 1)),
                     ('RXE_10', (0, 1)),
                     ('RXE_11', (0, 1)),
                     ('RXE_12', (0, 1)),
                     ('RXE_13', (0, 1)),
                     ('RXE_14', (0, 1)),
                     ('RXE_15', (1, 1)),
                     ('RXE_16', (0, 1)),
                     ('RXE_17', (0, 1)),
                     ('RXE_18', (0, 1)),
                     ('RXE_19', (0, 1)),
                     ('RXE_20', (0, 1)),
                     ('RXE_21', (0, 1)),
                     ('RXE_22', (0, 1)),
                     ('RXE_23', (0, 1)),
                     ('RXE_24', (0, 1)))),
            'RXG': ('sequence',
                    (('RXG_1', (1, 1)),
                     ('RXG_2', (0, 1)),
                     ('RXG_3', (0, -1)),
                     ('RXG_4', (1, 1)),
                     ('RXG_5', (1, 1)),
                     ('RXG_6', (0, 1)),
                     ('RXG_7', (1, 1)),
                     ('RXG_8', (0, 1)),
                     ('RXG_9', (0, 1)),
                     ('RXG_10', (0, 1)),
                     ('RXG_11', (0, 1)),
                     ('RXG_12', (0, 1)),
                     ('RXG_13', (0, -1)),
                     ('RXG_14', (0, 1)),
                     ('RXG_15', (0, 1)),
                     ('RXG_16', (0, 1)))),
            'RXO': ('sequence',
                    (('RXO_1', (1, 1)),
                     ('RXO_2', (1, 1)),
                     ('RXO_3', (0, 1)),
                     ('RXO_4', (1, 1)),
                     ('RXO_5', (0, 1)),
                     ('RXO_6', (0, -1)),
                     ('RXO_7', (0, -1)),
                     ('RXO_8', (0, 1)),
                     ('RXO_9', (0, 1)),
                     ('RXO_10', (0, 1)),
                     ('RXO_11', (0, 1)),
                     ('RXO_12', (0, 1)),
                     ('RXO_13', (0, 1)),
                     ('RXO_14', (0, 1)),
                     ('RXO_15', (0, 1)),
                     ('RXO_16', (0, 1)),
                     ('RXO_17', (0, 1)))),
            'RXR': ('sequence',
                    (('RXR_1', (1, 1)),
                     ('RXR_2', (0, 1)),
                     ('RXR_3', (0, 1)),
                     ('RXR_4', (0, 1)))),
            'STF': ('sequence',
                    (('STF_1', (1, 1)),
                     ('STF_2', (0, -1)),
                     ('STF_3', (0, 1)),
                     ('STF_4', (0, -1)),
                     ('STF_5', (0, 1)),
                     ('STF_6', (0, 1)),
                     ('STF_7', (0, 1)),
                     ('STF_8', (0, -1)),
                     ('STF_9', (0, -1)),
                     ('STF_10', (0, -1)),
                     ('STF_11', (0, -1)),
                     ('STF_12', (0, -1)),
                     ('STF_13', (0, -1)),
                     ('STF_14', (0, -1)),
                     ('STF_15', (0, -1)),
                     ('STF_16', (0, 1)))),
            'UB1': ('sequence',
                    (('UB1_1', (0, 1)),
                     ('UB1_2', (0, 1)),
                     ('UB1_3', (0, 1)),
                     ('UB1_4', (0, 1)),
                     ('UB1_5', (0, 1)),
                     ('UB1_6', (0, 1)),
                     ('UB1_7', (0, -1)),
                     ('UB1_8', (0, 1)),
                     ('UB1_9', (0, 1)),
                     ('UB1_10', (0, -1)),
                     ('UB1_11', (0, 1)),
                     ('UB1_12', (0, 1)),
                     ('UB1_13', (0, 1)),
                     ('UB1_14', (0, 1)),
                     ('UB1_15', (0, 1)),
                     ('UB1_16', (0, -1)),
                     ('UB1_17', (0, 1)),
                     ('UB1_18', (0, 1)),
                     ('UB1_19', (0, 1)),
                     ('UB1_20', (0, 1)),
                     ('UB1_21', (0, 1)),
                     ('UB1_22', (0, 1)),
                     ('UB1_23', (0, 1)))),
            'UB2': ('sequence',
                    (('UB2_1', (0, 1)),
                     ('UB2_2', (0, 1)),
                     ('UB2_3', (0, -1)),
                     ('UB2_4', (0, 1)),
                     ('UB2_5', (0, 1)),
                     ('UB2_6', (0, -1)),
                     ('UB2_7', (0, -1)),
                     ('UB2_8', (0, -1)),
                     ('UB2_9', (0, -1)),
                     ('UB2_10', (0, -1)),
                     ('UB2_11', (0, 1)),
                     ('UB2_12', (0, -1)),
                     ('UB2_13', (0, -1)),
                     ('UB2_14', (0, -1)),
                     ('UB2_15', (0, 1)),
                     ('UB2_16', (0, -1)))),
            'URD': ('sequence',
                    (('URD_1', (0, 1)),
                     ('URD_2', (0, 1)),
                     ('URD_3', (1, -1)),
                     ('URD_4', (0, -1)),
                     ('URD_5', (0, -1)),
                     ('URD_6', (0, -1)),
                     ('URD_7', (0, 1)))),
            'URS': ('sequence',
                    (('URS_1', (1, -1)),
                     ('URS_2', (0, 1)),
                     ('URS_3', (0, 1)),
                     ('URS_4', (0, -1)),
                     ('URS_5', (0, -1)),
                     ('URS_6', (0, -1)),
                     ('URS_7', (0, -1)),
                     ('URS_8', (0, -1))))}
