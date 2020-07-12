#!/usr/bin/python3
# coding = UTF-8
# code by va1id



class Animal:
    def eat(self):
        print('吃')


    def drink(self):
        print('喝')


    def sleep(self):
        print('睡')


class Dog(Animal):
    def bark(self):
        print('汪汪叫')

class XiaoTianQuan(Dog):
    def fly(self):
        print('I can fly')
        print('I can bark')
        
    # 子类中对于弗雷德方法进行重写
    def bark(self):
        print('Icanbark')


dog = XiaoTianQuan()
dog.bark()
dog.fly()