#!/usr/bin/python3
# coding=utf-8
class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))


student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]
print(sorted(student_objects, key=lambda student: student.age))

from operator import itemgetter, attrgetter

student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]

print(sorted(student_tuples, key=itemgetter(0)))
# 对于对象
print(sorted(student_objects, key=attrgetter('age')))

print(sorted(student_tuples, key=itemgetter(1, 2)))

print(1 in [1, 2, 3])

mydict = {'Li': ['M', 7],
          'Zhang': ['E', 2],
          'Wang': ['P', 3],
          'Du': ['C', 9],
          'Ma': ['C', 2],
          'Zhe': ['H', 7]}
print(mydict.items())
print(sorted(mydict.items(), key=lambda k: k[1][0]))
# print(sorted(mydict.items(), key=itemgetter(1)))

gameresult = [
    {"name": "Bob", "wins": 10, "losses": 3, "rating": 75.00},
    {"name": "David", "wins": 3, "losses": 5, "rating": 57.00},
    {"name": "Carol", "wins": 4, "losses": 5, "rating": 57.00},
    {"name": "Patty", "wins": 9, "losses": 3, "rating": 71.48}]

for i in sorted(gameresult, key=itemgetter("rating", "name")):
    print(i)
