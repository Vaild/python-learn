#!/usr/bin/python3
# coding = UTF-8
# code by va1id


def add_card(card_list):
    """
    增加一个新的名片
    :return: 增加后的所有的名片的列表
    """
    print('1. 新建名片')
    company = input('公司：')
    name = input('姓名：')
    title = input('职位：')
    phone = input('电话：')
    email = input('邮箱：')
    card_dict = {"company": company, "name": name, "title": title, "phone": phone, "email": email}
    card_list.append(card_dict)


def search_card(card_list):
    """
    寻找某个特定的名片
    :return:
    """
    print('3. 查询名片')
    # 两种情况分别返回了true和false，为了判别到底是哪里种情况，可进行扩展
    if len(card_list) == 0:
        print('当前无名片！')
        return True
    search_key = input('输入您要查询的名字：')
    card_num = len(card_list)
    for card_index in range(card_num):
        if card_list[card_index]["name"] == search_key:
            print('*' * 30)
            print(card_list[card_index]["company"])
            print(card_list[card_index]["name"], '\t', card_list[card_index]["title"])
            print('电话：{}\nE-mail：{}'.format(card_list[card_index]["phone"], card_list[card_index]["email"]))
            print('*' * 30)
            return card_index
        else:
            pass
    else:
        print('未找到该名片!')
        return False


def show_all_card(card_list):
    """
    展示所有的名片
    :return:
    """
    for card in card_list:
        print('*' * 30)
        print(card["company"])
        print(card["name"], '\t', card["title"])
        print('电话：{}\nE-mail：{}'.format(card["phone"], card["email"]))
        print('*' * 30)


def del_card(card_list, card_index):
    """
    删除所查找到的名片
    :param card_list:
    :param search_key:
    :return:
    """
    card_list.pop(card_index)
    print('删除成功！')


def alter_card(card_list, card_index):
    """
    指定要修改的个数与项目，进行修改
    :param card_list:
    :param card_index:
    :return:
    """
    al_num = int(input('请输入您要修改的项目数：'))
    for i in range(al_num):
        al_item = input('输入您要修改的项目：')
        card_list[card_index][al_item] = input('输入您要修改的值：')
    print('修改成功！')
