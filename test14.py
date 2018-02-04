#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from timeit import Timer
Timer("a,b=b,a","a=20;b=10").timeit()

def getval(num):
    return sum(num)/len(num)

import doctest
doctest.testmod()