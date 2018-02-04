#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

print(type(1))
print(type("roob"))
print(type(str))
print(type(int))
print(type(list))

foo = type("Foo",(),{'bar':True})
print(foo)

names = "x"
print(type(names))

print(names.__class__.__class__)