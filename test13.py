#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from datetime import date
import os
import glob

now = date.today()
print(now)
birthday = date(2018,3,20)
print(birthday)

dd = birthday-now
print(dd.days)


import zlib
s = b"this is a day"
t = zlib.compress(s)
print(len(t))
m = zlib.decompress(t)
print(str(m))




# for line in dir(os):
#     print(line)

# help(os)

lists = ["filename:"+x for x in glob.glob("*.py")]
for line in lists:
    print(line)

# x = glob.glob("*.py")
# print(x)

import sys
print(sys.argv)

import re
x = re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
print(x)

y = re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
print(y)

import random

xm = random.choice(("x","y","z"))
print(xm)

xy = random.sample(range(12),10)
print(xy)

xw = random.random()
print(xw)
print(int(round(xw)))

print(random.randrange(6))



