#!/usr/bin/python3
# coding = UTF-8
# code by va1id


class Gun:
    bullet_count = 0
    def __init__(self, model=None):
        self.model = model


    def add_bullet(self, count):
        self.bullet_count += count


    def shoot(self):
        if self.bullet_count == 0:
            print('请及时装弹。')
            return
        else:
            print('开始射击')
            self.bullet_count -= 1
            print('剩余%d颗子弹。' % self.bullet_count)


class Soldior:
    def __init__(self, name=None, gun=None):
        self.name = name
        self.gun = gun

    def fire(self):
        if self.gun == None:
            print('没有枪')
        else:
            print('开火')
            self.gun.add_bullet(100)
            self.gun.shoot()


ak = Gun('AK47')
pr = Soldior('xiaoming')
pr.gun = ak
pr.fire()
