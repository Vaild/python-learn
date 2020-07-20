#!/usr/bin/python3
# coding = UTF-8
# code by va1id


class Node:
    def __init__(self, var):
        self.elem = var
        self.lchild = None
        self.rchild = None


class Tree:
    def __init__(self):
        self.root = None
        self.queque = []

    def build_tree(self, var):
        node = Node(var)
        self.queque.append(node)
        if self.root == None:
            self.root = node
        else:
            if self.queque[0].lchild == None:
                self.queque[0].lchild = node
            elif self.queque[0].rchild == None:
                self.queque[0].rchild = node
                self.queque.pop(0)

    def preorder(self, node):
        if node:
            print(node.elem, end=' ')
            self.preorder(node.lchild)
            self.preorder(node.rchild)

if __name__ == '__main__':
    tree = Tree()
    for i in range(1,11):
        tree.build_tree(i)
    tree.preorder(tree.root)

