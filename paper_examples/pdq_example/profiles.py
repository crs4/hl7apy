from hl7apy import load_message_profile
import os

_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

PDQ_REQ_MP = load_message_profile(os.path.join(_ROOT_PATH, './pdq_req'))
PDQ_RES_MP = load_message_profile(os.path.join(_ROOT_PATH, './pdq_res'))
    


