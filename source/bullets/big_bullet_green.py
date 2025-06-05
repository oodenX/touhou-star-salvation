import random
import math
from source.bullets import bullet
import pygame

from .bullet import Bullet
from .. import constant as C


class BigBulletGreen(bullet.Bullet):
    def __init__(self, x, y, angle, speed=5):
        target_x = x + math.cos(math.radians(angle)) * speed
        target_y = y + math.sin(math.radians(angle)) * speed
        Bullet.__init__(self, x, y, target_x, target_y, speed, 48, 32)
        self.image = pygame.image.load(C.big_bullet_green_image)