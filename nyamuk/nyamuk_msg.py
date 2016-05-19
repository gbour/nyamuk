"""
Copyright(c)2012 Iwan Budi Kusnanto
"""
import time

import nyamuk_const as NC

class NyamukMsg:
    """Nyamuk message."""
    def __init__(self, topic=None, payload=None, qos=-1, retain=False):
        self.mid = 0
        self.topic = topic
        self.payload = payload
        self.payloadlen = -1 if payload is None else len(payload)
        self.qos = qos
        self.retain = retain

    def __repr__(self):
        return "id={0}, topic='{1}', qos={2}, retain={3}".format(self.mid, self.topic, self.qos, self.retain)

class NyamukMsgAll:
    
    def __init__(self):
        #next
        self.timestamp = time.time()
        self.direction = NC.DIRECTION_NONE
        self.state = NC.MS_INVALID
        self.dup = False
        self.msg = NyamukMsg()
