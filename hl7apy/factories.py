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
This module contains factory functions for hl7apy base data types.
The functions get the value of the data type as string and return the correct object
"""

import re
from datetime import datetime
from decimal import Decimal, InvalidOperation
from types import FunctionType

from hl7apy import load_library, get_default_validation_level, get_default_version
from hl7apy.exceptions import InvalidDataType

def datatype_factory(datatype, value, version=None, validation_level=None):
    """
    Factory function for both base and complex datatypes. It generates the correct object according
    to the datatype in input.
    It should be noted that if you use the factory it is not possible to specify
    some parameters for the datatype (e.g. the format for datetime base datatypes)
    If the value is not valid for the datatype specified if the ``validation_level`` is
    :attr:`hl7apy.consts.VALIDATION_LEVEL.QUIET` it generates an :class:`hl7apy.base_datatypes.ST` object

    :type datatype: ``basestring``
    :param datatype: The datatype to be generated

    :param value: The value of the datatype

    :type version: ``basestring``
    :param version: A valid HL7 version. It must be one of :attr:`hl7apy.SUPPORTED_LIBRARIES`

    :type validation_level: ``int``
    :param validation_level: It must be a value from class :attr:`validation_level` :class:`VALIDATION_LEVEL`

    :rtype: The type specified in datatype

    :raises :exc:`hl7apy.exceptions.ValueError`: If the ``validation_level`` is :attr:`hl7apy.consts.VALIDATION_LEVEL.STRICT`
     and the value is not valid for the specified datatype

    :raises :exc:`hl7apy.exceptions.InvalidDatatype`: If the ``datatype`` specified is not valid for the given ``version``

    """

    from hl7apy.validation import Validator

    if validation_level is None:
        validation_level = get_default_validation_level()

    if version is None:
        version = get_default_version()

    lib = load_library(version)

    base_datatypes = lib.get_base_datatypes()

    factories = base_datatypes.copy()

    if 'DT' in factories:
        factories['DT'] = date_factory
    if 'TM' in factories:
        factories['TM'] = timestamp_factory
    if 'DTM' in factories:
        factories['DTM'] = datetime_factory
    if 'NM' in factories:
        factories['NM'] = numeric_factory
    if 'SI' in factories:
        factories['SI'] = sequence_id_factory

    try:
        factory = factories[datatype]
        if isinstance(factory, FunctionType):
            return factory(value, base_datatypes[datatype])
        return factory(value)
    except KeyError:
        raise InvalidDataType(datatype)
    except ValueError, e:
        if Validator.is_strict(validation_level):
            raise e
        #TODO: Do we really want this? In that case the parent's datatype must be changed accordingly
        return factories['ST'](value)

def date_factory(value, datatype_cls):
    """
    Creates a :class:`hl7apy.base_datatypes.DT` object

    The value in input must be a string parsable with :meth:`datetime.strptime`.
    The date format is chosen according to the length of the value as stated in this table:

    +-------+-----------+
    |Length |Format     |
    +=======+===========+
    |4      |``%Y``     |
    |       |           |
    +-------+-----------+
    |6      |``%Y%m``   |
    |       |           |
    +-------+-----------+
    |8      |``%Y%m%d`` |
    |       |           |
    +-------+-----------+

    Some examples that work are:

    >>> from hl7apy.base_datatypes import DT
    >>> date_factory("1974", DT) #doctest: +ELLIPSIS
    <hl7apy.base_datatypes.DT object at 0x...>
    >>> date_factory("198302", DT) #doctest: +ELLIPSIS
    <hl7apy.base_datatypes.DT object at 0x...>
    >>> date_factory("19880312", DT) #doctest: +ELLIPSIS
    <hl7apy.base_datatypes.DT object at 0x...>

    If the value does not match one of the valid format it raises :exc:`ValueError`

    :type value: ``basestring``
    :param value: the value to assign the date object

    :type datatype_cls: `class`
    :param value: the :class:`hl7apy.base_datatypes.DT` class to use. It has to be one implementation of the different version modules

    :rtype: :class:`hl7apy.base_datatypes.DT`
    """

    format = _get_date_format(value)
    dt_value = _datetime_obj_factory(value, format)
    return datatype_cls(dt_value, format)

def timestamp_factory(value, datatype_cls):
    """
    Creates a :class:`hl7apy.base_datatypes.TM` object

    The value in input must be a string parsable with :meth:`datetime.strptime`.
    It can also have an offset part specified with the format +/-HHMM.
    The offset can be added with all the allowed format
    The date format is chosen according to the length of the value as stated in this table:

    +-------+-----------------+
    |Length |Format           |
    +=======+=================+
    |2      |``%H``           |
    +-------+-----------------+
    |4      |``%H%M``         |
    +-------+-----------------+
    |6      |``%H%M%S``       |
    +-------+-----------------+
    |10-13  |``%H%M%S.%f``    |
    +-------+-----------------+

    Some examples that work are:


    >>> from hl7apy.base_datatypes import TM
    >>> timestamp_factory("12", TM) #doctest: +ELLIPSIS
    <hl7apy.base_datatypes.TM object at 0x...>
    >>> timestamp_factory("12+0300", TM) #doctest: +ELLIPSIS
    <hl7apy.base_datatypes.TM object at 0x...>
    >>> timestamp_factory("1204", TM) #doctest: +ELLIPSIS
    <hl7apy.base_datatypes.TM object at 0x...>
    >>> timestamp_factory("120434", TM) #doctest: +ELLIPSIS
    <hl7apy.base_datatypes.TM object at 0x...>
    >>> timestamp_factory("120434-0400", TM) #doctest: +ELLIPSIS
    <hl7apy.base_datatypes.TM object at 0x...>

    If the value does not match one of the valid format it raises :exc:ValueError`

    :type value: ``basestring``
    :param value: the value to assign the date object

    :type datatype_cls: `class`
    :param value: the :class:`hl7apy.base_datatypes.TM` class to use. It has to be one implementation of the different version modules

    :rtype: :class:`hl7apy.base_datatypes.TM`
    """

    value, offset = _split_offset(value)
    form = _get_timestamp_format(value)
    dt_value = _datetime_obj_factory(value, form)
    return datatype_cls(dt_value, form, offset)

def datetime_factory(value, datatype_cls):
    """
    Creates a :class:`hl7apy.base_datatypes.DTM` object

    The value in input must be a string parsable with :meth:`datetime.strptime`.
    It can also have an offset part specified with the format +HHMM -HHMM.
    The offset can be added with all the allowed format.
    The date format is chosen according to the length of the value as stated in this table:

    +-------+-----------------------+
    |Length |Format                 |
    +=======+=======================+
    |4      |``%Y``                 |
    +-------+-----------------------+
    |6      |``%Y%m``               |
    +-------+-----------------------+
    |8      |``%Y%m%d``             |
    +-------+-----------------------+
    |10     |``%Y%m%d%H``           |
    +-------+-----------------------+
    |12     |``%Y%m%d%H%M``         |
    +-------+-----------------------+
    |14     |``%Y%m%d%H%M%S``       |
    +-------+-----------------------+
    |18-21  |``%Y%m%d%H%M%S.%f``    |
    +-------+-----------------------+

    Some examples that work are:


    >>> from hl7apy.base_datatypes import DTM
    >>> datetime_factory("1924", DTM) #doctest: +ELLIPSIS
    <hl7apy.base_datatypes.DTM object at 0x...>
    >>> datetime_factory("1924+0300", DTM) #doctest: +ELLIPSIS
    <hl7apy.base_datatypes.DTM object at 0x...>
    >>> datetime_factory("19220430", DTM) #doctest: +ELLIPSIS
    <hl7apy.base_datatypes.DTM object at 0x...>
    >>> datetime_factory("19220430-0400", DTM) #doctest: +ELLIPSIS
    <hl7apy.base_datatypes.DTM object at 0x...>

    If the value does not match one of the valid format it raises :exc:`ValueError`

    :type value: ``basestring``
    :param value: the value to assign the date object

    :type datatype_cls: `class`
    :param value: the :class:`hl7apy.base_datatypes.DTM` class to use. It has to be one implementation of the different version modules

    :rtype: :class:`hl7apy.base_datatypes.DTM`
    """

    value, offset = _split_offset(value)
    date_format = _get_date_format(value[:8])
    try:
        timestamp_form = _get_timestamp_format(value[8:])
    except ValueError as e:
        if not value[8:]: #if it's empty
            timestamp_form = ''
        else:
            raise e

    form = '{0}{1}'.format(date_format, timestamp_form)
    dt_value = _datetime_obj_factory(value, form)
    return datatype_cls(dt_value, form, offset)

def numeric_factory(value, datatype_cls):
    """
    Creates a :class:`hl7apy.base_datatypes.NM` object

    The value in input can be a string representing a decimal number or a ``float``.
    (i.e. a string valid for :class:`decimal.Decimal()`).
    If it's not, a :exc:`hl7apy.exceptions.ValueError` is raised
    Also an empty string or ``None`` are allowed

    :type value: ``basestring`` or ``None``
    :param value: the value to assign the numeric object

    :type datatype_cls: :class:`hl7apy.base_datatypes.NM`
    :param value: the :class:`hl7apy.base_datatypes.NM` class to use. It has to be one implementation of the different version modules

    :rtype: :class:`hl7apy.base_datatypes.NM`
    """
    if not value:
        return datatype_cls()
    try:
        return datatype_cls(Decimal(value))
    except InvalidOperation:
        raise ValueError('{0} is not an HL7 valid NM value'.format(value))

def sequence_id_factory(value, datatype_cls):
    """
    Creates a :class:`hl7apy.base_datatypes.SI` object

    The value in input can be a string representing an integer number or an ``int``.
    (i.e. a string valid for ``int()``  ).
    If it's not, a :exc:`ValueError` is raised
    Also an empty string or ``None`` are allowed

    :type value: ``basestring`` or ``None``
    :param value: the value to assign the date object

    :type datatype_cls: `class`
    :param value: the SI class to use. It has to be loaded from one implementation of the different version modules

    :rtype: :class:`hl7apy.base_datatypes.SI`
    """
    if not value:
        return datatype_cls()
    try:
        return datatype_cls(int(value))
    except ValueError:
        raise ValueError('{0} is not an HL7 valid SI value'.format(value))

def _split_offset(value):
    offset = re.search('\d*((-|\+)(1[0-2]|0[0-9])([0-5][0-9]))$', value)
    if offset:
        offset = offset.groups()[0]
        return value.replace(offset, ''), offset
    return value, ''

def _get_date_format(value):
    if len(value) == 4:
        format = '%Y'
    elif len(value) == 6:
        format = '%Y%m'
    elif len(value) == 8:
        format = '%Y%m%d'
    else:
        raise ValueError('{0} is not an HL7 valid date value'.format(value))

    return format

def _get_timestamp_format(value):
    if len(value) == 2:
        format = '%H'
    elif len(value) == 4:
        format = '%H%M'
    elif len(value) == 6:
        format = '%H%M%S'
    elif 10 <= len(value) <= 13 and value[9] == '.':
        format = '%H%M%S.%f'
    else:
        raise ValueError('{0} is not an HL7 valid date value'.format(value))

    return format

def _datetime_obj_factory(value, format):
    try:
        dt_value = datetime.strptime(value, format)
    except ValueError:
        raise ValueError('{0} is not an HL7 valid date value'.format(value))
    return dt_value


if __name__ == '__main__':
    import doctest
    doctest.testmod()