import pygame
import random
from .. import constant as C, tools
from ..charactors import myself
# 弹幕的父类
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = C.bullet_image
        self.rect = (16, 16)
        self.x = x
        self.y = y
        self.come = True
        self.center_x = self.x + 8
        self.center_y = self.y + 8
        self.timer = 0
        self.alive = True
        self.speed = 5
        self.bullet_kind = random.randint(0, 15)

    def out_of_bounds(self):
        # 检查是否出界
        if self.y < 0:
            self.alive = False
        self.center_x = self.x + 8
        self.center_y = self.y + 8

    def draw(self, surface):
        self.out_of_bounds()
        surface.blit(self.get_bullet(self.bullet_kind), (self.x + 8, self.y - 16))
        self.y -= self.speed

    def get_bullet(self, i):
        return pygame.image.load(self.image).subsurface(pygame.Rect((i * 16, 0, 16, 16)))
