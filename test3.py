#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from collections import Counter

l = ["2","b","4","c","d","lm"]
print(type(l) == list)
print(l)
print(l[::2])

print(l[-2])

s1 = "I'm a good sutdent"
s2 = s1.partition("good")
s3 = s1.partition("eem")

print(s1)
print(s2)
print(s3)

print("====================")
x = Counter(s1)
print(x)
print(len(x))
for line in x:
    print(line)

print("========================")
num=10
print("16进制: %#x" % num)

print("2进制: " ,bin(num))

print("8进制: %#o" % num)


print("========================")

listx = ['Google', 'Runoob', 1997, 2000]
print(listx*2)
print(listx+listx)
print(len(listx))
print(1997 in listx)
print("=======================")
for x in listx:print(x)

x1 = [1,2,4,7]
x2 = ["a","b"]

x3 = [x1,x2]

print(x1)
print(x2)
print(x3)

print(x3[0][1])

strx = ("this","a","min")
print(list(strx))

print(max(x1))
del x1[0]
print(min(x1))

x1.append(50)
x1.append(60)
x1.append(2)
x1.append(4)
x1.append(2)
x1.append(7)

print(x1)
print(x1.count(7))

x1.extend([23,56,45])
print(x1)

print(x1.index(23))

x1.insert(0,"dos")
print(x1)

m = x1.pop()
print(m)

print(x1)

print(x1.pop(0))

x1.remove(60)

print(x1)
x1.reverse()

print(x1)
x1.sort(reverse=True)
print(x1)

mm = x1.copy()
x1.clear()

print(x1)
print(mm)

for i in range(5):
    for i in range(5):
        print(0,end='')
    print("")

mx = [[0 for i in range(5)] for i in range(5)]
print(mx)

print("==============================")
for line in range(15):
    print(line)
print("==============================")

my = [line for line in range(15)]
print(my[::2])

lm = [None]*10
print(lm)