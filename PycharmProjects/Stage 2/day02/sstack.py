"""
    栈模型的顺序存储
"""

# 自定义异常
class StackError(Exception):
    pass

# 顺序栈类
class Sstack:
    def __init__(self):
        self.__stack = []

    # 入栈
    def push(self, value):
        self.__stack.append(value)

    # 出栈
    def pop(self):
        if self.is_empty():
            raise StackError("Stack is empty")
        return self.__stack.pop()

    # 查看栈顶元素
    def top(self):
        if self.is_empty():
            raise StackError("Stack is empty")
        return self.__stack[-1]

    # 判断是否为空
    def is_empty(self):
        return len(self.__stack) == 0



if __name__ == '__main__':
    stack01 = Sstack()



