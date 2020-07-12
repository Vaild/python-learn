#!/usr/bin/python3
# coding = UTF-8
for tail in range(1, 10):
    for head in range(1, 10):
        if tail >= head:
            print('{} * {} = {}  '.format(head, tail, head*tail), end='')
        else:
            break
    print('\n')