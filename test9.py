#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from sound.filter.one import *

setNum()

# from test7 import fib2,fib1

#
# fib1(10)
# print()
# result = fib2(10)
# print(result)

from test7 import *
import test7
import os
import sys
sys.ps1 = '11111'
sys.ps2 = '22222'
print(sys.ps1)
print(sys.ps2)


fib1(25)
print()
print(__name__)

x = dir(os)
print(x)
for m in x:
    print(m)

