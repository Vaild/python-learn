#!/usr/bin/python3
# coding=utf-8
class Node(object):
    """节点类"""

    def __init__(self, elem=-1, pNext=None):
        self.elem = elem
        self.pNext = pNext
