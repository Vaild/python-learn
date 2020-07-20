#!/usr/bin/python3
# coding = UTF-8
# code by va1id


import threading
import time
def thread1():
    while True:
        print('1')
        time.sleep(1)

def thread2():
    while True:
        print('2')
        time.sleep(1)

if __name__ == '__main__':
    x = threading.Thread(target=thread1)
    x.start()
    y = threading.Thread(target=thread2)
    y.start()

    x.join()
    y.join()