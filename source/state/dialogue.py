import time

import pygame
from .. import constant as C

class Dialogue:
    def __init__(self):
        self.background = pygame.image.load(C.dialogue_background)
        self.finished = False
        self.num = 1
        # 下一个状态是关卡
        self.next = 'level'

    def choose_enter(self, keys):
        # 按下回车键进入
        if keys[pygame.K_RETURN]:
            self.num += 1
            time.sleep(0.2)

    def update(self, surface, keys):
        if self.num > 5:
            self.finished = True
        else:
            # 加载图片
            surface.blit(self.background, (0, 0))
            plot = pygame.image.load(C.plot + str(self.num) + '.png')
            plot_tip = pygame.image.load(C.plot_tip)
            surface.blit(plot, (0, 0))
            surface.blit(plot_tip, (0, 0))
        self.choose_enter(keys)
