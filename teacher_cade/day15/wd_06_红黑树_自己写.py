RED = 0
BLACK = 1


def left_rotate(tree, node):
    if not node.right:
        return False
    node_right = node.right
    node_right.p = node.p
    if not node.p:
        tree.root = node_right
    elif node == node.p.left:
        node.p.left = node_right
    else:
        node.p.right = node_right
    if node_right.left:
        node_right.left.p = node
    node.right = node_right.left
    node.p = node_right
    node_right.left = node


def right_rotate(tree, node):
    if not node.left:
        return False
    node_left = node.left
    node_left.p = node.p
    if not node.p:
        tree.root = node_left
    elif node == node.p.left:
        node.p.left = node_left
    elif node == node.p.right:
        node.p.right = node_left
    if node_left.right:
        node_left.right.p = node
    node.left = node_left.right
    node.p = node_left
    node_left.right = node


def rbtree_print(node, key, direction):
    if node:
        if direction == 0:  # tree是根节点
            print("%2d(B) is root" % node.value)
        else:  # tree是分支节点
            print("%2d(%s) is %2d's %6s child" % (
                node.value, ("B" if node.color == 1 else "R"), key, ("right" if direction == 1 else "left")))

        rbtree_print(node.left, node.value, -1)
        rbtree_print(node.right, node.value, 1)


class RedBlackTreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.p = None  # 父亲的藏宝图
        self.color = RED  # 放入节点默认是红色


class RBTree:

    def __init__(self):
        self.root = None

    def insert(self, node_value):
        new_node = RedBlackTreeNode(node_value)
        temp_root = self.root
        temp_cur = temp_root
        while temp_cur:
            temp_dad = temp_cur
            if new_node.value < temp_cur.value:
                temp_cur = temp_cur.left
            else:
                temp_cur = temp_cur.right

        if not temp_root:
            self.root = new_node  # 新建节点作为树根
            new_node.color = BLACK
            return
        elif new_node.value > temp_dad.value:
            temp_dad.right = new_node
            new_node.p = temp_dad
        else:
            temp_dad.left = new_node
            new_node.p = temp_dad

        self.insert_fixup(new_node)

    def insert_fixup(self, node):
        while node.p and node.p.color == RED:
            dad = node.p
            grandpa = dad.p
            if not grandpa:
                break
            if grandpa.left == dad:
                uncle = grandpa.right
                if uncle and uncle.color == RED:
                    grandpa.color = RED
                    dad.color = BLACK
                    uncle.color = BLACK
                    node = grandpa
                    continue
                elif dad.right == node:
                    left_rotate(self, dad)
                    node = dad
                dad = node.p
                dad.color = BLACK
                grandpa.color = RED
                right_rotate(self, grandpa)

            elif grandpa.right == dad:
                uncle = grandpa.left
                if uncle and uncle.color == RED:
                    grandpa.color = RED
                    dad.color = BLACK
                    uncle.color = BLACK
                    node = grandpa
                    continue
                elif dad.left == node:
                    right_rotate(self,dad)
                    node = dad
                dad = node.p
                dad.color = BLACK
                grandpa.color = RED
                left_rotate(self,grandpa)
        self.root.color = BLACK


if __name__ == '__main__':
    data = (7, 4, 1, 8, 5, 2, 9, 6, 3)
    tree = RBTree()
    for i in data:
        tree.insert(i)

    rbtree_print(tree.root, tree.root.value, 0)
