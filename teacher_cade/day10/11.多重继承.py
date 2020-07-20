#!/usr/bin/python3
# coding=utf-8

class A:
    def test(self):
        print('I am A test')

    def demo(self):
        print('I am A demo')


class B:
    def test(self):
        print('I am B test')

    def demo(self):
        print('I am B demo')


class C(A, B):
    def test(self):
        print('I am C test')


print(C.__mro__)
muti = C()
muti.demo()
