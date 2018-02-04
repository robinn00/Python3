#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

def singleton(cls):
        print(cls)
        _instance = {}
        def _singleton(*args, **kargs):
                print(*args)
                if cls not in _instance:
                        _instance[cls] = cls(*args, **kargs)
                        print(_instance[cls])
                return _instance[cls]
        return _singleton

@singleton
class A(object):
        a = 1
        def __init__(self, x = 0):
                self.x = x

a1 = A(2)
a2 = A(3)

print(id(a1))
print(id(a2))
print(a1.x)
print(a2.x)