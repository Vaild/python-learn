#!/usr/bin/python3
# coding=utf-8

# def main():
#     print(i)
#
#
# if __name__ == '__main__':
#     i = 3
#     main()

def demo1():
    num = int(input("输入整数："))
    print(num)
    return num


def demo2():
    return demo1()


def main():
    # 利用异常的传递性，在主程序捕获异常
    try:
        print(demo2())
    except Exception as result:
        print("未知错误 %s" % result)


if __name__ == '__main__':
    main()
