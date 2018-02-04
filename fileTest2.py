#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import os
import os.path

ls = []
paths = r"C:\Users\admin\Desktop\demos\Python3"

def getPyfilelist(path,ls):
    try:
        if os.path.isdir(path):
            for line in os.listdir(path):
                files = os.path.join(paths,line)
                if os.path.isdir(files)==True:
                    getPyfilelist(files,ls)
                else:
                    if files[files.rfind(".")+1:].upper() == "PY":
                        ls.append(files)
    except RecursionError:
        print("error")

getPyfilelist(paths,ls)
for line in ls:
    print(line)