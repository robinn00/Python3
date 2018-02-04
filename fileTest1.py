#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

filename = "runoob.txt"
start = filename.rfind(".")+1
print(filename[start:])


def getFilename(file):
    return file[file.rfind(".")+1:]

print(getFilename("no.jpeg"))

