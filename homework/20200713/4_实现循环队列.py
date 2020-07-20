#!/usr/bin/python3
# coding = UTF-8
# code by va1id

import random
class CycleQueue:
    """
    实现循环队列，其功能包括
    1.出队
    2.入队
    3.统计当前循环队列当中的元素个数
    4.判满
    5.判空
    """
    def __init__(self, size):
        self.size = size
        self.queue = [0]*size
        self.front = 0
        self.rear = 0

    # 判空
    def empty(self):
        return self.rear == self.front

    # 判满
    def overflow(self):
        return (self.rear + 1) % self.size == self.front

    # 入队
    def enqueue(self, var):
        if self.overflow():
            print('本循环队列已满！')
        else:
            self.queue[self.rear] = var
            self.rear = (self.rear + 1) % self.size

    # 出队
    def dequeue(self):
        if self.empty():
            print('本循环队列已空！')
        else:
            self.front = (self.front + 1) % self.size

    # 此时循环队列中的元素个数
    def length(self):
        return (self.rear - self.front + self.size) % self.size


if __name__ == '__main__':
    cq = CycleQueue(11)
    for i in range(10):
        cq.enqueue(random.randint(0, 100))
    print(cq.queue)
    print(cq.length())
    cq.dequeue()
    print(cq.queue)
    print(cq.length())
    cq.enqueue(11)
    print(cq.queue)
    print(cq.length())
    print(cq.overflow())