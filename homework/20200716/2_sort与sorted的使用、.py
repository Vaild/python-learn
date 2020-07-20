#!/usr/bin/python3
# coding = UTF-8
# code by va1id

import operator
class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.person_dict = {'name': self.name, 'age': self.age, 'sex': self.sex}

    def __repr__(self):
        return repr((self.name, self.age, self.sex))


person_list = [
    Person('c', 18, 0),
    Person('a', 19, 0),
    Person('d', 18, 1)
]
print(person_list)
# 如果要是传入对象的话则需要在最后的比较参数，对象.属性就可以
print(sorted(person_list, key=lambda person: person.name))
print(sorted(person_list, key=lambda person: person.age))
print(sorted(person_list, key=lambda person: person.sex))
print(sorted(person_list, key=operator.attrgetter('name')))
# print(person_list.sort())列表自带的sort函数不支持对对象进行排序

# 的字典进行遍历，首先将其内部的键值对转换为可以遍历的元组
x = Person('e', 18, 1)
print(sorted(x.person_dict.items(), key=lambda a: a[0]))
# 字典嵌套列表
dict_list = {'x': [3, 9, 6, 4, 7], 'p': [6, 7, 3, 5, 4], 'z':[1, 2, 3, 4, 5]}
print(dict_list.items())
print(sorted(dict_list.items(), key=lambda a:a[1][4]))
print(sorted(dict_list.items(), key=operator.itemgetter(1)))


# 列表嵌套字典
c = Person('c', 18, 0)
a = Person('a', 19, 0)
d = Person('d', 18, 1)
person_dict = [
    c.person_dict,
    a.person_dict,
    d.person_dict
]
# itemsgeter 可以对多个参数进行排序
print(sorted(person_dict, key=operator.itemgetter('name', 'age')))
