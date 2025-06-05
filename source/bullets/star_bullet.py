import random
import math
from source.bullets import bullet
import pygame

from .bullet import Bullet
from .. import constant as C

class StarBullet(bullet.Bullet):
    def __init__(self, x, y, angle, speed=5):
        target_x = x + math.cos(math.radians(angle)) * speed
        target_y = y + math.sin(math.radians(angle)) * speed
        Bullet.__init__(self, x, y, target_x, target_y, speed, 16, 16)
        self.image = (pygame.image.load(C.star_bullet_image)
                      .subsurface((random.randint(0, 7) * 32, 0, 32, 32)))
        self.original_image = self.image
        self.rect = self.image.get_rect(center=(x, y))
        self.angle = 0

    def update(self, surface):
        super().update(surface)
        self.angle += 5
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)