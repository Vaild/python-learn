#!/usr/bin/python3
# coding = UTF-8
# code by va1id

# 通过deque实现循环队列
from collections import deque
queue = deque([1, 2, 3, 4, 5])
# 入队
queue.append(6)
print(len(queue))
print(queue)
# 从左侧出队
queue.popleft()
print(len(queue))
print(queue)
# 打印队尾元素
print(queue[-1])
# 打印队首元素
print(queue[0])

#####################
# 队列已经实现的差不多了,联系其他操作

print('-'*50)
print(queue)
queue.insert(1, 10)
print(queue)
queue.remove(4)
print(queue)
print(queue.index(10))