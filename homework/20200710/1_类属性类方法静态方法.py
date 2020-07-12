#!/usr/bin/python3
# coding = UTF-8
# code by va1id


class Person:
    # 类属性
    count = 0
    # 初始化
    def __init__(self, name, age=None, height=None):
        self.name = name
        self.age = age
        self.height = height
        Person.count += 1
    # 类方法在内部可以调用类属性
    @classmethod
    def PersonNum(cls):
        print('目前共有%d人。'% cls.count)
    # 不调用类方法类属性 对象
    @staticmethod
    def help():
        print('详情访问：\nhttps://docs.python.org/3/tutorial/index.html')


xiaoming = Person('xiaoming')
xiaomei = Person('xiaomei', 18, 165)
hanhan = Person('hanhan')
Person.PersonNum()