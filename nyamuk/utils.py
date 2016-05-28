#!/usr/bin/env python
# -*- coding: utf8 -*-

# encode unicode string to utf8
#
def utf8encode(unistr):
    if type(unistr) is unicode:
        return unistr.encode('utf8')

    return unistr

def MOSQ_MSB(A):
    """get most significant byte."""
    return (( A & 0xFF00) >> 8)
    
def MOSQ_LSB(A):
    """get less significant byte."""
    return (A & 0x00FF)

