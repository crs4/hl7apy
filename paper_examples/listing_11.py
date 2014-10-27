from hl7apy.core import Message, SubComponent
import hl7apy.parser
from hl7apy.v2_5 import get_base_datatypes
IS = get_base_datatypes()['IS']

m = Message("ADT_A01", version="2.5")

# base datatype value (string)
m.msh.msh_3 = "GHH_ADT"

# it will create to an instance of
# DTM base datatype
m.msh.msh_7 = "20080115153000"

# ER7 representation, MSH_9 is a complex
# datatype of 3 components
m.msh.msh_9 = "ADT^A01^ADT_A01"

# copy from another element
m.evn.evn_2 = m.msh.msh_7

# parser function
m.msh.msh_9 = hl7apy.parser.\
  parse_field("ADT^A01^ADT_A01", name="MSH_9")

s = SubComponent(datatype="IS")
# base datatype instance (IS)
s.value = IS("AAA")