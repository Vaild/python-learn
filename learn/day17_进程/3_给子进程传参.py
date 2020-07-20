#!/usr/bin/python3
# coding = UTF-8
# code by va1id

import time
from multiprocessing import Queue, Process
def send_process(message, send_q):
    for i in message:
        print('正在写入', i)
        send_q.put(i)
        print('已经写入', i)
        time.sleep(0.2)


def receive_process(send_q):
    while True:
        print('已经读取', send_q.get(timeout=True))
        time.sleep(1)

#         send_q.get()
if __name__ == '__main__':
    message = ['A', 'B', 'C']
    send_q = Queue(len(message))
    x = Process(target=send_process, args=(message, send_q))
    y = Process(target=receive_process, args=(send_q, ))
    x.start()
    y.start()
    x.join()
    y.join()
