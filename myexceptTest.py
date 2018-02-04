#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

class myexcept(Exception):
    def __init__(self,values):
        self.values = values
    def __str__(self):
        return repr(self.values)
try:
    raise myexcept(2*2)
except myexcept as me:
    print(me.values)