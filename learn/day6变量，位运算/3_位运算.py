#!/usr/bin/python3
# coding = UTF-8
i = 110
print(bin(i))
print(hex(i))
print(oct(i))
print('-'*50)
i = -110
print(bin(i))
print(hex(i))
print(oct(i))

print(~5)
print(~0)
print(~(-5))

print('-'*50)

i = 5
i = i << 1
print(i)

i = -5
i = i << 1
print(i)

i = 5
i = i >> 1
print(i)

j = -5
j = j >> 1
print(j)

print('*'*50)
print(100&10)
print(100|11)


print(bin(12))
print(bin(-12&0xff))

print(5^8)
print(5^9)

n = 7^11
print(n)
m = n&(-n)
print(m)