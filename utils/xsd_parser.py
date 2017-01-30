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

from __future__ import absolute_import, print_function

import sys
import os
import re
from optparse import OptionParser
from lxml import objectify
import pprint
from hl7apy.utils import iteritems


if sys.version_info[0] <= 2:
    def iteritems(d, **kw):
        return d.iteritems(**kw)
else:
    def iteritems(d, **kw):
        return iter(d.items(**kw))


class XSDParser(object):

    def __init__(self, input_path, output_path, to_parse):
        self.input_path = input_path
        self.output_path = output_path
        try:
            methods = [getattr(self, p) for p in to_parse]
        except Exception as ex:
            print("Invalid parsing options.", ex, sep=' ')
            sys.exit(1)
        for m in methods:
            m()

    def parse_segments(self):
        """
        Parses the segments.xsd file found in the input_path and stores
        the results in the segments.py module.
        """
        content = self.parse_schema("segments.xsd")[0]
        self.generate_module("segments.py", content)

    def parse_fields(self):
        """
        Parses the fields.xsd file found in the input_path and stores
        the results in the fields.py module.
        """
        content = self.parse_schema("fields.xsd")[0]
        self.generate_module("fields.py", content)

    def parse_datatypes(self):
        """
        Parses the datatypes.xsd file found in the input_path and stores
        the results in the datatypes.py module.
        """
        parse_res = self.parse_schema("datatypes.xsd")
        content, types = parse_res[0], parse_res[2]
        content.update(types)
        content = {k: v for k, v in iteritems(content) if not k.endswith("_CONTENT")}
        self.generate_module("datatypes.py", content)

    def parse_messages(self):
        """
        Retrieves XSD files list from messages.xsd for parsing and stores
        all the results in the messages.py module.
        """
        parse_res = self.parse_schema("messages.xsd")
        content, includes = parse_res[0], parse_res[1]
        message_files = includes
        message_def = {}
        groups = {}
        for f in message_files:  # each file describes an HL7 message
            message, ext = os.path.splitext(f)
            content = self.parse_schema(f)[0]
            message_def[message] = content[message.upper()]
            groups.update(g for g in iteritems(content) if g[0] != message)
        self.generate_module("messages.py", message_def)
        self.generate_module("groups.py", groups)

    def parse_schema(self, schema_file):
        """
        Parses the given XSD file using the lxml library then returns a dictionary
        containing parsing results.
        """

        try:
            schema_path = os.path.join(self.input_path, schema_file)
            with open(schema_path) as xml_file:
                data = xml_file.read()
        except Exception as ex:
            print("Error occurred while opening the XSD file: ", ex, sep=' ')
            sys.exit(1)

        try:
            f = objectify.XML(data)
        except Exception as ex:
            print("Invalid XSD file: ", schema_file, ex, sep=' ')
            sys.exit(1)

        try:
            includes = [i.get('schemaLocation') for i in f.include]
        except:
            includes = []  # no xsd:include found

        try:
            types = [Node(c).to_dict() for c in f.complexType]
        except Exception as ex:
            complex_types = {}  # no xsd:complexType found,
        else:
            complex_types = dict((node.get('name'), node.get('content')) for node in types)
        try:
            elements = {}
            for e in f.element:
                node = Node(e, complex_types).to_dict()
                content = node.get('content')
                if content:
                    if content.get('type') == 'annotation':
                        content = node['content']
                elements[node.get('name')] = content
        except Exception as ex:
            elements = {}  # no xsd:element found
        return elements, includes, complex_types

    def reduce_content_size(self, content):
        to_delete = []
        for key, value in iteritems(content):
            if value is not None:
                if value['type'] in ('sequence', 'choice') and value.get('content'):
                    try:
                        new_value = (value['type'],
                                     tuple((x['ref'], (x.get('min', 0), x.get('max', -1))) for x in value['content']))
                    except:
                        new_value = None
                elif value['type'] == 'annotation':
                    new_value = ('leaf', value['datatype'], value.get('libraryLongName'), value.get('table'))
                else:
                    new_value = None
                if new_value is None:
                    to_delete.append(key)
                else:
                    content[key] = new_value
        for k in to_delete:
            del content[k]

    def generate_module(self, module_name, module_content):
        """
        Stores parsing results in a python module.
        """
        module_path = os.path.join(self.output_path, module_name)
        constant_name = os.path.splitext(module_name)[0]
        self.reduce_content_size(module_content)
        try:
            if not os.path.exists(self.output_path):
                os.mkdir(self.output_path)
            with open(module_path, "w") as output_file:
                output_file.write("{0} = ".format(constant_name.upper()))
                pprint.pprint(module_content, output_file)
        except Exception as ex:
            print("Error occurred while saving the output to: ", module_name, ex, sep=' ')
            sys.exit(1)


