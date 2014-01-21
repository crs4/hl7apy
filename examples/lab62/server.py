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

import SocketServer
import re

from actor import LIP

#: MLLP encoding chars
SB = "\x0b"
EB = "\x1c"
CR = "\x0d"

class MLLProtocol(object):
    """
    MLLProtocol class

    It just check if an incoming stream of bytes matches the following regexp:

    \x0b{string_containing_carriage_returns}\x1c\x0d
    """
    validator = re.compile(SB + "(([^\r]+\r){1,})" + EB + CR)

    @staticmethod
    def get_message(line):
        message = None
        matched = MLLProtocol.validator.match(line)
        if matched is not None:
            message = matched.groups()[0]
        return message

class MLLPServer(SocketServer.StreamRequestHandler):
    """
    Simplistic implementation of a TCP server implementing the MLLP protocol

    HL7 messages are encoded between bytes \x0b and \x1c\x0d
    """

    def handle(self):
        line = ''
        while True:
            char = self.rfile.read(1)
            if not char:
                print 'client disconnected'
                break
            line += char
            # check if incoming buffer contains a HL7 message
            message = MLLProtocol.get_message(line)
            if message is not None:
                # delegate message response to the LIP actor
                response = LIP.reply(message)
                # encode the response
                self.wfile.write(response)
                line = ''

if __name__ == "__main__":
    HOST, PORT = "localhost", 6000

    server = SocketServer.TCPServer((HOST, PORT), MLLPServer)
    server.serve_forever()