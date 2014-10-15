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

import sys
import os
import re
from optparse import OptionParser
from lxml import objectify
import pprint
import collections
import cPickle

class TableParser(object):

    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path
        self.parse_tables()

    def parse_tables(self):
        files = [f for f in os.listdir(self.input_path) if f.endswith('.xml')]
        try:
            if not os.path.exists(self.output_path):
                os.mkdir(self.output_path)
        except Exception, ex:
            print "Error occurred while saving the output to: ", self.output_path, ex
            sys.exit(1)

        for f in files:
            filename, ext = os.path.splitext(f)
            content = self.parse_table_file(f)
            file_path = os.path.join(self.output_path, filename)
            with open(file_path, "w") as output_file:
                output_file.write("TABLES = ")
                pprint.pprint(content, output_file)

    def parse_table_file(self, file):
        """
        Parses the given table file using the lxml library then returns a dictionary
        containing parsing results.
        """

        tables = {}
        try:
            schema_path = os.path.join(self.input_path, file)
            with open(schema_path) as xml_file:
                data = xml_file.read()
        except Exception, ex:
            print "Error occurred while opening the table file: ", ex
            sys.exit(1)

        try:
            f = objectify.XML(data)
        except Exception, ex:
            print "Invalid XML file: ", file, ex
            sys.exit(1)

        for t in f.hl7tables.hl7table:
            try:
                children = [(c.get('code'), c.get('description')) for c in t.tableElement]
            except:
                continue
            else:
                table_id = "HL7{}".format(t.get("id"))
                tables[table_id] = (t.get("name"), tuple(children))

        return tables

if __name__ == '__main__':
    usage = "%prog [options] message_table_folder"
    example = "Example: python table_parser.py /home/user/tables"
    parser = OptionParser(usage=usage, epilog=example)
    parser.add_option("-o", "--output_dir",
                        action="store", dest="output_dir", default="./tables",
                        help="output path [%default]")
    (options, args) = parser.parse_args()
    try:
        path = args[0]
    except:
        parser.error("Please specify the folder containing table files.")
    else:
        if not os.path.isdir(path):
            parser.error("Folder %s not found." % path)
        TableParser(path, options.output_dir)
