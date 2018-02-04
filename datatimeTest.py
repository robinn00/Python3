#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import time

# x = time.localtime(time.time())
# print(x)
#
# y = time.asctime(x)
# print(y)

# import calendar
#
# x = calendar.month(2020,2)
# print(x)


class A:
    bar = 1

a = A()
print(a.bar)

setattr(a,"bar","robin")
print(a.bar)

x = getattr(a,"bar")
print(x)

y = abs(20)
print(y)

x = min(10,20,56,89)
print(x)

sy = (10,-1,-5,23,89,56)
print(min(sy))


tuples = (5,23,56,-1,-8)
print(tuples)

print(all(tuples))

print(dir())

for line in dir():
    print(line)

xx = slice(8)

ox = range(10)

for xyz in ox[xx]:
    print(xyz,end=' ')
print()
print(ox[xx])

xm = any([0, '', False])
print(xm)


xu = divmod(5,2)
print(xu)

for m in xu:
    print(m)

print(object())

list_1 = [12,23,56,11,20,3,1]
print(list_1)

list_1.sort()
print(list_1)


tuple_1 = (12,56,23,98,2,45,7,1,56)
print(tuple_1)
tuple_1 = sorted(tuple_1)
print(tuple_1)

x = sorted([5, 2, 3, 1, 4])
print(x)

strx = "runoob"
print(ascii(strx))

print(repr(strx))
print()


print("======================================")
lists_2 = ["spring","java","mooven","py"]
xyzy = enumerate(lists_2)
for i in xyzy:
    print(i[0],i[1])

print("======================================")


print(list(enumerate(lists_2)))

class B:
    @staticmethod
    def prs():
        print("prs")

B.prs()

b = B()
b.prs()
