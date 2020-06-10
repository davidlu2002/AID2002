"""
    二叉树的添加方法
"""
class Node:
    """
        二叉树的一个节点元素
    """
    def __init__(self, value):
        self.value = value
        self.lbranch = None
        self.rbranch = None
    def __str__(self):
        return "该节点是%d" % (self.value)

class Tree:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root == None

    def add(self, value):
        if self.is_empty():
            self.root = Node(value)
            return
        else:
            queue_list = []
            queue_list.append(self.root)

            while True:
                cur = queue_list.pop(0)

                if cur.lbranch == None:
                    cur.lbranch = Node(value)
                    return
                elif cur.rbranch == None:
                    cur.rbranch = Node(value)
                    return
                else:
                    queue_list.append(cur.lbranch)
                    queue_list.append(cur.rbranch)

    def breadth_traversal(self):
        if self.root == None:
            print(None)
        else:
            queue_list = []
            queue_list.append(self.root)
            while len(queue_list) != 0:
                cur = queue_list.pop(0)
                print(cur)
                if cur.lbranch != None:
                    queue_list.append(cur.lbranch)
                if cur.rbranch != None:
                    queue_list.append(cur.rbranch)

    count = 0
    def preorder_traversal(self, node):
        """
            先序遍历：根左右
        :return:
        """
        self.count += 1
        print(self.count)
        if node == None:
            return None
        print(node)
        # 递归
        self.preorder_traversal(node.lbranch)
        self.preorder_traversal(node.rbranch)

    def inorder_traversal(self, node):
        """
            中序遍历：根左右
        :param node: self.root
        """
        if node == None:
            return None
        self.inorder_traversal(node.lbranch)
        print(node)
        self.inorder_traversal(node.rbranch)

    def postorder_traversal(self, node):
        """
            后序遍历
        :param node: self.root
        """
        if node == None:
            return None
        self.postorder_traversal(node.lbranch)
        self.postorder_traversal(node.rbranch)
        print(node)

tree01 = Tree()
for i in range(10):
    tree01.add(i)

# tree01.breadth_traversal()
tree01.preorder_traversal(tree01.root)
# tree01.inorder_traversal(tree01.root)
# tree01.postorder_traversal(tree01.root)


