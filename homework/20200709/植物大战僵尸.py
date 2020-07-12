#!/usr/bin/python3
# coding = UTF-8
# code by va1id


class SunFlower:
    def __init__(self, life = None):
        self.life = life

    def ProductSun(self):
        print('生产阳光')

    def Wave(self):
        print('摇晃')

class Shooter:
    def __init__(self, life=None, bullet=None):
        self.life = life
        self.bullet = bullet
    def Fire(self):
        self.bullet -= 1
    def bullet_num(self):
        print('剩余%d颗子弹。' % self.bullet)

class PeaShooter(Shooter):
    def Fire(self):
        super().Fire()
        print('发射子弹')

class FrozenShooter(Shooter):
    def FrozenFire(self):
        super().FrozenFire()
        print('发射冰冻子弹')

class Zombie:
    def __init__(self, life=None):
        self.life = life
    def Bite(self):
        print('咬')
    def Move(self):
        print('移动')

class DrumZombie(Zombie):
    def __init__(self, drum=None):
        super(DrumZombie, self).__init__()
        self.drum = drum

class JumpZombie(Zombie):
    def __init__(self, bamboo=None):
        super(JumpZombie, self).__init__()
        self.bamboo = bamboo
    def Jump(self):
        print('跳')


sun1 = SunFlower()
sun2 = SunFlower()
sun1.Wave()
sun1.ProductSun()
sun2.ProductSun()

shooter1 = PeaShooter(100, 100)
shooter2 = FrozenShooter(100, 100)
shooter1.Fire()
shooter2.Fire()
shooter2.bullet_num()


zombie1 = Zombie()
zombie2 = DrumZombie()
zombie3 = JumpZombie()
zombie1.Bite()
zombie2.Move()
zombie3.Jump()
