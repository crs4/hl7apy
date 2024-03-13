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

from __future__ import absolute_import
import socket
import unittest
from threading import Thread

from hl7apy.mllp import MLLPServer, AbstractHandler
from hl7apy.mllp import InvalidHL7Message, UnsupportedMessageType


HOST = 'localhost'
PORT = 2576
INVALID_MESSAGE = 'INVALID MESSAGE'
UNSUPPORTED_MESSAGE = 'INVALID MESSAGE'

PDQ_REQ_TPL = \
    'MSH|^~\\&|REC APP|REC FAC|SENDING APP|SENTING FAC|20110708163513||{}|1|D|2.5|||||ITA||EN\r' \
    'QPD|IHE PDQ Query|111069|@PID.3.1^1||||\r' \
    'RCP|I|'

PDQ_REQ = PDQ_REQ_TPL.format('QBP^Q22^QBP_Q21')

PDQV_REQ = PDQ_REQ_TPL.format('QBP^ZV1^QBP_Q21')

PDQ_RES_TPL = \
    'MSH|^~\\&|SENDING APP|SENDING FAC|REC APP|REC FAC|20110708163514||{}|2|D|2.5|||||ITA||EN\r' \
    'MSA|AA|26775702551812240|\r' \
    'QAK|1|OK||1|1|0\r' \
    'QPD|IHE PDQ Query|111069|@PID.3.1^1010110909194822~@PID.5.1^SMITH||||\r' \
    'PID|1||1^^^lis||MOUSE^MICKEY^^^^^A||19690113|M|||VIA VIA^^CAGLIARI^^^100^H^^|||||||MOSMCK|||||CAGLIARI|||||\r'

PDQ_RES = PDQ_RES_TPL.format('RSP^K22^RSP_K21')

PDQV_RES = PDQ_RES_TPL.format('RSP^ZV2^RSP_ZV2')


class PDQHandler(AbstractHandler):

    def reply(self):
        return PDQ_RES


class ErrorHandler(AbstractHandler):
    def __init__(self, exc, msg):
        super(ErrorHandler, self).__init__(msg)
        self.exc = exc

    def reply(self):
        if isinstance(self.exc, InvalidHL7Message):
            return INVALID_MESSAGE
        elif isinstance(self.exc, UnsupportedMessageType):
            return UNSUPPORTED_MESSAGE


class CustomArgsPDQHandler(AbstractHandler):

    def __init__(self, msg, is_pdqv):
        super(CustomArgsPDQHandler, self).__init__(msg)
        self.is_pdqv = is_pdqv

    def reply(self):
        if self.is_pdqv:
            return PDQV_RES
        return PDQ_RES


def launch_server(host, port, handlers):
    server = MLLPServer(host, port, handlers, timeout=3)
    thread = Thread(target=server.serve_forever)
    thread.daemon = True
    thread.start()

    return server, thread


def stop_server(server, thread):
    server.shutdown()
    thread.join()


class TestMLLPWithErrorHandler(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        handlers = {
            'QBP^Q22^QBP_Q21': (PDQHandler,),
            'QBP^ZV1^QBP_Q21': (CustomArgsPDQHandler, True),
            'ERR': (ErrorHandler,)
        }
        cls.server, cls.thread = launch_server(HOST, PORT, handlers)

    @classmethod
    def tearDownClass(cls):
        stop_server(cls.server, cls.thread)

    def _client(self, msg):
        # establish the connection
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect((HOST, PORT))
            sock.sendall(msg.encode('utf-8'))
            res = []
            while True:
                received = sock.recv(1)
                if not received:
                    break
                res.append(received)
        finally:
            sock.close()

        return b''.join(res).decode('utf-8')

    def test_good_message(self):
        msg = '\x0b{}\x1c\x0d'.format(PDQ_REQ)
        res = self._client(msg)
        self.assertEqual(res, PDQ_RES)

    def test_good_message_with_args(self):
        msg = '\x0b{}\x1c\x0d'.format(PDQV_REQ)
        res = self._client(msg)
        self.assertEqual(res, PDQV_RES)

    def test_not_er7_message(self):
        msg = '\x0bWRONG\x1c\x0d'
        res = self._client(msg)
        self.assertEqual(res, UNSUPPORTED_MESSAGE)

    def test_unsupported_message(self):
        msg = '\x0b{}\x1c\x0d'.format(PDQ_RES)
        res = self._client(msg)
        self.assertEqual(res, UNSUPPORTED_MESSAGE)

    def test_timeout(self):
        msg = '\x0b{}\x1c'.format(PDQ_REQ)
        res = self._client(msg)
        self.assertEqual(res, '')


class TestMLLPWithoutErrorHandler(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        handlers = {
            'QBP^Q22^QBP_Q21': (PDQHandler,)
        }
        cls.server, cls.thread = launch_server(HOST, PORT + 1, handlers)

    @classmethod
    def tearDownClass(cls):
        stop_server(cls.server, cls.thread)

    def _client(self, msg):
        # establish the connection
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect((HOST, PORT + 1))
            sock.sendall(msg.encode('utf-8'))
            res = []
            while True:
                received = sock.recv(1)
                if not received:
                    break
                res.append(received)
        finally:
            sock.close()

        return b''.join(res).decode('utf-8')

    def test_good_message(self):
        msg = '\x0b{}\x1c\x0d'.format(PDQ_REQ)
        res = self._client(msg)
        self.assertEqual(res, PDQ_RES)

    def test_not_er7_message(self):
        msg = '\x0bWRONG\x1c\x0d'
        res = self._client(msg)
        self.assertEqual(res, '')

    def test_unsupported_message(self):
        msg = '\x0b{}\x1c\x0d'.format(PDQ_RES)
        res = self._client(msg)
        self.assertEqual(res, '')

    def test_timeout(self):
        msg = '\x0b{}\x1c'.format(PDQ_REQ)
        res = self._client(msg)
        self.assertEqual(res, '')


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestMLLPWithErrorHandler))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestMLLPWithoutErrorHandler))
    unittest.TextTestRunner().run(suite)
