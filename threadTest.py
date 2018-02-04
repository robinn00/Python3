#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import time
import _thread

def printTime(threadname,delay):
    n = 0
    while n < 5:
        time.sleep(delay)
        n += 1
        print("{0},{1}".format(threadname,time.ctime(time.time())))


try:
    _thread.start_new_thread(printTime,("thr_1",2,))
    _thread.start_new_thread(printTime,("thr_2",4,))
except:
    print("error:..")

while True:
    pass