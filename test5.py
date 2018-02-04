#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
import sys

def getNum():
    cnt = 0
    a,b = 0,1
    while True:
        print(b,end=",")
        a,b = b,a+b
        cnt += 1
        if cnt>100:
            break

getNum()

print("")
a,b,c=20,40,89
print(a,b,c,sep="|")
print(a,b,c,end="")
print("")

list1 = ["1","5","b","s","20"]
x = iter(list1)



print("=====================")
def getN(n):
    a,b,cnt = 0,1,0
    while True:
        if cnt>n:
            break
        yield b
        a,b = b,a+b
        cnt += 1

x = getN(10)
while True:
    try:
        print(next(x),end=' | ')
    except StopIteration:
        sys.exit()