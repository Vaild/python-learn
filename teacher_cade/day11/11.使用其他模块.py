#!/usr/bin/python3
# coding=utf-8

import wd_01_测试模块1 as DogModule

DogModule.say_hello()
# 不可用其他文件的main内的变量
# print(DogModule.title)
print(DogModule.__file__)
print(DogModule.__name__)
# from wd_01_测试模块1 import *
#
# say_hello()

import random

print(random.__file__)
