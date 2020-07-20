RED = 0
BLACK = 1


# 左旋，tree是树对象，node是要调整的节点
def left_rotate(tree, node):
    # 防止用户搞错了
    if not node.right:
        return False
    node_right = node.right
    node_right.p = node.p
    # node是根，就要修改根
    if not node.p:
        tree.root = node_right
    # 看node是G的左孩子，那么node_right就要作为G的左孩子
    elif node == node.p.left:
        node.p.left = node_right
    # 看node是G的右孩子，那么node_right就要作为G的右孩子
    else:
        node.p.right = node_right
    # 判断node_right是否有左孩子，如果有，那么变为node的右孩子
    if node_right.left:
        node_right.left.p = node
    # 变为node的右孩子，没孩子给的是None
    node.right = node_right.left
    node.p = node_right
    node_right.left = node


# 右旋
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

    # 通过二叉查找，找到位置
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
            parent = node.p
            grandpa = parent.p
            # 先写父亲在爷爷的左边
            if parent == grandpa.left:
                # 情形三
                if grandpa.right and grandpa.right.color == RED:
                    parent.color = BLACK
                    grandpa.right.color = BLACK
                    grandpa.color = RED
                    node = grandpa
                    continue
                # 情形四
                if node == parent.right:
                    left_rotate(self, parent)
                    parent, node = node, parent
                # 情形五
                parent.color = BLACK
                grandpa.color = RED
                right_rotate(self, grandpa)
            else:
                if grandpa.left and grandpa.left.color == RED:
                    parent.color = BLACK
                    grandpa.left.color = BLACK
                    grandpa.color = RED
                    node = grandpa
                    continue
                # 情形四
                if node == parent.left:
                    right_rotate(self, parent)
                    parent, node = node, parent
                # 情形五
                parent.color = BLACK
                grandpa.color = RED
                left_rotate(self, grandpa)
        self.root.color = BLACK


if __name__ == '__main__':
    data = (7, 4, 1, 8, 5, 2, 9, 6, 3)
    tree = RBTree()
    for i in data:
        tree.insert(i)

    rbtree_print(tree.root, tree.root.value, 0)
