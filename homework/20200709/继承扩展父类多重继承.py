#!/usr/bin/python3
# coding = UTF-8
# code by va1id


class F1:
    def a(self):
        print('a')


    def b(self):
        print('b')


    def c(self):
        print('c')


class F2(F1):
    def b(self):
        # super对父类进行扩展，若没有super则进行覆盖
        super(F2, self).b()
        print('d')


class F3:
    def e(self):
        print('e')


    def f(self):
        print('f')
# 多重继承
class F(F1, F3):
    def f(self):
        print('g')


test = F()
test.a()
test.e()
test.f()
print('-'*100)
res = F2()
res.a()
res.b()