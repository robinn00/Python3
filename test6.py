#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

def area(w,h):
    return w*h

result = area(10,30)
print(result)

w = 15
h = 56
print("width:",w,"height:",h," result:",area(w,h))

b = 10

def setNum(a):
    a = 6
print(b)
setNum(b)
print(b)

def changeList(mylist):
    mylist.append([1,2,3,56])
    print("修改后的值"+str(mylist))

mxlist = [20,56,23,45,78]
print(mxlist)
changeList(mxlist)
print(mxlist)

def getName(name):
    print(name)

getName("ROBINN")
getName(name="dos")

def getName(age,name):
    print("age:",age,"name:",name)
getName(20,"robs")
getName(name="dosx",age=56)

def getName(age=20,name='mssoft'):
    print(age,name)

getName(name="doms")



def setInfo(name,*infos,**kwinfos):
    print(name)
    print(infos)
    print(kwinfos)

setInfo("预约","yishi","hloj","154",key="dom",age=20)

setInfo("dom")
setInfo("domx", "dms", "mos", "dox", "doms")

num = lambda x,y:x+y
print(num(10,20))


a = 10
def test():
    global  a
    a = a + 1
    print(a)
test()

print("=====================")
result = 20
def sum(a,b):
    # global result
    result = a+b
    print(result)
    return result

print(result)
print(sum(10,50))
print(result)
print("=====================")


x = 10
def outer():
    y=20
    def inter():
        nonlocal y
        y=50
        print(y)
    inter()
    print(y)

outer()

print("=================")
xm = int(3.23)


gen = (i*2 for i in range(5))
print(next(gen))
print(next(gen))




print("==============================")

ls = [
    [1,3,5],
    [2,4,6],
    [7,8,9],
    [11,22,33]
]


for i in range(3):
    lsx = []
    for row in ls:
        lsx += [row[i]]
    print(lsx)


msx = [[row[x] for row in ls] for x in range(3)]
print(msx)


questions=['name','quest','favorite color']
answers=['qinshihuang','the holy','blue']
for q,a in zip(questions,answers):
    print('what is your %s? it is %s' %(q,a))
    print('what is your {0}? it is {1}'.format(q,a))