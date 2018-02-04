#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import socket
import sys

serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
hostname = socket.gethostname()
port = 9999
serversocket.bind((hostname,port))
serversocket.listen(10)

while True:
    socketclient,addr = serversocket.accept()
    print("连接地址：{0}".format(addr))
    msg = "测试教程"+"\r\n"
    socketclient.send(msg.encode("utf-8"))
    socketclient.close()