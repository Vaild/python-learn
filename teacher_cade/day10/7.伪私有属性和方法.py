#!/usr/bin/python3
# coding=utf-8

# !/usr/bin/python3
# coding=utf-8

class Women:

    def __init__(self, name):
        self.name = name
        # 不要问女生的年龄
        self._age = 18

    def boyfriend(self):
        self._secret()

    def _secret(self):
        print("我的年龄是 %d" % self._age)


xiaofang = Women("小芳")
# 伪私有属性，外部不能直接访问
print(xiaofang._age)

xiaofang._secret()
