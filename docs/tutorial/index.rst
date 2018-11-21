.. _tutorial:

Getting started
===============

The following tutorial shows you the main features of the library.

Introduction
------------

HL7apy implements classes for messages, groups, segments, fields, components and subcomponents as
defined by the HL7 v2 standard. The elements have a hierarchical relationship and the API gives you the interface
for adding, removing and visiting the tree nodes.

Create a message from scratch
-----------------------------

You can create a new message by instantiating the :class:`hl7apy.core.Message` class:

.. code-block:: python

  >>> from hl7apy.core import Message

  >>> m = Message("ADT_A01")
  >>> m2 = Message()

You can both create a message specifying a structure (e.g. ADT_A01) or create a new message with no predefined structure.

Your new message can be populated as follows:

.. code-block:: python

  >>> pid = Segment("PID")
  >>> patient_group = Group("OML_O33_PATIENT")

  # add a Segment instance
  >>> m.add(pid)

  # add a Group instance
  >>> m2.add(patient_group)

  # create a Segment named MSA and add it to m2
  >>> msa = m2.add_segment('MSA')

  # create a Group named ADT_A01_INSURANCE and add it to m
  >>> g = m.add_group("ADT_A01_INSURANCE")

  # assign a Segment instance
  >>> m.pid = pid

  # assign a string
  >>> m.pid = "PID|1||566-554-3423^^^GHH^MR||EVERYMAN^ADAM^A|||M|||2222 HOME STREET^^ANN ARBOR^MI^^USA||555-555-2004~444-333-222|||M"
  # equivalent to
  >>> m.pid.value = "PID|1||566-554-3423^^^GHH^MR||EVERYMAN^ADAM^A|||M|||2222 HOME STREET^^ANN ARBOR^MI^^USA||555-555-2004~444-333-222|||M"

  # copy from another_message child
  >>> m.pid = m2.oml_o33_patient.pid

You can also populate your message without explicit creation of its children, as in the following example:

.. code-block:: python

  >>> from hl7apy.core import Message

  >>> m = Message("ADT_A01")
  >>> m.pid.pid_5.pid_5_1 = 'EVERYMAN'
  >>> m.pid.pid_5.pid_5_2 = 'ADAM'

The ``PID`` segment is created during child traversal, as well as their related fields and components.
The previous snippet of code is equivalent to:

.. code-block:: python

  >>> from hl7apy.core import Message

  >>> m = Message("ADT_A01")
  >>> pid = Segment("PID")
  >>> pid_5 = Field("PID_5")
  >>> pid_5.pid_5_1 = 'EVERYMAN'
  >>> pid_5.pid_5_2 = 'ADAM'
  >>> pid.add(pid_5)
  >>> m.add(pid)


ADT_A01 example
---------------

Suppose you want to create the following ADT_A01 message:

::

  MSH|^~\&|GHH_ADT||||20080115153000||ADT^A01^ADT_A01|0123456789|P|2.5||||AL
  EVN||20080115153000||AAA|AAA|20080114003000
  PID|1||566-554-3423^^^GHH^MR||EVERYMAN^ADAM^A|||M|||2222 HOME STREET^^ANN ARBOR^MI^^USA||555-555-2004~444-333-222|||M
  NK1|1|NUCLEAR^NELDA^W|SPO|2222 HOME STREET^^ANN ARBOR^MI^^USA

You can create it from scratch by using the core classes, or by using the :func:`hl7apy.parser.parse_message` function;
in the following snippet of code, we show you a way to create it from scratch:

.. code-block:: python

  >>> from hl7apy.core import Message

  >>> m = Message("ADT_A01", version="2.5")
  >>> m.msh.msh_3 = 'GHH_ADT'
  >>> m.msh.msh_7 = '20080115153000'
  >>> m.msh.msh_9 = 'ADT^A01^ADT_A01'
  >>> m.msh.msh_10 = "0123456789"
  >>> m.msh.msh_11 = "P"
  >>> m.msh.msh_16 = "AL"
  >>> m.evn.evn_2 = m.msh.msh_7
  >>> m.evn.evn_4 = "AAA"
  >>> m.evn.evn_5 = m.evn.evn_4
  >>> m.evn.evn_6 = '20080114003000'
  >>> m.pid = "PID|1||566-554-3423^^^GHH^MR||EVERYMAN^ADAM^A|||M|||2222 HOME STREET^^ANN ARBOR^MI^^USA||555-555-2004~444-333-222|||M"
  >>> m.nk1.nk1_1 = '1'
  >>> m.nk1.nk1_2 = 'NUCLEAR^NELDA^W'
  >>> m.nk1.nk1_3 = 'SPO'
  >>> m.nk1.nk1_4 = '2222 HOME STREET^^ANN ARBOR^MI^^USA'

