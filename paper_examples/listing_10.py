from hl7apy.core import Segment

s = Segment("PID")
s.value = "PID|||654321^^^123456~abcdef^^^fedcba||Family^Name^^^^^"

# it is the same as s.pid_13[0]
print s.pid_3.to_er7()

# if it exists, it returns the second
# instance of pid_13
print s.pid_3[1].to_er7()