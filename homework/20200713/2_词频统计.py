#!/usr/bin/python3
# coding = UTF-8
# code by va1id

# class Statistics:
#     def __init__(self, file):
#         self.file = open(file, mode='r')
file = open('The_Holy_Bible.txt', mode='r')
statistics = {}
line = 0
danci = 0
character = 0
# 对句子进行分割
for sentence in file:
    line += 1
    for word in sentence.split():
        danci += 1
        for i in word:
            character += 1
        if word not in statistics:
            statistics[word] = 1
        else:
            statistics[word] += 1
result = sorted(statistics.items(), key=lambda item:item[1])
# result.reverse()
print('字符数共有 ', character)
print('行数共有 ', line)
print('单词数共有 ', danci)
print('词频：')
for i in range(-1, -11, -1):
    print('%s--%d' % result[i])
