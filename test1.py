#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


ax = (1,3,5)
ay = ("bb","cc","mm")

print(ax*2)
print(ay+ax*2)
print("==============================")

list_1 = ["a","b","c","d","e"]
list_2 = [1,2,4]

print(list_1+list_2)
print(list_2 * 2)
print(list_2[0]==1)

print("==============================")



strx = "china"
print(strx[0:5])
lenx = -len(strx)+1
print(strx[-len(strx):])

print(strx*3)

print(10/30)
print(10//30)

a=b=c=1
print(a,b,c)

a,bb,c=10,36,"string"
print(c)

del a
print(bb)


def x():
    a, b, cnt = 0, 1, 0
    while True:
        print(a,end=' | ')
        a,b = b,a+b
        if cnt > 20:
            break
        cnt += 1

x()

a=1
b=2
print(a)
print(b)
print(a,end=' | ')
print(b,end=" | ")

import sys;x="doit";sys.stdout.write(x);

print("\n===================")
for arg in sys.argv:
    print(arg)

print("\n===================")
for path in sys.path:
    print(path)

print("\n===================")
print(len(sys.argv))
print(sys.argv[0])
print("\n===================")


print(str(sys.argv))


print("==================================")
a=11
print(isinstance(a,int))
ab = ["a","b","c"]
print(type(a) == int)
print(type(ab)==list)

class A():
    pass

class B(A):
    pass
x = A()
y = B()
print(type(A))
print(type(x))
print(isinstance(x,A))

print(type(B)==type)
print(type(y) == B)
print(isinstance(y,B))
print(isinstance(y,A))
print(type(y) == A)

print("==================================")