.. _parsing:

Parsing
-------

You can use the provided ER7 parsers to parse a message string:

.. code-block:: python

  >>> from hl7apy.parser import parse_message

  >>> msh = "MSH|^~\&|GHH_ADT||||20080115153000||ADT^A01^ADT_A01|0123456789|P|2.5||||AL\r"
  >>> evn = "EVN||20080115153000||AAA|AAA|20080114003000\r"
  >>> pid = "PID|1||566-554-3423^^^GHH^MR||EVERYMAN^ADAM^A|||M|||2222 HOME STREET^^ANN ARBOR^MI^^USA||555-555-2004~444-333-222|||M\r"
  >>> nk1 = "NK1|1|NUCLEAR^NELDA^W|SPO|2222 HOME STREET^^ANN ARBOR^MI^^USA\r"
  >>> pv1 = "PV1|1|I|GHH PATIENT WARD|U||||^SENDER^SAM^^MD|^PUMP^PATRICK^P|CAR||||2|A0|||||||||||||||||||||||||||||2008\r"
  >>> in1 = "IN1|1|HCID-GL^GLOBAL|HCID-23432|HC PAYOR, INC.|5555 INSURERS CIRCLE^^ANN ARBOR^MI^99999^USA||||||||||||||||||||||||||||||||||||||||||||444-33-3333"

  >>> s = msh + evn + pid + nk1 + pv1 + in1
  >>> message = parse_message(s)

By default, :func:`hl7apy.parser.parse_message` assigns the segments found to the relevant HL7 group.
You can disable this behaviour by passing ``find_groups=False`` to the function. In this case, the segments found are assigned as direct children of the :class:`hl7apy.core.Message` instance.

ER7 parsers for segments, fields and components are also provided:

.. code-block:: python

  >>> from hl7apy.parser import parse_segment, parse_field, parse_component

  >>> pid = "PID|1||566-554-3423^^^GHH^MR||EVERYMAN^ADAM^A|||M|||2222 HOME STREET^^ANN ARBOR^MI^^USA||555-555-2004~444-333-222|||M\r"
  >>> segment = parse_segment(pid)
  >>> field = parse_field("EVERYMAN^ADAM^A") # it will return an instance of Field()
  >>> component = parse_component("ID&TEST&TEST2") # it will return an instance of Component()

Each parser will return an instance of the corresponding core class (e.g. :func:`hl7apy.parser.parse_field` will return a :class:`hl7apy.core.Field` instance).

You can pass the ``name`` argument to both :func:`hl7apy.parser.parse_field` and :func:`hl7apy.parser.parse_component`
functions to assign the name of the corresponding :class:`hl7apy.core.Field` and :class:`hl7apy.core.Component` instances returned by the functions, since it is
not possible to infer their names by simply parsing the input strings:

.. code-block:: python

  >>> from hl7apy.parser import parse_field, parse_component

  >>> field = parse_field("EVERYMAN^ADAM^A", name="PID_5") # it will return an instance of Field("PID_5")
  >>> component = parse_component("AUTH&1.3.6.1.4.1.21367.2011.2.5.17&ISO", name="CX_4") # it will return an instance of Component("CX_4")

ER7 encoding
------------

You can get the ER7-encoded string of ``Message``, ``Group``, ``Segment``, ``Field``, ``Component`` instances by simply calling the :meth:`hl7apy.Element.to_er7` method:

.. code-block:: python

  >>> from hl7apy.parser import parse_segment

  >>> pid = "PID|1||566-554-3423^^^GHH^MR||EVERYMAN^ADAM^A|||M|||2222 HOME STREET^^ANN ARBOR^MI^^USA||555-555-2004~444-333-222|||M\r"
  >>> segment = parse_segment(pid)
  >>> print(segment.to_er7())

You can also use custom encoding chars:

