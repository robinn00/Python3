#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import json

data = {
    "addr": "sichuan chengdu",
    "name": "wulizi",
    "sex": "female",
}

# print(data)
# print(repr(data))
# print(str(data))

jsonstr = json.dumps(data)
print(jsonstr)

# with open("json.txt","w",encoding="utf-8") as f:
#     f.write(jsonstr)

# with open("json.json","w") as f:
#     json.dump(data,f)


# with open("json.json","r") as f:
#     datas= json.load(f)
#     print(datas)

jsondata = json.loads(jsonstr)
print(jsondata["name"])
print(jsondata["addr"])
print(jsondata["sex"])