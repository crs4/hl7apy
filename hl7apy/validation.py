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
import traceback

from hl7apy import load_reference
from hl7apy.consts import VALIDATION_LEVEL
from hl7apy.exceptions import ChildNotFound, ValidationError, ValidationWarning


class Validator(object):
    """
    Class that handles validation. It defines validation levels and validate
    an element using :attr:`VALIDATION.STRICT <hl7apy.consts.VALIDATION_LEVEL.STRICT>` validation level
    """

    def __init__(self, level):
        super(Validator, self).__init__()
        self.level = level

    @staticmethod
    def validate(element, reference=None, report_file=None):
        """
        Checks if the :class:`Element <hl7apy.core.Element>` is a valid HL7 message according to the reference
        specified. If the reference is not specified, it will be used the official HL7 structures for the
        elements.
        In particular it checks:

        * the maximum and minimum number of occurrences for every child
        * that children are all allowed
        * the datatype of fields, components and subcomponents
        * the values, in particular the length and the adherence with the HL7 table, if one is specified

        It raises the first exception that it finds.

        If :attr:`report_file` is specified, it will create a file with all the errors that occur.

        :param element: :class:`Element <hl7apy.core.Element>`: The element to validate
        :param reference: the reference to use. Usually is None or a message profile object
        :param report_file: the name of the report file to create

        :return: The True if everything is ok
        :raises: :exc:`ValidationError <hl7apy.exceptions.ValidationError>`: when errors occur
        :raises: :exc:`ValidationWarning <hl7apy.exceptions.ValidationWarning>`: errors concerning the values
        """

        from hl7apy.core import is_base_datatype

        def _check_z_element(el, errs, warns):
            if el.classname == 'Field':
                if is_base_datatype(el.datatype, el.version) or \
                        el.datatype == 'varies':
                    return True
                elif el.datatype is not None:
                    # if the datatype the is a complex datatype, the z element must follow the correct
                    # structure of that datatype
                    # Component just to search in the datatypes....
                    dt_struct = load_reference(el.datatype, 'Datatypes_Structs', el.version)
                    ref = ('sequence', dt_struct, el.datatype, None, None, -1)
                    _check_known_element(el, ref, errs, warns)
            for c in el.children:
                _is_valid(c, None, errs, warns)
            return True

        def _check_repetitions(el, children, cardinality, child_name, errs):
            children_num = len(children)
            min_repetitions, max_repetitions = cardinality
            if max_repetitions != -1:
                if children_num < min_repetitions:
                    errs.append(ValidationError("Missing required child {}.{}".format(el.name, child_name)))
                elif children_num > max_repetitions:
                    errs.append(ValidationError("Child limit exceeded {}.{}".format(el.name, child_name)))
            else:
                if children_num < min_repetitions:
                    errs.append(ValidationError("Missing required child {}.{}".format(el.name,
                                                                                      child_name)))

        def _check_table_compliance(el, ref, warns):
            table = ref[4]
            if table is not None:
                try:
                    table_ref = load_reference(table, 'Table', el.version)
                except ChildNotFound:
                    pass
                else:
                    table_children = table_ref[1]
                    if el.to_er7() not in table_children:
                        warns.append(ValidationWarning("Value {} not in table {} in element {}.{}".
                                                       format(el.to_er7(), table, el.parent.name,
                                                              el.name)))

        def _check_length(el, ref, warns):
            max_length = ref[5]
            if -1 < max_length < len(el.to_er7()):
                warns.append(ValidationWarning("Exceeded max length ({}) of {}.{}".
                                               format(max_length, el.parent.name, el.name)))

        def _check_datatype(el, ref, errs):
            ref_datatype = ref[2]
            if el.datatype != ref_datatype:
                errs.append(ValidationError("Datatype {} is not correct for {}.{} (it must be {})".
                                            format(el.datatype, el.parent.name, el.name, ref[1])))

        def _get_valid_children_info(ref):
            valid_children = {c[0] for c in ref[1]}
            children_refs = ref[1]
            return valid_children, children_refs

        def _get_child_reference_info(ref):
            child_name, cardinality = ref[0], ref[2]
            return child_name, cardinality

        def _check_known_element(el, ref, errs, warns):
            if ref is None:
                try:
                    ref = load_reference(el.name, el.classname, el.version)
                except ChildNotFound:
                    errs.append(ValidationError("Invalid element found: {}".format(el)))

            if ref[0] in ('sequence', 'choice'):
                element_children = {c.name for c in el.children if not c.is_z_element()}
                valid_children, valid_children_refs = _get_valid_children_info(ref)

                # check that the children are all allowed children
                if not element_children <= valid_children:
                    errs.append(ValidationError("Invalid children detected for {}: {}".
                                                format(el, list(element_children - valid_children))))

                # iterates the valid children
                for child_ref in valid_children_refs:
                    # it gets the structure of the children to check
                    child_name, cardinality = _get_child_reference_info(child_ref)
                    try:
                        # it gets all the occurrences of the children of a type
                        children = el.children.get(child_name)
                    except Exception:
                        # TODO: it is due to the lack of element in the official reference files...  should
                        # we raise an exception here?
                        pass
                    else:
                        _check_repetitions(el, children, cardinality, child_name, errs)
                        # calls validation for every children
                        for c in children:
                            _is_valid(c, child_ref[1], errs, warns)

                # finally calls validation for z_elements
                z_children = [c for c in el.children if c.is_z_element()]
                for c in z_children:
                    _is_valid(c, None, errs, warns)
            else:
                _check_table_compliance(el, ref, warns)

                _check_length(el, ref, warns)

                if el.datatype == 'varies':  # TODO: it should check the real rule
                    return True
                _check_datatype(el, ref, errs)

                # For complex datatypes element, the reference is the one of the datatype
                if not is_base_datatype(el.datatype, el.version) and el.datatype is not None:
                    # Component just to search in the datatypes....
                    ref = load_reference(el.datatype, 'Datatypes_Structs', el.version)
                    _is_valid(el, ref, errs, warns)

        def _is_valid(el, ref, errs, warns):
            if el.is_unknown():
                errs.append(ValidationError("Unknown element found: {}.{}".format(el.parent, el)))
                return

            if el.is_z_element():
                return _check_z_element(el, errs, warns)

            return _check_known_element(el, ref, errs, warns)

        errors = []
        warnings = []

        _is_valid(element, reference, errors, warnings)

        if report_file is not None:
            with open(report_file, "w") as f:
                for e in errors:
                    f.write("Error: {}\n".format(e))
                for w in warnings:
                    f.write("Warning: {}\n".format(w))

        if errors:
            raise errors[0]

        return True

    @staticmethod
    def is_strict(level):
        """
        Check if the given validation level is strict

        :type level: ``int``
        :param level: validation level (see :class:`VALIDATION_LEVEL <hl7apy.consts.VALIDATION_LEVEL>`)
        :rtype: ``bool``
        :return: ``True`` if validation level is strict
        """
        return level == VALIDATION_LEVEL.STRICT

    @staticmethod
    def is_tolerant(level):
        """
        Check if the given validation level is tolerant

        :type level: ``int``
        :param level: validation level (see :class:`VALIDATION_LEVEL <hl7apy.consts.VALIDATION_LEVEL>`)
        :rtype: ``bool``
        :return: ``True`` if validation level is tolerant
        """
        return level == VALIDATION_LEVEL.TOLERANT

    @staticmethod
    def is_quiet(level):
        """
        Equal to :func:`is_tolerant <Validator.is_tolerant>`. Kept for backward compatibility
        :param level:
        :rtype: ``bool``
        :return: ``True`` if validation level is tolerant
        """
        return Validator.is_tolerant(level)
