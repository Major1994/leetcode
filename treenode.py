from inspect import stack

class stack:
    def __init__(self):
        self.elems = []
    def push(self, value):
        self.elems.append(value)

    def pop(self):
        return self.elems.pop()

    def is_empty(self):
        return len(self.elems)==0
    def print(self):
        [print(value) for value in self.elems]

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, node=None):
        self.root = node

    def add(self, value):
        node = Node(value)

        if self.root is None:
            self.root=node
            return

        # 1. 临时列表，存将要遍历的节点
        node_list = [self.root]

        # 2. 遍历临时列表中的节点，找空位置
        while node_list:

            current = node_list.pop(0)

            # 3.遍历当前节点
            # 先看左子节点有没有位置
            if current.left is None:
                current.left = node
                return
            else:
                # 如果节点没有位置，把当前节点放入临时列表去遍历
                node_list.append(current.left)

            # 再看右子节点有没有位置
            if current.right is None:
                current.right = node
                return
            else:
                # 如果节点没有位置，把当前节点放入临时列表去遍历
                node_list.append(current.right)

    # 广度优先遍历
    def breath_travel(self):
        if self.root is None:
            return
        # 1. 临时列表，存将要遍历的节点
        node_list = [self.root]

        # 2. 遍历临时列表中所有的点
        while node_list:
            current = node_list.pop(0)
            print(current.value)
            # 3. 当前点 左右节点入临时列表
            if current.left is not None:
                node_list.append(current.left)

            if current.right is not None:
                node_list.append(current.right)

    # 深度遍历，先遍历最深的节点的值
    def depth_traval_by_nodelist(self):
        if self.root is None:
            return
        # 1. 临时栈，保存遍历路径上的所有节点
        node_list = stack()
        node_list.push(self.root)
        # 2. 按倒序遍历临时列表中所有的点
        while node_list:
            node_list.print()
            # 倒序弹出节点
            current = node_list.pop()
            print(current.value)
            # 3. 当前点 左右节点入临时列表

            #栈 先进后出，保证 弹出时 先左后右，压入时 先右后左
            if current.right is not None:
                node_list.push(current.right)
            if current.left is not None:
                node_list.push(current.left)

    # 深度优先遍历——递归法
    def depth_travel_by_recurrent(self):

        # 前序遍历
        def pre_travel(node):
            if node is None:
                return

            print(node.value)
            pre_travel(node.left)
            pre_travel(node.right)

        # 前序遍历
        def mid_travel(node):
            if node is None:
                return

            mid_travel(node.left)
            print(node.value)
            mid_travel(node.right)

        # 后序遍历
        def last_travel(node):
            if node is None:
                return

            last_travel(node.left)
            last_travel(node.right)
            print(node.value)

        pre_travel(self.root)
        mid_travel(self.root)
        last_travel(self.root)

if __name__ == '__main__':
    bi_tree = BinaryTree()

    for i in range(20):
        bi_tree.add(i)
    bi_tree.breath_travel()

    for i in range(20):
        bi_tree.add(i)
    bi_tree.depth_travel_by_recurrent()

    for i in range(20):
        bi_tree.add(i)
    bi_tree.depth_traval_by_nodelist()