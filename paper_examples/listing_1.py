from hl7apy.core import Message

adt_a01 = Message("ADT_A01")
adt_a01.msh.sending_application.hd_1 =  "Sending App"
adt_a01.msh.sequence_number = "123"

adt_a01.pid.patient_name = "Doe^John"
adt_a01.pid.patient_identifier_list = "123456"