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

import os
import uuid
import datetime

from hl7apy import load_message_profile
from hl7apy.core import Message
from hl7apy.parser import parse_message
from hl7apy.utils import check_date
from hl7apy.v2_5 import DTM
from hl7apy.mllp import MLLPServer, AbstractHandler, UnsupportedMessageType, InvalidHL7Message

_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))


class PDQSupplier(AbstractHandler):
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
        res.msh.msh_5 = self.incoming_message.msh.msh_3
        res.msh.msh_6 = self.incoming_message.msh.msh_4
        res.msh.msh_7.ts_1 = DTM(datetime.datetime.now())
        res.msh.msh_9 = 'RSP^K22^RSP_K21'
        res.msh.msh_10 = uuid.uuid4().hex

        # MSA creation
        res.msa.msa_1 = ack_code
        res.msa.msa_2 = self.incoming_message.msh.msh_10.msh_10_1

        # QAK creation
        res.qak.qak_1 = self.incoming_message.qpd.qpd_2
        res.qak.qak_2 = 'OK' if len(patients) > 0 else 'NF'
        res.qak.qak_4 = str(len(patients))

        # QPD creation
        res.qpd = self.incoming_message.qpd

        # RSP_K21_QUERY_RESPONSE creation
        res.add_group('rsp_k21_query_response')
        g = res.rsp_k21_query_response
        for i, p in enumerate(patients):
            # add a pid segment for every patient
            g.add_segment('PID')
            g.pid[i].pid_3.cx_1, g.pid[i].pid_5.xpn_1, g.pid[i].pid_5.xpn_2 = p[:]

        return res.to_mllp()

    def _create_error(self, error_code):
        res = self._create_response('AR', 'AR', [])
        return res

    def reply(self):
        print('Received a message')
        print(repr(self.incoming_message.to_er7()))
        query_params = dict((self.FIELD_NAMES[q.qip_1.value], q.qip_2.value)
                            for q in self.incoming_message.qpd.qpd_3
                            if q.qip_1.value in self.FIELD_NAMES)
        print("Extracted query params: {}".format(query_params))
        if '' in query_params.values():
            return self._create_error(1)
        else:
            patients = [('0001', 'John', 'Smith')]
            return self._create_response('AA', 'OK', patients)


class HL7ErrorHandler(AbstractHandler):
    def __init__(self, exc, incoming_message):
        super(HL7ErrorHandler, self).__init__(incoming_message)
        self.exc = exc

    def reply(self):

        if isinstance(self.exc, UnsupportedMessageType):
            err_code, err_msg = 101, 'Unsupported message'
        elif isinstance(self.exc, InvalidHL7Message):
            err_code, err_msg = 102, 'Incoming message is not an HL7 valid message'
        else:
            err_code, err_msg = 100, 'Unknown error occurred'

        parsed_message = parse_message(self.incoming_message)

        m = Message("ACK")
        m.MSH.MSH_9 = "ACK^ACK"
        m.MSA.MSA_1 = "AR"
        m.MSA.MSA_2 = parsed_message.MSH.MSH_10
        m.ERR.ERR_1 = "%s" % err_code
        m.ERR.ERR_2 = "%s" % err_msg

        return m.to_mllp()


if __name__ == '__main__':
    handlers = {
        'QBP^Q22^QBP_Q21': (PDQSupplier,),
        'ERR': (HL7ErrorHandler,)
    }

    server = MLLPServer('localhost', 6789, handlers)
    server.serve_forever()
