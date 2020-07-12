#!/usr/bin/python3
# coding = UTF-8


def Not_re(seta, setb):
    return seta ^ setb



set1 = {'A','D','B'}
set2 = {'D','E','C'}
print(Not_re(set1,set2))