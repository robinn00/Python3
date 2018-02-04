#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

class Person:
    age = 200
    def __init__(self,name,sex):
        self.name = name
        self.sex = sex
    def speak(self):
        print("name={0},sex={1}".format(self.name,self.sex))

p = Person("ROB","FEMALE")
p.speak()


class Student(Person):
    addr = ''
    def __init__(self,name,sex):
        Person.__init__(self,name,sex)
        self.addr = "sichuan"
    def speak(self):
        print("student:   name={0},sex={1}".format(self.name,self.sex))

    def __getAddr(self):
        print("china== "+self.addr)
    def __str__(self):
        return "这个同学的名字叫{name},性别为{sex},住在{addr},年龄为：{age}".format(name=self.name,sex=self.sex,addr=self.addr,age=self.age)


stu = Student("Yanmangzi","Male")
stu.speak()
print(stu.addr)
stu._Student__getAddr()

print(stu)

print(dir(stu))