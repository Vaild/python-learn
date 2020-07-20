#!/usr/bin/python3
# coding=utf-8
import threading
import time


def work1(num_list):
    num_list.append(2)
    print('work1 %d %s' % (id(num_list), num_list))


def work2(num_list):
    time.sleep(1)
    print('work2 %d %s' % (id(num_list), num_list))


def main():
    num_list = [1]
    t1 = threading.Thread(target=work1, args=(num_list,))
    t1.start()

    t2 = threading.Thread(target=work2, args=(num_list,))
    t2.start()

    while len(threading.enumerate()) != 1:
        time.sleep(1)
    print('main thread %s' % num_list)


if __name__ == '__main__':
    main()
