#!/usr/bin/python3
# coding = UTF-8


# def Find_Two(list):
#     list1 = set(list)
#     num = 0
#     for i in list1:
#         n = list.count(i)
#         if n == 1 and num <2:
#             print(i)
#             num += 1
#         elif num >= 2:
#             break
#         else:
#             pass
# list2 = [1,2,3,4,1,2,3,5]
# Find_Two(list2)


def find_one_number(list):
    result = 0
    for i in list:
        result = result ^ i
    return result

def find_two_number(list):
    result = find_one_number(list)
    value = result & (-result)
    # list1 = []
    # list2 = []
    num1, num2 = 0, 0

    for i in list:
        if i & value == True:
            # list1.append(i)
            num1 = num1 ^ i
        else:
            # list2.append(i)
            num2 = num2 ^ i
    # n = find_one_number(list1)
    # m = find_one_number(list2)
    print(num1, num2)

if __name__ == '__main__':
    list = [1, 2, 3, 4, 1, 2, 3, 5]
    find_two_number(list)
