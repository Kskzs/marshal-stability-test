# -*- coding: utf-8 -*-
import marshal

def dumps(obj):
    return marshal.dumps(obj)

def loads(buf):
    return marshal.loads(buf)

def full_cycle(x):
    b = dumps(x)
    return loads(b)