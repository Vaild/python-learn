#!/usr/bin/python3
# coding = UTF-8
# code by va1id


from multiprocessing import Process
import time
import os
def run_son_process():
    while True:
        print()
        print('zijicheng',os.getppid())
        time.sleep(1)
        p.terminate()
        p.join()


if __name__ == '__main__':
    print('进程即将启动')
    p = Process(target=run_son_process)
    p.start()
    while True:
        print('dad')
        time.sleep(1)
        print('fujincheng',os.getpid())