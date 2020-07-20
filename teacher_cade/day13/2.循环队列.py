#!/usr/bin/python3
# coding=utf-8

# from collections import deque
#
# # 增删查改
# queue = deque(["Eric", "John", "Michael"])
# queue.append('luke')
# print(queue)
# print(queue.popleft())
# print(queue)
class CircleQueue:
    def __init__(self, size):
        self.queue = [0] * size
        self.max_size = size
        self.front = 0
        self.rear = 0

    def enqueue(self, val):
        if (self.rear + 1) % self.max_size == self.front:
            print('queue is full')
            return
        self.queue[self.rear] = val
        # 注意取余
        self.rear = (self.rear + 1) % self.max_size

    def dequeue(self):
        if self.rear == self.front:
            print('queue is empty')
            return None
        val = self.queue[self.front]
        self.front = (self.front + 1) % self.max_size
        return val


if __name__ == '__main__':
    c = CircleQueue(5)
    c.enqueue('a')
    c.enqueue('b')
    c.enqueue('c')
    c.enqueue('d')
    c.enqueue('e')
    print(c.queue)
    print(c.dequeue())
    c.enqueue('e')
    print(c.queue)
