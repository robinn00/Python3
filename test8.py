#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import test7

print(test7.x)
test7.fib1(10)
print()
result = test7.fib2(10)
print(result)


print("========================================================================")
x1 = test7.fib1
x1(20)
print()
y1 = test7.fib2
result = y1(20)
print(result)

for x in result:
    print(x)

print("==================================")
m = iter(result)
try:
    while True:
        print(next(m))
except StopIteration:
    pass