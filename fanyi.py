#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests
from lxml import etree
from bs4 import BeautifulSoup
import sys
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
session = requests.Session()
url = "http://fanyi.baidu.com/v2transapi?from=en&to=zh&query=China&simple_means_flag=3&sign=585660.789645&token=295e6c3dbaf0d712ee9900a1da95920e"
req = session.get(url)
req.encoding = 'utf8'
with open("x.txt","w",encoding='utf-8') as f:
    f.write(str(req.content))
root = etree.HTML(req.content)

# items = root.xpath('//ol/li/div[@class="item"]')
# # word = input("请输入英文单词:\n")
# # url = "http://fanyi.baidu.com/?aldtype=16047#en/zh/"+word
# url = "http://fanyi.baidu.com/v2transapi?from=en&to=zh&query=China&simple_means_flag=3&sign=585660.789645&token=295e6c3dbaf0d712ee9900a1da95920e"
# headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
# content = requests.get(url,headers=headers)
# content.encoding='utf-8'
# bsobj = BeautifulSoup(content.text,"lxml")
# with open("x.txt","w",encoding='utf-8') as f:
#     f.write(str(content.text))
# # xm = bsobj.find_all("span")
# # print(xm)

