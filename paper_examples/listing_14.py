import os
import uuid
import datetime

from hl7apy import load_message_profile
from hl7apy.core import Message
from hl7apy.parser import parse_message
from hl7apy.utils import check_date
from hl7apy.consts import VALIDATION_LEVEL as VL
from hl7apy.v2_5 import DTM

from hl7apy.mllp import MLLPServer, AbstractTransactionHandler

_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

class PDQSupplier(AbstractTransactionHandler):

    REQ_MP = load_message_profile(os.path.join(_ROOT_PATH, './pdq_req'))
    RES_MP = load_message_profile(os.path.join(_ROOT_PATH, './pdq_res'))

    FIELD_NAMES = {
        '@PID.5.1.1': 'SURNAME',
        '@PID.5.2': 'NAME',
        '@PID.7.1': 'DOB'
    }

    MISSING_PARAMS = 1

    def __init__(self, message):
        msg = parse_message(message, message_profile=self.REQ_MP)
        super(PDQSupplier, self).__init__(msg)

    def _create_response(self, ack_code, query_ack_code, patients):
        res = Message('RSP_K21', reference=self.RES_MP)
        res.msh.msh_5 = self.msg.msh.msh_3
        res.msh.msh_6 = self.msg.msh.msh_4
        res.msh.msh_7.ts_1 = DTM(datetime.datetime.now())
        res.msh.msh_9 = 'RSP^K22^RSP_K21'
        res.msh.msh_10 = uuid.uuid4().hex

        # MSA creation
        res.msa.msa_1 = ack_code
        res.msa.msa_2 = self.msg.msh.msh_10.msh_10_1

        # QAK creation
        res.qak.qak_1 = self.msg.qpd.qpd_2
        res.qak.qak_2 = 'OK' if len(patients) > 0 else 'NF'
        res.qak.qak_4 = str(len(patients))

        # QPD creation
        res.qpd = self.msg.qpd

        # RSP_K21_QUERY_RESPONSE creation
        res.add_group('rsp_k21_query_response')
        g = res.rsp_k21_query_response
        for i, p in enumerate(patients):
            # add a pid segment for every patient
            g.add_segment('PID')
            # p[0] and p[1] are the surname and the name
            g.pid[i].pid_5.xpn_1, g.pid[i].pid_5.xpn_2 = p[:2]

        return res.to_mllp()

    def _create_error(self, error_code):
        res = self._create_response('AR', 'AR', [])
        return res

    def reply(self):
        print self.msg.qpd.qpd_3.datatype
        params = dict((self.FIELD_NAMES[q.qip_1], q.qip_2)
                      for q in self.msg.qpd.qpd_3
                      if q.qip_1 in self.FIELD_NAMES)
        if '' in params.values() or not check_date(params.get('DOB', '')):
            return self._create_error(1)
        else:
            # patients = self.dao.get_data(params)
            patients = []
            return self._create_response('AA', 'NF', patients)


srvr = MLLPServer('localhost', 6789, {'QBP_Q21': PDQSupplier})
srvr.serve_forever()