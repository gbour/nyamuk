"""Nyamuk event."""
import socket

import nyamuk_const as NC

#mqtt event
EV_CONNACK = NC.CMD_CONNACK
EV_PUBLISH = NC.CMD_PUBLISH
EV_SUBACK = NC.CMD_SUBACK

#non mqtt event
EV_NET_ERR = 1000

class BaseEvent:
    """Event Base Class."""
    def __init__(self, tipe):
        self.type = tipe

class EventConnack(BaseEvent):
    """CONNACK received."""
    def __init__(self, ret_code, session_present = 0):
        BaseEvent.__init__(self, NC.CMD_CONNACK)
        self.ret_code = ret_code
        # v3.1.1 only
        self.session_present = session_present

    def __str__(self):
        return "CONNACK(retcode={0}, session={1})".format(self.ret_code, self.session_present)

class EventPublish(BaseEvent):
    """PUBLISH received."""
    def __init__(self, msg):
        BaseEvent.__init__(self, NC.CMD_PUBLISH)
        self.msg = msg

    def __str__(self):
        return "PUBLISH({0})".format(self.msg)

class EventSuback(BaseEvent):
    """SUBACK received."""
    def __init__(self, mid, granted_qos):
        BaseEvent.__init__(self, NC.CMD_SUBACK)
        self.mid = mid
        self.granted_qos = granted_qos

    def __str__(self):
        return "SUBACK(id={0}, gqos={1})".format(self.mid, self.granted_qos)

class EventUnsuback(BaseEvent):
    """UNSUBACK received."""
    def __init__(self, mid):
        BaseEvent.__init__(self, NC.CMD_UNSUBACK)
        self.mid = mid

    def __str__(self):
        return "UNSUBACK(id={0})".format(self.mid)

class EventPuback(BaseEvent):
    """PUBACK received."""
    def __init__(self, mid):
        BaseEvent.__init__(self, NC.CMD_PUBACK)
        self.mid = mid

    def __str__(self):
        return "PUBACK(id={0})".format(self.mid)

class EventPubrec(BaseEvent):
    """PUBREC received."""
    def __init__(self, mid):
        BaseEvent.__init__(self, NC.CMD_PUBREC)
        self.mid = mid

    def __str__(self):
        return "PUBREC(id={0})".format(self.mid)

class EventPubrel(BaseEvent):
    """PUBREL received."""
    def __init__(self, mid):
        BaseEvent.__init__(self, NC.CMD_PUBREL)
        self.mid = mid

    def __str__(self):
        return "PUBREL(id={0})".format(self.mid)

class EventPubcomp(BaseEvent):
    """PUBCOMP received."""
    def __init__(self, mid):
        BaseEvent.__init__(self, NC.CMD_PUBCOMP)
        self.mid = mid

    def __str__(self):
        return "PUBCOMP(id={0})".format(self.mid)

class EventNeterr(BaseEvent):
    """Network error event."""
    def __init__(self, errnum, msg):
        BaseEvent.__init__(self, EV_NET_ERR)
        self.errnum = errnum
        self.msg = msg

class EventPingResp(BaseEvent):
    """PINGRESP received."""
    def __init__(self):
        BaseEvent.__init__(self, NC.CMD_PINGRESP)

    def __str__(self):
        return "PINGRESP()"

