#!/usr/bin/python3
# coding = UTF-8
# code by va1id


# class Dog:
#     def __init__(self, name, species, color):
#         self.name = name
#         self.species = species
#         self.color = color
#
#
#     def head(self):
#         print('一只{}的{}叫{}'.format(color, species, name))
#
#
#     def bark(self):
#         print('看见生人汪汪叫')
#
#
#     def tie(self):
#         print('看见家人摇尾巴')
#
#
# dog1 = Dog('大黄', '狗狗', '黄色的')
# dog1.head()
# dog1.bark()
# dog1.tie()


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