# coding: utf-8
# 用数组实现循环队列

class cirularQueue(object):
    """cirularQueue"""
    def __init__(self, length = 10):
        self.maxLength = length + 1
        self.list = [0] * self.maxLength
        self.front = 0
        self.rear = 0

    def isEmpty(self):
        if self.front == self.rear:
            return True
        else:
            return False

    def isFull(self):
        if (self.rear + 1) % self.maxLength == self.front:
            return True
        else:
            return False

    def push(self, value):
        if self.isFull():
            return False
        self.list[self.rear] = value
        self.rear += 1
        if self.rear >= self.maxLength:
            self.rear %= self.maxLength
        return True

    def pop(self):
        if self.isEmpty():
            return False
        else:
            res =  self.list[self.front]
            self.front += 1
            if self.front >= self.maxLength:
                self.front %= self.maxLength

            return res

if __name__ == "__main__":

    testQ = cirularQueue()
    for i in range(1, 20):
        if testQ.push(i):
            print testQ.list
    print testQ.pop()
    print testQ.list
    testQ.push(11)
    testQ.push(12)
    print testQ.list
    print testQ.pop()
    print testQ.list
    testQ.push(13)
    testQ.push(14)
    print testQ.list
