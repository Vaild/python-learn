#!/usr/bin/python3
# coding = UTF-8
# code by va1id


import os
def DFS(path, space):
    list = os.listdir(path)
    for file in list:
        print(' '*space,end='')
        print(file)
        if os.path.isdir(path + '/' + file):
            DFS(path + '/' + file, space+4)

if __name__ == '__main__':
    DFS('..', 2)
