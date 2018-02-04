#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from urllib import request
resp = request.urlopen("https://qiong.bi/")
content = resp.read().decode("utf-8")
print(content)