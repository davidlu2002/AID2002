"""
    制作并实现线性表的链式存储
"""
class Node:
    """
        链表节点
    """
    def __init__(self, value):
        # item存放的是数据
        self.value = value
        # next存放的是下一个节点的地址
        self.next = None
    def __str__(self):
        return "该节点是%s" % (self.value)


class Single_Linked_List:
    """
        单链表
    """
    def __init__(self):
        self.head = None

    def is_empty(self):
        """
            判断链表是否为空
        :return: True：空  False：不为空
        """
        if self.head == None:
            return True
        return False

    def clear(self):
        """
            清空链表
        """
        self.head = None

    def get_length(self):
        """
            获取链表内的节点个数
        :return: 个数
        """
        if self.head == None:
            return 0
        temp = self.head
        length = 1
        while temp.next != None:
            temp = temp.next
            length += 1
        return length

    # 增操作
    def __get_final_node(self):
        """
            得到链表中最后一个节点
        :return:链表中的最后一个节点
        """
        temp = self.head
        while True:
            if temp.next == None:
                return temp
            else:
                temp = temp.next

    def append(self, node):
        """
            在链表尾部新增一个节点
        :param node: 新增的节点
        """
        if self.head == None:
            self.head = node
        else:
            final_node = self.__get_final_node()
            final_node.next = node

    def insert(self, index, node):
        """
            向链表中插入一个节点
        :param index: 需要插入的位置（如果为0，在链表开头插入节点）
        :param node: 需要插入的节点
        """
        temp = self.head
        if index == 0:
            node.next = temp
            self.head = node
        else:
            try:
                for i in range(index - 1):
                    temp = temp.next
                node.next = temp.next
                temp.next = node
            except AttributeError:
                raise IndexError("insert index out of range")

    # 删除操作

    def __remove_first_node(self):
        """
            删除链表中的第一个节点
        """
        temp = self.head
        if temp.next == None:
            self.head = None
        else:
            self.head = temp.next
            temp.next = None

    def remove(self, value):
        """
            根据节点的value删除一个节点
        :param value: 需要删除的节点的value
        """
        temp = self.head
        pre = None
        # 是否需要删除第一个节点
        if temp.value == value:
            self.__remove_first_node()
            return

        # 删除第一个节点后的节点
        while temp is not None:
            if temp.value == value:
                pre.next = temp.next
                temp.next = None
            else:
                pre = temp
                temp = temp.next


            # 是否需要删除链表中最后一个节点
            if temp.next.next == None:
                if temp.next.value == value:
                    temp.next = None
                    break
                else:
                    raise ValueError("x not in linked list")

            temp = temp.next

    # 改动操作
    def update(self, index, value):
        """
            更改链表中某一个节点的value
        :param index: 链表中节点的位置
        :param value: 需要更改的数据
        """
        temp = self.head
        try:
            for i in range(index - 1):
                temp = temp.next
            temp.value = value
        except AttributeError:
            raise IndexError("update index out of range")

    # 查操作
    def get_all_node(self):
        """
            获取链表中所有节点
        """
        if self.head == None:
            print("该链表无节点")
        else:
            temp = self.head
            while True:
                if temp == None:
                    break
                else:
                    print(temp)
                    temp = temp.next

    def find(self, index = 1):
        """
            根据索引查找链表中的节点
        :param index:节点的索引
        :return:需要查找的节点（如果为None则不存在）
        """
        if self.is_empty():
            return None
        try:
            temp = self.head
            for i in range(index - 1):
                temp = temp.next
            return temp
        except AttributeError:
            return None

if __name__ == '__main__':
    manager = Single_Linked_List()
    node01 = Node(11)
    node02 = Node(12)
    node03 = Node(15)

    manager.append(node01)
    manager.append(node02)
    manager.append(node03)

    manager.remove(11)

    manager.update(2, 100)

    result = manager.find(2)
    print(result)
    print("=================================")

    manager.get_all_node()
    print("=================================")

    manager.clear()
    print(manager.is_empty())