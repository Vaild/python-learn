#!/usr/bin/python3
# coding = UTF-8
# code by va1id

import os
import time
from multiprocessing import Process
def son():
    while True:
        print('son process')
        print('son pid : ', os.getpid())
        time.sleep(2)


if __name__ == '__main__':
    x = Process(target=son)
    x.start()
    while True:
        print()
        print('dad process')
        print('dad pid : ', os.getpid())
        time.sleep(2)
