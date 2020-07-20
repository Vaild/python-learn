#!/usr/bin/python3
# coding = UTF-8
# code by va1id


import gevent
import urllib.request
def downlod(url):
    print('GET: ', url)
    gevent.sleep(1)
    res = urllib.request.urlopen(url)
    size = res.read()
    with open('file.html', mode='wb') as file:
        file.write(size)

    print('从%s获取到 %d byte的数据.' %(url, len(size)))

if __name__ == '__main__':
    gevent.joinall([
        gevent.spawn(downlod, 'https://va1id.top'),
        # gevent.spawn(downlod, 'https://www.baidu.com'),
        # gevent.spawn(downlod, 'https://www.aliyun.com')
    ])