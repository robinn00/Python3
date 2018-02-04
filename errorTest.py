#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

try:
    print(10*(1/0))
except Exception:
    print("ZeroDivisionError")

# while True:
#     try:
#         num = int(input("input:"))
#         break
#     except ValueError:
#         print("ValueError....")


# try:
#     f = open("do.txt")
#     s = f.readline()
#     num = int(s.strip())
# except FileNotFoundError as fnf:
#     print("{0}".format(fnf))
# except ValueError as ve:
#     print("{0}".format(ve))
# except:
#     print("error")
# finally:
#     print("finally")

try:
    raise NameError("valuesinfos")
except NameError:
    print("xxxxxxxxx")
    raise

