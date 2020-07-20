#!/usr/bin/python3
# coding = UTF-8
# code by va1id


from collections.abc import Iterable, Iterator
print(isinstance([], Iterable))
print(isinstance([], Iterator))
print()
print(isinstance((), Iterable))
print(isinstance((), Iterator))
print()
print(isinstance({}, Iterable))
print(isinstance({}, Iterator))
print()
print(isinstance(set(), Iterable))
print(isinstance(set(), Iterator))