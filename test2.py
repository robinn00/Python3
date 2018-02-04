#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
strs = "china"
x = ".".join(strs)
print(x)





a1 = 20
b1 = 50
print(a1 and b1)

def getinfo(arg, *args, **kwargs):
    print(arg)
    print(args)
    print(kwargs)


dicts = {"aa","bb","cc","dd","ff","mm","bb","dd","ff"}
sets = set(dicts)

print(sets)

tuples = ("aa","bb","cc","dd","cc","mm","aa")
x = set(tuples)
print(x)

if "xxx" in dicts:
    print("True")
else:
    print("False")


print(sets - x)
print(sets | x)
print(sets & x)
print(sets ^ x)

dicts = {"name":"robs","sex":"female","age":"20","addr":"sichuan"}
print(dicts)

print(dicts.keys())
print(dicts.values())

for line in dicts.keys():
    print(line)


mm = {x: x+y for x,y in dicts.items()}
print(mm)

dicts.clear()
print(dicts)

print("=======================")
getinfo(12)
getinfo(12,23,25,56,89,a=2,b="ss")

def gettuples(a,b,c):
    a,b,c = a+1,b+3,c+5
    return (a,b,c)

x = gettuples(2,4,8)
print(x)

mx = [line*line for line in gettuples(2,4,8) if line%3 == 0]
print(mx)
