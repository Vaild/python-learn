#!/usr/bin/python3
# coding = UTF-8
# code by va1id


from multiprocessing import Queue
q = Queue(4)
q.put('1')
q.put('2')
q.put('3')
q.put('4')
q.put('4')

print(q.get())
print(q.get())
print(q.get())
print(q.get())
try:
    print(q.get(timeout=True))
except:
    pass