
Core classes
============

.. automodule:: hl7apy.core

.. autoclass::  Element

.. autoclass::  Message
    :members: to_er7, to_mllp, validate, add_segment, add_group, add

.. autoclass::  Group
    :members: to_er7, validate, add_segment, add_group, add

.. autoclass::  Segment
    :members: to_er7, validate, add_field, add

.. autoclass::  Field
    :members: to_er7, validate, add_component, add

.. autoclass::  Component
    :members: to_er7, validate, add_subcomponent, add

.. autoclass::  SubComponent
    :members: to_er7, validate
