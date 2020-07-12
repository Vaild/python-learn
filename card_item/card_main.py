#!/usr/bin/python3
# coding = UTF-8
# code by va1id


import card_tools
card_list = []
while True:
    # 打印菜单
    print('*' * 50)
    print('欢迎使用【名片管理系统】\n')
    print('1. 新建名片')
    print('2. 显示全部')
    print('3. 查询名片\n')
    print('0. 退出系统')
    print('*' * 50)

    choice = input('选择您要进行的操作：')
    if choice in ['1', '2', '3']:
        if choice == '1':
            card_tools.add_card(card_list)
        elif choice == '2':
            card_tools.show_all_card(card_list)
        # 查找特定名片，并询问是不是要对其进行操作
        else:
            card_index = card_tools.search_card(card_list)
            # 如果返回一个bool值说明这是一个空的列表或者是没有找到
            if isinstance(card_index, bool):
                # 如果是false则说明是没找到，则提示是不是要添加这个名片
                if card_index == False:
                    add_or = input('是不是要添加此人名片：y/n')
                    if add_or == 'y':
                        card_tools.add_card(card_list)
                    else:
                        pass
                else:
                    pass
            else:
                print('您是不要对该名片进行操作：\n1.删除\n2.修改')
                select = input('请选择您要做出的操作：')
                if select in ['1', '2']:
                    if select == '1':
                        card_tools.del_card(card_list, card_index)
                    else:
                        card_tools.alter_card(card_list, card_index)
    elif choice == '0':
        break
    else:
        print('输入错误，没有相关操作，请确定后重新输入！')
