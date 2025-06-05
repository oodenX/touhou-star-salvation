import pygame
from .. import constant as C

class MainMenu:
    def __init__(self):
        self.background = pygame.image.load(C.background)
        self.menu_hint = pygame.image.load(C.menu_hint)
        self.menu_text = pygame.image.load(C.menu_text)
        self.finished = False
        # 下一个状态是对话
        self.next = 'dialogue'

    def choose_enter(self, keys):
        # 通过空格进入游戏
        if keys[pygame.K_SPACE]:
            self.finished = True

    def update(self, surface, keys):
        self.choose_enter(keys)
        surface.blit(self.background, (0, 0))
        surface.blit(self.menu_hint, (340, 400))
        surface.blit(self.menu_text, (0, 0))


