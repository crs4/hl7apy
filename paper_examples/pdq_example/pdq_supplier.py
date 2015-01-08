from hl7apy.v2_5 import DTM
from hl7apy.utils import check_date
from hl7apy.mllp import AbstractTransactionHandler
from hl7apy.parser import parse_message
from hl7apy.core import Message
from dao import DAO
from profiles import PDQ_REQ_MP, PDQ_RES_MP
from parameters import PDQ_FIELD_NAMES

import datetime
import uuid

class PDQSupplier(AbstractTransactionHandler):

  REQ_MP = PDQ_REQ_MP
  RES_MP = PDQ_RES_MP
  FIELD_NAMES = PDQ_FIELD_NAMES

  def __init__(self, message):
    self.dao = DAO()
    msg = parse_message(message, message_profile=self.REQ_MP)
    super(PDQSupplier, self).__init__(msg)

  def _create_res(self, ack_code, query_ack_code, patients):
    res = Message('RSP_K21', reference=self.RES_MP)
    r, q = res.msh, self.msg.msh
    r.msh_5, r.msh_6 = q.msh_3, q.msh_4
    res.msh.msh_5 = self.msg.msh.msh_3
    res.msh.msh_6 = self.msg.msh.msh_4
    r.msh_7.ts_1 = DTM(datetime.datetime.now())
    r.msh_9 = 'RSP^K22^RSP_K21'
    r.msh_10 = uuid.uuid4().hex

    # MSA creation
    r, q = res.msa, self.msg.msh
    r.msa_1, r.msa_2 = ack_code, q.msh_10.msh_10_1

    # QAK creation
    r, q = res.qak, self.msg.qpd
    r.qak_1 = q.qpd_2
    r.qak_2 = 'OK' if len(patients) > 0 else 'NF'
    r.qak_4 = str(len(patients))

    # QPD creation
    res.qpd = self.msg.qpd

    # RSP_K21_QUERY_RESPONSE creation
    g = res.add_group('rsp_k21_query_response')
    for i, p in enumerate(patients):
      g.add_segment('PID')
      g.pid[i].pid_1 = str(i)
      g.pid[i].pid_5 = "%s^%s" % (p[0], p[1])
    return res

  def _create_err(self, code, desc):
    res = self._create_res('AR', 'AR', [])
    res.ERR.ERR_1, res.ERR.ERR_2 = code, desc
    return res

  def reply(self):
    params = dict((self.FIELD_NAMES[q.qip_1.value], q.qip_2.value)
                   for q in self.msg.qpd.qpd_3
                   if q.qip_1.value in self.FIELD_NAMES)
    
    if ('' in params.values() or     
       (params.has_key('DOB') and   
        not check_date(params.get('DOB')))):
      res = self._create_err("100", "Invalid params.").to_mllp()
      return res
    else:
      p = self.dao.get_data(params)
      if len(p)>0:
        return self._create_res('AA', 'OK', p).to_mllp()
      else:
        return self._create_res('AA', 'NF', p).to_mllp()