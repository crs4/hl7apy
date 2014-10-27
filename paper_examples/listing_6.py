import hl7apy
from hl7apy.core import Message

mp = hl7apy.load_message_profile("./pdq")
m = Message("RSP_K21", reference=mp["RSP_K21"])