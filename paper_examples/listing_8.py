from hl7apy.core import Segment, Field

segment = Segment("PID")
unkn_field = Field()
segment.add(unkn_field)