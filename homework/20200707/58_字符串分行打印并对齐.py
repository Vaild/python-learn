#!/usr/bin/python3
# coding = UTF-8


str_list = ['ok', 'hello', 'thanks']
for i in str_list:
    print(i.ljust(6))

for i in str_list:
    print(i.rjust(6))

for i in str_list:
    print(i.center(6))