.. code-block:: python

  >>> from hl7apy.parser import parse_segment

  >>> custom_chars = {'FIELD': '!', 'COMPONENT': '@', 'SUBCOMPONENT': '%', 'REPETITION': '~', 'ESCAPE': '$'}
  >>> pid = "PID|1||566-554-3423^^^GHH^MR||EVERYMAN^ADAM^A|||M|||2222 HOME STREET^^ANN ARBOR^MI^^USA||555-555-2004~444-333-222|||M\r"
  >>> segment = parse_segment(pid)
  >>> print(segment.to_er7(encoding_chars=custom_chars))

For ``Message`` objects, you can get the string ready to be sent using mllp, by calling :meth:`hl7apy.Element.to_mllp` method:

.. code-block:: python

  >>> m = Message('OML_O33')
  >>> m.to_mllp()

Datatypes
---------

Library supports both base and complex datatypes according to standard specifications.
Elements that can have a datatype are Field, Component and SubComponent, the latter supports only base datatypes.
Components and SubComponents name are defined as follows:

  * If the name is specified it must be <complex_datatype>_<position>
  * If the name is not specified it is the name of the datatype

.. code-block:: python

  >>> f = Field('PID_1')
  >>> f.datatype # it prints 'SI'
  >>> f = Field('PID_3')
  >>> f.datatype # it prints 'CX'
  >>> c = Component('CX_10') # the component is part of a complex datatype (CX)
  >>> s = SubComponent('CWE_1') # the subcomponent is part of a complex datatype (CWE)
  >>> c = Component(datatype='CWE') # the name is 'CWE'
  >>> s = SubComponent(datatype='ST') # the name is 'ST'

The library implements base datatypes classes and validation of their values

.. code-block:: python

  >>> from hl7apy.v2_4 import ST, NM, DTM #...the list of datatypes depends on the version

  >>> s = ST('some information')
  >>> s = ST(1000*'a') # it raises an exceptions since the given value exceeds the max length for an ST datatype
  >>> n = NM(111)
  >>> n = NM(11111) # it raises an exceptions since the given value exceeds the max length for a NM datatype
  >>> d = DTM('20131010')
  >>> d = DTM('10102013') # it raises an exceptions since the given value is not a valid DTM value

In the case of SubComponent the :attr:`value` can also be an instance of a base datatype

.. code-block:: python

  >>> s = SubComponent(datatype="FT")
  >>> s.value = FT('some information')

The ``WD`` datatype is not an actual datatype. It is used to identify Fields Withdrawn by the specification. If this
field is present, STRICT validation fails.

Elements manipulation
---------------------

You can visit an element's children in different ways:

    * by name
    * by long name (as defined in HL7 official structures)
    * by position

.. code-block:: python

    >>> s = Segment('PID')
    >>> s.pid_5 # by name
    >>> s.patient_name # by long name
    >>> s.pid_5.pid_5_1 # by position

Please note that child traversal is case insensitive (e.g. s.PATIENT_NAME is the same as s.patient_name)

By default the returned child is always the first, because usually an element have only one instance for a child.
If you want to access to another child you have to specify the index

.. code-block:: python

    >>> s.pid_13 # it is the same as s.pid_13[0]
    >>> s.pid_13[1] # it returns the second instance of pid_13 (if it exists)

If you want to access to a Field's children you can also use the following syntax:

.. code-block:: python

    >>> org_5 = Field('org_5') # the datatype is CX
    >>> org_5.org_5_10 # it returns the tenth component of the field. It is the same as org_5.cx_10
    >>> org_5.org_5_10_3 # it returns the third subcomponent of the tenth component of the field. It is the same as org_5.cx_10.cwe_3

    >>> org_4 = Field('ORG_4') # the datatype is ID
    >>> org_4.org_4_1_1 # it raises an exception since org_4_1 is a base_datatype and doesn't have a subcomponent

If you want to iterate over an element's children

.. code-block:: python

    >>> m = Message()
    >>> for child in m.children:
    >>>     # do something useful with child

You can also iterate over all the repetitions of a given child

.. code-block:: python

    >>> m = Message('OML_O33')
    >>> for spm in m.spm: # in this case returns all the children named spm, not just the first one
    >>>     # do something useful with spm

You can delete a child from an elements

