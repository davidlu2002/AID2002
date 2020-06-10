"""
    栈模型的链式存储
"""

class StackError(Exception):
    pass

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def __str__(self):
        return "该节点是%s" % (self.value)

# 第一种方法：
# 该种类每次调用添加或删除方法都需要遍历链表，得到最后一个元素，
# 相比第二种方法更复杂，麻烦

"""
class LStack:
    def __init__(self):
        self._head = None

    def push(self, value):
        if self.is_empty():
            self._head = Node(value)
        else:
            temp = self._head
            while not temp.next == None:
                temp = temp.next
            temp.next = Node(value)

    def pop(self):
        temp = self._head
        pre = None
        if self._head == None:
            raise StackError("stack is empty")

        elif pre == None:
            self._head = None
            return temp

        while temp.next is not None:
            pre = temp
            temp = temp.next
        pre.next = None
        return temp

    def top(self):
        if self._head == None:
            return None
        temp = self._head
        while not temp.next == None:
            temp = temp.next
        return temp

    def is_empty(self):
        return self._head == None

l = LStack()
for i in range(10):
    l.push(i)

print(l.top())

"""

class LStack:
    def __init__(self):
        self._top = None

    def is_empty(self):
        return self._top is None

    def push(self, value):
        node = Node(value)
        node.next = self._top
        self._top = node

    def pop(self):
        if self._top is None:
            raise StackError("Stack is empty")
        temp = self._top
        self._top = temp.next
        temp.next = None
        return temp

if __name__ == '__main__':
    ls = LStack()
    ls.push(1)
    ls.push(2)
    ls.push(3)
    print(ls.pop())
    print(ls.pop())
    print(ls.pop())
    print(ls.pop())
"""