#!/usr/bin/python3
# coding = UTF-8
# code by va1id



test = open('readme', mode='rb+')
# test.write('人生苦短'.encode('utf-8'))
res = test.read()
print(res.decode('utf-8'))
test.close()