.. code-block:: python

    >>> m = Message('OML_O33')
    >>> del m.MSA # it deletes the first msa
    >>> del m.spm[1].spm_1 # it deletes the spm_1 field of the second spm segment

During children traversal if you try to access to an element which has not been created yet, it returns an empty list (if the child is valid)

.. code-block:: python

    >>> f = Field('PID_3')
    >>> f.cx_10 # it returns []
    >>> f.cx_30 # it raises an exception since cx_30 does not exist
    >>> f.cx_10 = Component('CX_10')
    >>> f.cx_10 # it returns [<Component CX_10>]

Version 2.7
-----------

Version 2.7 introduced the new delimiter # in MSH.2 which is optional. By default, when a version 2.7 (or newer) Message
 is created HL7apy includes the delimiter.

.. code-block:: python

    >>> m = Message('ADT_A01', version='2.7')
    >>> print(m.to_er7())
    'MSH|^~\\&#|||||20181024144452|||||2.7'

If the delimiter is not wanted it is possible to include the encoding chars without it

.. code-block:: python

    >>> from hl7apy import DEFAULT_ENCODING_CHARS
    >>> m = Message('ADT_A01', version='2.7', encoding_chars=DEFAULT_ENCODING_CHARS)
    >>> print(m.to_er7())
    'MSH|^~\\&|||||20181024144452|||||2.7'

When a 2.7 message is parsed, the delimiter is included if present in the original message

.. code-block:: python

  >>> hl7_1 = "MSH|^~\&#|GHH_ADT||||20080115153000||ADT^A01^ADT_A01|0123456789|P|2.7||||AL\r"
  >>> hl7_2 = "MSH|^~\&|GHH_ADT||||20080115153000||ADT^A01^ADT_A01|0123456789|P|2.7||||AL\r"
  >>> m1 = parse_message(hl7_1)
  >>> m1.to_er7()
  'MSH|^~\\&#|GHH_ADT||||20080115153000||ADT^A01^ADT_A01|0123456789|P|2.7||||AL'
  >>> m2 = parse_message(hl7_2)
  'MSH|^~\\&|GHH_ADT||||20080115153000||ADT^A01^ADT_A01|0123456789|P|2.7||||AL'


Message Profiles
----------------

It is possible to create or parse a message using message profiles instead of the standard HL7 structures.

To use a message profile, first you need to create a file that HL7apy can interpret. The file must be created using
the utility script ``hl7apy_profile_parser`` which needs the XML static definition of the profile as input.

The command below will create the file for ``message_profile.xml``

.. code-block:: bash

    python hl7apy_profile_parser message_profile.xml -o $HOME/message_profile

To create messages according to a message profile, it is necessary to load the corresponding file and pass it when
instantiating of parsing a :class:`Message <hl7apy.core.Message>`

.. code-block:: python

    >>> from hl7apy import load_message_profile
    >>> mp = load_message_profile('$HOME/message_profile')
    >>> m1 = Message('RSP_K21', reference=mp)
    >>> m2 = parse_message(er7_str, message_profile=mp)

Now the children will be created using the profile specification

.. important::

    The message profile can be specified just for the message and not for other elements. The structures of the children
    will be kept internally by the :class:`Message <hl7apy.core.Message>`.
    This means that when populating the message, in case of message profile, in order to guarantee that the correct
    children references will be used, it is necessary to create each child using element's traversal or the specific
    :class:`Element <hl7apy.core.Element>`'s methods (``add_group``, ``add_segment``, ecc) instead of the ``add()``
    method.

    For example, let's consider a message profile that specifies the datatype of the PID.3 to be CWE (the official
    one is CX).

    .. code-block:: python

        >>> mp = load_message_profile('$HOME/message_profile')
        >>> m = Message('RSP_K21', reference=mp)
        >>> m.pid.pid_3.cwe_1 = 'aaa'  # populate the first occurrence of pid_3.
        >>> pid_3 = m.pid.add_field('PID_3')  # create a second occurrence
        >>> pid_3.cwe_1 = 'bbb'

    In this example, since we are using traversal and ``add_field()`` method, the library will use the PID.3 structure
    specified in the message profile.
    If we create the children separately the library will use the official HL7 structures.

    .. code-block:: python

        >>> m = Message('RSP_K21', reference=mp)
        >>> pid_3 = Field('PID_3')
        >>> pid_3.cwe_1  #  this will raise an error, since the official datatype is 'CX'

