__author__ = 'xianbing'
# -*- coding:utf-8 -*-

try:
    f=open('blah','r')
except IOError,e:
    print('could not open file：',e)

def safe_float(obj):
    try:
        retval=float(obj)
    except ValueError:
#pass
        retval='could not convert non-number to float'
    except TypeError:
        retval='object type cannot be convered to float'
        return retval



print safe_float('bad')
print safe_float(())

try:
    float(['float() does not','like lists',2])
except TypeError,diag:
    pass
type(diag)