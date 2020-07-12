#!/usr/bin/python3
# coding = UTF-8
# code by va1id


import os
os.mkdir('test2')
os.chdir('./test2/')
os.mkdir( 'test1')
file = open('name',mode='w+')
file.close()
file = open('name1',mode='w+')
file.close()
# os.remove('.', name)
os.chdir('..')
os.chdir('./test2')
os.rename('name', 'replace')
os.remove('name1')

print(os.getcwd())
print(os.path.isdir('test2'))
os.chdir('./test2')
os.rmdir('test1')
os.mkdir('123')
os.mkdir('345')

os.chdir('./test2')
os.removedirs()