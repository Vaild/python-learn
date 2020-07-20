#!/usr/bin/python3
# coding=utf-8


class MusicPlayer(object):
    instance = None

    def __new__(cls, *args, **kwargs):
        # 1. 创建对象时，new方法会被自动调用
        print("创建对象，分配空间")

        # 2. 为对象分配空间,先判断是否分配过了
        if cls.instance is None:
            cls.instance = super().__new__(cls)

        # 3. 返回对象的引用
        return cls.instance

    def __init__(self):
        print("播放器初始化")


# 创建播放器对象
player = MusicPlayer()

print(player)
player1 = MusicPlayer()

print(player is player1)
