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

from actor import LB
from server import MLLProtocol

def query(host, port, patient_id):
    """
    Establish a TCP connection to the given host and port and send a QBP_Q11 message
    :param host: address to connect to
    :param port: port to connect to
    :param patient_id: patient_id for the query message
    """
    # generate a QBP_Q11 message
    message = LB.send(patient_id)
    # establish the connection
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((host, port))
        # send the message
        sock.sendall(message)
        # receive the answer
        received = sock.recv(1024*1024)
        message = MLLProtocol.get_message(received)
        # handle the response
        LB.receive(message)
    finally:
        sock.close()

if __name__ == '__main__':
    host, port = 'localhost', 6000
    patient_id = '100002'
    query(host, port, patient_id)
