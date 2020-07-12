#!/usr/bin/python3
# coding = UTF-8
# code by va1id



file_source = open('readme', mode='r')
file = open('file', mode='r+', encoding='utf-8')
while True:
    text_source = file_source.readline()
    file.write(text_source)
    if len(text_source) == 0:
        break
file_source.close()

while True:
    x = file.readline()
    print(x, end='')
    if len(x) == 0:
        break

file.close()