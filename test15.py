#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


x = eval("5+5")
print(x)
exec("for i in range(8):print(i,end='')")

print()
print(bool(0))
print(bool(5))

class C:
    name = "robs"
    sex = "fm"
    @staticmethod
    def ins():
        print("method")

    @classmethod
    def dos(cls):
        print("cls : dos")
        print(cls.sex)
        print(cls.name)
        cls.ins()


print("======================================")
c = C()
c.ins()
C.ins()

C.dos()

result = sum([1,3,5,25,43,6])
result = sum((3,5,23,54,64))
print(result)

def is_old(n):
    return n%2 == 1

print()
nlist = filter(is_old,[1,2,3,5,6,7,8,9,11,12,13,14,16])
for x in nlist:
    print(x,end=' | ')

print()
print(vars())

