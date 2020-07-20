#!/usr/bin/python3
# coding=utf-8
import time
from multiprocessing import Process


def run_proc():
    while True:
        print('I am child process')
        time.sleep(1)
        pass


if __name__ == '__main__':
    p = Process(target=run_proc)
    p.start()
    while True:
        print('I am parent process')
        time.sleep(1)
        pass
