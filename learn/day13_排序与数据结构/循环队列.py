#!/usr/bin/python3
# coding = UTF-8
# code by va1id

class CycleQueue:
    def __init__(self, length):
        self.cyclequeue = [0]*length
        self.cyclequeue = [0]*length
        self.rear = 0
        self.front = 0
        self.length = length

    def empty(self):
        return self.rear == self.front

    def overflow(self):
        return (self.rear+1)%self.length == self.front

    def enqueque(self, var):
        if self.overflow():
            print('队列已满')
        else:
            self.cyclequeue[self.rear] = var
            self.rear = (self.rear + 1) % self.length

    def dequeque(self):
        if self.empty():
            print('队列已空')
        else:
            # queque_num = self.cyclequeue.pop(self.front)
            queque_num = self.cyclequeue[self.front]
            self.front = (self.front + 1) % self.length
            return queque_num

    def size(self):
        return (self.rear - self.front + self.length) % self.length



if __name__ == '__main__':
        q = CycleQueue(5)
        q.enqueque(5)
        q.enqueque(4)
        q.enqueque(4)
        q.enqueque(4)
        print(q.cyclequeue)
        print(q.size())
        q.dequeque()
        print(q.cyclequeue)
        print(q.size())