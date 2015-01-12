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
from SocketServer import StreamRequestHandler, TCPServer

from hl7apy.parser import get_message_info


class _MLLPRequestHandler(StreamRequestHandler):
    def __init__(self, *args, **kwargs):
        StreamRequestHandler.__init__(self, *args, **kwargs)

    def _extract_hl7_message(self, msg):
        message = None
        matched = self.validator.match(msg)
        if matched is not None:
            message = matched.groups()[0]
        return message

    def _route_message(self, msg):
        try:
            seps, msg_type, version = get_message_info(msg)
            try:
                h = self.server.handlers[msg_type](msg)
                return h.reply()
            except KeyError:
                raise Exception('Cannot handle this message type')
        except Exception as e:
            raise Exception('An error occurred parsing message: %s' % e)

    def setup(self):
        sb = "\x0b"
        eb = "\x1c"
        cr = "\x0d"

        self.validator = re.compile(sb + "(([^\r]+\r)+)" + eb + cr)
        StreamRequestHandler.setup(self)

    def handle(self):
        line = ''
        while True:
            char = self.rfile.read(1)
            if not char:
                break
            line += char
            # check if incoming buffer contains an HL7 message
            message = self._extract_hl7_message(line)
            if message is not None:
                response = self._route_message(message)
                # encode the response
                self.wfile.write(response)
                line = ''


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
    def __init__(self, host, port, handlers):
        self.host = host
        self.port = port
        self.handlers = handlers

        TCPServer.__init__(self, (host, port), _MLLPRequestHandler)

    def add_handler(self, name, fun):
        self.handlers[name] = fun


class AbstractTransactionHandler(object):
    """
        Abstract transaction handler. Handlers should implement the
        :func:`reply() <AbstractTransactionHandler.reply>` method which handle the incoming message.

        :param message: a :obj:`Message <hl7apy.core.Message>` object
    """
    def __init__(self, message):

        self.msg = message

    def reply(self):
        """
            Abstract method. It should implement the handling of the request message and return the response
        """
        raise NotImplementedError("The method reply() must be implemented in subclasses")
