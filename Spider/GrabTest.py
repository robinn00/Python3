#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from psd_tools import PSDImage
psd = PSDImage.load("../test.psd")
print(psd.header)
for line in psd.layers:
    if line.text_data:
        print(line)
    else:
        # x = line.as_PIL()
        # print(x)
        pass

merged_image = psd.as_PIL()
merged_image.save("d.jpg")

# layer = psd.layers[2]
# txt = layer.text_data.text
# print(txt)


# layer1 = psd.layers[0]
#
# print(layer1.as_PIL())