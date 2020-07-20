#!/usr/bin/python3
# coding=utf-8


class Tool(object):
    # 使用赋值语句，定义类属性，记录创建工具对象的总数
    count = 0

    @classmethod
    def show_tool_count(cls):
        print("工具对象的数量 %d" % cls.count)

    def __init__(self, name):
        self.name = name
        # self.count = 5

        # 针对类属性做一个计数+1
        Tool.count += 1

    @staticmethod
    def show_class_function(cls):
        print('I am a static method' + cls)


# 创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("铁锹")

# 知道使用 Tool 类到底创建了多少个对象?
# 不能使用类名去访问对象属性 Tool.name
print("现在创建了 %d 个工具" % Tool.count)
Tool.count += 5
Tool.show_tool_count()
Tool.show_class_function('hello')
