from hl7apy.core import Message
from hl7apy.parser import parse_field

custom_chars = {
  "FIELD": "!",
  "COMPONENT": "@",
  "SUBCOMPONENT": "%",
  "REPETITION": "~",
  "ESCAPE": "$"
}

msh_9 = "ADT^A01^ADT_A01"
field = parse_field(msh_9)

# it will use default encoding chars
print field.to_er7()

# it will use custom encoding chars
# defined above
print field.to_er7(encoding_chars=custom_chars)

m = Message('RSP_K21')
print repr(m.to_mllp())