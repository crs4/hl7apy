#!/usr/bin/env python
from __future__ import print_function
from hl7apy.core import Message, Segment, Field, Component, SubComponent

INDENT=4

def __dump(thing, with_value=False):
    p = '{:<60}'.format(thing)
    if with_value:
        v = thing.value

        # For objects of base_datatypes, e.g. SI, ST, IS, ID, TN,
        # we need to get their .value
        try:
            p += '     Value: ({}) "{}"'.format(type(v).__name__, v.value)
        except AttributeError:
            p += '     Value: ' + str(v)

    print(p)
    return True

def _dump_default(thing):
    return __dump(thing, False)

def _dump_default_with_value(thing):
    return __dump(thing, True)


def _dump_field_or_component(thing):
    __dump(thing, True)

    # Don't bother showing Components or SubComponents for these simple types
    if (not args.verbose) and thing.datatype in ('NM', 'ST', 'TS', 'ID', 'IS'):
        return False

    return True


def dump_thing(thing, indent=0):

    dumper = {
        Message:        _dump_default,
        Segment:        _dump_default,
        Field:          _dump_field_or_component,
        Component:      _dump_field_or_component,
        #SubComponent:   _dump_subcomponent,
    }.get(type(thing),  _dump_default_with_value)

    print(' '*indent, end='')
    if not dumper(thing):
        # Don't dump children
        return

    try:
        children = thing.children
    except AttributeError:
        return

    for c in children:
        dump_thing(c, indent + INDENT)


if __name__ == '__main__':
    from hl7apy.parser import parse_message, parse_segment
    from hl7apy.consts import VALIDATION_LEVEL
    import hl7apy
    import argparse

    ap = argparse.ArgumentParser()
    ap.add_argument('file', type=argparse.FileType('r'))
    ap.add_argument('-s', '--strict', action='store_true')
    ap.add_argument('-v', '--verbose', action='store_true')
    global args
    args = ap.parse_args()

    if args.strict:
        hl7apy.set_default_validation_level(VALIDATION_LEVEL.STRICT)


    raw = args.file.read()
    raw = raw.replace('\r\n', '\r')
    raw = raw.replace('\n', '\r')


    msg = parse_message(raw)
    dump_thing(msg)
