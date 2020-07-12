#!/usr/bin/python3
# coding = UTF-8
name = input('请输入您的姓名：')
company = input('请输入您的公司：')
title = input('请输入您的职位：')
phone = input('请输入您的电话：')
email = input('请输入您的邮箱：')

print('*' * 30)
print(company, '\n')
print('{} ({})\n'.format(name, title))
print('电话：%s' % phone)
print('邮箱：%s' % (email))
print('*' * 30)