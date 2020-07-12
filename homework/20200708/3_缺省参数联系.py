#!/usr/bin/python3
# coding = UTF-8
# code by va1id


def quesheng(name='keyi', sex='男', qq='123'):
    print(name, sex, qq)

if __name__ == '__main__':
    quesheng()
    quesheng(name='1', sex='女', qq='321')
    quesheng('2', '男', '567')
    quesheng(name='1', sex='女')
    # quesheng(name='1', sex='女', '1234') 不能混合用