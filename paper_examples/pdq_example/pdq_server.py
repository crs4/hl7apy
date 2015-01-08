from hl7apy.mllp import MLLPServer
from pdq_supplier import PDQSupplier

srvr = MLLPServer('localhost', 6790, {'QBP_Q21': PDQSupplier})
srvr.serve_forever()