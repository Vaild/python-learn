#!/usr/bin/python3
# coding = UTF-8
# code by va1id


class Node:
    def __init__(self, elem):
        self.elem = elem
        self.lchild = None
        self.rchild = None

class Tree:
    def __init__(self):
        self.root = None
        self.queue = []

    def build_tree(self, var):
        node = Node(var)
        self.queue.append(node)
        if self.root is None:
            self.root = node
        else:
            if self.queue[0].lchild == None:
                self.queue[0].lchild = node
            elif self.queue[0].rchild == None:
                self.queue[0].rchild = node
                self.queue.pop(0)


    def preorder(self, node):
        if node:
            print(node.elem, end=' ')
            self.preorder(node.lchild)
            self.preorder(node.rchild)

    def midorder(self, node):
        if node:
            self.midorder(node.lchild)
            print(node.elem, end=' ')
            self.midorder(node.rchild)

    def lastorder(self, node):
        if node:
            self.lastorder(node.lchild)
            self.lastorder(node.rchild)
            print(node.elem, end=' ')


if __name__ == '__main__':
    tree = Tree()
    for i in range(1,11):
        tree.build_tree(i)
    tree.preorder(tree.root)
    print()
    tree.midorder(tree.root)
    print()
    tree.lastorder(tree.root)
