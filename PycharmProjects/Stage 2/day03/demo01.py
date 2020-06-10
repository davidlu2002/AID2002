class QueueError(Exception):
    pass

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def __str__(self):
        return "该节点是{}".format(self.value)

class Lqueue:
    def __init__(self):
        self._front = None
        self._rear = None

    def is_empty(self):
        return self._front == None

    def get_rear(self):
        return self._rear
    def enqueue(self, value):
        if self.is_empty():
            self._front = Node(value)
            self._rear = self._front
        else:
            self._rear.next = Node(value)
            self._rear = self._rear.next

    def outqueue(self):
        temp = self._front
        if self.is_empty():
            raise QueueError("Queue is empty")
        if self._rear == self._front:
            self._rear = self._front = None
            return temp

        self._front = self._front.next
        return temp

if __name__ == '__main__':
    q01 = Lqueue()
    for i in range(10):
        q01.enqueue(i)
    for i in range(11):
        print(q01.outqueue())
    print(q01.is_empty())

