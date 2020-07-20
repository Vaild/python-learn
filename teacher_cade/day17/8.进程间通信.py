#!/usr/bin/python3
# coding=utf-8
# coding=utf-8
from multiprocessing import Queue

q = Queue(3)  # 初始化一个Queue对象，最多可接收三条put消息
q.put("消息1")
q.put("消息2")
print(q.full())  # False
q.put("消息3")
print(q.full())  # True
# print(q.get())
# print(q.get())
# print(q.get())
# message = None
# try:
#     message = q.get(block=False)
# except:
#     pass
# finally:
#     print(message)
q.put('消息4')
