#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests
import json

url = "http://fanyi.baidu.com/v2transapi"
headers = {
    "Cookie":"BIDUPSID=159708445DAB314017B6627D71A08917; PSTM=1517187915; BAIDUID=BA00E39ABDF399D637A0E71D69438350:FG=1; MCITY=-75%3A; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; locale=zh; PSINO=3; H_PS_PSSID=25640_1456_21119; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1517212963,1517213095,1517213125; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1517218141; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
    "X-Requested-With":"XMLHttpRequest"
}
data = {
    "from":"en",
    "to":"zh",
    "query":"China",
    "transtype":"realtime",
    "simple_means_flag":"3",
    "sign":"585660.789645",
    "token":"295e6c3dbaf0d712ee9900a1da95920e"
}

content = requests.post(url,data=data,headers=headers).content
content = str(content)
content = content[2:]
content = "\'"+content[:len(content)-1]+"\'"

print(content)
with open("x.txt", "w", encoding='utf-8') as f:
    f.write(content)