#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

class Animal:
    name = "Animal"
    age = 20
    addr = "sichuan chengdu"
    __weight = 50
    _heihgt = 120

    def __init__(self,name,age,addr):
        print("__initxxx__")
        self.name = name
        self.age = age
        self.addr = addr
    def __new__(cls, *args, **kwargs):
        print(cls)

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getAddr(self):
        return self.addr

    def setName(self,name):
        self.name = name

    def printClass(self):
        print(self)
        print(self.__class__)

    def getWeight(self):
        return self.__weight

dog = Animal("zm", 30, "china")
# dog.printClass()

# print(dog.getWeight())
# print(dog._Animal__weight)
# print(dog._heihgt)


class pig(Animal):
    def __new__(cls,name,age,addr):
        print("__new__")
        print(name)
        print(age)
        print(addr)

    def __init__(self,name,age,addr):
        print("__init__")
        print("Name:"+name)
        print("age:"+age)
        print("addr:"+addr)


dog = Animal("animal",20,"chinasss")
pig1 = pig("pig",10,"sichuan")
# print(pig1)