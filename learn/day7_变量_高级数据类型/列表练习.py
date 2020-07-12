#!/usr/bin/python3
# coding = UTF-8


# list = [1,3,4,3,4,5,6,7,89,8,67]
# list1 = ['a', 'b', 'c']
# print(list.count(4))
# list.append(4)
# print(list)
# list.insert(4, 3)
# print(list)
# list.reverse()
# print(list)
# list.extend(list1)
# print(list)
# list1.clear()
# print(list1)


#
# list1 = ['张三', '李四', '张三', '李四', '张三', '李四', '王五']
# list2 = set(list1)
# print('列表中共有%d个名字。'% len(list2))
# for i in list2:
#     print('{}共有{}个。'.format(i, list1.count(i)))
#
# list1.sort()
# print(list1)
# list1.sort(reverse=True)
# print(list1)


# 列表生成
a = [x for x in range(1, 100, 2)]
print(a)

b = [j for i in range(10) for j in range(i)]
print(b)

c = [c*r for c in range(5) for r in range(5)]
print(c)
c = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]
print(c)

d = [j for x in c for j in x]
print(d)

e = [i for i in range(18) if i % 2 == 0]
print(e)