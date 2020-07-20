import pygame

clock = pygame.time.Clock()
i = 0

# 游戏循环
while True:
    # 设置屏幕刷新帧率，每秒60次
    clock.tick(1)

    print(i)
    i += 1
