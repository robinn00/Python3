#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


L = ('Google', 'Taobao', 'Runoob')
num = (1)
print(num)
num = (1,)
print(num)

num = (10,23,56,89,1)
print(num)
strx = ["Google","Runoob","Taobao","Baidu"]
print(max(num))
print(min(num))
print(len(num))
print(tuple(strx))


setobj = {"Google","Runoob","Taobao","Baidu","Doms","Taobao"}
print(setobj)

dicts = {"g":"Google","r":"Runoob","t":"Taobao","b":"Baidu"}
print(dicts)
dicts["r"] = "Ros"
print(dicts)

del dicts["g"]
print(dicts)
dicts["dos"]="dox"
dicts[("a","b")] = "msinfos"
print(dicts)

print(len(dicts))
print(str(dicts))
print(type(dicts) == dict)


print(dicts)
x = dicts.popitem()

print(x)

print(dicts.keys())
print(dicts.values())

dicts3 = {"a":"aa","b":"bb"}
dicts.update(dicts3)
print(dicts)

dicts.setdefault("key")

print(dicts)

print('key' in dicts)

for k,w in dicts.items():
    print(k,w)

print(dicts.get('b'))

xml = dicts.copy()
print(xml)

dicts.clear()
print(dicts)


x = {}
y = x.fromkeys({"A":"aaa","B":"bbb"})
print(y)



