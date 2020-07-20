#!/usr/bin/python3
# coding = UTF-8
# code by va1id

import time
import os
import multiprocessing
def copy_file(source_path, file_name, new_file):
    file = open(source_path + '/' + file_name, mode='rb')
    file_c = open(new_file + '/' + new_file, mode='wb')
    while True:
        time.sleep(0.1)
        text = file.read(1024)
        if text:
            file_c.write(text)
        else:
            break

def process_pool():
    source_path = input('输入要复制的文件夹：')
    file_list = os.listdir(source_path)
    new_file = source_path + 'copy'
    pool = multiprocessing.Pool(3)
    queue = multiprocessing.Manager().Queue()
    try:
        os.mkdir(new_file)
    except:
        pass
    for file_name in file_list:
        pool.apply_async(copy_file, args=(source_path, file_name, new_file))
    pool.close()
    sum_of_file = len(file_list)
    while True:
        file_name = queue.get()
        if file_name in file_list:
            file_list.remove(file_name)
        else:
            pass
        copy_speed = (sum_of_file - len(file_list)) * 100 / sum_of_file
        print('共有%d个文件，已经完成%.2f.'%(sum_of_file, copy_speed), end='')
        if copy_speed >= 100:
            break

if __name__ == '__main__':
    process_pool()