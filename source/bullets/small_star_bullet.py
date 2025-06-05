import random
import math
from source.bullets import bullet
import pygame

from .bullet import Bullet
from .. import constant as C

class SmallStarBullet(bullet.Bullet):
    def __init__(self, x, y, angle, speed=5):
        target_x = x + math.cos(math.radians(angle)) * speed
        target_y = y + math.sin(math.radians(angle)) * speed
        Bullet.__init__(self, x, y, target_x, target_y, speed, 8, 8)
        self.image = (pygame.image.load(C.small_star_bullet_image)
                      .subsurface((random.randint(0, 15) * 16, 0, 16, 16)))
        self.original_image = self.image
        self.rect = self.image.get_rect(center=(x, y))
        self.angle = 0

    def update(self, surface):
        super().update(surface)
        self.angle += 5
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)



