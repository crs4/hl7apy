from hl7apy.core import Message

m = Message('ADT_A01')

m.msh.msh_9 = "ADT^A01^ADT_A01" # parse_field
m.evn = "EVN||20080115153000||AAA" \
  "|AAA|20080114003000" # parse_segment
m.evn.evn_5.xcn_1 = "AAA" # parse_component
