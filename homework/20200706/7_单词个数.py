#!/usr/bin/python3
# coding = UTF-8

def Output_word(str):
    import string
    length = len(str)
    j = True
    count = 0
    for before in range(length):
        after = before + 1
        if str[0] in string.ascii_letters and j == True:
            count += 1
            j = False
        else:
            pass
        if str[before] == ' ' and str[after] in string.ascii_letters:
            count += 1
        else:
            pass
    return count


str = 'New     hello         world  how   are  you   \n'
print(Output_word(str))