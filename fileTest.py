#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


# f = open("text.txt","w",encoding="utf-8")
# f.write("本节中剩下的例子假设已经创建了一个称为 f 的文件对象。")
# f.close()
# print(f.closed)
#
#
# f = open("text.txt","rb")
# print(f.read().decode("utf-8"))
# f.close()
# print(f.closed)

f = open("text.txt","rb")
while True:
    x = f.readline().decode("utf-8")
    if x:
        print(x)
    else:
        break

f = open("text.txt","rb")
lists = f.readlines()
for x in lists:
    print(x.decode("utf-8"))

print("===================================")
f = open("text.txt","rb")
for line in f:
    print(line.decode("utf-8").strip("\r\n"))

import sys
print(sys.getdefaultencoding())
print("===================================")
f = open("text.txt","rb")
while True:
    try:
        print(next(f).decode("utf-8").strip("\r\n"))
    except StopIteration:
        print("StopIteration error")
        break


val = ("www.baidu.com",4)
f = open("val.txt","w")
f.write(str(val))
f.close()

with open("val.txt","rb") as f:
    print(f.read())
    print(f.tell())
    f.seek(5)
    print(f.tell())
    print(f.read(f.tell()))


from urllib import request
res = request.urlopen("http://www.baidu.com/")
content = res.read().decode("utf-8")
f = open("baidu.txt","w",encoding="utf-8")
f.write(str(content))

num = int(input("请输入数字："))
print(num*2)

