#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

# import sys
# for line in sys.argv:
#     print(line)
#
# print()
# for p in sys.path:
#     print(p)
#

x = 1
y = 2
strs = "dom"
print()
print("|"+__name__+"|")
def fib1(n):
    a,b,c = 0,1,0
    while c<n:
        print(b,end=',')
        a,b=b,a+b
        c+=1


def fib2(n):
    result = []
    a,b,c = 0,1,0
    while c<n:
        result.append(b)
        a,b = b,a+b
        c+=1
    return result
#
# fib1(10)
# print()
# result = fib2(10)
# print(result)
