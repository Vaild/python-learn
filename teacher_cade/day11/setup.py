#!/usr/bin/python3
# coding=utf-8

from distutils.core import setup

setup(name="wd_message",  # 包名
      version="1.0",  # 版本
      description="wangdao's 发送和接收消息模块",  # 描述信息
      long_description="完整的发送和接收消息模块",  # 完整描述信息
      author="luke",  # 作者
      author_email=" wangdao@cskaoyan.com",  # 作者邮箱
      url="www.cskaoyan.com",  # 主页
      py_modules=["wd_message.send_message",
                  "wd_message.receive_message"])
