#!/usr/bin/python3
# coding = UTF-8
# code by va1id


class Dog:
    def __init__(self, name,  color):
        self.name = name
        self.color = color


    def __str__(self):
        print('这是干啥的')


    def __del__(self):
        print('这又是干啥的。')


    def head(self):
        print('一只{}的狗狗叫{}'.format(self.color, self.name))


    def bark(self):
        print('看见生人汪汪叫')


    def tie(self):
        print('看见家人摇尾巴')


dog1 = Dog('大黄',  '黄色的')
print(dir(dog1))
dog1.__str__()
# dog1.__del__()
