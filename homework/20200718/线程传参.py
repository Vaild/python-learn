#!/usr/bin/python3
# coding = UTF-8
# code by va1id



import threading
import time
def work1(list1):
    i = 1
    while True:
        list1.append(i)
        i += 1
        time.sleep(1)

def work2(list1):
    while True:
        print(list1)
        time.sleep(2)


if __name__ == '__main__':
    a = [1, 2, 3]
    x = threading.Thread(target=work1, args=(a, ))
    x.start()
    y = threading.Thread(target=work2, args=(a, ))
    y.start()

    x.join()
    y.join()