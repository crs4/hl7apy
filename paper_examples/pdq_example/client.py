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

import socket

from hl7apy.parser import parse_message

def query(host, port):
    msg = \
        'MSH|^~\&|REC APP|REC FAC|SENDING APP|SENTING FAC|20110708163513||QBP^Q22^QBP_Q21|111069|D|2.5|||||ITA||EN\r' \
        'QPD|IHE PDQ Query|111069|@PID.5.1.1^PATIENT_SURNAME||||\r' \
        'RCP|I|'
    # establish the connection
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((host, port))
        # send the message
        sock.sendall(parse_message(msg).to_mllp())
        # receive the answer
        received = sock.recv(1024*1024)
        return received
    finally:
        sock.close()

if __name__ == '__main__':
    host, port = 'localhost', 6789
    res = query(host, port)
    print repr(res)
