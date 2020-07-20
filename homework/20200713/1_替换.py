#!/usr/bin/python3
# coding = UTF-8
# code by va1id

# 同时删去了数字
import string
import os
file = open('The_Holy_Bible.txt', mode='r')
file1 = open('holy_bible.txt', mode='a')
for text in file:
    del_symbol = string.punctuation + string.digits
    for letter in text:
        if letter in del_symbol:
            text = text.replace(letter, ' ')
    text = text.lower()
    file1.write(text)
print('转换完成')
file.close()
file1.close()
os.remove('The_Holy_Bible.txt')
os.rename('holy_bible.txt', 'The_Holy_Bible.txt')