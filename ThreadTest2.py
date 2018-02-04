#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import threading
import time

threadLock = threading.Lock()
threads = []

class MyThread(threading.Thread):
    def __init__(self,threadId,threadname,cnt):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.threadname = threadname
        self.cnt = cnt

    def run(self):
        print("开始线程"+self.threadname)
        threadLock.acquire()
        print_Time(self.threadId,self.threadname,self.cnt)
        threadLock.release()
        print("结束线程"+self.threadname)

def print_Time(threadId,threadname,cnt):
    n = 0
    while n < 5:
        time.sleep(cnt)
        n += 1
        print("{0},{1},{2}".format(threadId,threadname,time.ctime(time.time())))

mythread_1 = MyThread("id_001","threadname_001",2)
mythread_2 = MyThread("id_002","threadname_002",5)
mythread_1.start()
mythread_2.start()

threads.append(mythread_1)
threads.append(mythread_2)
for i in threads:
    i.join()

# mythread_1.join()
# mythread_2.join()
print("sys.exit()退出主线程")