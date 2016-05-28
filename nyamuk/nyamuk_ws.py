"""
Nyamuk websocket networking module.
Copyright(c) 2016 Guillaume Bour
"""
import websocket

import nyamuk_const as NC

SUBPROTOCOLS = {
    3: ['mqttv3.1'],
    4: ['mqtt']
}

def connect((server, port), use_ssl, ssl_opts, mqtt_version):
    ws = websocket.WebSocket()
    ws.settimeout(1)

    try:
        ws.connect('ws://{0}:{1}'.format(server, port), subprotocols=SUBPROTOCOLS.get(mqtt_version))
    except websocket.WebSocketBadStatusException as e:
        return (NC.ERR_CONN_REFUSED, "return code is {0}".format(e.status_code))

    ws._NYAMUK_READ_CACHE = bytearray()
    return (NC.ERR_SUCCESS, ws)
   
def read(ws, count):
    """Read from websocket and return it's byte array representation.
    count = number of bytes to read

    NOTE: as websocket is reading entire frame, and nyamuk engine is waiting a precise number of bytes,
          we cache remaining bytes in _NYAMUK_READ_CACHE array, and return it on next turn
    """
    if count > len(ws._NYAMUK_READ_CACHE):
        data = ws.recv()
        ws._NYAMUK_READ_CACHE.extend(data)

    data                  = ws._NYAMUK_READ_CACHE[0:count]
    ws._NYAMUK_READ_CACHE = ws._NYAMUK_READ_CACHE[count:]

    return data, 0, ""

def write(ws, payload):
    """Write payload to socket."""
    length = ws.send_binary(payload)

    return length, None