.. important::

    From version `1.3.0` the structure of message profiles has changed and the previous versions structures are not
    supported anymore. To use the new structure just recreate it with the `hl7apy_profile_parser`

Validation
----------

The library supports 2 levels of validation: ``STRICT`` and ``TOLERANT``.

In ``STRICT`` mode, the elements should completely adhere to the structures defined by HL7. In particular, the library checks:
    * children name (e.g. a segment is not a valid child of a message according to the message's structure)
    * children cardinality (e.g. a segment is mandatory and it is missing in the message)
    * value constraints (e.g. a field of datatype ST that exceeds 200 chars)

Moreover, when using ``STRICT`` validation it is not possible to instantiate an unknown element - instantiating a ``Message``,
``Group``, ``Field``, ``Component`` with ``name=None`` is not allowed.

The following examples will raise an exception in case of ``STRICT`` validation:

.. code-block:: python

  >>> from hl7apy.core import Message
  >>> from hl7apy.consts import VALIDATION_LEVEL

  >>> m = Message("ADT_A01", validation_level=VALIDATION_LEVEL.STRICT) # note that the MSH segment is automatically created when instantiating a Message
  >>> m.add_segment('MSH') # a Message cannot have more than 1 MSH segment
  Traceback (most recent call last):
  ...
  MaxChildLimitReached: Cannot add <Segment MSH>: max limit (1) reached for <Message ADT_A01>

  >>> m.msh.pid_1 = Field('PID_1')
  Traceback (most recent call last):
  ...
  ChildNotValid: <Field PID_1 (SET_ID_PID) of type SI> is not a valid child for <Segment MSH>

  >>> m.msh.msh_7 = 'abcde' # its value should be a valid DTM value (e.g. 20130101)
  Traceback (most recent call last):
  ...
  ValueError: abcde is not an HL7 valid date value

In ``TOLERANT`` mode, the library does not perform the checks listed above, but you can still verify if an
element created with ``TOLERANT`` validation is compliant to the standard by calling the
:func:`hl7apy.core.Element.validate` method:

.. code-block:: python

  >>> from hl7apy.core import Message

  >>> m = Message("ADT_A01")
  >>> m.validate()

When a message is created using a message profile, the validation will be performed using it as reference.

The validate method can also save a report file with all the errors and warnings occurred during validation.
You just need to specify the file path as input

.. code-block:: python

    >>> m.validate(report_file='report')

Z Elements
----------

The library supports the use of Z Elements which are Z messages, Z segments and Z fields

A Z Message can be created using a name starting with Z: both parts of the trigger event must start with a Z

.. code-block:: python

  >>> m = Message('ZBE_Z01') # This is allowed
  >>> m = Message('ZBEZ01') # This is not allowed
  >>> m = Message('ZBE_A01') # This is not allowed

You can add every kind of segment to a Z Message, both normal segment or Z segment. Also groups are allowed.

.. code-block:: python

  >>> m = Message('ZBE_Z01') # This is allowed
  >>> m.pid = 'PID|1||566-554-3423^^^GHH^MR||EVERYMAN^ADAM^A|||M|||2222 HOME STREET^^ANN ARBOR^MI^^USA||555-555-2004~444-333-222|||M\r'
  >>> m.zin = 'ZIN|aa|bb|cc'
  >>> m.add(Group('ADT_A01_INSURANCE'))

When encoding to ER7, segments and groups are encoded in the order of creation

.. code-block:: python

  >>> m = Message('ZBE_Z01') # This is allowed
  >>> m.pid = 'PID|1||566-554-3423^^^GHH^MR||EVERYMAN^ADAM^A|||M|||2222 HOME STREET^^ANN ARBOR^MI^^USA||555-555-2004~444-333-222|||M\r'
  >>> m.zin = 'ZIN|aa|bb|cc'
  >>> m.to_er7()
  'MSH|^~\\&|||||20140731143925|||||2.5\rPID|1||566-554-3423^^^GHH^MR||EVERYMAN^ADAM^A|||M|||2222 HOME STREET^^ANN ARBOR^MI^^USA||555-555-2004~444-333-222|||M\rZIN|aa|bb|cc'

A Z segment is a segment that have the name starting with a Z

.. code-block:: python

  >>> s = Segment('ZBE') # This is allowed
  >>> s = Segment('ZCEV') # This is not allowed

As other segments, you can add fields with the positional name or unknown fields, (the latter in ``TOLERANT`` only)

.. code-block:: python

  >>> s = Segments('ZIN')
  >>> s.zin_1 = 'abc'
  >>> s.add_field('zin_2')
  >>> zin_3 = Field('ZIN_3', datatype='CX')
  >>> s.add(zin_3)

Z fields are fields belonging to a Z segment. They're named with the name of the segment plus the position

.. code-block:: python

  >>> f = Field('ZIN_1')

By default a Z field's datatype is ``ST``. When the value assigned to the ``Field`` contains more than one component, its datatype is converted to ``None``

.. code-block:: python

  >>> f = Field('ZIN_1')
  >>> f.datatype # 'ST'
  >>> f.value = 'abc^def'
  >>> f.datatype # None

Validation of Z elements follow the same rules of the other elements. So for example you can't a Field of datatype None is not validated

.. code-block:: python

  >>> f = Field('ZIN_1')
  >>> f.value = 'abc^def'
  >>> f.validate() # False

MLLP Server implementation
--------------------------

HL7apy provides an implementation of MLLP server that can be found in the module :mod:`hl7apy.mllp`.
To manage different types of incoming messages, it is necessary to implement a specific handler for every kind of
message. All handlers must be passed to :class:`MLLPServer <hl7apy.mllp.MLLPServer>` in the :attr:`handlers` dictionary
(see the :class:`MLLPServer <hl7apy.mllp.MLLPServer>` documentation for details about :attr:`handlers`).

For example, let's consider a situation where we need to handle QBP^Q21^QBP_Q21 messages. We will create a class
for this kind of message, subclassing :class:`AbstractHandler <hl7apy.mllp.AbstractHandler>`.

.. code-block:: python

  >>> from hl7apy.parser import parse_message
  >>> from hl7apy.mllp import AbstractHandler
  >>>
  >>> class PDQHandler(AbstractHandler):
  >>>     def reply(self):
  >>>         msg = parse_message(self.incoming_message)
  >>>         # do something with the message
  >>>
  >>>         res = Message('RSP_K21')
  >>>         # populate the message
  >>>         return res.to_mllp()

Then we instantiate the server with the correct :attr:`handlers`.

.. code-block:: python

  >>> from hl7apy.mllp import MLLPServer

  >>> handlers = {
  >>>     'QBP^Q22^QBP_Q21': (PDQHandler,) # value is a tuple
  >>> }

  >>> server = MLLPServer('localhost', 2575, handlers)

We can also implement a handler that accepts custom arguments. In the example below, the handler is provided
with the name of the demographic database to retrieve the patients information from.

.. code-block:: python

  >>> from hl7apy.parser import parse_message
  >>> from hl7apy.mllp import AbstractHandler
  >>>
  >>> class PDQHandler(AbstractHandler):
  >>>     def __init__(self, msg, database_name):
  >>>         super(PDQHandler, self).__init__(msg)
  >>>         self.database_name = database_name
  >>>
  >>>     def reply(self):
  >>>         msg = parse_message(self.incoming_message)
  >>>         # do something with the message
  >>>         res = Message('RSP_K21')
  >>>         # populate the message
  >>>         return res.to_mllp()
  >>>
  >>> handlers = {
  >>>     'QBP^Q22^QBP_Q21': (PDQHandler, 'db_name')
  >>> }

It is also possible to implement a subclass of
:class:`AbstractErrorHandler <hl7apy.mllp.AbstractErrorHandler>` to handle exceptions that may
occur (e.g., the reception of an unsupported message). The instance of the :exc:`Exception` can be accessed through
the attribute :attr:`exc`.

.. code-block:: python

  >>> from hl7apy.mllp import UnsupportedMessageType
  >>>
  >>> class ErrorHandler(AbstractErrorHandler):
  >>>     def reply(self):
  >>>         if isinstance(self.exc, UnsupportedMessageType):
  >>>             # return your custom response for unsupported message
  >>>         else:
  >>>             # return your custom response for general errors
  >>>
  >>>
  >>> handlers = {
  >>>     'QBP^Q22^QBP_Q21': (PDQHandler, 'demographic_db'),
  >>>     'ERR': (ErrorHandler,)
  >>> }
