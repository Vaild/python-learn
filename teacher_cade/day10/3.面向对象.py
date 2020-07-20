#!/usr/bin/python3
# coding=utf-8

# object类叫基类
class Person:
    """
    人类
    """

    def __init__(self, name, age, height, house=None):
        self.name = name
        self.age = age
        self.height = height
        self.house = house

    # 对对象输出的时候，可以打印对象的信息
    def __str__(self):
        return 'I am handsome'

    def __del__(self):
        print('I will over')

    def run(self):
        print(self.name + 'I can run')

    def eat(self):
        print('I can eat')


xiaoming = Person('xiaoming', 18, 175, '豪宅')
print(Person)
xiaoming.run()
xiaohong = Person('xiaohong', 17, 165)
xiaohong.run()
print(xiaoming.house)
xiaohong.house = '无房'
print(xiaohong.house)
xiaowang = xiaoming
print(xiaoming is xiaowang)
print(xiaoming == xiaowang)
