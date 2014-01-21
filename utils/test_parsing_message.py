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

import os
import sys
import time
from collections import defaultdict
from optparse import OptionParser

from hl7apy import SUPPORTED_LIBRARIES
from hl7apy.parser import parse_message
from hl7apy.validation import VALIDATION_LEVEL

def get_parser():
    parser = OptionParser("usage: %prog -d directory -o output_file -n number_of_message")
    parser.add_option("-d", "--input_dir",  type="string", dest="input_dir",
                      help="directory containing .hl7 files")
    parser.add_option("-o", "--output_file", type="string", dest="output_file",
                      help="statistics file. By default its stdout")
    parser.add_option("-n", "--number_of_message", type="int", dest="n_msg",
                      help="maximum number of message to parse")
    return parser

def usage():
    print "Parse HL7 messages contained in the directory specified and print a report."
    print "-h show this help"
    print "-d directory"
    print "-n message number limit"
    print "-d "

def print_report(n_messages, msg_per_version, msg_per_type, exceptions,
                 elapsed_time, output_file, time_per_message):

    with open(output_file, 'w') if output_file else sys.stdout as output:
        for validation in ('STRICT', 'QUIET'):
            n_exceptions = len(exceptions[validation])
            output.write("Validation {0}\n".format(validation))
            output.write(80 * "-")
            output.write("\n\nParsed {0} messages in {1}\n".format(n_messages[validation], elapsed_time))
            output.write("Succeed: {0} - Failed {1}\n\n\n".format(n_messages[validation] - n_exceptions, n_exceptions))

            output.write("Succeeded message per version:\n\n")
            for version in sorted(SUPPORTED_LIBRARIES):
                output.write("{0}: {1}\n".format(version, msg_per_version[validation][version]))

            output.write("\n\nMessage types details:\n\n")
            for k, v in msg_per_type[validation].items():
                output.write("{0}: {1}\n".format(k, v))

            output.write("\n\nProblems occurred:\n\n")

            for ex in exceptions[validation]:
                output.write("Problem: {0}: \n".format(ex['ex']))
                output.write("Filename {0}: \n".format(ex['file_name']))
                output.write("Message: {0}: \n\n".format(repr(ex['msg'])))

            output.write("\n\nMessage time statistics:\n\n")
            for tpm in time_per_message[validation]:
                output.write("Num of segments: {0}\tTime: {1}\n".format(tpm[0], tpm[1]))

def parse_messages(directory, limit=-1, output_file=None):
    exceptions = {'QUIET': [], 'STRICT': []}
    msg_per_versions = {'QUIET': defaultdict(int), 'STRICT': defaultdict(int)}
    msg_per_type = {'QUIET': defaultdict(int), 'STRICT': defaultdict(int)}
    parsing_time = {'QUIET' : [], 'STRICT' : []}
    files = _get_files(directory)[:limit]
    n_messages = {'QUIET' : 0, 'STRICT' : len(files)}

    start = time.time()
    for f in files:
        with open(f) as hl7_file:
            msg_str = hl7_file.read()
            msg_str = msg_str.replace('\r\n', '\r')
            msg_str = msg_str.replace('\n', '\r')
            try:
                msg_start = time.time()
                msg = parse_message(msg_str, VALIDATION_LEVEL.STRICT)
                msg_end = time.time()

                msg_per_versions['STRICT'][msg.version] += 1
                msg_per_type['STRICT'][msg.msh.msh_9.to_er7()] += 1
                parsing_time['STRICT'].append((len(msg.children), msg_end - msg_start))
            except Exception as e:
                n_messages['QUIET'] += 1
                try:
                    msg_start = time.time()
                    msg = parse_message(msg_str, VALIDATION_LEVEL.QUIET)
                    msg_end = time.time()
                    msg_per_versions['QUIET'][msg.version] += 1
                    msg_per_type['QUIET'][msg.msh.msh_9.to_er7()] += 1
                    parsing_time['QUIET'].append((len(msg.children), msg_end - msg_start))
                    exceptions['STRICT'].append({'ex': e, 'file_name' : f, 'msg' : msg_str})
                except Exception as e:
                    exceptions['QUIET'].append({'ex': e, 'file_name' : f, 'msg' : msg_str})


    elapsed_time = time.time() - start

    print_report(n_messages, msg_per_versions, msg_per_type, exceptions,
                 elapsed_time, output_file, parsing_time)

def _get_files(directory):
    try:
        files = os.listdir(directory)
        return [ os.path.abspath( '{0}/{1}'.format(directory, f) ) for f in files if f.endswith('.hl7') ]
    except IOError:
        print "Invalid directory"
if __name__ == '__main__':
    parser = get_parser()
    options, args = parser.parse_args()
    if not options.input_dir:
        parser.error('input_dir must be set')

    input_dir = options.input_dir
    output_file = options.output_file
    n_msg = options.n_msg or -1

    parse_messages(input_dir, n_msg, output_file)
