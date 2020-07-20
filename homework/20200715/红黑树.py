#!/usr/bin/python3
# coding = UTF-8
# code by va1id


RED = 0
BLACK = 1


# def spin_left(tree, node):
#     # 防止用户搞错了
#     if not node.rchild:
#         return False
#     node_right = node.rchild
#     node_right.parent = node.parent
#     # node是根，就要修改根
#     if not node.parent:
#         tree.root = node_right
#     # 看node是G的左孩子，那么node_right就要作为G的左孩子
#     elif node == node.parent.lchild:
#         node.parent.lchild = node_right
#     # 看node是G的右孩子，那么node_right就要作为G的右孩子
#     else:
#         node.parent.rchild = node_right
#     # 判断node_right是否有左孩子，如果有，那么变为node的右孩子
#     if node_right.lchild:
#         node_right.lchild.parent = node
#     # 变为node的右孩子，没孩子给的是None
#     node.rchild = node_right.lchild
#     node.parent = node_right
#     node_right.lchild = node
#
#
# # 右旋
# def spin_right(tree, node):
#     if not node.lchild:
#         return False
#     node_left = node.lchild
#     node_left.parent = node.parent
#     if not node.parent:
#         tree.root = node_left
#     elif node == node.parent.lchild:
#         node.parent.lchild = node_left
#     elif node == node.parent.rchild:
#         node.parent.rchild = node_left
#     if node_left.rchild:
#         node_left.rchild.parent = node
#     node.lchild = node_left.rchild
#     node.parent = node_left
#     node_left.rchild = node

RED = 0
BLACK = 1
def spin_left(tree, node):
    if node.rchild == None:
        return False
    # 记录即将改变的指针
    dad = node.parent
    node_right = node.rchild
    # 最后node的父节点必定是现在node的右孩子
    node_right.parent = dad
    if node.parent == None:
        tree.root = node_right
    elif node == dad.lchild:
        dad.lchild = node_right
    else:
        dad.rchild = node_right
    if node_right.lchild:
        node_right.lchild.parent = node
    node.rchild = node_right.lchild
    node.parent = node_right
    node_right.lchild = node


def spin_right(tree, node):
    if node.lchild == None:
        return False
    dad = node.parent
    node_left = node.lchild
    node_left.parent = dad
    if not dad:
        tree.root = node_left
    elif node == dad.lchild:
        dad.lchild = node_left
    elif node == dad.rchild:
        dad.rchild = node_left
    # 左旋与右旋刚开始这个部分写错了， 在调试的时候就在insert_adjust里反复横跳，就是跳不出循环，指针指错
    # 要注意修改某一指针之前，要看这一指针较以前相比是否已经发生变化
    if node_left.rchild:
        node_left.rchild.parent = node
    node.lchild = node_left.rchild
    node.parent = node_left
    node_left.rchild = node


# copy by 龙哥
def rbtree_print(node, key, direction):
    if node:
        if direction == 0:  # tree是根节点
            print("%2d(B) is root" % node.value)
        else:  # tree是分支节点
            print("%2d(%s) is %2d's %6s child" % (
                node.value, ("B" if node.color == 1 else "R"), key, ("right" if direction == 1 else "left")))

        rbtree_print(node.lchild, node.value, -1)
        rbtree_print(node.rchild, node.value, 1)
# yishang

class RBTNode:
    def __init__(self, value):
        self.value = value
        self.lchild = None
        self.rchild = None
        self.parent = None
        self.color = RED


class RBTree:
    def __init__(self):
        self.root = None

    def insert(self, var):
        node = RBTNode(var)
        if self.root is None:
            node.color = BLACK
            self.root = node
            return
        else:
            # 用于比较大小
            cmpnode = self.root
            while cmpnode:
                # 记录最后一个None 的父亲节点用于插入
                point = cmpnode
                if node.value > cmpnode.value:
                    cmpnode = cmpnode.rchild
                elif node.value < cmpnode.value:
                    cmpnode = cmpnode.lchild
                else:
                    break
            else:
                if node.value > point.value:
                    point.rchild = node
                    node.parent = point
                else:
                    point.lchild = node
                    node.parent = point
            self.insert_adjust(node)

    def insert_adjust(self, node):
        dad = node.parent
        # grandfather = dad.parent
        while dad and dad.color == RED:
            dad = node.parent
            grandfather = dad.parent
            # 这是两种不需要调整的情况
            if grandfather == None:
                break
            # 左边的情况
            if grandfather.lchild and grandfather.lchild == dad:
                # 情况三，grand的两个孩子都存在，最后变色，grand变色
                if grandfather.rchild and grandfather.rchild.color == RED:
                    grandfather.lchild.color = BLACK
                    grandfather.rchild.color = BLACK
                    grandfather.color = RED
                    node = grandfather
                    continue
                # 情况四五，grand存在右孩子但是黑色这种情况与没有有孩子情况相当
                # 情况四，当前新加入的节点就是父亲节点的右子树，只要左旋变为情况五即可
                elif dad.rchild and dad.rchild == node:
                    spin_left(self, dad)
                    node = dad
                # 情况五，右旋变色
                # 之前在这个地方，对于情况的判断混乱，加了一个elif，导致在第五种请款的时候老是跳不出循环
                dad.color = BLACK
                grandfather.color = RED
                dad = node.parent
                spin_right(self, grandfather)
            elif grandfather.rchild and grandfather.rchild == dad:
                if grandfather.lchild and grandfather.lchild.color == RED:
                    grandfather.rchild.color = BLACK
                    grandfather.lchild.color = BLACK
                    grandfather.color = RED
                    node = grandfather
                    # 下面这一个continue忘写了， 导致建树总是不对
                    continue
                elif dad.lchild and dad.lchild == node:
                    spin_right(self, dad)
                    node = dad
                dad.color = BLACK
                grandfather.color = RED
                dad = node.parent
                spin_left(self, grandfather)
            self.root.color = BLACK

    def delete(self, var):
        pass


if __name__ == '__main__':
    data = (7, 4, 1, 8, 5, 2, 9, 6, 3)
    tree = RBTree()
    i = RBTNode(1)
    for i in data:
        tree.insert(i)

    rbtree_print(tree.root, tree.root.value, 0)
