from hl7apy.core import Message, Segment, Field

s = Segment("PID")
s.value = "PID|||654321^^^123456||Family^Name^^^^^"

# by name, it refers to a Field instance
print s.pid_5

# by description, it refers to a Field instance
print s.patient_name

# by position, it refers to a Component instance
print s.pid_5.pid_5_1

message = Message("RSP_K21")

# by description, recursively on the message
# children
print message.msh.date_time_of_message.time

# iterates over PID-5 children of the PID
# segment
for name in s.pid_5:
	print name

# iterates over all the fields of the PID
# segment
for child in s.children:
	print child

# its datatype is CX
org_5 = Field("org_5")
org_5.value = "^^^^^^^^^AG&&DEP"
# it returns the tenth component of the field,
# it is the same as org_5.cx_10
print org_5.org_5_10

# it returns the third subcomponent of the tenth
# component of the field, it is the same as
# org_5.cx_10.cwe_3
print org_5.org_5_10_3