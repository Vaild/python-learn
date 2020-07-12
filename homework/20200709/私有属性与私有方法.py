#!/usr/bin/python3
# coding = UTF-8
# code by va1id


class Person:
    def __init__(self, name, __age, height, __weight ):
        self.name = name
        self.__age = __age
        self.height = height
        self.__weight = __weight


    def read_personal_1(self):
        print('{}的年龄是{}，体重{}'.format(self.name, self.__age, self.__weight))


    def __getpersonal(self):
        print('{}的年龄是{}，体重{}'.format(self.name, self.__age, self.__weight))


    def read_personal_2(self):
        self.__getpersonal()


ming = Person('小明', 18, 175, '90kg')
# print(ming.__age)
ming.read_personal_1()
# ming.__getpersonal()
ming.read_personal_2()