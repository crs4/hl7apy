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

"""
HL7apy - validation
"""

from hl7apy import load_reference
from hl7apy.consts import VALIDATION_LEVEL

class Validator(object):
    """
    Class that handles validation. It defines validation levels and validate
    an element using :attr:`hl7apy.consts.VALIDATION_LEVEL.STRICT` validation level
    """
    def __init__(self, level):
        super(Validator, self).__init__()
        self.level = level

    @staticmethod
    def validate(element):
        """
        Checks if the :class:`hl7apy.core.Element` is a valid HL7 message according to the official structures.
        It checks if it follows the max and min number of occurrences for every child and if it
        doesn't contain children not allowed.

        :param element: :class:`hl7apy.core.Element`
        :return: The element to be validated
        """

        from hl7apy.core import is_base_datatype

        def _is_valid(ref, element):
            children = set([ child.name for child in element.children ])
            valid_children = set([ child[0] for child in ref[1] ])
            if not children <= valid_children:
                return False
            for child in ref[1]:
                child_name, cardinality = child
                min, max = cardinality

                children = element.children.get(child_name)
                num_children = len(children)
                if max != -1:
                    if num_children < min or num_children > max:
                        return False
                else:
                    if num_children < min:
                        return False
                for el in children:
                    if not Validator.validate(el):
                        return False
            return True

        if element.is_unknown():
            return False
        ref = load_reference(element.name, element.classname, element.version)
        if ref[0] in ('sequence', 'choice'):
            return _is_valid(ref, element)
        else: # it's an element that has a datatype
            if element.datatype != ref[1]:
                return False
            if element.is_unknown():
                return False
            if not is_base_datatype(element.datatype, element.version):
                # Component just to search in the datatypes....
                ref = load_reference(element.datatype, 'Component', element.version)
                return _is_valid(ref, element)

        return True

    @staticmethod
    def is_strict(level):
        """
        Check if the given validation level is strict

        :type level: ``int``
        :param level: validation level (see `hl7apy.consts.VALIDATION_LEVEL`)
        :rtype: ``bool``
        :return: ``True`` if validation level is strict
        """
        return level == VALIDATION_LEVEL.STRICT

    @staticmethod
    def is_quiet(level):
        """
        Check if the given validation level is quiet

        :type level: ``int``
        :param level: validation level (see `hl7apy.consts.VALIDATION_LEVEL`)
        :rtype: ``bool``
        :return: ``True`` if validation level is quiet
        """
        return level == VALIDATION_LEVEL.QUIET
