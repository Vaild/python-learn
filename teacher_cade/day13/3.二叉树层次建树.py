#!/usr/bin/python3
# coding=utf-8
from collections import deque


class Node(object):
    """节点类"""

    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class Tree:
    """树类"""

    def __init__(self):
        self.root = None
        self.queue = deque()

    def build_tree(self, val):
        # 初始化节点
        node = Node()
        node.elem = val
        # 进树
        if self.root == None:
            self.root = node
            self.queue.append(node)
        else:  # 不是树根的时候
            self.queue.append(node)
            if self.queue[0].lchild == None:
                self.queue[0].lchild = node
            elif self.queue[0].rchild == None:
                self.queue[0].rchild = node
                self.queue.popleft()

    def pre_order(self, node):
        if node:
            print(node.elem, end=' ')
            self.pre_order(node.lchild)
            self.pre_order(node.rchild)

    def mid_order(self, node):
        if node:
            self.mid_order(node.lchild)
            print(node.elem, end=' ')
            self.mid_order(node.rchild)

    def last_order(self, node):
        if node:
            self.last_order(node.lchild)
            self.last_order(node.rchild)
            print(node.elem, end=' ')


if __name__ == '__main__':
    tree = Tree()
    for i in range(1, 11):
        tree.build_tree(i)

    tree.pre_order(tree.root)
    print()
    tree.mid_order(tree.root)
    print()
    tree.last_order(tree.root)
