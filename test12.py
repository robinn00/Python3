#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

for x in range(1, 11):
    print( repr(x).rjust(2), repr(x*x).rjust(3), end=' ' )
    print( repr(x*x*x).rjust(4) )

print()
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

print("12".zfill(4))
print("300".zfill(5))
print("-3.12".zfill(7))
print("3.14159265359".zfill(5))

print("{0}hello{1}".format("ni","jao"))
print("{} dox {} hello".format("wx","mo"))
print("{name} hello world{addr}".format(name="robs",addr="sichuang"))
print("{0} hx {1} dom {other} kail".format("doms","mols",other="word"))


import math

print("常量pi值近似为:{}".format(math.pi))
print("常量pi值近似为:{!r}".format(math.pi))

print("{0:.3f}".format(math.pi))

table={"Google":1,"Runoob":2,"Taobao":3}

for key,val in table.items():
    print("{0:10}==>{1:10d}".format(key,val))

print("===========================================")
print("Google:{0[Google]:d};Runoob:{0[Runoob]:d};Taobao:{0[Taobao]:d}".format(table))


print("Google:{Google:d};Runoob:{Runoob:d};Taobao:{Taobao:d}".format(**table))

print("常量pi值近似为:%5.3f" % math.pi)

strs = input("input:")
print(strs)

