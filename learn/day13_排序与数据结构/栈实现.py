#!/usr/bin/python3
# coding = UTF-8
# code by va1id


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, var):
        self.stack.append(var)

    def pop(self):
        if self.empty():
            print('kong')
        else:
            return self.stack.pop()

    def empty(self):
        return self.stack == []

    def top(self):
        if self.empty():
            return None
        else:
            return self.stack[-1]

    def length(self):
        return len(self.stack)

if __name__ == '__main__':
    s = Stack()
    for i in range(10):
        s.push(i)
        print('-'*20)
        print(s.top())
        print(s.length())
    for i in range(5):
        print('-'*20)
        print(s.pop())
