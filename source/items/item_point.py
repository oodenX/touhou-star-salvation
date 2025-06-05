import random
import pygame
from .. import constant as C


# 物品的父类
class Item(pygame.sprite.Sprite):
    def __init__(self, top):
        pygame.sprite.Sprite.__init__(self)
        self.x = random.randint(0, 627)
        self.y = 0
        self.top = top
        self.center_x = self.x + 8
        self.center_y = self.y + 8
        self.state = 0
        self.image = (pygame.image.load(C.item_image)
                      .subsurface(pygame.rect.Rect(self.top, 0, 16, 16)))
        self.speed = random.randint(3, 5)
        self.timer = pygame.time.get_ticks()

    def check(self, x, y):
        if self.y > 704:
            return 1
        if (self.center_x - x) * (self.center_x - x) + (self.center_y - y) * (self.center_y - y) <= 16 * 16:
            return 2
        self.y += self.speed
        self.center_x = self.x + 8
        self.center_y = self.y + 8
        return 0

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
    #
    # def update(self, surface, x, y):
    #     if pygame.time.get_ticks() - self.timer > 50:
    #         self.y += self.speed
    #     self.center_x = self.x + 8
    #     self.center_y = self.y + 8
    #     self.state = self.check(x, y)
    #     self.draw(surface)