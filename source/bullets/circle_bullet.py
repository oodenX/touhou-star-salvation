import random
import math
from source.bullets import bullet
import pygame

from .bullet import Bullet
from .. import constant as C

class CircleBullet(bullet.Bullet):
    def __init__(self, x, y, angle, speed=5):
        target_x = x + math.cos(math.radians(angle)) * speed
        target_y = y + math.sin(math.radians(angle)) * speed
        Bullet.__init__(self, x, y, target_x, target_y, speed, 16, 16)
        self.image = (pygame.image.load(C.circle_bullet_image)
                      .subsurface((random.randint(0, 7) * 32, 0, 32, 32)))
