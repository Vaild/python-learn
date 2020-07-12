#!/usr/bin/python3
# coding = UTF-8
# code by va1id


class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height


    def run(self):
        print('{}今年{}岁，身高{}，每天早上跑完步，回去吃东西。'.format(self.name, self.age, self.height))


    def eat(self):
        print('{}今年{}岁，身高{}，{}不跑步，{}喜欢吃东西。'.format(self.name, self.age, self.height,self.name, self.name))


ming = Person('小明', 18, 1.75)
mei = Person('小美', 17, 1.65)
ming.run()
mei.eat()