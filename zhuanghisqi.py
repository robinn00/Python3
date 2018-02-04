#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

def commonfun(func):
    def yzm():
        print("yanzhengma..........")
        return func()
    return yzm

@commonfun
def getInfoA():
    print("A  infos")
    print("====================\n\n")

@commonfun
def getInfoB():
    print("B  infos")
    print("####################\n\n")

@commonfun
def getInfoC():
    print("C  infos")
    print("@@@@@@@@@@@@@@@@@@@\n\n")


getInfoA()

getInfoB()

getInfoC()


def debug(func):
    def printfinfo():
        print("xxxxxxxxxxxxxx")
        return func()
    return printfinfo

def setNum():
    print("setnuming...")

ps = debug(setNum)
ps()

s = [i for i in range(1, 10)]
print(s)

a, b = 1, 1
for i in range(1,11):
    b = a * i
    a = b

print(b)