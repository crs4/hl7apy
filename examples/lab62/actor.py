# -*- coding: utf-8 -*-
#
# Copyright (c) 2012-2014, CRS4
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

import uuid

from hl7apy.core import Message, Segment
from hl7apy.parser import parse_message

class LB(object):
    """
    Label broker implementation
    """
    @staticmethod
    def send(patient_id):
        # create a QBP_Q11 query message for the given patient_id
        m = Message("QBP_Q11")
        m.MSH.sending_application = "LB module" # same as m.msh.msh_3
        m.MSH.receiving_application = "LIP module" # same as m.msh.msh_5
        m.MSH.MSH_9 = "QBP^SLI^QBP_Q11"
        m.MSH.MSH_10 = uuid.uuid4().hex
        m.QPD.QPD_1 = "SLI^Specimen Labeling Instructions^IHE_LABTF"
        m.QPD.query_tag = uuid.uuid4().hex
        m.QPD.QPD_3 = patient_id
        m.RCP = "RCP|I||R"
        return m.to_mllp()

    @staticmethod
    def receive(message):
        # print to stdout the data received
        print "Received by LB"
        try:
            # parse the incoming HL7 message
            m = parse_message(message, find_groups=False)
        except:
            print 'parsing failed', repr(message)
        else:
            print "Message type:", m.MSH.message_type.to_er7()
            print "Message content:", repr(m.to_er7())
            surname, name = m.PID.PID_5.family_name.to_er7(), m.PID.PID_5.given_name.to_er7()
            print "Patient data:", surname, name

class LIP(object):
    """
    Label information provider implementation
    """

    @staticmethod
    def nak(message):
        """
        Build a NAK response for the incoming message

        :param message: incoming message
        :return: a NAK message
        """
        response = Message("ACK")
        response.MSH.MSH_9 = "ACK"
        response.MSA.MSA_1 = "AE"
        response.MSA.MSA_2 = message.MSH.MSH_10
        response.MSA.MSA_3 = "Message type not supported"
        return response

    @staticmethod
    def reply(message):
        """
        Parse the incoming message and return the ER7 encoded response

        :param message: incoming message
        :return: response encoded to ER7 - it can be a NAK or RSP_K11 message
        """
        print "Received by LIP", repr(message)

        try:
            # parse the incoming message
            m = parse_message(message, find_groups=False)
        except:
            print 'parsing failed', repr(message)
            response = LIP.nak()
        else:
            print "Message type:", m.MSH.message_type.to_er7()
            print "Message content:", repr(m.to_er7())
            if m.MSH.MSH_9.MSH_9_3.to_er7() == 'QBP_Q11':
                # create a new RSP_K11 message
                response = Message("RSP_K11")
                response.MSH.MSH_9 = "RSP^K11^RSP_K11"
                # add MSA segment
                response.MSA = "MSA|AA"
                response.MSA.MSA_2 = m.MSH.MSH_10
                # create a QAK segment
                qak = Segment("QAK")
                qak.qak_1 = m.QPD.QPD_2
                qak.qak_2 = "OK"
                qak.qak_3 = "Q22^Specimen Labeling Instructions^IHE_LABTF"
                qak.qak_4 = "1"
                # add the QAK segment to the RSP_K11 message
                response.add(qak)
                # copy the QPD segment from the incoming message
                response.QPD = m.QPD
                # create a PID segment
                response.PID.PID_1 = '1'
                response.PID.PID_5.PID_5_1 = 'PATIENT_SURNAME'
                response.PID.PID_5.PID_5_2 = 'PATIENT_NAME'
                response.PID.PID_6 = "19800101"
                response.PID.PID_7 = "F"
                # create a SPM segment
                spm = Segment("SPM")
                # create an OBR segment
                obr = Segment("OBR")
                spm.SPM_1 = '1'
                spm.SPM_2 = "12345"
                obr.OBR_4 = "ORDER^DESCRIPTION"
                # add spm and obr to the RSP_K11 response
                response.add(spm)
                response.add(obr)
            else:
                response = LIP.nak(m)
        return response.to_mllp() # encode to ER7
