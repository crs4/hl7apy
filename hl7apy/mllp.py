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

import re
import socket
from SocketServer import StreamRequestHandler, TCPServer, ThreadingMixIn

from hl7apy.parser import get_message_type
from hl7apy.exceptions import HL7apyException, ParserError


class UnsupportedMessageType(HL7apyException):
    def __init__(self, msg_type):
        self.msg_type = msg_type

    def __str__(self):
        return 'Unsupported message type %s' % self.msg_type


class InvalidHL7Message(HL7apyException):
    def __str__(self):
        return 'The string received is not a valid HL7 message'


class _MLLPRequestHandler(StreamRequestHandler):
    def __init__(self, *args, **kwargs):
        StreamRequestHandler.__init__(self, *args, **kwargs)

    def setup(self):
        self.sb = "\x0b"
        self.eb = "\x1c"
        self.cr = "\x0d"
        self.validator = re.compile(self.sb + "(([^\r]+\r)*([^\r]+\r?))" + self.eb + self.cr)
        self.handlers = self.server.handlers
        self.timeout = self.server.timeout

        StreamRequestHandler.setup(self)

    def handle(self):
        end_seq = "{}{}".format(self.eb, self.cr)
        try:
            line = self.request.recv(3)
        except socket.timeout:
            self.request.close()
            return

        if line[0] != self.sb:  # First MLLP char
            self.request.close()
            return

        while line[-2:] != end_seq:
            try:
                char = self.rfile.read(1)
                if not char:
                    break
                line += char
            except socket.timeout:
                self.request.close()
                return

        message = self._extract_hl7_message(line)
        if message is not None:
            try:
                response = self._route_message(message)
            except Exception as e:
                self.request.close()
            else:
                # encode the response
                self.wfile.write(response)
        self.request.close()

    def _extract_hl7_message(self, msg):
        message = None
        matched = self.validator.match(msg)
        if matched is not None:
            message = matched.groups()[0]
        return message

    def _route_message(self, msg):
        try:
            try:
                msg_type = get_message_type(msg)
            except ParserError:
                raise InvalidHL7Message

            try:
                handler, args = self.handlers[msg_type][0], self.handlers[msg_type][1:]
            except KeyError:
                raise UnsupportedMessageType(msg_type)

            h = handler(msg, *args)
            return h.reply()
        except Exception as e:
            try:
                err_handler, args = self.handlers['ERR'][0], self.handlers['ERR'][1:]
            except KeyError:
                raise e
            else:
                h = err_handler(e, msg, *args)
                return h.reply()


class MLLPServer(TCPServer):
    """
        A :class:`TCPServer <SocketServer.TCPServer>` subclass that implements an MLLP server
        receives HL7 messages encoded in MLLP and redirects them to the
        correct handler.

        :param host: the address of the listener
        :param port: the port of the listener
        :param handlers: a dictionary that specify the handler classes for every kind of supported message.
            The keys of the dictionary must be the message type and the values the handlers classes.
            The latter must be subclasses of :class:`AbstractTransactionHandler` that implement the
            :func:`reply() <AbstractTransactionHandler.reply>` method
    """
    allow_reuse_address = True

    def __init__(self, host, port, handlers, timeout=10):
        self.host = host
        self.port = port
        self.handlers = handlers
        self.timeout = timeout
        TCPServer.__init__(self, (host, port), _MLLPRequestHandler)

    def add_handler(self, name, fun):
        self.handlers[name] = fun


class AbstractTransactionHandler(object):
    """
        Abstract transaction handler. Handlers should implement the
        :func:`reply() <AbstractTransactionHandler.reply>` method which handle the incoming message.

        :param message: an er7-formatted hl7 message
    """
    def __init__(self, message):
        self.incoming_message = message

    def reply(self):
        """
            Abstract method. It should implement the handling of the request message and return the response
        """
        raise NotImplementedError("The method reply() must be implemented in subclasses")
