"""
Element instantiation example:
"""

from hl7apy.core import Message, Segment, SubComponent
from hl7apy.v2_5 import get_base_datatypes
FT = get_base_datatypes()['FT']

adt_a01 = Message("ADT_A01", version="2.5")
ins = adt_a01.add_group("ADT_A01_INSURANCE")

pid = Segment("PID")

s = SubComponent(datatype="FT")
s.value = FT("some information")