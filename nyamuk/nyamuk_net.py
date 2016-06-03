"""
Nyamuk networking module.
Copyright(c) 2012 Iwan Budi Kusnanto
"""
import ssl
import socket
import errno

import nyamuk_const as NC

def connect(addr, use_ssl, ssl_opts, version=None):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if use_ssl:
        opts = {
            'do_handshake_on_connect': True,
            'ssl_version': ssl.PROTOCOL_TLSv1
        }
        opts.update(ssl_opts)
        #print opts, addr

        try:
            sock = ssl.wrap_socket(sock, **opts)
        except Exception, e:
            return (NC.ERR_UNKNOWN, "failed to initiate SSL connection: {0}".format(e))

    setkeepalives(sock)
    
    #self.logger.info("Connecting to server ....%s", self.server)

    """Connect to some addr."""
    try:
        sock.connect(addr)
    except ssl.SSLError as e:
        return (ssl.SSLError, e.strerror if e.strerror else e.message)
    except socket.herror as (_, msg):
        return (socket.herror, msg)
    except socket.gaierror as (_, msg):
        return (socket.gaierror, msg)
    except socket.timeout:
        return (socket.timeout, "timeout")
    except socket.error as e:
        return (socket.error, e.strerror if e.strerror else e.message)

    #set to nonblock
    sock.setblocking(0)

    return (NC.ERR_SUCCESS, sock)
    
def read(sock, count):
    """Read from socket and return it's byte array representation.
    count = number of bytes to read
    """
    data = None

    try:
        data = sock.recv(count)
    except ssl.SSLError as e:
        return data, e.errno, e.strerror if strerror else e.message
    except socket.herror as (errnum, errmsg):
        return data, errnum, errmsg
    except socket.gaierror as (errnum, errmsg):
        return data, errnum, errmsg
    except socket.timeout:
        return data, errno.ETIMEDOUT, "Connection timed out"
    except socket.error as (errnum, errmsg):
        return data, errnum, errmsg
    
    ba_data = bytearray(data)
    
    if len(ba_data) == 0:
        return ba_data, errno.ECONNRESET, "Connection closed"
    
    return ba_data, 0, ""

def write(sock, payload):
    """Write payload to socket."""
    try:
        length = sock.send(payload)
    except ssl.SSLError as e:
        return -1, (ssl.SSLError, e.strerror if strerror else e.message)
    except socket.herror as (_, msg):
        return -1, (socket.error, msg)
    except socket.gaierror as (_, msg):
        return -1, (socket.gaierror, msg)
    except socket.timeout:
        return -1, (socket.timeout, "timeout")
    except socket.error as (_, msg):
        return -1, (socket.error, msg)
    
    return length, None

def setkeepalives(sock):
    """set sock to be keepalive socket."""
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