class Node(object):

    def __init__(self, xml_node, types=None):
        """"
        Simpler representation of an XML node for storing relevant information
        from the HL7.org XSD files.
        """
        self.node = xml_node
        self.types = types if types is not None else []
        self.tag = xml_node.tag.replace("{http://www.w3.org/2001/XMLSchema}", "")
        self.name = self._sanitize(self.node.get('name'))
        self.type = self._sanitize(self.node.get('type'))
        self.ref = self._sanitize(self.node.get('ref'))
        self.min = self.node.get('minOccurs')
        self.max = -1 if self.node.get('maxOccurs') == 'unbounded' else self.node.get('maxOccurs')

        if self.min is not None:
            self.min = int(self.min)

        if self.max is not None:
            self.max = int(self.max)

        if self.tag != 'annotation':
            self.children = [Node(c, self.types) for c in self.node.iterchildren()]
        else:
            self.children = []

        self.children = [c for c in self.children if c.tag != 'any']

    def _sanitize(self, s):
        if s is not None:
            s = s.strip().upper()
            s = re.sub("\W+", "_", s)
            if s.endswith('_'):
                s = s[:-1]
            if s.startswith('_'):
                s = s[1:]
            m = re.match("^(C[MNKQ])(_[A-Z]+\d*){1,}(_\d+){0,}$", s)
            if m is not None:
                s = re.sub("_\d+$", "", s)
                s = s[2:].replace("_", "")
                s += m.groups()[2] or ''
        return s

    def to_dict(self):
        node_dict = dict(self.get_node_attrs())
        node_children = [c.to_dict() for c in self.children
                            if c.tag not in ['attributeGroup', 'complexContent', 'simpleContent']]
        ref = node_dict.get('ref') or node_dict.get('type')
        if node_dict.get('tag'):
            if node_dict['tag'] in ['sequence', 'annotation', 'choice']:
                node_dict['type'] = node_dict['tag']
            if node_dict['tag'] == 'annotation':  # describes datatypes and fields
                try:
                    node_dict['longName'] = self.node.documentation.text
                except:
                    pass
                else:
                    node_dict['longName'] = self.node.documentation.text
                    node_dict['libraryLongName'] = self._sanitize(self.node.documentation.text)
                    node_dict['datatype'] = self.node.appinfo.find('{urn:hl7-org:v2xml}Type') or \
                                            self.node.appinfo.find('{urn:hl7-org:v2xml}type') or \
                                            self.node.appinfo.find('{urn:com.sun:encoder-hl7-1.0}Type')
                    if node_dict['datatype'] in ('CM', 'CN', 'CQ', 'CK'):
                        parent = self.node.getparent()
                        try:
                            ct = parent.complexContent
                        except:
                            pass
                        else:
                            node_dict['datatype'] = self._sanitize(ct.extension.get('base'))

                    node_dict['table'] = self.node.appinfo.find('{urn:hl7-org:v2xml}Table') or \
                                         self.node.appinfo.find('{urn:com.sun:encoder-hl7-1.0}Table')
            del(node_dict['tag'])
        if ref in self.types:
            node_dict['content'] = self.types[ref]
        elif node_children:
            if len(node_children) == 1 and not node_dict.get('type') in ('sequence', 'choice'):
                node_dict['content'] = node_children[0]
            else:
                node_dict['content'] = node_children
        return node_dict

    def get_node_attrs(self):
        return [(attr, getattr(self, attr)) for attr in ['name', 'type', 'ref', 'min', 'max', 'tag']
                if getattr(self, attr) is not None]

if __name__ == '__main__':
    usage = "%prog [options] xsd_folder"
    example = "Example: python xsd_parser.py --segments --messages /home/user/hl7_2.5_xsd/"
    parser = OptionParser(usage=usage, epilog=example)
    parser.add_option("-a", "--all",
                        action="store_true", dest="all",
                        help="parse all XSD files")
    parser.add_option("-s", "--segments",
                        action="append_const", dest="to_parse",
                        help="parse segments.xsd file", const='parse_segments')
    parser.add_option("-f", "--fields",
                        action="append_const", dest="to_parse",
                        help="parse fields.xsd file", const='parse_fields')
    parser.add_option("-d", "--datatypes",
                        action="append_const", dest="to_parse",
                        help="parse datatypes.xsd file", const='parse_datatypes')
    parser.add_option("-m", "--messages",
                        action="append_const", dest="to_parse",
                        help="parse XSD files defining HL7 messages", const='parse_messages')
    parser.add_option("-o", "--output_dir",
                        action="store", dest="output_dir", default="./hl7_2_5",
                        help="output path [%default]")
    (options, args) = parser.parse_args()
    try:
        path = args[0]
    except:
        parser.error("Please specify the folder containing HL7.org XSD files.")
    else:
        if not os.path.isdir(path):
            parser.error("Folder %s not found." % path)
        if not options.all and not options.to_parse:
            parser.error("Please specify the HL7.org XSD files to be parsed. \n" +
                "Example: python xsd_parser.py --all /home/user/hl7_2.5_xsd")
        elif options.all:
            options.to_parse = ['parse_segments', 'parse_fields', 'parse_datatypes', 'parse_messages']
        XSDParser(path, options.output_dir, options.to_parse)
