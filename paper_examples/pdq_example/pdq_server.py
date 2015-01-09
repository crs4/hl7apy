from hl7apy.mllp import MLLPServer
from .pdq_supplier import PDQHandler

srvr = MLLPServer(host='localhost', port=6789, handlers={'QBP_Q21': PDQHandler})
srvr.serve_forever()