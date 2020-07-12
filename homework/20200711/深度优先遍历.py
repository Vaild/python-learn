#!/usr/bin/python3
# coding = UTF-8
# code by va1id


import os
def DFS(path):
    list = os.listdir(path)
    for i in list:
        print(i)
        if os.path.isdir(path + '/' + i):
            DFS(path + '/' + i)

if __name__ == '__main__':
    DFS('.')
